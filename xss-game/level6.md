# level 6

In `index.html`, we observe:

```js
scriptEl.src = url;
```

where `url` is the segment (after '#' in page's URL)

We can host an attacker js file which can be provided as src (http(s) is being filtered, but that's not a problem; can provide link without http(s)) \
Or we can do this:

```text
#data:text/javascript,alert(1)
```
