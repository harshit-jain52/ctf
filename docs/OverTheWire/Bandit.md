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

## level 12 -> level 13

```shell
xxd -r data.txt > data
file data
> data: gzip compressed data, was "data2.bin", last modified: Fri Aug 15 13:15:53 2025, max compression, from Unix, original size modulo 2^32 584
mv data data.gz
gzip -d data.gz
file data
> data: bzip2 compressed data, block size = 900k
mv data data.bz2
bzip2 -d data.bz2
file data
> data: gzip compressed data, was "data4.bin", last modified: Fri Aug 15 13:15:53 2025, max compression, from Unix, original size modulo 2^32 20480
mv data data.gz
gzip -d data.gz
file data
> data: POSIX tar archive (GNU)
mv data data.tar
tar -xvf data.tar
> data5.bin
file data5.bin
> data5.bin: POSIX tar archive (GNU)
tar -xvf data5.bin
> data6.bin
file data6.bin
> data6.bin: bzip2 compressed data, block size = 900k
bzip2 -d data6.bin
> bzip2: Can't guess original name for data6.bin using data6.bin.out
file data6.bin.out
> data6.bin.out: POSIX tar archive (GNU)
tar -xvf data6.bin.out
> data8.bin
file data8.bin
> data8.bin: gzip compressed data, was "data9.bin", last modified: Fri Aug 15 13:15:53 2025, max compression, from Unix, original size modulo 2^32 49
mv data8.bin data8.bin.gz
gzip -d data8.gz
file data8
> data8: ASCII text
```

## level 13 -> level 14

```shell
cat sshkey.private
```

Password is not accessible, we got a private sshkey for next level

```shell
ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220
```

## level 14 -> level 15

```shell
cat /etc/bandit_pass/bandit14 | nc localhost 30000
```

## level 15 -> level 16

```shell
cat /etc/bandit_pass/bandit15 | ncat --ssl localhost 30001
```

## level 16 -> level 17

```shell
nmap -p 31000-32000 --script ssl-enum-ciphers localhost
```

Possible ports: 31518, 31790

```shell
cat /etc/bandit_pass/bandit16 | ncat --ssl localhost 31518
cat /etc/bandit_pass/bandit16 | ncat --ssl localhost 31790
```

Port 31790 gives a private ssh key

## level 17 -> level 18

```shell
diff passwords.old passwords.new 
```

## level 18 -> level 19

```shell
ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat readme"
```

## level 19 -> level 20

```shell
./bandit20-do cat /etc/bandit_pass/bandit20
```

## level 20 -> level 21

```shell
cat /etc/bandit_pass/bandit20 | nc -l -p 12345
```

```shell
./suconnect 12345
```

## level 21 -> level 22

```shell
bandit21@bandit:~$ cd /etc/cron.d/

bandit21@bandit:/etc/cron.d$ ls
behemoth4_cleanup  cronjob_bandit23  leviathan5_cleanup    sysstat
clean_tmp          cronjob_bandit24  manpage3_resetpw_job
cronjob_bandit22   e2scrub_all       otw-tmp-dir

bandit21@bandit:/etc/cron.d$ cat cronjob_bandit22 
@reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null

bandit21@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit22.sh
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv

bandit21@bandit:/etc/cron.d$ cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
```

## level 22 -> level 23

```shell
bandit22@bandit:~$ cat /etc/cron.d/cronjob_bandit23 
@reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
* * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null

bandit22@bandit:~$ cat /usr/bin/cronjob_bandit23.sh
#!/bin/bash
myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)
echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"
cat /etc/bandit_pass/$myname > /tmp/$mytarget

bandit22@bandit:~$ whoami
bandit22

bandit22@bandit:~$ echo I am user bandit23 | md5sum | cut -d ' ' -f 1
8ca319486bfbbc3663ea0fbe81326349

bandit22@bandit:~$ cat /tmp/8ca319486bfbbc3663ea0fbe81326349
```

## level 23 -> 24

```shell
bandit23@bandit:~$ cat /etc/cron.d/cronjob_bandit24 
@reboot bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
* * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
```

```shell
bandit23@bandit:~$ cat /usr/bin/cronjob_bandit24.sh
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname/foo
echo "Executing and deleting all scripts in /var/spool/$myname/foo:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23" ]; then
            timeout -s 9 60 ./$i
        fi
        rm -f ./$i
    fi
done
```

```shell
bandit23@bandit:~$ mktemp -d
/tmp/tmp.OAoC8cNtjQ

bandit23@bandit:~$ cd /tmp/tmp.OAoC8cNtjQ

bandit23@bandit:/tmp/tmp.OAoC8cNtjQ$ touch pass.txt

bandit23@bandit:/tmp/tmp.OAoC8cNtjQ$ vi script.sh

bandit23@bandit:/tmp/tmp.OAoC8cNtjQ$ cat script.sh 
#!/bin/bash
cat /etc/bandit_pass/bandit24 > /tmp/tmp.OAoC8cNtjQ/pass.txt

bandit23@bandit:/tmp/tmp.OAoC8cNtjQ$ chmod 777 -R /tmp/tmp.OAoC8cNtjQ

bandit23@bandit:/tmp/tmp.OAoC8cNtjQ$ cp script.sh /var/spool/bandit24/foo/
```

After a minute or so, password will be written into `pass.txt`
