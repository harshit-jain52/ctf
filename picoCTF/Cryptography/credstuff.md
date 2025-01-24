# credstuff

1. Get line number:

    ```shell
    grep -n "cultiris" usernames.txt
    ```

2. Get the password:

    ```shell
    head -n <lineno> passwords.txt | tail -n 1
    ```

3. ROT13
