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