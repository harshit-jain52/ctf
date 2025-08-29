# DoughBot

> Forensics

```text
Our state-of-the-art smart mixer, DoughBot, crashed during a routine kneading cycle. Luckily, a technician was monitoring the device over UART and captured the memory output just before the reboot.

Analyze the captured dump and see what the DoughBot was trying to say before it rebooted.
```

points: `20`

solves: `704`

author: `rvsmvs`

---

We are provided with a file: `doughbot_dump.bin`

It contains a line: `// dev.note: bootlog_flag=YnJ1bm5lcnttMXgzZF9zMWduYWxzXzRfc3VyZX0=`

Decoding (`echo "YnJ1bm5lcnttMXgzZF9zMWduYWxzXzRfc3VyZX0" | base64 -d`) gives the flag
