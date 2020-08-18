# Getting started with Requests

## Get

One of the most common HTTP methods is GET. The GET method indicates that you’re trying to get or retrieve data from a specified resource. To make a GET request, invoke requests.get().

### Response 

Example from HTTP for humans:

```python
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
