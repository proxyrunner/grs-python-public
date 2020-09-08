# Working with Dictionaries

Everything you need in order to optimize your operations with dictionaries in Python.

## Dictionaries vs. Lists

* dictionaries are unordered
    + there is no first item in dictionary
* order in lists matter for comparing if two lists are the same
    + order of key-value pairs in dictionary do no matter

### Example Program to track Birthdays

```python
bdays = {'gil':'march','christine':'july'}

while True: 
    print('Enter a name: ')
    name = input()
    if name == '':
        break
    if name in bdays:
        print(bdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday month?')
        bday = input()
        bdays[name] = bday
        print('Birthday database updated.')
```

## Iterate over Keys and Values

```python
spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)
for k in spam.keys():
    print(k)
for i in spam.items():
    print(i)
```

### Checking existence of keys and values



```python
# CREATE DICTIONARY
spam = {'name':'gangstalicious', 'age':10, 'color': 'red'}
# CHECK KEYS
'name' in spam.keys()
# CHECK VALUES
'color' in spam.keys()
'color' not in spam.keys()
'color' in spam
```
