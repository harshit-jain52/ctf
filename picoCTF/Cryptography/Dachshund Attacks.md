# Dachshund Attacks

Small d, so weiner's attack:

```python
from pwn import *
import owiener
from Crypto.Util.number import long_to_bytes

conn = remote('mercury.picoctf.net', 36463, level = 'debug')
conn.recvline()
e = int(conn.recvline().decode('utf-8').split(':')[1].strip())
n = int(conn.recvline().decode('utf-8').split(':')[1].strip())
c = int(conn.recvline().decode('utf-8').split(':')[1].strip())

conn.close()
d = owiener.attack(e, n)
m = pow(c, d, n)
print(long_to_bytes(m).decode('utf-8'))
```
