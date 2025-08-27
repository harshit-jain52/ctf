# Redacted RSA 1

> I have a RSA private key, but it is partially redacted. Can you recover that? Run `openssl pkeyutl -decrypt -inkey key-recovered.pem -in encrypted.txt -out plaintext.txt` after you have recovered the key.

The private key given:

```text
-----BEGIN RSA PRIVATE KEY-----
MIIJKQIBAAKCAgEAnUe2Sb9N9kIoN4z0PAJJShtZDjAr3ow9bzFGF/aoxfF+Rbdr
J0e5QjAgpIoNjVJVeFkb6LdPpAfrJga7cQH2gvFDXHAOoB4KwsJ2IdX67aGZT9A3
z6J+ttXxrJXx1btVeM9SYdhje6SZ7bgsN5SIyqHKaeRUneiE+OLhS7YjaBY6YcVl
4ez0bkYF7z/GbFeF1JFhlKPhnLeL958dzyb6y/G1eXggyrEakFKtfAusojHmAbIE
J2C7U8AIevYxpOEpMcLNwpOx+W5uajySf9HbeWnMVYu9w/tKc2eG5Sys2Lx/0alz
HHJQfFaA+/+NfchuFuAJQv2vfqPtTBcX8wt6EdVdYTZE9PFmyAOenjnEXvlo4Jut
UPS5x6ZEJglhq/6v/LF27oYwFzLsUoozS5C8//i0c06dgCJdb8Q7vn0D6n5P5zgT
4O/NUVeE+e3k60ML0G6btqxjz9lb+6e+kzFDXPEbUw9miydHe1E7I+9AtVGCVNC3
x68YTTaw9S8F7mhPES51AiO8U/zf3SUqaVLSbjSMI/O3SFmRLGOYJfa9Z+wX6mym
6ww99oXth1hxvFVZ6BpsnJhGNNRpsTtCurmY4NoGy6KyzghZP31gfao3/kzeHA0G
4up5RtOBpgPE8tgINfhaGUIULqLGZUY3rM1PKjVRWY4iprimn/y6XpyHYNsCAwEA
AQKCAgAFAUKyPxW2h+1qsyAUhsgZRRyE4JCM0O6liq5d1doSDnjDtC4DPnuNOSXY
xpHe1OdmYIOMWMT+hcf8Wkt9sZ/ME+xeVSyJ+NrDztdehUYqaLGNwiT8hQG+RLmf
kdfzwrXaFdLbzTyBM0A4udsiW6YsuJBN5Vex/LO6jdG4jI+84LQz50myMk2m8rB+
qAti6DgYhxXRWpOz3n1kQFp8/JMPiV4KgwGcIZ2kSRU/NMnmEWtt02HhdOkRJbO/
YfU7d3TNohLVJckMlHCMDehli+KNjwnTERLVWTpJyNoYkd7gOMNigx9oINUh18jb
/ApfHdEvBisVSChdAc9r0/JNqChWuyqC3yv4KI4KBwoIResB1+tpGOW72QFQVQKL
eL8ZtN6G0FXBPt8sijlrmnKHW2A8Ys/pIIo1DT1nTAZJkvGO6jvPuzmMP26YJrle
Syy2P2nNMNyQSOta89yh9UfdDnRUon6jYNcYAPzfoXNjinmyoFMYYnZGdqbq4CJR
goaQ8sWeV16RlAa2U7PlvgpwvFa8+JD96aO5rCqLDggtHZ65knyyQUglrM2JXzr1
IE3YbCNBSCBLTYxl376KI/DwIOD8t1sybAXQF2zZ8OmPdj1O9BuoKk0UGLQbWS0/
v6KIfdf/7F9vFWdTXaSflKXpDkpAG9FMf1hFXT53dcVoauflJQ**************
****************************************************************
****************************************************************
****************************************************************
****************************************************************
****************************************************************
****************************************************************
****************************************************************
****************************************************************
****************************************************************
****************************************************************
****************************************************************
****************************************************************
****************************************************************
****************************************************************
****************************************************************
****************************************************************
****************************************************************
****************************************************************
****************************************************************
****************************************************************
****************************************************************
****************************************************************
****************************************************************
****************************************************************
****************************************************************
****************************************************************
************************************************************
-----END RSA PRIVATE KEY-----
```

Refer to this [helpful blog](https://c15c01337.medium.com/the-art-of-cryptographic-recovery-decrypting-with-an-incomplete-private-key-deddb704834b) on decrypting incomplete private key

Using Cyberchef:

![image](./images/rsa1.png)

1. After first **0282**, we have **0201**, which indicates next 513 bytes represent the integer *n*
2. Next, we notice **0203010001**, which indicates *e* = 0x010001 = 65537
3. After second **0282**, we have **0200**, which indicates next 512 bytes represent the integer *d*

Find p,q from n,e,d using [solution of CryptoHack's Crossed Wires](../Cryptohack/RSA/Public%20Exponent.md)

```python
import random
from Crypto.Util.number import GCD, inverse, long_to_bytes
from Crypto.PublicKey import RSA


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

n = int('009d47b649bf4df64228378cf43c02494a1b590e302bde8c3d6f314617f6a8c5f17e45b76b2747b9423020a48a0d8d525578591be8b74fa407eb2606bb7101f682f1435c700ea01e0ac2c27621d5faeda1994fd037cfa27eb6d5f1ac95f1d5bb5578cf5261d8637ba499edb82c379488caa1ca69e4549de884f8e2e14bb62368163a61c565e1ecf46e4605ef3fc66c5785d4916194a3e19cb78bf79f1dcf26facbf1b5797820cab11a9052ad7c0baca231e601b2042760bb53c0087af631a4e12931c2cdc293b1f96e6e6a3c927fd1db7969cc558bbdc3fb4a736786e52cacd8bc7fd1a9731c72507c5680fbff8d7dc86e16e00942fdaf7ea3ed4c1717f30b7a11d55d613644f4f166c8039e9e39c45ef968e09bad50f4b9c7a644260961abfeaffcb176ee86301732ec528a334b90bcfff8b4734e9d80225d6fc43bbe7d03ea7e4fe73813e0efcd515784f9ede4eb430bd06e9bb6ac63cfd95bfba7be9331435cf11b530f668b27477b513b23ef40b5518254d0b7c7af184d36b0f52f05ee684f112e750223bc53fcdfdd252a6952d26e348c23f3b74859912c639825f6bd67ec17ea6ca6eb0c3df685ed875871bc5559e81a6c9c984634d469b13b42bab998e0da06cba2b2ce08593f7d607daa37fe4cde1c0d06e2ea7946d381a603c4f2d80835f85a1942142ea2c6654637accd4f2a3551598e22a6b8a69ffcba5e9c8760db',16)
d = int('050142b23f15b687ed6ab3201486c819451c84e0908cd0eea58aae5dd5da120e78c3b42e033e7b8d3925d8c691ded4e76660838c58c4fe85c7fc5a4b7db19fcc13ec5e552c89f8dac3ced75e85462a68b18dc224fc8501be44b99f91d7f3c2b5da15d2dbcd3c81334038b9db225ba62cb8904de557b1fcb3ba8dd1b88c8fbce0b433e749b2324da6f2b07ea80b62e838188715d15a93b3de7d64405a7cfc930f895e0a83019c219da449153f34c9e6116b6dd361e174e91125b3bf61f53b7774cda212d525c90c94708c0de8658be28d8f09d31112d5593a49c8da1891dee038c362831f6820d521d7c8dbfc0a5f1dd12f062b1548285d01cf6bd3f24da82856bb2a82df2bf8288e0a070a0845eb01d7eb6918e5bbd9015055028b78bf19b4de86d055c13edf2c8a396b9a72875b603c62cfe9208a350d3d674c064992f18eea3bcfbb398c3f6e9826b95e4b2cb63f69cd30dc9048eb5af3dca1f547dd0e7454a27ea360d71800fcdfa173638a79b2a0531862764676a6eae02251828690f2c59e575e919406b653b3e5be0a70bc56bcf890fde9a3b9ac2a8b0e082d1d9eb9927cb2414825accd895f3af5204dd86c234148204b4d8c65dfbe8a23f0f020e0fcb75b326c05d0176cd9f0e98f763d4ef41ba82a4d1418b41b592d3fbfa2887dd7ffec5f6f1567535da49f94a5e90e4a401bd14c7f58455d3e7775c5686ae7e525',16)
e = 65537
p, q = find_pq(n,d,e)


key = RSA.construct((n,e,d,p,q))
pem = key.export_key('PEM')

with open('key-recovered.pem', 'w') as f:
    f.write(pem.decode())
```

```text
-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----
```
