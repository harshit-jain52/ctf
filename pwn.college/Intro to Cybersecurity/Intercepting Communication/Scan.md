# Scan

## Scan 1

Find live host:

```shell
nmap -sn <subnet>
```

Connect:

```shell
nc <host> <port>
```

## Scan 2

Tune `nmap` to find live host:

```shell
nmap -sn <subnet> --min-rate 10000 -T5 --max-retries 1
```

Connect:

```shell
nc <host> <port>
```
