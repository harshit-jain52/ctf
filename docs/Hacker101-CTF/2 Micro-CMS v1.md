# Micro-CMS v1

Exploring the site gives us few observations:

- It's a markdown page editing site.
- New page can be created at `/page/create`
- Pages can be viewed at `/page/<page-num>` and edited at `/page/edit/<page-num>`

## Flag 0

_Testing_ is page-1 and _Markdown Test_ is page 2. On creating new pages, the page numbers assigned are 11, 12,... \
This seems weird. Viewing all pages from 3 to 10, all give **Page Not Found**, except for the 5th page which says **Forbidden** -- read-protected. \
Hmm..it's _read-protected_, is it _write-protected_? Go to `/page/edit/5` and there's the flag.

## Flag 1

## Flag 2

## Flag 3
