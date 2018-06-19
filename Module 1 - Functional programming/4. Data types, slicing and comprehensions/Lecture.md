# Data types, slicing, comprehensions

## Data types

### Numbers

Both integers and floating point numbers fall under the Python numbers category (there are other number types that we're not going to talk about here, just keep this in mind).

We've already talked about assigning variables. So, let's do that with numbers:

```python
fisrt_number = 15
second_number = 1.72

print(type(fisrt_number))
print(type(second_number))
```

Output:

```text
<class 'int'>
<class 'float'>
```

Other than that, there are a couple of important things we need to mention here:

1. The numbers `1` and `1.0` are not the same from Python's perspective. They represent different data type.
1. Floating point numbers are accurate up to 15 decimal places. It's due to the way the processor computes floating point numbers. You can read more about that [here](https://en.wikipedia.org/wiki/IEEE_754). If you need to work with very small or very large numbers, you should consider using a special library.
1. The length of the integer numbers can be of any length. The only limit is the available memory.

### Strings

#### Declaring strings and using string methods

Python strings are sequences of unicode characters. Python makes no difference between single or double quotes when representing strings.

Multiline strings are denoted with triple quotes (''' or """).

We have a big list of functions we can use on strings:

```python
greeting = 'Hello'

print(greeting.lower())
print(greeting.upper())
print(greeting.startswith('G'))
print(greeting.endswith('o'))

greeting_with_whitespace = '     Hello      '
print(greeting_with_whitespace)
print(greeting_with_whitespace.strip())
```

Output:

```text
hello
HELLO
False
True
     Hello      
Hello
```

Since strings are sequences, we can iterate over them:

```python
name = 'John'
for ch in name:
    print(ch)
```

Output:

```text
J
o
h
n
```

#### Formatting strings

When referring to string formatting, people usually mean inserting some string in between another.

The most common way is through concatenation:

```python
name = 'John'
print('Hello, ' + name + '!')
```

Output:

```text
Hello, John!
```

This works, but when there are multiple strings that we want to insert, it gets messy. So, a better way is needed and this is where string formatting comes handy.

There are several ways to do it, though:

##### The old Python 2 style (which is supported in Python 3)

```python
greeting = "My name is %s and I am %d years old."
print(greeting % ("John", 21))
```

Output:

```text
My name is John and I am 21 years old.
```

Different data types require different identifier:

* `%s` for strings
* `%i` for integers
* `%d` for decimal integers
* `%f` for floating point numbers

...and many more. You can check [this](https://docs.python.org/3/library/string.html#format-specification-mini-language) for a more complete reference.

##### The Python 3 brackets style

We can use the `.format` function to achieve that:

```python
greeting = "My name is {} and I am {} years old."
print(greeting.format("John", 21))
```

Output:

```text
My name is John and I am 21 years old.
```

This method supports both positional and named arguments:

```python
print("We are learning {0} and we {1} it!".format("Python", "love"))

print("We are learning {language} and we {feeling} it!".format(language="Python", feeling="love"))
```

Output:

```text
We are learning Python and we love it!

We are learning Python and we love it!
```

##### Python 3.6 style

As of Python 3.6, a new way for string formatting has been introduced.

```python
language = 'Python'
feeling = 'love'

# Directly use variables
message = f'We are learning {language} and we {feeling} it!'

print(message)
```

Output:

```text
We are learning Python and we love it!
```

### Lists

Arrays in Python are called `lists`.

Lists are ordered sequences of items, separated by commas and enclosed within square brackets `[]`:

```python
items = [1, 2, "three", 4.0]

# Similarly to strings, arrays can be iterated with a for loop

for item in items:
    print(item)
```

Output:

```text
1
2
three
4.0
```

*Note*: As you can see, list items don't need to be of the same type.

We can access a specific list item by using its index. **Indices start from 0**:

```python
items = [1, 2, "three", 4.0]

print(items[0])
print(items[1])
print(items[2])
print(items[3])
```

Output:

```text
1
2
three
4.0
```

Getting list's size is done with the `len` function:

```python
items = [1, 2, "three", 4.0]
items_size = len(items)
print(items_size)
```

Output:

```text
4
```

***Note***: The `len` function also works on strings, tuples, sets, our own objects (we'll see this in the OOP module of the course) etc.

Here some of the features Python lists support:

```python
# Lists sizes can be changed
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)
# Result: [1, 2, 3, 4]


# Two lists can be concatenated
first_list = [1, 2, 3]
second_list = [4, 5, 6]
concatenated_list = first_list + second_list
print(concatenated_list)
# Result: [1, 2, 3, 4, 5, 6]


# Items can be removed
numbers = [1, 2, 3, 4]
numbers.pop()  # .pop() removes the last item and returns it, so you can assing it to a variable
print(numbers)
# Result: [1, 2, 3]


# Lists can have lists
first_list = [1, 2, 3]
second_list = [4, 5, 6]
first_list.append(second_list)
print(first_list)
# Result: [1, 2, 3, [4, 5, 6]]


# Accessing list items with a negative index
numbers = [1, 2, 3, 4, 5]
print(numbers[-1])
# Result: 5


# Changing the value at index
numbers = [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers)
# Result: [10, 2, 3, 4, 5]


# List multiplication
multiplicated_list = [1] * 10
print(multiplicated_list)
# Result: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


# Sometimes we need both index and item as we iterate over a list. We can get them with the enumerate() function
names = ['John', 'Mark', 'Jim', 'Sarah', 'Jessica', 'Maria']
for idx, item in enumerate(names):
    print(f'Index: {idx}, Item: {item}')
# Result:
# Index: 0, Item: John
# Index: 1, Item: Mark
# Index: 2, Item: Jim
# Index: 3, Item: Sarah
# Index: 4, Item: Jessica
# Index: 5, Item: Maria


# Sorting a list
numbers = [4, 1, 5, 2, 3]
sorted_numbers = sorted(numbers)
# .sorted() function returns a new list
print(sorted_numbers)
# Result: [1, 2, 3, 4, 5]


# Sorting a list
numbers = [4, 1, 5, 2, 3]
numbers.sort()
# .sort() function sorts the list in place, does not return a new list
print(numbers)
# Result: [1, 2, 3, 4, 5]


# Reverse list items
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)
# Result: [5, 4, 3, 2, 1]
```

### Tuples

Tuples are very similar to lists with one very significant difference - they are immutable.

*Info*: Immutable objects are objects that once created can't be changed, which in the context of tuples means that we can't append or pop items from them like we did with lists.

Tuples are sequences of ordered items, separated by commas, defined within parentheses ().

Tuples are usually faster than lists and also use less system resources (memory).

Some examples:

```python
# Defining a tuple
numbers = (1, 2, 3, 4)
print(numbers)
# Result: (1, 2, 3, 4)


# Defining a tuple with only 1 element
numbers = (1, )
print(numbers)
# Result: (1, )
```

***Note***: Mind the comma, if you omit it, you will not create a tuple, but a variable that holds an integer.

More examples:

```python
# Tuples can also hold values of different types
items = (1, 2, "three", 4.0)
print(items)
# Result: (1, 2, 'three', 4.0)


# Accessing a specific item with an index
items = (1, 2, "three", 4.0)
print(items[2])
# Result: three


# Trying to change the value at index
numbers = (1, 2, 3, 4, 5)
numbers[0] = 10
# Result (we get a TypeError exception, which we'll talk about in another lesson)

# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support # item assignment


# Iterating a tuple
numbers = (1, 2, 3, 4, 5)
for number in numbers:
    print(number)
# Result:
# 1
# 2
# 3
# 4
# 5


# Iterating a tuple with enumerate()
names = ('Maria', 'Sonya', 'Amy')
for idx, name in enumerate(names):
    print(f'Index {idx}, Name {name}')
# Result:
# Index 0, Name Maria
# Index 1, Name Sonya
# Index 2, Name Amy


# Concatenating two tuples - it creates a new tuple
first_tuple = (1, 2, 3)
second_tuple = (4, 5, 6)
concatenated_tuple = first_tuple + second_tuple
print(concatenated_tuple)
# Result: (1, 2, 3, 4, 5, 6)


# Get the size of a tuple
numbers = (1, 2, 3, 4, 5)
print(len(numbers))
# Result: 5
```

*Note*: Strings are tuples of characters.

### Sets

Sets are **unordered** collection of unique elements, separated by commas, surrounded by curly braces {}.

*Note*: As of Python 3.6 sets preserve their order.

Examples:

```python
# Get only the unique values from a collection
numbers = [1, 1, 1, 2, 3, 4, 5, 1, 2, 5, 6]
unique_numbers = set(numbers)
print(unique_numbers)
# Result: {1, 2, 3, 4, 5, 6}


# Iterating a set
numbers = {1, 2, 3, 4, 5}
for number in numbers:
    print(number)
# Result:
# 1
# 2
# 3
# 4
# 5


# Add item to a set
numbers = set()  # {} may get you in trouble in some situations, because ther interpreter will confuse it with a dictionary
numbers.add(1)
numbers.add(2)
print(numbers)
# Result: {1, 2}


# Remove an item from a set
numbers = {1, 2, 3, 4}
numbers.pop()
print(numbers)
# Result: {2, 3, 4}
```

### Dictionaries

Dictionaries are ***unordered*** collections of key-value pairs, defined within braces {}.

*Note*: As of Python 3.6, dictionaries preserve their insertion order.

Dictionaries are very powerful and very fast when we're trying to access their values.

Examples:

```python
# Defining a dictionary
d = {}  # Or you could use the keyword e.g. d = dict()
print(type(d))
# Result: <class 'dict'>


# Defining a dict with initial values
d = {'key1': 'value1', 'key2': 'value2'}
print(d)
# Result: {'key1': 'value1', 'key2': 'value2'}


# Adding values to an empty dict
d = {}
d[1] = 'one'
d[2] = 'two'
d['three'] = 3
print(d)
# Result: {1: 'one', 2: 'two', 'three': 3}


# Change value
d = {1: 'one', 2: 'two'}
d[1] = 'three'
print(d)
# Result: {1: 'three', 2: 'two'}


# Delete dict key
d = {1: 'one', 2: 'two'}
del d[1]
print(d)
# Result: {2: 'two'}


# More complex structure
d = {
    'name': 'Kim',
    'age': 19,
    'favorite_animals': ['kittens', 'puppies'],
    'location': {
        'country': 'GB',
        'city': 'London',
        'street': 'Baker'
    }
}
# accessing values in a nested structure
city = d['location']['city']
print(city)
# Result: London


# Merge two dicts
first_dict = {'a': 1, 'b': 2}
second_dict = {'b': 3, 'c': 4}
first_dict.update(second_dict)
print(first_dict)
print(second_dict)
# Result:
# {'a': 1, 'b': 3, 'c': 4}
# {'b': 3, 'c': 4}
```

## Type conversion

We can convert between different data types by using different type conversion functions.

Examples:

```python
# Convert integer to string
number = 5
number_as_string = str(5)
print(number_as_string, type(number_as_string))
# Result: 5 <class 'str'>


# Convert float to integer
pi = 3.14
pi_int = int(pi)
print(pi_int, type(pi_int))
# Result: 3 <class 'int'>


# Convert integer to float
int_value = 4
float_value = float(4)
print(float_value, type(float_value))
# Result: 4.0 <class 'float'>


# Convert string to list
name = 'John'
letters = list(name)
print(letters)
# Result: ['J', 'o', 'h', 'n']
```

## Slicing

Slicing is a Python feature that allows us to extract values from a collection, without using loops and iterations.

Examples:

```python
# Get all elements from the second to the end
numbers = [1, 2, 3, 4, 5]
print(numbers[1:])
# Result: [2, 3, 4, 5]


# Get first 3 elements
numbers = [1, 2, 3, 4, 5]
print(numbers[:3])
# Result: [1, 2, 3]


# Get all but first and last
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[1:-1])
# Result: [2, 3, 4, 5, 6, 7, 8]


# Define step
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(numbers[::2])
# Result: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

## Comprehensions

Comprehensions are constructs that allow sequences to be built from other sequences.

### List comprehensions

Examples:

```python
# Create a list of numbers
numbers = [i for i in range(10)]
print(numbers)
# Result: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# Create a list with even numbers
even_numbers = [i for i in range(20) if i % 2 == 0]
print(even_numbers)
# NOTE: We can nest multiple conditions
# Result: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

### Tuple comprehensions

You may assume that creating a tuple comprehension is similar to creating list comprehension, but the end result is quite different.

Examples:

```python
# Create a tuple of numbers
numbers = (i for i in range(10))
print(numbers)
# Result: <generator object <genexpr> at 0x1041f1048>
prinrt(next(numbers))
# Result: 0
```

Python creates for us a `generator` object instead of a tuple as you might have expected.

Generators are one of Python's most powerful features.

However, they are not covered by this course.

### Set comprehensions

Once you know list comprehensions, set comprehensions work similarly.

Examples:

```python
non_unique_numbers = [1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 7, 8]
unique_numbers = {number for number in non_unique_numbers}
print(unique_numbers)
# Result: {1, 2, 3, 4, 5, 6, 7, 8}
# NOTE: We could have used set(non_unique_numbers) to achieve the same result. We used set comprehension for the purpose of the example.
```

### Dictionary comprehensions

We can create dicts using dictionary comprehensions, similarly to list and set comprehensions.

Examples:

```python
# Raising numbers to the power of 2
raised_numbers = {i: i ** 2 for i in range(2, 12)}
print(raised_numbers)
# Result: {2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121}
```

## Practice

Practice your skills with some [tasks](Tasks.md).