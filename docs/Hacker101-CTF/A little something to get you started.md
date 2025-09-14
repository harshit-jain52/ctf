# A little something to get you started

## Flag 0

Get the source code by inspecting or curl.

```bash
curl https://xxxxxxxxxx.ctf.hacker101.com/
```

```html
.
.
<style>
    body {
        background-image: url("background.png");
    }
</style>
.
.
```

The presence of bg image for a page with white bg seems suspicious. Go to the `background.png` using browser or curl, and there's the flag.

```bash
curl https://xxxxxxxxxx.ctf.hacker101.com/background.png
```
