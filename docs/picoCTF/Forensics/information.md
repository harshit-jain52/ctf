# information

1. Check out metadata:

    ```shell
    exiftool cat.jpg
    ```

2. Value of License field seems b64-encoded; decode it:

    ```shell
    echo "<License>" | base64 -d
    ```
