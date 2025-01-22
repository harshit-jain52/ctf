# TLS Part 1: The Protocol

## 4. Saying Hello

```shell
curl --tls-max 1.2 -v https://tls1.cryptohack.org
```

```shell
openssl s_client -tls1_2 -connect tls1.cryptohack.org:443
```

## 5. Decrypting TLS 1.2

1. Open tha capture file in Wireshark
2. Edit -> Preferences -> RSA Keys -> Add new keyfile -> Select the .pem file containing private key
3. Filter the packets: `http2`
4. Check out the packet no. 27

## 6. Decrypting TLS 1.3

1. Open tha capture file in Wireshark
2. Edit -> Preferences -> Protocols -> TLS -> (Pre)-Master-Secret log filename -> Select the keylogfile
3. Filter the packets: `http2`
4. Check out the packet no. 27
