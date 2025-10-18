# SmartCoffee

## Files Provided

A binary `firmware_x86.elf` and `logs.txt`

## Approach

Executing the binary gives the following output:

```text
Initializing ADC... OK
I2C devices found: 2
Loading EEPROM... OK
Device Serial: SC-01-ABC123
EEPROM DUMP (raw):
95 aa 95 97 a1 a7 bf f7 
bc 9b b7 f7 b7 aa b1 a9 
9b a7 f0 aa 9b a0 f4 9b 
ac f0 b6 a0 b3 f0 b6 f7 
b9 
(Note: bytes are likely obfuscated.)
Entering diagnostic loop...
diag_ok
diag_ok
diag_ok
```

We know the flag format is `QnQSec{...}`, and the 1st & 3rd byte in the dump are same. The obfuscation could be XOR

## Solve Script

```python
dump = """
95 aa 95 97 a1 a7 bf f7 
bc 9b b7 f7 b7 aa b1 a9 
9b a7 f0 aa 9b a0 f4 9b 
ac f0 b6 a0 b3 f0 b6 f7 
b9
"""

data = bytes(int(byte, 16) for byte in dump.split())
key = ord('Q') ^ 0x95
decoded = bytes(byte ^ key for byte in data)
print(decoded.decode('utf-8'))
```
