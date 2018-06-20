# Functions

Why do we need functions? - DRY (Don't Repeat Yourself); isolation; encapsulation.

## Defining functions

The `def` keyword is used to define a function:

```python
def function_name():
    pass
```

*Note*: With the `pass` keyword, you declare an empty block, which is something not otherwise allowed in Python due to its nature. Another way to do the same, is the three dots e.g. (only in Python 3):

```python
def function_name():
    ...
```

Now, lets create a function that does something:

```python
def sum_two_numbers():
    print(2 + 3)

# This is how you call a function
sum_two_numbers()
# Result: 5
```

## Function parameters

Ok, but what if we want to sum two different numbers? Create another function? No.

This is where parameters come handy.

Parameters are special kind of variables, that are provided to the functions as input data.

The examples below should make it much clearer:

```python
def sum_two_numbers(first_number, second_number):
    print(first_number + second_number)

sum_two_numbers(1, 2)
sum_two_numbers(3, 7)
sum_two_numbers(7.15, 4.82)

# Result:
# 3
# 10
# 11.97
```

## Returning values

But what if we don't want to print the result, but to make the calculation and pass the result to the caller of the function?

We can use the `return` keyword:

```python
def sum_two_numbers(first_number, second_number):
    return first_number + second_number

first_calculation = sum_two_numbers(1, 2)
second_calculation = sum_two_numbers(3, 7)
third_calculation = sum_two_numbers(7.15, 4.82)

print(first_calculation)
print(second_calculation)
print(third_calculation)

# Result:
# 3
# 10
# 11.97
```

Instead of printing the result, we returned it. We can assign the returned value to a variable and use it.

*Note*: Functions in Python always return one value.

## Unpacking

We can trick functions into returning multiple values by returning lists, tuples or other collections of elements:

```python
def split_filename(filename):
    # List with splitted values
    splitted_values = filename.split('.')
    name = splitted_values[0]
    extension = splitted_values[1]
    return (name, extension)

filename, extension = split_filename('MyCoolSong.mp3')
print(filename)
print(extension)
# Result:
# MyCoolSong
# mp3
```

This technique is called `unpacking`.

It works with all collection types.

Consider the following examples:

```python
# Unpacking two values
first, second = ('one', 'two')
print(first)
print(second)
# Result:
# one
# two


# Unpacking multiple values
# Lets say we want the first and the last values
first, *middle, last = [1, 2, 3, 4, 5, 6]
print(first)
print(middle)
print(last)
# Result:
# 1
# [2, 3, 4, 5]
# 6


# Getting only the first and the second values, ignoring the rest
first, second, *rest = [1, 2, 3, 4, 5, 6]
print(first)
print(second)
print(rest)
# Result:
# 1
# 2
# [3, 4, 5, 6]


# Trying to unpacking invalid number of values
first, second, third = (1, 2)
# Result:
# Traceback (most recent call last):
#    File "<stdin>", line 1, in <module>
# ValueError: not enough values to unpack (expected 3, got 2)
```

## Positional and named parameters

Ok, lets go back to the functions.

Python supports both positional and named parameters:

```python
def function(first, second):
    print(f'First param: {first}')
    print(f'Second param: {second}')

function(1, 3)  # Positional
function(first=2, second=5)  # Named
function(second=5, first=2)  # Order doesnt matter when passing named parameters

# Result:
# First param: 1
# Second param: 3

# First param: 2
# Second param: 5

# First param: 2
# Second param: 5
```

Some parameters can be optional, by setting default values:

```python
def function(first, second=5):
    print(f'First param: {first}')
    print(f'Second param: {second}')

function(1)  # Using the default value
function(1, 10)  # Setting both values

# Result:
# First param: 1
# Second param: 5

# First param: 1
# Second param: 10
```

*Note*: The rule is - optional parameters must always be after required.

Result of function can be parameter of another function:

```python
def sum_numbers(first, second):
    return first + second

def print_result(result):
    print(result)

print_result(sum_numbers(2 , 4))

# Result: 6
```

## *`args` and **`kwargs`

Sometimes we need to be able to handle unknown number of arguments. In those cases, we can use the special `*args` (short for arguments) and `**kwargs` (short for key-word arguments):

```python
def print_numbers(*args):
    for argument in args:
        print(argument, end=' ')

# Note: we can pass as many as we want
print_numbers(1, 2.17, 3, 'four', 5)

# Result: 1 2.17 3 four 5


def print_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f'Key: {key}, Value: {value}')

print_user_info(first_name='Sarah', last_name='Conner', age=35, phone='12312382')
# Result:
# Key: first_name, Value: Sarah
# Key: last_name, Value: Conner
# Key: age, Value: 35
# Key: phone, Value: 12312382
```

*Note*: `args` and `kwargs` is just a naming convention, the code will still work if you call them something else, but it's strongly recommended not to do that, since Python developers are used to using them that way.

*Note*: Using `args` and `kwargs` is typically needed when we write libraries and modules for somebody else. When we're writing specific logic, this is not needed.

## Function annotations

Function annotations are a Python 3 feature that lets us add metadata to function parameters and return value.

Examples:

```python
# Without default values
def sum_two_numbers(first_numbers: int, second_number: int) -> int:
    return first_numbers + second_number

# With default values
def sum_two_numbers(first_numbers: int = 2, second_number: int = 5) -> int:
    return first_numbers + second_number

def example_function(names: set = set(), ages: list = []) -> dict:
    ...

def example_function(first_param: str, second_param: bool) -> None:
    pass
```

*Note*: Python will remain a dynamically typed language, which means that you can pass any type as a function argument, even though there are annotations.

Some tools, however, use them and try to help the developers with hints and warnings, such as IDEs, static code analysts etc.

## Function overloading

The term refers to a programming technique where we can have multiple functions with the same name and different number of parameters.

Example (C#):

```csharp
public void SayHi()
{
    Console.WriteLine("Hello");
}

public void SayHi(string name)
{
    Console.WriteLine("Hello, " + name);
}

SayHi();
SayHi("Roger");

// Result:
// Hello
// Hello, Roger
```

There is no such concept in Python.

If you try to create two functions with the same names, the last one declared will overwrite the rest:

```python
def say_hi():
    print('hi')

def say_hi(name):
    print('hi, ' + name)

say_hi()
say_hi('Sarah')

# Result:
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: say_hi() missing 1 required positional argument: 'name'

# hi, Sarah
```

The first function has been overwritten (think replaced) by the second one, because it has the same name, that's why the exception is thrown - it expects argument name to be supplied.

## Practice

Practice your skills with some [tasks](Tasks.md).