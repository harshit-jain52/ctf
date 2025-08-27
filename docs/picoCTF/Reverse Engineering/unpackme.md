# packer

1. Trying `file` and `strings`:

    ```shell
    file unpackme-upx 
    >   unpackme-upx: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, no section header
    ```

    Can't use GDB as file is stripped

    ```shell
    strings unpackme-upx
    >   .
        .
        UPX!
        UPX!
    ```

    Hmm... It is packed with [UPX](https://linux.die.net/man/1/upx)

2. Unpack:

    ```shell
    upx -d unpackme-upx
    file unpackme-upx
    >   unpackme-upx: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, BuildID[sha1]=5e4be04529afcdb8fa8855e3138c3f51047fa123, for GNU/Linux 3.2.0, not stripped
    ```

    "not stripped" yay! GDB time now

3. `break` at main, `run`, and `disas`:

    ```gdb
    .
    .
    0x0000000000401ec0 <+125>:  call   0x410d30 <__isoc99_scanf>
    0x0000000000401ec5 <+130>:  mov    -0x3c(%rbp),%eax
    0x0000000000401ec8 <+133>:  cmp    $0xb83cb,%eax
    0x0000000000401ecd <+138>:  jne    0x401f12 <main+207>
    .
    .
    ```

    Seems the desired number is 0xb83cb = 754635
