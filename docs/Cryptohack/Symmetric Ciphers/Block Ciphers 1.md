# Block Ciphers 1

## 1. ECB CBC WTF

```python
import requests

ciphertext = requests.get('https://aes.cryptohack.org/ecbcbcwtf/encrypt_flag').json()['ciphertext']
iv_hex = ciphertext[:32]
ciphertext = ciphertext[32:]
plaintext = requests.get('https://aes.cryptohack.org/ecbcbcwtf/decrypt/' + ciphertext).json()['plaintext']

for i in range(0, len(plaintext), 32):
    iv = ''
    if i == 0:
        iv = iv_hex
    else:
        iv = ciphertext[i-32:i]
    
    print(bytes([a ^ b for a, b in zip(bytes.fromhex(iv), bytes.fromhex(plaintext[i:i+32]))]).decode(), end='')
```

## 3. Flipping Cookie

```python
import requests

url = 'https://aes.cryptohack.org/flipping_cookie/'

cookie = requests.get(url+'get_cookie/').json()['cookie']
iv_bytes = list(bytes.fromhex(cookie[:32]))
real = 'admin=False'
fake = ';admin=True'

for i in range(len(real)):
    iv_bytes[i] ^= ord(real[i]) ^ ord(fake[i])

iv_hex = ''.join([hex(b)[2:].zfill(2) for b in iv_bytes])
print(requests.get(url+'check_admin/'+iv_hex+cookie[32:]+'/'+iv_hex+'/').json())
```

## 4. Lazy CBC

```python
import requests

url = 'https://aes.cryptohack.org/lazy_cbc/'

"""
d(ct0) = iv ^ pt0
d(ct1) = ct0 ^ pt1

if ct0 = ct1, then iv = pt0 ^ pt1 ^ ct0
"""

res = requests.get(url + 'receive/' + '0'*64).json()
pt = res['error'].split(':')[1].strip()
# print(pt)
pt0 = bytes.fromhex(pt[:32])
pt1 = bytes.fromhex(pt[32:64])

iv = bytes([pt0[i]^pt1[i] for i in range(16)]).hex()
# print(iv)

flag = requests.get(url+'get_flag/' + iv).json()['plaintext']
print(bytes.fromhex(flag))
```
