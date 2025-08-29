# Where Robots Cannot Search

> Web

```text
Ahh, the Brunnerne company.
But they have a secret, hidden away from robot search.
```

points: `30`

solves: `755`

author: `The Mikkel`

---

At `/robots.txt`:

```text
ser-agent: *
Disallow: /admin
Disallow: /private
Disallow: /hidden
Disallow: /flag.txt
```

Flag at `/flag.txt`
