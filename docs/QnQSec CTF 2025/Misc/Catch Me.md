# Catch Me

## Files Provided

A GIF of many QRs

![gif](../media/qrs.gif)

## Approach

Converted the GIF to a collection of JPGs [online](https://www.iloveimg.com/convert-to-jpg/gif-to-jpg)

Scanning every QR displayed a text looked like Base64-decoding

## Solve Script

```python
import os
import base64
from pyzbar.pyzbar import decode
from PIL import Image

dir_path = "iloveimg-converted"

for filename in sorted(os.listdir(dir_path)):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        file_path = os.path.join(dir_path, filename)
        img = Image.open(file_path)
        result = decode(img)

        if result:
            for r in result:
                qr_data = r.data.decode("utf-8")
                try:
                    decoded = base64.b64decode(qr_data).decode("utf-8")
                    print(decoded)
                except Exception as e:
                    pass
```
