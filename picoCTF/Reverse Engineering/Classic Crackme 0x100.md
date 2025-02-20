# Classic Crackme 0x100

1. Start gdb, `break` at main, `run`, and `disas` main
2. We see a *memcmp* at the end of code, the result of which seems to make the program jump to print success or failure message:

    ```gdb
    0x0000000000401364 <+494>:  mov    %rcx,%rsi
    0x0000000000401367 <+497>:  mov    %rax,%rdi
    0x000000000040136a <+500>:  call   0x401060 <memcmp@plt>
    0x000000000040136f <+505>:  test   %eax,%eax
    ```

3. Set a breakpoint and look at the arguments of memcmp:

    ```gdb
    (gdb) b *main+500
    Breakpoint 2 at 0x40136a: file main_sample.c, line 32.
    (gdb) c
    Continuing.
    Enter the secret password: abcdef

    Breakpoint 2, 0x000000000040136a in main () at main_sample.c:32
    32  in main_sample.c
    (gdb) x/s $rsi
    0x7fffffffdd40: "ztqittwtxtieyfrslgtzuxovlfdnbrsnlrvyhhsdxxrfoxnjbl"
    (gdb) x/s $rdi
    0x7fffffffdd00: "aefjhlTWQTvWTWWZQVTWTWWZTWQZWZZ]QTNWTWWZTW]ZWZZ]TY"
    ```

    Multiple runs with different password input print the same *$rsi* but different *$rdi* \
    On checking, *$rsi* is not the password, but could be an encoded form of it
4. The final value of *$rsi* could be a shift of what is entered, and this can be verified by inputs "aaaaaaaaaaaaaaa..." and "bbbbbbbbbbbbb.."
5. Simple python script to reverse the shifting:

    ```python
    s = "ruuxuxxauxxaxaaduxxaxaadxaadaddguxxaxaadxaadaddgxa" # $rsi
    t = 'r'*len(s) # input

    l = [(ord(t[i]) - ord(s[i]) + 26) % 26 for i in range(len(s))]

    f = 'ztqittwtxtieyfrslgtzuxovlfdnbrsnlrvyhhsdxxrfoxnjbl' # $rdi

    ans = [chr((ord(f[i]) - ord('a') + l[i]) % 26 + ord('a')) for i in range(len(f))]
    print(''.join(ans))
    ```
