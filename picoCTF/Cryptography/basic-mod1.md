# basic-mod1

```python
with open('message.txt', 'r') as file:
    l = file.read().split()
    print(l)

    for num in l:
        num = int(num)%37
        if num < 26:
            print(chr(num+ord('A')), end='')
        elif num < 36:
            print(num-26, end='')
        else:
            print('_', end='')
```
