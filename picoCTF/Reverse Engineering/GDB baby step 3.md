# GDB baby step 3

Give executing permission and start gdb; break at main and run

1. Disassemble main(): `disas main`

   ```gdb
   .
   .
   0x0000000000401111 <+11>:   mov    %rsi,-0x20(%rbp)
   0x0000000000401115 <+15>:   movl   $0x2262c96b,-0x4(%rbp)
   0x000000000040111c <+22>:   mov    -0x4(%rbp),%eax
   .
   .
   ```

2. Set a breakpoint after movl: `break *main+22`

3. Examine the bytes: `x/4xb $rbp-4`
