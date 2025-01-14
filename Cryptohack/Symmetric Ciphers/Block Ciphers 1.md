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
