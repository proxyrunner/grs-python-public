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

Please see ![File Manipulation](https://github.com/gil-ryan/grs-python-public/blob/master/py-admin-fundamentals/file-manipulation.md) for more information on __open__ and __readlines()__ as issued Python commands.

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

List slices give us the ability to parse, or slice and dice a new list from an existing list. You may also use negative indices:

```python
In [29]: output[-50:-25]
```

Output:

```
Out[29]:
['\n',
 'If you require further assistance please contact us by sending email to\n',
 'export@cisco.com.\n',
 '\n',
 'Cisco 7206VXR (NPE400) processor (revision A) with 491520K/32768K bytes of memory.\n',
 'Processor board ID 4279256517\n',
 'R7000 CPU at 150MHz, Implementation 39, Rev 2.1, 256KB L2 Cache\n',
 '6 slot VXR midplane, Version 2.1\n',
 '\n',
 'Last reset from power-on\n',
 '\n',
 'PCI bus mb0_mb1 (Slots 0, 1, 3 and 5) has a capacity of 600 bandwidth points.\n',
 'Current configuration on bus mb0_mb1 has a total of 1600 bandwidth points. \n',
 'The set of PA-2FE, PA-POS-2OC3, and I/O-2FE qualify for "half \n',
 'bandwidth points" consideration, when full bandwidth point counting \n',
 'results in oversubscription, under the condition that only one of the \n',
 'two ports is used. With this adjustment, current configuration on bus \n',
 'mb0_mb1 has a total of 1200 bandwidth points. \n',
 'This configuration has oversubscripted the PCI bus and is not a \n',
 'supported configuration. \n',
 '\n',
 'PCI bus mb2 (Slots 2, 4, 6) has a capacity of 600 bandwidth points.\n',
 'Current configuration on bus mb2 has a total of 1200 bandwidth points \n',
 'The set of PA-2FE, PA-POS-2OC3, and I/O-2FE qualify for "half \n',
 'bandwidth points" consideration, when full bandwidth point counting \n']
```

Notice it works the same way with _negative_ indices.
