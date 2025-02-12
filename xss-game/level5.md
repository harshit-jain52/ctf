# level 5

In `signup.html`, we observe:

```html
<a href="{{ next }}">Next >></a>
```

where `{{ next }}` is the query parameter (default: confirm) on signup page

Change the parameter:

```text
?next=javascript:alert(1)
```

Click on 'Go' and then 'Next'
