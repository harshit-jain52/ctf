# Snooze

> Warmups

```text
Don't bug me, I'm sleeping! Zzzz... zzz... zzzz....
Uncover the flag from the file presented.
```

```shell
file snooze 
> snooze: compress'd data 16 bits
```

A bit of searching led to [this](https://fileinfo.com/extension/z)

```shell
mv snooze snooze.z
uncompress snooze.z
file snooze
> snooze: ASCII text
```

The text is the flag
