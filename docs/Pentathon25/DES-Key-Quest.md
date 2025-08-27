# DES-Key-Quest

> Crypto - Easy

**Description**: Welcome to the world of block ciphers! Your mission is to uncover the secret key used in this challenge.

A text file given:

```text
DES-ECB:e1d5e1fcaae4aba0b735c8fb2ae8797728b073a34b14c57be236c819e6d5f4bbd94f5748ff9d1e008fcad8d403e23d02845a51513bb1e65027ed1bebdcb70973d411a0503cf06c261cb04e1ce1c12925
```

We only have the ciphertext and the encryption method; description asks to "uncover the secret key"; this hints towards a [weak-key DES problem](https://noob-atbash.github.io/CTF-writeups/cyberwar/crypto/chal-5.html)

The key `0xFFFFFFFFFFFFFFFF` worked!

```text
Hey you guessed the key right!! Heres the flag: flag{Y3MnH9qgcsTWY3MnH9qgcsTWw}
```
