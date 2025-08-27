# reverse

1. `break` at main, `run`, and `disas`:

    ```gdb
    .
    .
    0x000055555555527e <+181>:  test   %eax,%eax
    0x0000555555555280 <+183>:  jne    0x55555555529c <main+211>
    .
    .
    ```

    The result of test seems to decide the final jump..

2. Change the value of *$eax*:

    ```gdb
    (gdb) b *main+181
    Breakpoint 2 at 0x55555555527e
    (gdb) c
    Continuing.
    Enter the password to unlock this file: flag
    You entered: flag

    Breakpoint 2, 0x000055555555527e in main ()
    (gdb) set $rax=0
    (gdb) c
    Continuing.
    Password correct, please see flag: picoCTF{3lf_r3v3r5ing_succe55ful_7851ef7d}
    ```
