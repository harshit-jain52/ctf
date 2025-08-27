# substitution0

```python
with open("message.txt", "r") as file:
    key = file.readline().strip()
    message = file.read().strip()

    for c in message:
        if c.isalpha():
            if c.islower():
                print(chr(key.index(c.upper()) + ord('a')).lower(), end="")
            else:
                print(chr(key.index(c) + ord('A')), end="")
        else:
            print(c, end="")
```
