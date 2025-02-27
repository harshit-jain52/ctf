# rsa_oracle

Get the password:

```python
from pwn import *

conn = remote("titan.picoctf.net", 63266, level='debug')

# Encrypt 2
conn.recvuntil('E --> encrypt D --> decrypt.')
conn.sendline('E')
conn.recvline()
conn.sendline("\x02")
res = conn.recvuntil('E --> encrypt D --> decrypt.').decode('utf-8')
two = int(res.split('\n')[4].split()[-1])

# Decrypt encrypt(2)*pwd
with open('password.enc','r') as f:
    pwd = int(f.read().strip())

conn.sendline('D')
conn.recvline()
conn.sendline(str(two * pwd))
res = conn.recvuntil('E --> encrypt D --> decrypt.').decode('utf-8')
hex_value = res.split('\n')[0].split()[-1]

# Divide the result by 2 to get decrypt(pwd)
m2 = int(hex_value, 16)
m2 //= 2
pwd = bytes.fromhex(hex(m2)[2:]).decode('utf-8')
print(pwd)
```

Use the password in openssl decryption

```shell
openssl enc -aes-256-cbc -d -in secret.enc
```
