# Mind Your Ps and Qs

Small N, so factorizable:

```python
from factordb.factordb import FactorDB
from Crypto.Util.number import long_to_bytes

with open("values") as f:
    f.readline()
    c = int(f.readline().split(":")[1].strip())
    n = int(f.readline().split(":")[1].strip())
    e = int(f.readline().split(":")[1].strip())
    
    fdb = FactorDB(n)
    fdb.connect()
    p, q = fdb.get_factor_list()
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    m = pow(c, d, n)
    print(long_to_bytes(m))
```
