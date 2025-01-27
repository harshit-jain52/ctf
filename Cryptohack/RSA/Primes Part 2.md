# Primes Part 2

## 1. Infinite Descent

p and q are numerically close, so [Fermat Factorization](https://ir0nstone.notion.site/Factorize-b96056dc70f54cc7b42b32f8984cb7cf)

```python
from Crypto.Util.number import long_to_bytes, inverse
from math import isqrt

with open("output.txt", "r") as f:
    n = int(f.readline().split()[-1])
    e = int(f.readline().split()[-1]) 
    c = int(f.readline().split()[-1])

    a = isqrt(n) + 1
    b2 = a**2 - n

    while isqrt(b2)**2 != b2:
        a += 1
        b2 = a**2 - n
    
    b = isqrt(b2)
    p, q = a - b, a + b
    phi = (p-1)*(q-1)
    d = inverse(e, phi)
    m = pow(c, d, n)
    print(long_to_bytes(m))
```

## 2. Marin's Secrets

Mersenne Primes

```python
from Crypto.Util.number import long_to_bytes, inverse

def mersenne(n):
    n+=1
    return (1 << n) - 1

with open("output.txt", "r") as f:
    n = int(f.readline().split()[-1])
    e = int(f.readline().split()[-1]) 
    c = int(f.readline().split()[-1])
    bc = n.bit_count()
    for i in range(1, bc):
        p = mersenne(i)
        if n%p == 0:
            q = n//p
            # print(p,q)
            phi = (p-1)*(q-1)
            try:
                d = inverse(e, phi)
                m = pow(c, d, n)
            except ValueError:
                continue
            msg = long_to_bytes(m)
            if b"crypto" in msg:
                print(msg)
```
