# Signatures Part 1

## 1. Signing Server

```python
from pwn import *
import json

conn = remote("socket.cryptohack.org", 13374)
conn.recvline()

conn.sendline(json.dumps({"option": "get_secret"}).encode())
c = json.loads(conn.recvline().decode())["secret"]
conn.sendline(json.dumps({"option": "sign", "msg": str(c)}).encode())

signature = json.loads(conn.recvline().decode())["signature"][2:]
m = bytes.fromhex(signature)
print(m)
```
