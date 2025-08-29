# Half-Baked

```text
Boss wanted our cake webshop secured with RSA and said I should remember to use some good primes.
Not sure what that means, but he specifically asked for 2, I guess to save money.
Sounded easy enough, but now the whole system feels a bit half-baked 😕
```

points: `100`

solves: `433`

author: `Nissen`

---

N, e, c given. N is EVEN, actually it is **a power of 2**. So phi is just N/2

## Proof that $\varphi(N) = \tfrac{N}{2}$ when $N$ is a power of 2

Let $N = 2^k$ for some integer $k \geq 1$.

Euler’s totient function is given by  

$$
\varphi(N) = N \prod_{p \mid N}\left(1 - \frac{1}{p}\right),
$$

where the product runs over all distinct prime divisors of $N$.

Since the only prime divisor of $2^k$ is $2$, we get  

$$
\varphi(2^k) = 2^k \left(1 - \frac{1}{2}\right).
$$

$$
\varphi(2^k) = 2^k \cdot \frac{1}{2} = 2^{k-1}.
$$

$$
\varphi(N) = \frac{N}{2}.
$$

## Decryption script

```python
from Crypto.Util.number import long_to_bytes, inverse

N = 2999882211429630485883650302877390551374775896896788078868325571891218714007953558505041388044334470201821965796391409921668122818083570668568660678895962925314655342154580738160357641047430373917156721861167458749434940591017306495880180805391185380307427539761080193213111534709378234670214284858143824384128077373871882033779166821558334466322908873171079631967672353755842618738501413251304204009472
e = 65537
c = 406899880095774364291729342954053590589397159355690238625035627993181937179155345315119680672959072539867481892078815991872758149967716015787715641627573675995588117336214614607141418649060621601912927211427125930492034626696064268888134600578061035823593102305974307471288655933533166631878786592162718700742194241218161182091193661813824775250046054642533470046107935752737753871183553636510066553725

phi = N//2
d = inverse(e, phi)
m = pow(c, d, N)
print(long_to_bytes(m))
```
