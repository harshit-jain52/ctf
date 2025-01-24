# Interencdec

```python
import base64

with open("enc_flag", "r") as f:
    enc_flag = f.read().strip()
    f = base64.b64decode(enc_flag)
    f = str(f)[4:-4]
    f = base64.b64decode(f)
    f = str(f)[2:-1]


    def shift_letter(c, shift):
        if 'a' <= c <= 'z':
            return chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            return chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
        else:
            return c

    def shift_text(text, shift):
        return ''.join(shift_letter(c, shift) for c in text)

    for i in range(26):
        print(shift_text(f, i))
```
