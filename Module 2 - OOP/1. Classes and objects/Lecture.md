# Classes and objects

What is OOP useful for?

- Encapsulation
- Isolation
- No code duplication
- Inheritance
- ...

Everything in Python is an object.

## Difference between classes and objects

Often the two terms are used interchangeably, but they are not quite the same.

Classes are the templates from which objects are made.

If we're producing car parts, roofs, for example, we'll probably have a machine that bends the metal, according to a template. 

That template is the class. All roofs originate from that same template.

Once the roofs are manufactured, each roof starts living its own life. Those are objects.

 Now, let's get down to something more practical.

 Creating a class in Python is done with the `class` keyword:

```python
class Roof:
    pass
```

That's enough to create a valid class.

*Note*: Class names in Python should be in upper [CamelCase](https://en.wikipedia.org/wiki/Camel_case), which means they should start with a capital letter and each consecutive word should also start with a capital letter e.g.: `Car`, `CarRoof`, `AccessToken` etc.

Creating objects from our class:

```python
first_roof = Roof()

print(first_roof)
print(type(first_root))

# Result: 
# <__main__.Roof object at 0x10686f128>
# <class '__main__.Roof'>
```

Let's add a constructor. Constructors are the first method (functions in the context of classes are called `methods`) that is automatically executed upon creating new objects. In Python the `__init__` method plays the role of a constructor. Methods with two leading and training underscores in Python are magic methods and there are quite a few, serving different purposes - `__str__`, `__len__`, `__repr__` and so on:

```python
class Roof:

    def __init__(self):
        print('This is executed...')

roof = Roof()

# Result:
# This is executed...
```

*Note*: The `self` keyword refers to the current object, like `this` in other languages. It's always the first value in the methods and is ignored when passing arguments to the methods. It is not absolutely required to name it `self`, you can use a word of your choice, but it's highly recommended to use `self` as it's the *de facto* standard in the Python world.

Constructors are typically used to initialize object properties:

```python
class Roof:

    def __init__(self, color, width, height):
        self.color = color
        self.width = width
        self.height = height

roof = Roof('red', 80, 160)
print(roof.color)
print(roof.width)
print(roof.height)

# Result:
# red
# 80
# 160
```

Parameters in the `__init__` are passed when creating new objects - `Roof('red', 80, 160)`.

With the `self.property_name` syntax we assign values for the current object.

Then we can access those values with the following notation - `object_name.proerty_name`.

As you may have noticed, printing an object is not very descriptive:

```python
class Roof:
    pass

roof = Roof()
print(roof)

# Result:
# <__main__.Roof object at 0x1032471d0>
```

To make it more human-readable, we can use another magic method - `__str__`.

```python
class Roof:

    def __init__(self, color, width, height):
        self.color = color
        self.width = width
        self.height = height

    def __str__(self):
        return f"{self.color[0].upper() + self.color[1:]} door with {self.width} width and {self.height} height."

roof = Roof('red', 80, 160)
print(roof)

# Result:
# Red door with 80 width and 160 height.
```

*Note*: In most programming languages (if not in all), the equivalent of Python's `__str__` method must return a string. As you can see, Python makes no exception.

As discussed earlier, there is no function overloading in Python. Respectively, there is no method overloading:

```python
class Roof:

    def __init__(self, color, width, height):
        self.color = color
        self.width = width
        self.height = height

    def get_color(self):
        return self.color

    def get_color(self):
        return 'Black'

roof = Roof('red', 80, 160)
print(roof.get_color())

# Result: Black
```

In most OO languages, there is a mechanism for restricting the access to certain parts of a class through access modifiers.

You can use them to change the visibility of different parts of your class - fields, properties, methods, constants etc.

Typically, there are keywords for the access modifiers - `private`, `protected`, `internal`, `public`.

Usually, if a class member is marked as `private`, it's only visible inside that class and other classes can't access it (or not easily, at least).

There are no access modifiers in Python. The control is achieved, again, through a naming convention. If a class member starts with an underscore e.g. `def _do_something():`, it's meant to be private and used only inside the respective class and other people  should respect that.

*Note*: There are other paradigms and features that people are used to when using an OO language, like `interfaces` and `abstract` members. Python has neither of those.

Due to it's dynamic nature, Python allows us to add properties to an object on the fly, after the object's been created:

```python
class Roof:

    def __init__(self, color, width, height):
        self.color = color
        self.width = width
        self.height = height

roof = Roof('red', 80, 160)
roof.model = 'cf8372'
print(roof.model)
# Result: cf8372
```

If we create another object of type `Roof`, it won't have that property `model`.

*Note*: Dynamically adding properties to an object is considered a bad practice. If you need to do it, you should think very carefully if you're not doing something wrong. There are some rare situations, however, when it's helpful and using it is actually not a terrible idea.

We can also delete properties on the fly (only for the specific object):

```python
class Roof:
    def __init__(self, color, width, height):
        self.color = color
        self.width = width
        self.height = height

roof = Roof('red', 80, 160)
delattr(roof, 'color')
print(roof.color)
# Result: 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Roof' object has no attribute 'color'
```

## Practice

Practice your skills with some [tasks](Tasks.md).