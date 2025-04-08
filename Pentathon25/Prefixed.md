# Prefixed

> Crypto - Easy

**Description**: A secured message was intercepted during an ongoing surveillance op. Can you extract the password?

```python
from Crypto.Util.number import getPrime, bytes_to_long
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from FLAG import flag
import os

e = 3
p = getPrime(512)
q = getPrime(512)
N = p * q

password = os.urandom(8)

prefix = b"Hey! Hope you're having a great day :) Here's the super secret password: "+password

m = prefix

m_int = bytes_to_long(m)

c = pow(m_int, e, N)

cipher = AES.new(pad(password,16), AES.MODE_ECB)
enc_flag = cipher.encrypt(pad(flag,16))

with open("output.txt","w") as file:
    file.write(f"N = {N}")
    file.write(f"\ne = {e}")
    file.write(f"\nc = {c}")
    file.write(f"\nenc_flag = '{enc_flag.hex()}'")
```

e=3, but the [previous approach](./Master%20of%20Minuscule.md) doesn't work here as m**3 > n

We have a small public exponent, and a ciphertext with a known prefix and *random padding* of 8 bytes -> [Coppersmith's Short-Pad Attack](https://crypto-kantiana.com/elena.kirshanova/teaching/ssRabat/Lab3.pdf)

[SageMath](https://sagecell.sagemath.org/) script:

```python
from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad
from sage.all import *

N = 113528691533286135619486503678320426942405436180474026715996758683677273620129519001116625212172928404143292206747424792047626885904598039830205811087655674076216144385016876388583905072205758846659333410528359659982670712013937085712468715762412604882698926617336331191121959509580646315781717517765241646819
e = 3
c = 40904880594701466859625372156952907024430068347250260526789660288294080258335285636904107784524813673301828193071221087338467468677414521714440705760297402168021146846811193689952807596695023202233937346637481974945815018994581831095979752874809661624444485774095865972611500010651804775720777433470611240847
enc_flag = 'e0929dd13f9e646894ad757b0c3485d52f2fe369adfb1fa79e249effb630fd507ec4daa88611dfbac86db2d468cbf118'

prefix = b"Hey! Hope you're having a great day :) Here's the super secret password: "
m0 = bytes_to_long(prefix) << 64

PR.<x> = PolynomialRing(Zmod(N))
f = (m0 + x)^e - c
root = f.small_roots(X=2^64, beta=1)[0]

password = long_to_bytes(int(root))
cipher = AES.new(pad(password, 16), AES.MODE_ECB)
flag = unpad(cipher.decrypt(bytes.fromhex(enc_flag)), 16)
print(flag)
```
