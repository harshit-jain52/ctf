# BakeDown

> Mobile

```text
I just shipped the very first build of my BakeDown app. I haven't done much with it yet, but I did pack it with a few nice resources already.

Try loading it onto your phone or an emulator to try it out!

Oh and btw, did you know an APK is just a ZIP file with assembled Java code and resources like strings, fonts, and images? I heard apktool might be a good tool for decoding the contents!
```

```shell
apktool d BakeDown.apk
cd BakeDown/
```

Search in text:

```shell
grep -Ri "brunner{" .
./res/values/strings.xml:    <string name="flag_part_1">brunner{Th1s_Sh0uld_B3_Th3_</string>
```

Search for images:

```shell
find . -type f \( -iname "*.png" -o -iname "*.jpg" -o -iname "*.webp" \)
.
.
./res/drawable/cake.png
.
.
```

![image](../images/cake.png)
