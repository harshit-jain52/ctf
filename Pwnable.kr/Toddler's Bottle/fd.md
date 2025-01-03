# fd

1. `ls -la` and `file` commands tell us there are three files:
   1. An executable `fd`
   2. A C file: `fd.c`
   3. An inaccessible file: `flag`
2. `cat fd.c` : observing the source code tells us that the program accepts one cmd arg which, after being subtracted by `0x1234`, is supposed to be the **file descriptor** of a file whose first 32 bytes are read, which upon matching a particular string (also specified in the source) will reveal the contents of `flag`.
3. File descriptors:
   - *stdin* : 0
   - *stdout* : 1
   - *stderr* : 2
4. Run `./fd 4660` , type `LETMEWIN` and press ENTER.
