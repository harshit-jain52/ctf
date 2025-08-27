# flags are stepic

`Hint: In the country that doesn't exist, the flag persists`

Among all the countries shown, *Upanzi Republic* doesn't exist. Download its flag (upz.png) \
Challenge name is a clear hint to *Stepic* Steganography

```python
import stepic
from PIL import Image

img = Image.open('upz.png')
hidden_data = stepic.decode(img)
print(hidden_data)
```
