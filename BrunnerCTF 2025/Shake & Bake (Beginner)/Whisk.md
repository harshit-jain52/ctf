# Whisk

> Crypto

```text
Someone tried sabotaging our operation by "whisking” away the secret ingredient for the perfect brunsviger. All that's left on the workbench is this sticky note full of pastry-themed symbols and random letters.

Can you help us recover the secret ingredient?
```

`whisk.txt`:

```text
DR🥐 C🥐TZ🥐D 🧁SXZ🥐A🧁🥐SD 🧁C 🍰KE🍰FC K🍩M🥐. D🍩 O🍰Q🥐 🍰 Y🥐ZP🥐TD
OZ🥖SCM🧁X🥐Z, H🥐KD O🥖DD🥐Z E🧁DR OZ🍩ES C🥖X🍰Z, Y🍩🥖Z 🧁D 🍩M🥐Z DR🥐 E🍰ZH
A🍩🥖XR, 🍰SA K🥐D DR🥐 CFZ🥖Y C🥐🥐Y 🧁SD🍩 🥐M🥐ZF T🍩ZS🥐Z. D🍰CD🥐, CH🧁K🥐,
🍰SA Z🥐H🥐HO🥐Z: CR🍰Z🧁SX Y🍰CDZF N🍩F 🧁C H🍰SA🍰D🍩ZF.
OZ🥖SS🥐Z{S0_H0Z3_K🥖HYF_T1YR3Z}
```

This is clearly a Substitution Cipher problem. Start with replacing "OZ🥖SS🥐Z{" with "BUNNER{", then try to replace characters to make valid English words

```python
sub_map = {
    'O': 'B',
    'Z': 'R',
    '🥖': 'U',
    'S': 'N',
    '🥐': 'E'
}
    
with open("whisk.txt", "r", encoding="utf-8") as f:
    content = f.read()

new_content = ""
for e in content:
    if e in sub_map:
        new_content += sub_map[e]
    else:
        new_content += e.lower()

print(new_content)
```

Keep adding to the `sub_map` and re-running till flag is deciphered

```python
sub_map = {
    'O': 'B',
    'Z': 'R',
    '🥖': 'U',
    'S': 'N',
    '🥐': 'E',
    'H': 'M',
    'D': 'T',
    'C': 'S',
    'R': 'H',
    'T': 'C',
    '🧁': 'I',
    'Y': 'P',
    'X': 'G',
    'K': 'L',
    'A': 'D',
    'E': 'W',
    'F': 'Y'
}
```
