# Public Exponent

## 1. Salty

```python
from Crypto.Util.number import long_to_bytes

with open("output.txt", "r") as f:
    n = int(f.readline().split()[-1])
    e = int(f.readline().split()[-1]) # e=1
    c = int(f.readline().split()[-1])
    
    k = 0
    while True:
        m = n*k + c
        msg = long_to_bytes(m)
        if (msg.startswith(b"crypto")):
            print(msg)
            break
        k += 1
```

## 2. Modulus Inutilis

```python
from Crypto.Util.number import long_to_bytes

with open("output.txt", "r") as f:
    n = int(f.readline().split()[-1])
    e = int(f.readline().split()[-1])  # e=3, small public exponent
    c = int(f.readline().split()[-1])

    # c = m^3 mod n
    # since m^3 < n, m = c^(1/3)

    def int_cbrt(x):
        lo, hi = 0, x
        while lo < hi:
            mid = (lo + hi) // 2
            if mid**3 < x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    m = int_cbrt(c)
    print(long_to_bytes(m))
```

## 3. Everything is Big

```python
from Crypto.Util.number import long_to_bytes
import owiener

with open("output.txt", "r") as f:
    n = int(f.readline().split()[-1],16)
    e = int(f.readline().split()[-1],16) 
    c = int(f.readline().split()[-1],16)

    # Weiner's attack when d < 1/3 * N^(1/4)
    d = owiener.attack(e, n)
    m = pow(c, d, n)
    print(long_to_bytes(m))
```
