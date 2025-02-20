# HideToSee

Extract (no passphrase):

```shell
steghide extract -sf atbash.jpg
```

Atbash cipher:

```python
from Crypto.Util.number import inverse

with open('encrypted.txt', 'r') as file:
    flag = file.read().strip()
    
    for c in flag:
        if not c.isalpha():
            print(c, end='')
        elif c.isupper():
            print(chr(ord('Z')-(ord(c) - ord('A'))), end='')
        else:
            print(chr(ord('z')-(ord(c) - ord('a'))), end='')
```
