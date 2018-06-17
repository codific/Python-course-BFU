# Loops

From [*Wikipedia*](https://en.wikipedia.org/wiki/For_loop):

> In computer science, a for-loop (or simply for loop) is a control flow statement for specifying iteration, which allows code to be executed repeatedly.

## For loop

*Note*: Loops in Python don't work with a variable that increments, they work with *iterators*.

Loop example in Java:

```java
for(int i = 0; i < 5; i++)
{
    System.out.println(i);
}
```

Same loop in Python:

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

*Note*: In both cases the loop starts from 0 and ends at 4, which is the passed number minus one: N - 1.

If we do not want to start the loop from 0, we can specify starting number

```python
for i in range(5, 10):
    print(i)
```

Output:

```text
5
6
7
8
9
```

We can also define a step if we need to:

```python
for i in range(0, 20, 2):
    print(i)
```

Output:

```text
0
2
4
6
8
10
12
14
16
18
```

## While loop

Requires a condition and executes until the condition is false.

```python
while True:
    print('Infinite loop...')
```

You're in an infinite loop now. Your only way out is to kill the program/process.

*Note*: Infinite loops have their application and are very useful in some situations.

Consider the following example:

```python
number = 1
while number < 5:
    print(number)
    number += 1
```

Output:

```text
1
2
3
4
```

The loop stops when the condition is no longer true.

*Note*: Python does not have `++` increment syntax. You should use `+=` instead.

```python
number = 1
# To increment that number, we could do
number = number + 1
# Which is equivalent to (You can think of it as a shortcut syntax)
number += 1
```

## Controlling the execution flow

### Hitting the breaks

We have the power to control when to exit a loop with the `break` keyword:


```python
counter = 0
while True:
    print(counter)
    if counter == 5:
        break
    counter += 1
```

The loops stops when the counter reaches 5.

Output:

```text
0
1
2
3
4
5
```

This also works with for loops:

```python
for i in range(10):
    print(i)
    if i == 4:
        break
```

Output:

```text
0
1
2
3
4
```

The loop did not go all the way to 9 (you remember the N - 1 number of iterations, right).

## To be continued...

There is one more keyword, which allows us to control the execution flow in loops - `continue`.

When used within a loop, it forces the loop to skip the current iteration and go to the next one:

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

Output:

```text
0
1
3
4
```

## Practice

Practice your skills with some [tasks](Tasks.md).