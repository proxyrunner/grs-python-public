# Fundamentals

This is my sandbox that I utilize the confirm and learn information. This is not meant to be a primer of any kind. If you'd like to see my notes for Python and learn, you'll have to reach out to me directly.

## Looping through a List

ip_addr = ['10.1.1.1', '192.168.1.1', '172.16.1.1']

for addresses in ip_addr:
	print(addresses)

## Doing more while looping through a list

```python
for addresses in ip_addr:
	print(f"{addresses.title()}, is a list item.\n")
```

```output
10.1.1.1, Network Address!
192.168.1.1, Network Address!
172.16.1.1, Network Address!
```

### Extra Tips

* be careful with indentation
	+ it can cause scope errors
	+ it can cause compilation errors (syntax error in this case)


## Numerical Lists

Python has a _range()_ function that makes it easy to generate numbers.

```python
for number_value in range(1,10):
    print(number_value)
```

```output
1
2
3
4
5
6
7
8
9
```

* note the off by one behaviour that most programming languages follow.
    + that is because an array index begins with 0 (consider binary)

However, _number_range_ will only have the number __9__ stored, as it utilized the _range()_ function and finished at that. Lets make the numerical list we were talking about:

```python
num_list = list(range(1,11))
print(num_list)
```

```output
# NOW we get the full list.
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

_range()_ will take additional parameters:

```python
even_nums = list(range(2,11,2))
print(even_nums)
```

