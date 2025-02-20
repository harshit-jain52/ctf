# packer

1. Trying `file` and `strings`:

    ```shell
    file out
    >   out: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, no section header
    ```

    Can't use GDB as file is stripped

    ```shell
    strings out
    >   .
        .
        UPX!
        UPX!
    ```

    Hmm... It is packed with [UPX](https://linux.die.net/man/1/upx)

2. Unpack:

    ```shell
    upx -d out
    file out
    >   out: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, BuildID[sha1]=fedfa2b06929b414534771a3fdd291559e1190b1, for GNU/Linux 3.2.0, not stripped
    ```

    "not stripped" yay! GDB time now

3. `break` at main, `run`, and `disas`:

    ```gdb
    .
    .
    0x0000000000401f47 <+482>:  test   %eax,%eax
    0x0000000000401f49 <+484>:  jne    0x401f65 <main+512>
    .
    .
    ```

    The result of test seems to decide the final jump..

4. Change the value of *$eax*:

    ```gdb
    (gdb) b *main+482
    Breakpoint 2 at 0x401f47
    (gdb) c
    Continuing.
    Enter the password to unlock this file: random
    You entered: random


    Breakpoint 2, 0x0000000000401f47 in main ()
    (gdb) set $rax=0
    (gdb) c
    Continuing.
    Password correct, please see flag: 7069636f4354467b5539585f556e5034636b314e365f42316e34526933535f33373161613966667d
    ```

5. Convert hex to ASCII

    ```shell
    echo "7069636f4354467b5539585f556e5034636b314e365f42316e34526933535f33373161613966667d" | xxd -r -p
    ```
