# Python Classes and Inheritance

## Prerequisite

* abstract data types through classes
* __Coordinate__ example
* __Fraction__ example

### Today

* more on classes
    + getters and setters
    + information hiding
    + class variables
* inheritance

### implementing vs. using classes

#### implementing

- [ ] define the classe
- [ ] define __data attibutes__ (WHAT IS the object)
- [ ] define __methods__ (HOW TO use the object)

### using

- [ ] create __instances__ of object type
_ [ ] do __operations__ with them

## Defining Parent Classes

```python
class Animal(object):
    def __init__(self,age):
        self.age = age
        self.name = None

myanimal = Animal(3)
```

### Getter & Setter

Utilizing class _Animal_, we instantiate getter and setter methods in the same instance.

```python
def get_age(self):
    return self.age
def get_name(self):
    return self.name

def set_age(self, newage):
    self.age = newage
def set_name(self), newname ="":
    self.name = newname

def __str__(self):
    return "animal:"+str(self.name)+":"+str(self.age)
```

* getters and setters should be used outside of class to access data attributes