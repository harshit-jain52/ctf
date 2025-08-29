# Bandit

## level 0

```shell
ssh bandit0@bandit.labs.overthewire.org -p 2220
```

## level 0 -> level 1

```shell
cat readme
```

## level 1 -> level 2

[Dashed file names](https://stackoverflow.com/questions/42187323/how-to-open-a-dashed-filename-using-terminal)

```shell
cat < -
```

## level 2 -> level 3

```shell
cat < "--spaces in this filename--"
```

## level 3 -> level 4

```shell
ls -a
cd inhere/
ls -a
cat ...Hiding-From-You
```

## level 4 -> level 5

```shell
cd inhere/
find . -type f -exec file --mime {} + | grep 'text/'
> ./-file07: text/plain; charset=us-ascii
  ./-file00: text/plain; charset=unknown-8bit
cat < -file07
```

## level 5 -> level 6

```text
human-readable
1033 bytes in size
not executable
```

```shell
find inhere/ -type f -size 1033c ! -executable -exec file --mime {} + | grep 'text/'
> inhere/maybehere07/.file2: text/plain; charset=us-ascii
cat inhere/maybehere07/.file2
```

## level 6 -> level 7

```text
owned by user bandit7
owned by group bandit6
33 bytes in size
```

```shell
find / -type f -size 33c -user bandit7 -group bandit6
cat /var/lib/dpkg/info/bandit7.password
```

## level 7 -> level 8

```shell
grep "millionth" data.txt
```

## level 8 -> level 9

```shell
sort data.txt | uniq -c | sort -n | head 
```

## level 9 -> level 10

```shell
strings data.txt | grep "==="
```

## level 10 -> level 11

```shell
base64 -d data.txt
```

## level 11 -> level 12

```shell
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```
