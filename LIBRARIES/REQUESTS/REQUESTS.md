# Requests Library

## Notes

* Checkout uncurl for python

## Examples

```python
uncurl curl -u 91b649f241e84abe93b9c4fcb33e7c41:293eNtJLWJYj7zuBWOO5e2b24oUqbpCo -d grant_type=client_credentials https://us.battle.net/oauth/token

header = {'PRIVATE-TOKEN': 'my_token'}
response = requests.get(myUrl, headers=header)
```

### -

```python
import requests

myToken = '<token>'
myUrl = '<website>'
head = {'Authorization': 'token {}'.format(myToken)}
response = requests.get(myUrl, headers=head)
```
import requests
#import netmiko
from requests.auth import HTTPBasicAuth
from getpass import getpass

# Getting started with Requests

## Get

One of the most common HTTP methods is GET. The GET method indicaes that you’re trying to get or retrieve data from a specified resource. To make a GET request, invoke requests.get().

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


# Sample Token Script

## Simple Token

response = requests.get('https://website.com/id', 
    headers={'Authorization': 'access_token myToken'})

response = requests.get('https://us.battle.net/oauth/token', 
    headers={'Authorization': 'USaNbgqv2lEHqi1xznESNsIVHCQQFtD1SB'})

## Other

```python
"""
From any system with Python and the Requests libraries installed, start the Python interpreter or create a script and run:
"""

import requests, json
data = { 'username' : '#', 'password' : '#' }
r = requests.post('https://us.battle.net/oauth/authorize', data=json.dumps(data), verify = False)
token = json.loads(r.text)['session']
# 
"""
Now you can send subsequent requests (e.g. a GET request to https://address.of.opengear/api/v1/serialPorts/ for Console Servers, or https://address.of.opengear/api/v1/nodes/ for Lighthouse) setting your token in the headers:
"""

headers = { '91b649f241e84abe93b9c4fcb33e7c41' : '293eNtJLWJYj7zuBWOO5e2b24oUqbpCo' + token }
r = requests.get('https://us.battle.net/oauth/token', headers=headers, verify=False)
j = json.loads(r.text)
print(json.dumps(j, indent=4))
```
import requests
from getpass import getpass

user = input(“Enter username: “) 
pw = getpass()

r = requests.get('https://api.github.com/user', auth=(user, pw))


for key, value in student_score.items():
print(key, ' : ', value)

for key, value in dict1.items():
	print(key, ' : ', value)


>>> for key, value in dict1.items():
...     print(key, ' : ', value)
... 
login  :  gil-ryan
id  :  45831297
node_id  :  MDQ6VXNlcjQ1ODMxMjk3
avatar_url  :  https://avatars3.githubusercontent.com/u/45831297?v=4
gravatar_id  :  
url  :  https://api.github.com/users/gil-ryan
html_url  :  https://github.com/gil-ryan
followers_url  :  https://api.github.com/users/gil-ryan/followers
following_url  :  https://api.github.com/users/gil-ryan/following{/other_user}
gists_url  :  https://api.github.com/users/gil-ryan/gists{/gist_id}
starred_url  :  https://api.github.com/users/gil-ryan/starred{/owner}{/repo}
subscriptions_url  :  https://api.github.com/users/gil-ryan/subscriptions
organizations_url  :  https://api.github.com/users/gil-ryan/orgs
repos_url  :  https://api.github.com/users/gil-ryan/repos
events_url  :  https://api.github.com/users/gil-ryan/events{/privacy}
received_events_url  :  https://api.github.com/users/gil-ryan/received_events
type  :  User
site_admin  :  False
name  :  GRS
company  :  None
blog  :  gil-ryan.github.io
location  :  WASP-32
email  :  gil.s4@outlook.com
hireable  :  True
bio  :  COMPUTER MERCENARY
twitter_username  :  None
public_repos  :  22
public_gists  :  1
followers  :  4
following  :  39
created_at  :  2018-12-12T19:43:19Z
updated_at  :  2020-08-16T04:11:21Z
private_gists  :  3
total_private_repos  :  11
owned_private_repos  :  11
disk_usage  :  293861
collaborators  :  0
two_factor_authentication  :  False
plan  :  {'name': 'free', 'space': 976562499, 'collaborators': 0, 'private_repos': 10000}

>>> for key, value in head.items():
...     print(key, ' : ', value)
... 
Server  :  GitHub.com
Date  :  Sun, 16 Aug 2020 20:44:46 GMT
Content-Type  :  application/json; charset=utf-8
Transfer-Encoding  :  chunked
Status  :  200 OK
X-RateLimit-Limit  :  5000
X-RateLimit-Remaining  :  4982
X-RateLimit-Reset  :  1597613201
Cache-Control  :  private, max-age=60, s-maxage=60
Vary  :  Accept, Authorization, Cookie, X-GitHub-OTP, Accept-Encoding, Accept, X-Requested-With
ETag  :  W/"1621a253be981c56cda6d2738e5dd1d7"
Last-Modified  :  Sun, 16 Aug 2020 04:11:21 GMT
X-GitHub-Media-Type  :  github.v3; format=json
Access-Control-Expose-Headers  :  ETag, Link, Location, Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type, Deprecation, Sunset
Access-Control-Allow-Origin  :  *
Strict-Transport-Security  :  max-age=31536000; includeSubdomains; preload
X-Frame-Options  :  deny
X-Content-Type-Options  :  nosniff
X-XSS-Protection  :  1; mode=block
Referrer-Policy  :  origin-when-cross-origin, strict-origin-when-cross-origin
Content-Security-Policy  :  default-src 'none'
Content-Encoding  :  gzip
X-GitHub-Request-Id  :  D164:5C1B:59A1EA:1088705:5F399ABE

t = requests.get('https://api.github.com/events')

post request

t = requests.post('https://httpbin.org/post', data = {'key':'value'})

other requests

r = requests.put('https://httpbin.org/put', data = {'key':'value'})
r = requests.delete('https://httpbin.org/delete')
r = requests.head('https://httpbin.org/get')
r = requests.options('https://httpbin.org/get')


passing parameters in requests

payload = {'key1':'value1','key2':'value2'}
y = requests.get('https://httpbin.org/get', params=payload)

>>> y.url
'https://httpbin.org/get?key1=value1&key2=value2'

>>> payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
>>> 
>>> y = requests.get('https://httpbin.org/get', params=payload)
>>> y.url
'https://httpbin.org/get?key1=value1&key2=value2&key2=value3'
>>> 


for x in range(len(a)): 
    print a[x], 


Encoding

r.encoding
'utf-8'
r.encoding = 'ISO-8859-1'


Binary Response Content

from PIL import Image
from io import BytesIO

i = Image.open(BytesIO(r.content))

>>> import requests

>>> r = requests.get('https://api.github.com/events')
>>> r.json()
[{'repository': {'open_issues': 0, 'url': 'https://github.com/...

When JSON encoding fails, it will raise an exception. Sometimes with a code 204 (no content), or the VlaueError: No JSON could be decoded.

Always consider the the success of a .json() call does not indicate the success of the response. Some servers return a JSON object in a failed response. To check for a successful request, use r.raise_for_status() or check r.status_code is what you expect.

Raw Response Content

In the rare case that you’d like to get the raw socket response from the server, you can access r.raw. When accessing __raw__, make sure you set the parameter _stream=___True__ in your initial request. Once you do, here are the results:


> r = requests.get('https://api.github.com/events', stream=True)


>>> i = requests.get('https://api.github.com/events', stream=True)
>>> i.raw
<urllib3.response.HTTPResponse object at 0x10ea84da0>
>>> i.raw.read(10)
b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03'

with open(filename.txt, 'wb') as fd:
    for chunk in i.iter_content(chunk_size=128):
        fd.write(chunk)

Custom Headers

Adding HTTP headers to a request is done by simply passing a dictionary to the header’s parameters.

```python
url = “https://api.github.com/some/endpoint'
headers = {‘user-agent’ : ‘my-app/0.0.1’}
r = requests.get(url,headers=headers)
```
