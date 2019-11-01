# Working with both Python2 and Python3 

It is well known now that Python2 will be end of support early 2020.

```python
# Writing to standard output
from __future__ import print_function
# Reading from standard input
# there is now 'raw_input' in Python3, only Python2


try:
    ip_addr = raw_input("Enter an IP address: ")
except NameError:
    ip_addr = input("Enter an IP address: ")
print(ip_addr)
```
