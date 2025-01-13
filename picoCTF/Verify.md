# Verify

1. Get `checksum` of the file to find from `checksum.txt`
2. Find the file:

    ```shell
    sha256sum files/* | grep "<checksum>"
    ```

3. Flag:

    ```shell
    decrypt.sh files/<filename>
    ```
