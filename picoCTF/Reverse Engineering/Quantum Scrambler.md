# Quantum Scrambler

```python
import pwn
conn = pwn.remote('verbal-sleep.picoctf.net', 61849)
cypher = conn.recvline().decode().strip()
conn.close()
# print(cypher)
L = eval(cypher)
for x in L:
    if(type(x[0]) == str):
        print(chr(int(x[0], 16)), end='')
    if(type(x[-1]) == str):
        print(chr(int(x[-1], 16)), end='')
    elif(type(x[-1]) == list and type(x[-1][0]) == str):
        print(chr(int(x[-1][0], 16)), end='')
```
