# Data Formats

## 1. Privacy-Enhanced Mail?

```python
from Crypto.PublicKey import RSA

with open("privacy_enhanced_mail.pem", "r") as f:
    key = RSA.import_key(f.read())
    print(key.d)
```

## 2. CERTainly not

```shell
openssl x509 -in 2048b-rsa-example-cert.der -inform DER -out 2048b-rsa-example-cert.pem -outform PEM
```

```python
from Crypto.PublicKey import RSA

with open("2048b-rsa-example-cert.pem", "r") as f:
    key = RSA.import_key(f.read())
    print(key.n)
```

## 3. SSH Keys

```python
from Crypto.PublicKey import RSA

with open("bruce_rsa.pub", "r") as f:
    key = RSA.import_key(f.read())
    print(key.n)
```
