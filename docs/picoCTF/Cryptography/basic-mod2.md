# basic-mod2

```python
from Crypto.Util.number import inverse

with open('message.txt', 'r') as file:
    l = file.read().split()
    print(l)

    for num in l:
        num = int(num)%41
        num = inverse(num,41)
        if num <= 26:
            print(chr(num-1+ord('A')), end='')
        elif num <= 36:
            print(num-27, end='')
        else:
            print('_', end='')
```
