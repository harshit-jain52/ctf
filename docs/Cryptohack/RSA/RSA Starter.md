# Starter

## 1. Modular Exponentiation

```python
print(pow(12,65537,22663))
```

## 2. Public Keys

```python
e=65537
p=17
q=23
N = p*q

def encrypt(m):
    return pow(m, e, N)

m=12
print(encrypt(m))
```

## 3. Euler's Totient

```python
p = 857504083339712752489993810777
q = 1029224947942998075080348647219

print((1-p)*(1-q))
```

## 4. Private Keys

```python
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
phi = (p-1)*(q-1)
print(pow(e, -1, phi))
```

## 5. RSA Decryption

```python
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
phi = (p-1)*(q-1)
d = pow(e, -1, phi)

c = 77578995801157823671636298847186723593814843845525223303932
m = pow(c, d, p*q)
print(m)
```

## 6. RSA Signatures

```python
import hashlib
from Crypto.Util.number import *

flag = "crypto{Immut4ble_m3ssag1ng}"

with open("private.key", "r") as f:
    N = int(f.readline().split()[-1])
    d = int(f.readline().split()[-1])

    hash = hashlib.sha256(flag.encode()).digest()
    print(pow(bytes_to_long(hash), d, N))
```
