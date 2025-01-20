# Primes Part 1

## 1. Factoring

```python
from factordb.factordb import FactorDB
N = 510143758735509025530880200653196460532653147
f = FactorDB(N)
f.connect()
print(f.get_factor_list())
```

## 2. Inferius Prime

```python
from factordb.factordb import FactorDB
from Crypto.Util.number import inverse, long_to_bytes

N = 984994081290620368062168960884976209711107645166770780785733
f = FactorDB(N)
f.connect()
p,q = f.get_factor_list()
# print(p,q)

phi = (p-1)*(q-1)
e = 0x10001
d = inverse(e, phi)
ct = 948553474947320504624302879933619818331484350431616834086273
pt = long_to_bytes(pow(ct, d, N))
print(pt)
```

## 3. Monoprime

```python
from Crypto.Util.number import inverse, long_to_bytes

with open("output.txt", "r") as f:
    n = int(f.readline().split()[-1])
    e = int(f.readline().split()[-1])
    c = int(f.readline().split()[-1])
    phi = n-1
    d = inverse(e, phi)
    m = pow(c, d, n)
    print(long_to_bytes(m))
```

## 4. Square Eyes

```python
from Crypto.Util.number import inverse, long_to_bytes
from math import isqrt
with open("output.txt", "r") as f:
    n = int(f.readline().split()[-1])
    e = int(f.readline().split()[-1])
    c = int(f.readline().split()[-1])
    
    p = isqrt(n)
    # print(p)
    phi = p*(p-1)
    d = inverse(e, phi)
    m = pow(c, d, n)
    print(long_to_bytes(m))
```

## 5. Manyprime

```python
from Crypto.Util.number import inverse, long_to_bytes
from math import prod
from factordb.factordb import FactorDB

with open("output.txt", "r") as f:
    n = int(f.readline().split()[-1])
    e = int(f.readline().split()[-1])
    c = int(f.readline().split()[-1])
    
    fdb = FactorDB(n)
    fdb.connect()
    phi = prod(x-1 for x in fdb.get_factor_list())

    d = inverse(e,phi)
    m = pow(c, d, n)
    print(long_to_bytes(m))
```
