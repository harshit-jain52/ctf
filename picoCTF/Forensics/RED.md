# RED

`Hint 3: Check whatever Facebook is called now.`

Checking METAdata:

```shell
exiftool red.png
> Poem                            : Crimson heart, vibrant and bold,.Hearts flutter at your sight..Evenings glow softly red,.Cherries burst with sweet life..Kisses linger with your warmth..Love deep as merlot..Scarlet leaves falling softly,.Bold in every stroke.
strings red.png
>   Crimson heart, vibrant and bold,
    Hearts flutter at your sight.
    Evenings glow softly red,
    Cherries burst with sweet life.
    Kisses linger with your warmth.
    Love deep as merlot.
    Scarlet leaves falling softly,
    Bold in every stroke.x

```

```text
Poem: Crimson heart, vibrant and bold,.
    Hearts flutter at your sight..
    Evenings glow softly red,.
    Cherries burst with sweet life..
    Kisses linger with your warmth..
    Love deep as merlot..
    Scarlet leaves falling softly,.
    Bold in every stroke.
```

-> *C H E C K L S B*, hmmm..

Head on to CyberChef, **Extract LSB** with coulour pattern RGBA (`Hint 2: Red?Ged?Bed?Aed?`), decode (base64) the output
