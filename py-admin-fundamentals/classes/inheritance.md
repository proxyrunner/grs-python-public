# Inheritance in classse

## Inheritance: subclass

Let us define another class that will inherit directly from our _Animal_ class.

```python
class Cat(Animal):
# add new functionality via speak method
    def speak(self):
        print("meow")

# ovverrides __str__
    def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.age)
```

This class will inherit all attributes of Animal:

*  \_\_init\_\_()
* age, name
* get_age(), get_name()
* set_age(), set_name()
* \_\_str\_\_()