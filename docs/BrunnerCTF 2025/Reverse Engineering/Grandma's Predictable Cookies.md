# Grandma's Predictable Cookies

```text
Grandma encrypted her secret cookie recipe using her "special ingredient" a random number generator seeded with the exact time she baked it.

She thought it was uncrackable. But little did she know: Using the same oven clock every time makes your cookies easy to reverse-engineer.

Can you recover her delicious secret?
```

points: `100`

solves: `232`

author: `H4N5`

---
We are given a binary, and a `flag.enc` file:

```text
Encrypted flag: 3ec63cc41f1ac1980651726ab3ce2948882b879c19671269963e39103c83ebd6ef173d60c76ee5
Encryption time (approx): 1755860000
```

Decompiled using BinaryNinja on dogbolt:

```c
time_t rax_6 = get_current_time_danish();
srand(rax_6);

for (int32_t i = 0; i <= 0x3e7; i += 1)
    rand();

int64_t var_58_1 = rax_1 - 1;
void* rsp_1 = &buf - COMBINE(0, rax_1 + 0xf) / 0x10 * 0x10;

for (void* i_1 = nullptr; i_1 < rax_1; i_1 += 1)
{
    int32_t rax_19 = rand();
    *(i_1 + rsp_1) = *(i_1 + &buf) ^ rax_19;
}

printf("Encrypted flag: ");

for (void* i_2 = nullptr; i_2 < rax_1; i_2 += 1)
    printf("%02x", *(i_2 + rsp_1));

printf("\nEncryption time (approx): %ld\n", rax_6 / 0x2710 * 0x2710);
```

1. Timestamp is used as seed of random number generator. This timestamp, after decreasing precision, is printed at the end: 1755860000
2. 1000 (0 to 0x3e7=999) random integers are generated
3. Each byte of the flag is XOR'd with a newly generated random number, and the result's hex is printed

`decode.c`:

```c
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
  time_t timestamp = atoi(argv[1]);
  char hexstr[1024] = "3ec63cc41f1ac1980651726ab3ce2948882b879c19671269963e39103c83ebd6ef173d60c76ee5";

  srand(timestamp);
  for (int i = 0; i <= 999; ++i) rand();
  size_t len = strlen(hexstr);

  for (size_t i = 0; i < len; i += 2)
  {
    unsigned int byte;
    sscanf(hexstr + i, "%2x", &byte);
    int v5 = rand();
    byte ^= (unsigned int)(v5);
    printf("%c", byte);
  }
  printf("\n");

  return 0;
}
```

Brute force all the possible timestamps, flag is one of the outputs:

```shell
#!/bin/bash

CFILE="decode.c"

gcc "$CFILE" -o decode

for sec in {1755860000..1755869999}; do
    ./decode $sec
done
```
