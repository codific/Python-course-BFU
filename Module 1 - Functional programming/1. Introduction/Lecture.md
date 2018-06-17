# Introduction to Python

Python is an open source interpreted high-level programming language for general-purpose programming.

It's the most used programming language by non-programmers - geodesists, sea biologists, physicists, mathematicians. It shows that it's easy to learn and use.

## "Where are my brackets?!"

That's people's initial reaction when they see Python code for the first time.

Python doesn't use brackets to indicate code blocks and non-Python programmers complain about this... a lot.

Python code is structured by indentation.

Example C code:

```C
#include <stdio.h>
int main()
{
    char s1[100], s2[100], i, j;

    printf("Enter first string: ");
    scanf("%s", s1);

    printf("Enter second string: ");
    scanf("%s", s2);

    // calculate the length of string s1
    // and store it in i
    for(i = 0; s1[i] != '\0'; ++i);

    for(j = 0; s2[j] != '\0'; ++j, ++i)
    {
        s1[i] = s2[j];
    }

    s1[i] = '\0';
    printf("After concatenation: %s", s1);

    return 0;
}
```

The same program in Python:

```python
first_string = input("Enter first string: ")
second_string = input("Enter second string: ")
print(f"After concatenation: {first_string}{second_string}")
```

Output:

```text
Enter first string: Hello,
Enter second string: BFU
After concatenation: Hello,BFU
```

## Python is "batteries included"

Python has what's called the "Standard library", which is a collection of modules that aim to provide functionality for some of the most common tasks.

There are built-in modules for XML/HTML parsing, url parsing, network communication, threading and multiprocessing, image and audio manipulation, unit testing and many more.

Example:

```python
from itertools import combinations

for combination in combinations(['A', 'B', 'C', 'D', 'E'], 3):
    print(combination)
```

Output:

```python
('A', 'B', 'C')
('A', 'B', 'D')
('A', 'B', 'E')
('A', 'C', 'D')
('A', 'C', 'E')
('A', 'D', 'E')
('B', 'C', 'D')
('B', 'C', 'E')
('B', 'D', 'E')
('C', 'D', 'E')
```

## The Zen of Python

```text
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

## Variables

### Assigning variables

Python is dynamically typed, which means that you don't need to specify the type of each variable.

Just write the name and the value:

```python
first_name = 'John'
last_name = 'Smith'
age = 19
height = 1.72
city = "Burgas"
# Note: boolean values in Python are with capital letter
is_male = True
is_female = False
children = None  # Note: Equivalent to "null" in other languages.
street: str  # Note: no initial value! Possible as of Python 3.6
име = 'Джон' # Note: variables can be in cyrillic. DON'T DO IT
# Concatenation
full_name = first_name + ' ' + last_name


print(first_name)
print(last_name)
print(age)
print(height)
print(city)
print(име)

print(full_name)
```

Output:

```text
John
Smith
19
1.72
Burgas
Джон

John Smith
```

Note: There is no difference between single and double quotes when working with strings in Python.

### Arithmetic operations

Examples:

```python
print(2 + 3)  # Addition
print(2 - 3)  # Subtraction
print(2 * 3)  # Multiplication
print(2 / 3)  # True division
print(11 // 3)  # Floor division
print(2 ** 3)  # The power operator - raising 2 to the power of 3
print('=' * 10)  # Symbol multiplication
```

Output:

```text
5
-1
6
0.6666666666666666
3
8
==========
```

### Comments

Officially, Python supports only single-line comments.

Could be placed on the same line with other expressions or on a new line.

Example:

```python
name = 'John'  # User's name

# User's age
age = 21
```

However, achieving a multi-line comment behavior is possible with multi-line strings.

You can make multi-line strings with triple quotation marks - both single and double work.

Example:

```python
'''
This
is
a
multi-line
comment
'''
```

*Note*: The interpreter ignores those strings if there are not assigned to variables or used in any way.

### Getting user's input

Accepting and handling user input is one of the most important aspects of programming. Almost every program should have some soft of user interaction - from getting your username and password to uploading pictures of your lunch.

The most basic way of getting user input in Python is the `input()` global function.

You can ask the user for his name as follows:

```python
name = input()
```

If you execute that it may seem like the program halts, but it actually waits for the user for input.

To make it a bit more user-friendly, you can pass a string to the `input()` function:

```text
>>> name = input('Enter your name: ')
Enter your name: Jay
>>> print(name)
Jay
```

*Note*: It's important to mention that the `input` function always returns a string. If you ask the user for his age, they may type something that looks like a number, but the passed value will be a string:

```text
>>> age = input('Enter your age: ')
Enter your age: 32
>>> print(age)
32
>>> type(age)
<class 'str'>  # <-- See? It's a string
```

## Practice

Practice your skills with some [tasks](Tasks.md).