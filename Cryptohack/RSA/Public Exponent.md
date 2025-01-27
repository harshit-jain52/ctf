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

## 4. Crossed Wires

[Algorithm](https://www.di-mgt.com.au/rsa_factorize_n.html)

```python
import random
from Crypto.Util.number import GCD, inverse, long_to_bytes

with open("output.txt", "r") as f:
    N, d = f.readline().split(": ")[1].strip().strip("()").split(", ")
    my_key = (int(N), int(d))
    # print(my_key)

    friend_keys = []
    l = f.readline().split(": ")[1].strip().strip("[]").split(", ")
    for i in range(0, len(l), 2):
        friend_keys.append((int(l[i].strip("()")), int(l[i + 1].strip("()"))))
    # print(friend_keys)

    c = int(f.readline().split(": ")[1].strip())
    # print(c)

    def find_pq(N, d, e):
        k = d * e - 1
        while True:
            g = random.randint(2, N - 1)
            t = k
            while t % 2 == 0:
                t //= 2
                x = pow(g, t, N)
                y = GCD(x - 1, N)
                if 1 < y < N:
                    p = y
                    q = N // y
                    return p, q

    N, d = my_key
    e = 0x10001
    p, q = find_pq(N, d, e)
    # print(p, q)
    phi = (p - 1) * (q - 1)

    for key in friend_keys[::-1]:
        d = inverse(key[1], phi)
        c = pow(c, d, key[0])
    
    print(long_to_bytes(c))
```

## 5. Everything is Still Big

[Boneh-Durfee Attack](https://github.com/mimoo/RSA-and-LLL-attacks/blob/master/boneh_durfee.sage)

## 6. Endless Emails

Hastad's Broadcast Attack

```python
from Crypto.Util.number import long_to_bytes, inverse
from math import prod
from gmpy2 import iroot
from itertools import combinations

with open("output.txt", "r") as f:
    n_list = []
    c_list = []

    for _ in range(7):
        n = int(f.readline().split()[-1])
        e = int(f.readline().split()[-1]) 
        c = int(f.readline().split()[-1])
        n_list.append(n)
        c_list.append(c)
        f.readline()
        f.readline()

def cbrt(x):
    m, valid = iroot(x, 3)
    if valid:
        print("Cleartext:", long_to_bytes(m))

def crt(C, N): # Chinese Remainder Theorem
    total = 0
    modulo = prod(N)

    for n_i, c_i in zip(N, C):
        p = modulo // n_i
        total += c_i * inverse(p, n_i) * p
    return total % modulo

# Generate all possible combinations of at least 3 elements
for r in range(3, len(c_list) + 1):
    for c_subset, n_subset in zip(combinations(c_list, r), combinations(n_list, r)):
        result = crt(c_subset, n_subset)
        cbrt(result)
```
