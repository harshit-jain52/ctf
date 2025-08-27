# Shaken, Not Stirred

```text
After all that cake, I think it's time to sit back, relax, and have a drink 🍸 One vodka martini, please - shaken, not stirred of course!

...Aw man, I just saw the bartender add something strange, I just wanted a good old classic. Wonder if I can demix it and get it out 🤔
```

`encrypt.py`:

```python
import random
import sys
import time

### HELPER FUNCTIONS - IGNORE ###
def shake():
    time.sleep(0.5)
    for i in range(15):
        sys.stdout.write(f"    {' ' * (i % 3)}🪇 Shaking 🪇")
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write("\b" * 20)
        sys.stdout.write(" " * 20)
        sys.stdout.write("\b" * 20)

def printer(s):
    time.sleep(0.5)
    print(s)


### PROGRAM ###
printer("🍸 Welcome to the Martini MiXOR 3000! 🍸\n")

ingredients = [
    "🫗 Vodka",
    "🍾 Dry Vermouth",
    "🫙 Olive Brine",
    "🫒 Olive",
    "🥢 Toothpick",
]

printer("Adding ingredients to the shaker...")
shaker = 0
for ingredient in ingredients:
    # Mix ingredients together
    shaker ^= len(ingredient) * random.randrange(18)
    printer(f"  {ingredient}")

printer("  🏺 Secret ingredient\n")
with open("flag.txt", "rb") as f:
    secret = f.read().strip()
drink = bytes([b ^ shaker for b in secret])

# Shake well!
shake()
shake()
shake()

if all(32 < d < 127 for d in drink):
    printer("Drink's ready! Shaken, not stirred:")
    printer(f"🍸 {drink.decode()} 🍸")
else:
    printer("🫗 Oops! Shook your drink too hard and spilled it 🫗")
```

`output.txt`:

```text
🍸 Welcome to the Martini MiXOR 3000! 🍸

Adding ingredients to the shaker...
  🫗 Vodka
  🍾 Dry Vermouth
  🫙 Olive Brine
  🫒 Olive
  🥢 Toothpick
  🏺 Secret ingredient

Drink's ready! Shaken, not stirred:
🍸 wg`{{pgna}&J{!x&2fJWg`{{&g;;;_!x&fJWg`{{&gh 🍸
```

`decrypt.py`

```python
import random

ingredients = [
    "🫗 Vodka",
    "🍾 Dry Vermouth",
    "🫙 Olive Brine",
    "🫒 Olive",
    "🥢 Toothpick"
]

while True:
    shaker = 0
    for ingredient in ingredients:
        shaker ^= len(ingredient) * random.randrange(18)

    secret = b"wg`{{pgna}&J{!x&2fJWg`{{&g;;;_!x&fJWg`{{&gh"
    drink = bytes([b ^ shaker for b in secret])

    if all(32 < d < 127 for d in drink):
        flag = drink.decode()
        if "brunner{" in flag:
            print(flag)
            break
```
