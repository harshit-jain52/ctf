# Postbook

After signing up, exploring the site gives us few observations:

- User's profile is at `?page=profile.php&id=<user-id>`
- New page can be created at `/page/create`
- Posts can be viewed at `?page=view.php&id=<post-id>`, edited at `?page=edit.php&id=<post-id>` and deleted by `?page=delete.php&id=<md5-hashed-post-id>`

## Flag 0

## Flag 1

We can see two public posts in homepage with id=1 & id=3, and a new created post has id=4. \
Edit the URL to view the post at id=2.

## Flag 2

Post creation page doesn't take any URL params. How does it know which user is posting? \
On inspecting the form...

```html
<input type="hidden" name="user_id" value="3">
```

Change the `value` to "1"; and create post.

## Flag 3

## Flag 4

On saving an edited post, the page shown has `message=` in the URL. Text against this is displayed on the page with yellow highlight. Hmmmm. \
Go to the edit page of post id 1,2 or 3; and save.

## Flag 5

Postbook homepage must be using some browser storage to identify user (for private/public status of posts), as user id is not passed in the URL. \
Indeed, cookie stores a MD5 hash. Reversing the hash (using online tools) for 3rd user (user created by us) gives "3". \
Hash "1" and edit the value of cookie. Refresh/Open the homepage.

## Flag 6

Delete post of id 1,2 or 3 by md5 hashing and visiting the URL mentioned above.
