# flag

1. Download, give permission and run:

    ```shell
    wget http://pwnable.kr/bin/flag
    chmod 777 flag
    ./flag
    >   I will malloc() and strcpy the flag there. take it.
    ```

2. Trying `file` and `strings`:

    ```shell
    file flag
    >   flag: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, no section header
    ```

    Can't use GDB as file is stripped

    ```shell
    strings flag
    >   .
        .
        $Info: This file is packed with the UPX executable packer http://upx.sf.net $
        $Id: UPX 3.08 Copyright (C) 1996-2011 the UPX Team. All Rights Reserved. $
        .
        .
        UPX!
        UPX!
    ```

    Hmm... What is [UPX](https://linux.die.net/man/1/upx)

3. Unpack:

    ```shell
    upx -d flag
    file flag
    >   flag: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, for GNU/Linux 2.6.24, BuildID[sha1]=96ec4cc272aeb383bd9ed26c0d4ac0eb5db41b16, not stripped
    ```

    "not stripped" yay! GDB time now

4. `break` at main, `run`, and `disas`:

    ```gdb
    Breakpoint 1, 0x0000000000401168 in main ()
    (gdb) disas
    Dump of assembler code for function main:
    0x0000000000401164 <+0>:    push   %rbp
    0x0000000000401165 <+1>:    mov    %rsp,%rbp
    => 0x0000000000401168 <+4>: sub    $0x10,%rsp
    0x000000000040116c <+8>:    mov    $0x496658,%edi
    0x0000000000401171 <+13>:   call   0x402080 <puts>
    0x0000000000401176 <+18>:   mov    $0x64,%edi
    0x000000000040117b <+23>:   call   0x4099d0 <malloc>
    0x0000000000401180 <+28>:   mov    %rax,-0x8(%rbp)
    0x0000000000401184 <+32>:   mov    0x2c0ee5(%rip),%rdx        # 0x6c2070 <flag>
    0x000000000040118b <+39>:   mov    -0x8(%rbp),%rax
    0x000000000040118f <+43>:   mov    %rdx,%rsi
    0x0000000000401192 <+46>:   mov    %rax,%rdi
    0x0000000000401195 <+49>:   call   0x400320
    0x000000000040119a <+54>:   mov    $0x0,%eax
    0x000000000040119f <+59>:   leave
    0x00000000004011a0 <+60>:   ret
    End of assembler dump.
    ```

5. Break at the end, and look at \<flag\>:

    ```gdb
    (gdb) b *main+60
    Breakpoint 2 at 0x4011a0
    (gdb) c
    Continuing.
    I will malloc() and strcpy the flag there. take it.

    Breakpoint 2, 0x00000000004011a0 in main ()
    (gdb) x/s *0x6c2070
    0x496628:   "UPX...? sounds like a delivery service :)"
    ```
