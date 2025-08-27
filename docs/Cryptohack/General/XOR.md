# XOR

## 1. XOR Starter

```python
print("".join([chr(13^ord(c)) for c in "label"]))
```

## 2. XOR Properties

```python
# F = (F^K1^K2^K3)^(K2^K3)^K1
num = int("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf",16)^int("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1",16)^int("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313",16)
hex = hex(num)[2::]
flag = bytes.fromhex(hex).decode()
print(flag)
```

## 3. Favorite Byte

```python
hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
flag = bytes.fromhex(hex).decode()

for byte in range(256):
    print("".join([chr(ord(x)^byte) for x in flag]))

```

## 4. You either know, XOR you don't

```python
hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
flag = bytes.fromhex(hex).decode()

# print(chr(ord(flag[0])^ord('c')))
# print(chr(ord(flag[1])^ord('r')))
# print(chr(ord(flag[2])^ord('y')))
# print(chr(ord(flag[3])^ord('p')))
# print(chr(ord(flag[4])^ord('t')))
# print(chr(ord(flag[5])^ord('o')))
# print(chr(ord(flag[6])^ord('{')))
# print(chr(ord(flag[-1])^ord('}')))

key = "myXORkey"
for i in range(len(flag)):
    print(chr(ord(flag[i])^ord(key[i%len(key)])),end='')
```

## 5. Lemur XOR

```python
import cv2 as cv

img1 = cv.imread("flag.png")
img2 = cv.imread("lemur.png")

# print(img1.shape,img2.shape) # Same shape

xorimg = img1^img2

cv.imshow("XOR",xorimg)
cv.waitKey(0)
```
