# Encoding

## 1. ASCII

```python
print(''.join([chr(x) for x in [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]]))
```

## 2. Hex

```python
print(bytes.fromhex('63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'))
```

## 3. Base64

```shell
echo "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf" | xxd -r -p | base64
```

## 4. Bytes and Big Integers

```shell
echo "obase=16; ibase=10; 11515195063862318899931685488813747395775516287289682636499965282714637259206269" | bc | xxd -r -p
```

## 5. Encoding Challenge

```python
from pwn import *
import json
import base64
import codecs
from Crypto.Util.number import *

r = remote('socket.cryptohack.org', 13377, level='debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


for i in range(100):
    received = json_recv()
    match received["type"]:
        case "base64":
            decoded = base64.b64decode(received["encoded"]).decode()
        case "hex":
            decoded = bytes.fromhex(received["encoded"]).decode()
        case "rot13":
            decoded = codecs.decode(received["encoded"], 'rot_13')
        case "bigint":
            decoded = long_to_bytes(int(received["encoded"], 16)).decode()
        case "utf-8":
            decoded = "".join([chr(b) for b in received["encoded"]])

    to_send = {
        "decoded": decoded
    }
    json_send(to_send)

received = json_recv()
```
