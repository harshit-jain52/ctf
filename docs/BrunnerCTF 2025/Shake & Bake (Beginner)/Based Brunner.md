# Based Brunner

> Misc

```text
Brunsviger is just so based, I think I could eat it in any form - from binary to decimal!
```

points: `50`

solves: `331`

author: `Nissen`

---

`based.txt` and `encode.py` given:

```python
def encode_char(ch: str, base: int) -> str:
    """
    Encode a single character into a string of digits in the given base
    """
    value = ord(ch)
    digits = []
    while value > 0:
        digits.append(str(value % base))
        value //= base

    return "".join(reversed(digits))


with open("flag.txt") as f:
    text = f.read().strip()

# Encode the text with all bases from decimal to binary
for base in range(10, 1, -1):
    text = " ".join(encode_char(ch, base) for ch in text)

with open("based.txt", "w") as f:
    f.write(text)
```

Reverse logic to `decode.py`:

```python
def encode_char(ch: str, base: int) -> str:
    """
    Encode a single character into a string of digits in the given base
    """
    value = ord(ch)
    digits = []
    while value > 0:
        digits.append(str(value % base))
        value //= base

    return "".join(reversed(digits))


with open("based.txt") as f:
    text = f.read().strip()

for base in range(2, 11):
    curr = ""
    nums = []
    for c in text.split():
        if c == encode_char(' ', base):
            nums.append(curr)
            curr = ""
        else:
            ascii = int(c, base)
            # print(ascii)
            curr += chr(ascii)

    nums.append(curr)
    text = " ".join(nums)

print(text)
```
