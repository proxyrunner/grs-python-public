"""

"""

import requests

url = "https://google.com"
res = requests.get(url)

print("\nFirst example statement: \n\n")
print(res.status_code)

url = "http://httpbin.org/post"
payload = dict(key1='value1', key2='value2')
res = requests.post(url, data=payload)

print("Second statement: \n\n")

print(res.text)

