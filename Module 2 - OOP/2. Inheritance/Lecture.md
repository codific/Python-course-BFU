# Inheritance

\- What's the object-oriented way to become wealthy?  
\- Inheritance.

In object-oriented programming, inheritance enables new objects to take on the properties of existing objects. A class that is used as the basis for inheritance is called a superclass, base class or a parent class. A class that inherits from a superclass is called a subclass, derived class or a child class.

## Inherit from a parent class

Examples:

```python
class Mammal():

    def move():
        print('Moving...')

    def eat():
        print('Eating')

class Human(Mammal):
    pass

hooman = Human()
hooman.move()
hooman.eat()

# Result:
# Moving...
# Eating
```

We didn't specify any methods in the `Human` class. We used the methods from the parent class.

*Note*: In Python, we can have multiple classes in the same file, unlike some other languages.

We can call parent methods in the child class:

```python
class Mammal():

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def eat(self):
        print('Nom-nom')

class Human(Mammal):

    def __init__(self, name, weight):
        super().__init__(name, weight)

    def have_dinner(self):
        super().eat()

hooman = Human('Peter', 82)
hooman.have_dinner()
print(hooman.name)
print(hooman.weight)

# Result:
# Nom-nom
# Peter
# 82
```

We called the parent `__init__` and let it handle the name and weight params.

We can call all parent members in the child class.

In case we'd like to implement custom logic in the child class, we have to create a method with the same name and optionally call the parent or completely omit it:

```python
class Mammal():

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def eat(self):
        print('Nom-nom')

class Human(Mammal):

    def __init__(self, name, weight):
        super().__init__(name, weight)

    def eat(self):
        print('Eating pizza...')

hooman = Human('Peter', 82)
hooman.eat()

# Result: Eating pizza...
```

## Static methods

Static method is one that can be accessed without creating an instance of class.

These methods are suitable for making some kind of utility functionality, such as logging, where creating an instance for accessing these methods is costlier then simply accessing, without creating an instance.

To create static methods, we need to use the `@staticmethod` decorator (Note: decorators are a powerful Python feature, but are no covered in this course):

```python
class Human:

    @staticmethod
    def say_hi():
        print('Hello')

Human.say_hi()
# Result: Hello
```

*Note*: Static methods are called through the class. Note that we didn't specify `self` as the first argument. That's because static methods are not bound to the objects that we create.

## Multiple inheritance

Python supports multiple inheritance.

This means that a child class can inherit from more than one parent class.

```python
class Mammal():

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def eat(self):
        print('Nom-nom')


class Employee():

    def __init__(self, emp_no):
        self.emp_no = emp_no

    def work(self):
        print('Work smart, not hard.')


class Human(Mammal, Employee):

    def __init__(self, name, weight):
        Mammal.__init__(self, name=name, weight=weight)
        Employee.__init__(self, emp_no='123123')

    def eat(self):
        print('I like eating pizza...')


hooman = Human('Peter', 82)
hooman.work()
hooman.eat()

# Result:
# Work smart, not hard.
# I like eating pizza...
```

Note how calling parents' init methods has changed. This is because we need to specify which parent's init method we'd like to call.

***Important***: Using multiple inheritance is considered a bad practice. It makes debugging and maintenance hard.

Try to avoid it.

Multiple inheritance, however, has its application - you can create the so-called `mixins`, which are not covered in this course.

## Practice

Practice your skills with some [tasks](Tasks.md).