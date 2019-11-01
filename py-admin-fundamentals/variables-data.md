# Fundamental Commands for Data and Variables

Start by opening a file and reading it as a list:

```python
In [13]: f = open("show-version.txt")
In [15]: output = f.readlines()

In [16]: type(output)
Out[16]: list

In [17]: len(output)
Out[17]: 77
```

We see that __type__ specifies the data types.

We also see that __len__ specifies the literal length of the data type.

## List Slicing

Above we've opened a particular text file, when using list slicing, it will always include the first element, but __not__ element '5'. For example:

> output[0:5]

Output:

```
['R1#show ver\n',
 'Cisco IOS Software, 7200 Software (C7200-ADVENTERPRISEK9-M), Version 15.2(4)XB10, RELEASE SOFTWARE (fc1)\n',
 'Technical Support: http://www.cisco.com/techsupport\n',
 'Copyright (c) 1986-2012 by Cisco Systems, Inc.\n',
 'Compiled Wed 31-Oct-12 21:19 by prod_rel_team\n']
 ```