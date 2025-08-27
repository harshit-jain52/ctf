# GDB baby step 2

Give executing permission and start gdb; break at main and run

1. Disassemble main(): `disas main`
2. Set a breakpoint at the end of main, at the ret instruction: `break *0x<ins hex num>`
3. Look at the registers: `info r`
