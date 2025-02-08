# collision

1. `ls -la` and `file` commands tell us there are three files:

   1. An executable `col`
   2. A C file: `col.c`
   3. An inaccessible file: `flag`
2. `cat col.c` : observing the source code tells us that the program accepts a 20-bytes cmd arg which is converted from `const char*` to `int*`, 20 chars giving 5 integers, whose sum is compared to hashcode `0x21DD09EC`.
3. `0x21DD09EC` is not divisible by 5, so we can write it as `0x06C5CEC8 * 4 + 0x06C5CECC`
4. Due to **little-endianness**, we input the reverse of every 4 bytes:

   ```bash
   ./col `python -c "print('\xc8\xce\xc5\x06'*4+'\xcc\xce\xc5\x06')"`
   ```
