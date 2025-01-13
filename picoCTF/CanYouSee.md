# CanYouSee

```shell
unzip unknown.zip
exiftool ukn_reality.jpg
```

The value of `Attribution URL` looks like a base64-encoded string; decode it:

```shell
echo "<decoded>" | base64 -d
```
