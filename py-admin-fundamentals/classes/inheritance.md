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
