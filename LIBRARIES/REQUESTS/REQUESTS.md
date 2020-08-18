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