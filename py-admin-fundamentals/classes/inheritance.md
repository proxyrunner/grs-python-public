# Inheritance in classses

Here is a visual representation of the class inheritance example we're using:

![class hierarchy](https://github.com/gil-ryan/grs-python-public/blob/master/py-admin-fundamentals/img/class-hierarchy.PNG)


## Hierarchy

* parent class (superclass)
* child class (subclass)
    + inherits all data and behaviors of parent class
    + add more info
    + add more behavior
    + override behavior

## Inheritance: subclass

Let us define another class that will inherit directly from our _Animal_ class.

### New inhertiance subclasses

#### Subclass 1

```python
# Subclass 1
class Cat(Animal):
# add new functionality via speak method
    def speak(self):
        print("meow")

# ovverrides __str__
    def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.age)
```

#### This class will inherit all attributes of Animal:

*  \_\_init\_\_()
* age, name
* get_age(), get_name()
* set_age(), set_name()
* \_\_str\_\_()

But it also adds new functionality

* add new functionality with speak()
    + instance of type _Cat_ can be called with new methods
    + instance of type _Animal_ throws error if called with _Cat_'s new method
* __init__ is not missing, uses the _Animal_ version

#### Subclass 2

```python
# Subclass 2
class Person(Animal):
	def __init__(self, name, age):
		Animal.__init__(self, age)
		self.set_name(name)
		self.friends= []

	def get_friends(self):
		return self.friends

	def add_friend(self, fname):
		if fname not in self.friends:
		    self.friends.append(fname)

	def speak(self):
		print("hello")

	def age_diff(self, other):
		diff = self.age-other.age
		print(abs(diff), "year difference")

	def __str__(self):
		return "person:"+str(self.name)+":"+str(self.age)
```

#### Subclass 3

* subclass can have methods with the same name as superclass
* for an instance of a class, look for a method name in current class definition
* if not found, look for method name up the hierarchy (in parent, then grandparent, and so on)
* use first method up the hierarchy that you found with that method name

```python
# Subclass 3

class Student(Person):
        def __init__(self,name,age,major=None):
            Person.__init__(self,name,age)
            self.major=major
        def change_major(self,major):
            self.major = major
        def speak(self):
            r=random.random()
            if r<0.25:
                print("i have homework")
            elif 0.25 <= r < 0.5:
                print("i need sleep")
            elif 0.5 <= r < 0.75:
                print("i should eat")
            else:
                print("I am watching TV")
        def __str__(self):
            return "student:"+str(self.name)+":"+str(self.age)+":"+str(self.major)
```


### Lets use __tag__ to give a unique ID to each rabbit instance

#### Subclass 4

```python
class Rabbit(Animal):
    tag = 1
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self,age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag +=1
```

### Working with your own Types

```python
def __add__(self, other):
        # return object of same type as this class
        return Rabbit(0, self, other)
```

* define __+ operator__ between two _Rabbit_ instances
    + define what something like this does: _r4 = r1 + r2_ where _r1_ and _r2_ are _Rabbit_ instances
    + _r4_ is a new _Rabbit_ instance with age 0
    + _r4_ has _self_ as one parent and _other_ as the other parent
    + in __init__, __parent1 and parent2 are of type Rabbit__

* device that two rabbits are equal if they have the __same two parents__

```python
def __eq__(self,other):
        parents_same = self.parent1.rid == other.parent1.rid
            and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent2.rid == other.parent1.rid
            and self.parent1.rid == other.parent2.rid
        return parents_same or parents_opposite
```

* compare ids of parents since ids are unique
* note you can't compare objects directly
    + for example, with self.parent1 == other.parent1
    + this calls the __eq__ method over and over until call it on Nonce and gives and AttributeError when it tries to do None.parent1

## OOP

* create your own collection of data
* organize information
* division of work
* access information in a consistent manner
* add layers of complexity
* like functions, classes are a mechanism for decomposition and abstraction in programming