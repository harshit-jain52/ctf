# Tabby's Date

> Forensics

```text
Ohhhh, Tab, Tab, Tab.... what has she done. My friend Tabby just got a new laptop and she's been using it to take notes. She says she puts her whole life on there! She was so excited to finally have a date with a boy she liked, but she completely forgot the details of where and when. She told me she remembers writing it in a note... but she doesn't think she saved it!! She shared with us an export of her laptop files.
```

Zip Given:

```shell
tree C
```

```text
C
├── PerfLogs
├── ProgramData
│   └── Microsoft
│       └── Windows
│           └── Start Menu
│               └── Programs
│                   └── Accessories
├── Program Files
│   ├── Common Files
│   └── WindowsApps
├── Program Files (x86)
│   └── Common Files
├── Users
│   ├── Public
│   │   └── Desktop
│   └── Tabby
│       ├── AppData
│       │   ├── Local
│       │   │   ├── Microsoft
│       │   │   │   └── Windows
│       │   │   │       ├── Caches
│       │   │   │       ├── History
│       │   │   │       ├── INetCache
│       │   │   │       ├── Temporary Internet Files
│       │   │   │       └── UsrClass.dat
│       │   │   ├── Packages
│       │   │   │   ├── Microsoft.MicrosoftEdge_8wekyb3d8bbwe
│       │   │   │   │   └── LocalState
│       │   │   │   ├── Microsoft.WindowsNotepad_8wekyb3d8bbwe
│       │   │   │   │   └── LocalState
│       │   │   │   │       └── TabState
│       │   │   │   │           ├── 002d2531-9aff-42b1-b54d-b178c88063b4.bin
│       │   │   │   │           ├── 04165ca3-c82b-42ca-ab07-0c774ae66efd.bin
│       │   │   │   │           ├── 056941ef-d51d-4e57-9a55-b59d58bf3fcb.bin
│       │   │   │   │           ├── 14623d59-ad8c-43a8-b669-587f049a1516.bin
│       │   │   │   │           ├── 17de440f-3f69-4d8a-94fe-f3d4b9cf0c3f.bin
│       │   │   │   │           ├── 1aebb59c-5d51-41f1-918e-dec9e1a28ce1.bin
│       │   │   │   │           ├── 2d755c27-5840-47ad-a4ca-ed8041dd3047.bin
│       │   │   │   │           ├── 2e0dd6b6-ba93-4efc-9fd4-985dad74869a.bin
│       │   │   │   │           ├── 414e4071-60e6-4bb6-9a5a-f1e5bf6fe79c.bin
│       │   │   │   │           ├── 45dcdbe4-26b5-4e0b-ba2d-29e9e9c1e11b.bin
│       │   │   │   │           ├── 4f1c96a1-960c-4cee-9751-fe4b4f59fdd0.bin
│       │   │   │   │           ├── 5a57ac85-7e99-4bfc-9e13-f0d28a2bcc20.bin
│       │   │   │   │           ├── 66f955a8-6994-47c6-8326-0f128dafd0b9.bin
│       │   │   │   │           ├── 68d7e607-77c4-4d35-8ef2-0170a84efe5f.bin
│       │   │   │   │           ├── 68fefe2f-a7a6-4afa-b383-7fdc142aadde.bin
│       │   │   │   │           ├── 711f26f1-0eff-4a34-a78c-03562e44a36b.bin
│       │   │   │   │           ├── 7458196e-e979-4d94-982a-246fca3db028.bin
│       │   │   │   │           ├── 7ba066a2-e0cb-4c06-9339-316411a3da27.bin
│       │   │   │   │           ├── 9925cc8a-6440-4128-acae-f31541130a5e.bin
│       │   │   │   │           ├── 9bf7ca49-e491-4691-a21a-f3263bb695a2.bin
│       │   │   │   │           ├── 9e96bd4b-4155-4558-b97a-edcdf01d4584.bin
│       │   │   │   │           ├── a16d5079-b2f7-4a54-b3d5-b32256c4f238.bin
│       │   │   │   │           ├── a2048a5f-5cb5-460d-8ce6-70899de24d9c.bin
│       │   │   │   │           ├── a9da0602-fcd2-4793-9bab-70276e881006.bin
│       │   │   │   │           ├── af1fbc46-41cb-4d4b-9c34-02b874bfe9c6.bin
│       │   │   │   │           ├── b5074fe7-4f54-4728-afe9-1c063d211a82.bin
│       │   │   │   │           ├── b5154796-9d23-43ce-8a6c-c373e63f22c0.bin
│       │   │   │   │           ├── bcd5d203-1523-4b86-a572-c1c3afded478.bin
│       │   │   │   │           ├── c3cbe154-ef26-4e93-9183-c7fd323fe8c0.bin
│       │   │   │   │           ├── c4b77218-ef21-4a7f-9814-e4444f82475a.bin
│       │   │   │   │           ├── cb2f0c84-6293-4e63-8575-78dc879945e0.bin
│       │   │   │   │           ├── cd01dd8e-32f6-4f88-b9bb-4009afca3fea.bin
│       │   │   │   │           ├── dcfa4d00-41c8-439a-b1bd-2706dd8dbe0d.bin
│       │   │   │   │           ├── dea21c9d-4534-4d38-a60b-0a5c1b9b5928.bin
│       │   │   │   │           ├── e21dc9ae-2a03-42bf-8972-35ce8d524695.bin
│       │   │   │   │           ├── e6a849ab-6f02-452c-98e7-cdb03c577818.bin
│       │   │   │   │           ├── e86c9910-afca-4e83-87f6-600ed08a0570.bin
│       │   │   │   │           ├── ed9b5775-f35a-4770-a35e-e3c24b8bed47.bin
│       │   │   │   │           └── f1473e57-7637-4bd0-8158-53715ea20630.bin
│       │   │   │   └── Microsoft.Windows.Photos_8wekyb3d8bbwe
│       │   │   │       └── LocalState
│       │   │   └── Temp
│       │   ├── LocalLow
│       │   │   └── Microsoft
│       │   └── Roaming
│       │       └── Microsoft
│       │           └── Windows
│       │               ├── Recent
│       │               ├── Start Menu
│       │               │   └── Programs
│       │               └── Templates
│       ├── Desktop
│       │   └── desktop.ini
│       ├── Documents
│       │   └── desktop.ini
│       ├── Downloads
│       │   └── desktop.ini
│       ├── Favorites
│       ├── Links
│       ├── Music
│       │   └── desktop.ini
│       ├── NTUSER.DAT
│       ├── OneDrive
│       ├── Pictures
│       │   └── desktop.ini
│       ├── Saved Games
│       ├── Searches
│       └── Videos
│           └── desktop.ini
└── Windows
    ├── Fonts
    ├── Logs
    ├── System32
    │   └── drivers
    │       └── etc
    │           └── hosts
    ├── system.ini
    ├── SysWOW64
    ├── Temp
    └── win.ini
```

From the challenge description, it's clear we should look into the `.bin` files of Notepad LocalState

Printing the content of every file, we notice a few ASCII characters, including **{**,**}**. But these are obscured by a lot of null (`\x00`) characters.

Final solve script:

```python
import os

path = "C/Users/Tabby/AppData/Local/Packages/Microsoft.WindowsNotepad_8wekyb3d8bbwe/LocalState/TabState/"
for file in os.listdir(path):
    with open(os.path.join(path, file), "rb") as f:
        print(f.read().replace(b"\x00", b""))
```

Flag is present in the output
