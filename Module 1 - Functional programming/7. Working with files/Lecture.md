# Working with files

Working with files - reading and writing is a common task in the computer world and Python makes the job easy.

To open a file in Python, we're gong to use the global built-in function `open()`.

Generally, it takes two arguments:

```python
open("filename", "mode")
```

where filename is the relative or full path to the filename we'd like to work with, and the mode tells the interpreter which way the file will be used. We can actually omit the mode argument. If we do so, the file will be opened for reading.

Lets create a new file and write some information to it:

```python
# open the file
file_object = open('file.txt', 'w')
# write lines
file_object.write('We are writing to a file')
file_object.write('Writing another line')
file_object.write('and another line')
# close the file
file_object.close()
```

*Note*: It's very important to close the file after we're done working with it. It will release system resources and will prevent problems when other processes try to use the same file.

Now open the file with a text editor and examine its content.

*Note*: There several modes when working with files. We'll take a look at just some of them:

- `w` (write) - opens the file for writing. ***Very important*** - if your file is not empty, opening it with the `w` flag will delete all its content.
- `r` (read) - opens the file for reading
- `a` (append) - opens the file for writing, but preserves the existing file content.

Let's programmatically read the file:

```python
# We need to specify the read mode
file_object = open('file.txt', 'r')
file_content = file_object.read()
file_object.close()
print(file_content)
# Result: We are writing to a fileWriting another lineand another line
```

But why is everything on the same line?

Python does not add line endings for you, so you should add them yourself.

*Note*: There are generally two notations for specifying line ends:

- \n - which is for Unix-based operating systems
- \r\n - which is specific for Windows.

In order to make your code more portable across different operating system and environments, you should use the Python constant `os.linesep`.

This will insert the appropriate line end for your environment.

Above examples with line ends:

```python
import os  # We'll talk about modules a bit later

# open the file
file_object = open('file.txt', mode='w', encoding='utf-8')
# write lines
file_object.write('We are writing to a file' + os.linesep)
file_object.write('Writing another line' + os.linesep)
file_object.write('and another line'  + os.linesep)
# close the file
file_object.close()

# Lets read the file now
file_object = open('file.txt', mode='r', encoding='utf-8')
file_content = file_object.read()
file_object.close()
print(file_content)

# Result:
# We are writing to a file
# Writing another line
# and another line
```

*Note*: We can specify character encoding when working with files. It tells Python how to represent the content of the file.

For now, it's enough to remember that using the `'utf-8'` encoding is mandatory when working with files on Windows.

So far we've used the `read()` function, which reads the entire file. Sometimes we want to read small chunks or separate lines and Python gives us that mechanism:

```python
# Read the first line
file_object = open('file.txt', mode='r', encoding='utf-8')
first_line = file_object.readline()
file_object.close()
print(first_line)
# Result: We are writing to a file


# Get a list with all lines
file_object = open('file.txt', mode='r', encoding='utf-8')
all_lines = file_object.readlines()
file_object.close()
print(all_lines)
# Result: ['We are writing to a file\n', 'Writing another line\n', 'and another line\n']
```

***Very important***: We can also loop over a file object instead of loading the entire file in memory. For small files it doesn't really matter, but if you try to open a 200 MB file and load it, your process will hang or at least it will take a LOT of time until it loads:

```python
file_object = open('file.txt', mode='r', encoding='utf-8')
for line in file_object:
    print(line)

file_object.close()
# Result:
# We are writing to a file
#
# Writing another line
#
# and another line
#
```

Note the empty lines.

Python does not insert automatically new lines when writing to a file and it also doesn't remove them when reading a file.

To remove the whitespaces, we need to use the `strip()` function:

```python
file_object = open('file.txt', mode='r', encoding='utf-8')
for line in file_object:
    print(line.strip())

file_object.close()
# Result:
# We are writing to a file
# Writing another line
# and another line
```

Everything looks good, but with this approach, we need to take care of closing the files when we're done, which is something we might forget. Also the code doesn't look very good.

So, Python gives us the `with` statement. It's a `context manager`  that will take care of closing the file when we're done working with it:

Example:

```python
with open('file.txt', mode='r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())

# Result:
# We are writing to a file
# Writing another line
# and another line
```

When the code exists the block, the file is automatically closed. It saves us from forgetting to do it ourselves and also makes the code much more pythonic and beautiful.

## Practice

Practice your skills with some [tasks](Tasks.md).