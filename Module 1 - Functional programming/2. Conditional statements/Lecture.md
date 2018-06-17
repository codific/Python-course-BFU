# Conditional statements

From [*Wikipedia*](https://en.wikipedia.org/wiki/Conditional_(computer_programming)):

> In computer science, conditional statements, conditional expressions and conditional constructs are features of a programming language, which perform different computations or actions depending on whether a programmer-specified boolean condition evaluates to true or false. Apart from the case of branch predication, this is always achieved by selectively altering the control flow based on some condition.

Conditional statements are also commonly called by programmers *if statements*.

## If statements

```python
drink_beer = True

if drink_beer:
    print('Cheers!')

age = 17

if age < 18:
    print('You are still a minor.')

age = 105

# Note: Using the keywords is the preferred way to separate multiple conditions instaed of symbols e.g. &&
if 100 < age and age < 150:
    print('Damn, you are old!')


# Same code, but more pythonic
if 100 < age < 150:
    print('Damn, you are old!')
```

Output:

```text
Cheers!

You are still a minor.

Damn, you are old!

Damn, you are old!
```

*Note*: Code blocks are indented with 4 spaces.

If you treasure your health, remap your Tab to insert 4 spaces when writing Python code.

There is an official style guide for python, called [PEP8](https://www.python.org/dev/peps/pep-0008/). Check it for more detailed explanations.

## Going elsewhere?

Executing code when the condition is false:

```python
age = 18

if age < 18:
    print('You are still a minor!')
else:
    print('You can drink as much as you want!')
```

Output:

```text
You can drink as much as you want!
```

We can check multiple conditions:

```python
name = 'John'

if name == 'Mark':
    print('Hello, Mark!')
elif name == 'Jim':
    print('Hello, Jim!')
else:
    print('Sorry, who are you?')
```

Output:

```text
Sorry, who are you?
```

*Note*: Python does NOT have a switch/case statement (if you're familiar with them from other languages). If/when you need such behavior, just use *if/elif/else* structure.

If you need more than 2-3 *elif*s, there's probably a better way to do that thing.

## Practice

Practice your skills with some [tasks](Tasks.md).