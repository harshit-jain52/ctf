# Symmetric Starter

## 2. Password as Keys

```python
import hashlib
import requests
from Crypto.Cipher import AES

ciphertext = requests.get('https://aes.cryptohack.org/passwords_as_keys/encrypt_flag').json()['ciphertext']

with open("words") as f:
    words = [w.strip() for w in f.readlines()]

for word in words:
    word_hash = hashlib.md5(word.encode()).digest()
    
    # result = requests.get('https://aes.cryptohack.org/passwords_as_keys/decrypt/' + ciphertext + '/' + word_hash.hex()).json()
    # plaintext = bytes.fromhex(result['plaintext'])

    cipher = AES.new(bytes.fromhex(word_hash.hex()), AES.MODE_ECB)
    decrypted = cipher.decrypt(bytes.fromhex(ciphertext)).hex()
    plaintext = bytes.fromhex(decrypted)

    if b'crypto' in plaintext:
        print("key is",word,"flag:",plaintext)
        break
    else:
        print("key is not", word)
```
