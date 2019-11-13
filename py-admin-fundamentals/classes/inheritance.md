# Inheritance in classses

Here is a visual representation of the class inheritance example we're using:

![class hierarchy]()

## Inheritance: subclass

Let us define another class that will inherit directly from our _Animal_ class.

### New inhertiance subclass

```python
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
