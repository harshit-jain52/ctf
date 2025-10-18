# baby_baby_reverse

## Files Provided

A binary `main`

## Approachh

Decompiled the binary [online](https://dogbolt.org/)

```c
int32_t main(int32_t argc, char** argv, char** envp)
{
    void* fsbase;
    int64_t rax = *(fsbase + 0x28);
    int64_t var_228;
    __builtin_strcpy(&var_228, "Th1s_1s_th3_k3y");
    printf("Enter flag: ", argv, 0x79336b5f336874);
    char buf[0x208];
    int32_t result;
    
    if (fgets(&buf, 0x200, __TMC_END__))
    {
        uint64_t var_248_1 = strlen(&buf);
        
        if (var_248_1 && buf[var_248_1 - 1] == 0xa)
        {
            buf[var_248_1 - 1] = 0;
            var_248_1 -= 1;
        }
        
        if (var_248_1 == 0x29)
        {
            char var_24b_1 = 1;
            char var_24a_1 = 0;
            
            for (int64_t i = 0; i < 0x29; i += 1)
                var_24a_1 |= *(i + &encrypted) ^ *(&var_228 + COMBINE(0, i) % 0xf) ^ buf[i];
            
            char var_24b_2;
            
            var_24b_2 = var_24a_1 ? 0 : 1;
            
            if (!var_24b_2)
                puts("Wrong!");
            else
                puts("Correct!");
            
            result = 0;
        }
        else
        {
            puts("Wrong!");
            result = 0;
        }
    }
    else
    {
        puts("Input error");
        result = 1;
    }
    
    *(fsbase + 0x28);
    
    if (rax == *(fsbase + 0x28))
        return result;
    
    __stack_chk_fail();
    /* no return */
}
```

Find the address of `encrypted`:

```shell
readelf -sW main | grep -i encrypted
```

## Solve Script

```python
from pwn import ELF
import sys

binpath = "./main"
e = ELF(binpath)
addr = 0x4060
length = 41
data = e.read(addr, length)
key = b"Th1s_1s_th3_k3y"
flag = bytes([ data[i] ^ key[i % len(key)] for i in range(length) ])
print(flag.decode('utf-8', errors='replace'))
```
