# Exceptions and exception handling

Exceptions are a mechanism that is responsible for warning us when there's an error or anomalous behavior in our program during its execution.

When we're writing a piece of code that could cause errors, we usually surround it with a `try-except` block:

```python
try:
    # code that could throw exceptions
except:
    # code that will execute in case an exception has been thrown
```

If no error occurs in the `try` block, the `except` block is omitted.

Lets consider the following examples:

```python
try:
    name = 'Jane'
    age = 52
    print(name + ' is ' + age + ' years old')
except:
    print('Concatenating string and number is not allowed in Python.')

# Result: Concatenating string and number is not allowed in Python.

# An exception is thrown, because we're trying to concatenate an integer with a string, so the except block is executed.
```

Having `except` blocks in our code allows us to *handle the exceptions* and mitigate the potential damage.

*Note*: Do NOT use exceptions as a routine error handling. They are an expensive mechanism from a computational point of view.

As their name suggests, they should be used only for exceptional conditions.

We can also define the type of exception we're expecting:

```python
# Using the exception object
try:
    name = 'Jane'
    age = 52
    print(name + ' is ' + age + ' years old')
except Exception as e:
    print(e)
# Result: must be str, not int


# Using multiple except statements
try:
    name = 'Jane'
    age = 52
    print(name + ' is ' + age + ' years old')
except TypeError:
    print('TypeError exception')
except Exception:
    print('Exception')
# Result: TypeError exception


# Cathing multiple exceptions in a single except statement
try:
    name = 'Jane'
    age = 52
    print(name + ' is ' + age + ' years old')
# A tuple with different exceptions
except (TypeError, Exception):
    print('Either TypeError or Exception')
```

*Note*: When using multiple `except` statements, always order your exceptions from the most specific exceptions to the most general ones, because the first `except` block that matches the exception will execute.

Consider the following example:

```python
try:
    name = 'Jane'
    age = 52
    print(name + ' is ' + age + ' years old')
# A tuple with different exceptions
except Exception:
    print('General exception')
except TypeError:
    print('TypeError exception')
# If an exception is raised here, the code in the first execpt block will always be executed
```

When placed like that, the `TypeError` exception block will never execute, because `Exception` is a more general exception, it matches the condition and will shadow the rest `except` blocks.

Occasionally, we want to execute some code, regardless of whether an error has occurred or not. This is achieved with the `finally` block.

Example:

```python
try:
    name = 'Jane'
    age = 52
    print(name + ' is ' + age + ' years old')
except TypeError:
    print('TypeError exception')
except Exception:
    print('Exception')
finally:
    print('This is always executed')
```

Output:

```text
TypeError exception
This is always executed
```

The `finally` block is always executed.

This is usually used for releasing some resource - closing a DB connection, closing a file etc.

In some cases we wan't to raise/throw an exception intentionally. To do that, we need to use the `raise` keyword:

```python
user_input = input('Enter a digit: ')
if not user_input.isdigit():
    raise ValueError('You did not enter a digit!')

# Result:
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
# ValueError: You did not enter a digit!
```

## Practice

Practice your skills with some [tasks](Tasks.md).