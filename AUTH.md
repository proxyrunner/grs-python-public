# Web Authentication

## Tokens

### Simple Token

response = requests.get('https://website.com/id', 
    headers={'Authorization': 'access_token myToken'})

response = requests.get('https://us.battle.net/oauth/token', 
    headers={'Authorization': 'USaNbgqv2lEHqi1xznESNsIVHCQQFtD1SB'})
