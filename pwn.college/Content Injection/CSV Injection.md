# CSV Injection

## Teacher Login

```text

The Login
Welcome! Can you log in as teacher?

The User Database

USERNAME,IS_TEACHER
        

Add a User
Username:

Login
Username: 
```

The input fields are of **text** type

On adding a user, the database looks like:

```csv
USERNAME,IS_TEACHER
user,no
```

Injecting "yes" by adding a user of name "user2,yes"

```csv
USERNAME,IS_TEACHER
user2,yes,no
user,no
```

Log in by "user2" and we get the flag
