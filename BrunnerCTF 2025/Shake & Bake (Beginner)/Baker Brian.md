# Baker Brian

> Reverse Engineering

```text
Baker Brian says he has a plan to make him super rich, but he refuses to share any details 😠 Can you access his Cake Vault where he keeps all his business secrets?
```

We are given a file `auth.py`, which is used to check username and password on the server where the flag is

```python
if username != "Br14n_th3_b3st_c4k3_b4k3r":
    print("❌ Go away, only Baker Brian has access!")
    exit()
```

So, **Username**: `Br14n_th3_b3st_c4k3_b4k3r`

```python
words = password.split("-")

if not (
    len(words) > 0 and
    words[0] == "red"
):
    print("❌ Word 1: Wrong - get out!")
    exit()
```

**Password**: `red-`

```python
if not (
    len(words) > 1 and
    words[1][::-1] == "yromem"
):
    print("❌ Word 2: Wrong - get out!")
    exit()
```

**Password**: `red-memory-`

```python
if not (
    len(words) > 2 and
    len(words[2]) == 5 and
    words[2][0] == "b" and
    words[2][1] == "e" and
    words[2][2:4] == "r" * 2 and
    words[2][-1] == words[1][-1]
):
    print("❌ Word 3: Wrong - get out!")
    exit()
```

**Password**: `red-memory-berry-`

```python
if not (
    len(words) > 3 and
    words[3] == words[0][:2] + words[1][:3] + words[2][:3]
):
    print("❌ Word 4: Wrong - get out!")
    exit()
```

**Password**: `red-memory-berry-remember`
