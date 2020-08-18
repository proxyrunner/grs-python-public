# HTTP for Humans
    
Looks like a great guide, there are a lot of snippets of code so I gave it it's own directory.

## Requests

```
r = requests.get('https://api.github.com/user', auth=('user', 'pw'))
r.status_code
200
r.headers['content-type']
'application/json; charset=utf8'
r.encoding
'utf-8'
r.text
'{"type":"User"...'
r.json()
{'private_gists': 419, 'total_private_repos': 77, ...}
```