# OldMeetsNew

> Does it kind of defeat the purpose of me learning Morse code if I have to send it as a WAV anyway? Especially when the file won't even load properly!

- We are given a wav file, which doesn't open due to format error
- Looking at the header of the file, we notice **WIFF** at the start. For a wav file, it should be **RIFF**. Updating it fixes the format error, and we can listen to the morse code audio
- Use [Morse Code Decoder](https://morsecode.world/international/decoder/audio-decoder-adaptive.html) to get the text, which looks base32/64-encoded
- Decoding (base32) gives the flag
