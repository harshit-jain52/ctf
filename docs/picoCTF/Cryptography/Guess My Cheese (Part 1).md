# Guess My Cheese (Part 1)

`Hint: Remember that cipher we devised together Squeexy? The one that incorporates your affinity for linear equations???`

Clearly, **Affine Cipher**

Use the oracle to encrypt types of cheese (Google it), I used *FETA* and *BLUE*, to get mappings of characters with small value, i.e., 'A' and 'B' \

```text
Suppose, 'A'(= 0) -> x and 'B'(= 1) -> y \
a*0 + b = x mod 26 => b = x
a*1 + b = y mod 26 => a = (y-x)mod 26
```

Use these values on [online tools](https://cryptii.com/) to decipher the secret
