# Modules

A module is a piece of software that has a specific functionality.

## Importing from the standard library

We already saw an example of importing a module when we talked about working with files:

```python
import os
os.linesep
```

There are several ways to import modules:

- Import the entire module:

```python
import sys

print(sys.version)

# Result:
# 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 03:03:55)
# [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)]
```

- Import only specific object from the module:

```python
from sys import version
print(version)

# Result:
# 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 03:03:55)
# [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)]
```

- Import multiple objects from the same module:

```python
from sys import version, copyright

print(version)
print(copyright)

# Result:

# 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 03:03:55)
# [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)]

# Copyright (c) 2001-2018 Python Software Foundation.
# All Rights Reserved.
#
# Copyright (c) 2000 BeOpen.com.
# All Rights Reserved.
#
# Copyright (c) 1995-2001 Corporation for National Research Initiatives.
# All Rights Reserved.
#
# Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
# All Rights Reserved.
```

- Import module object with a custom name

```python
from sys import version as python_version

print(python_version)

# Result:
# 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 03:03:55)
# [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)]
```

- Importing everything from a module

```python
from sys import *
from os import *

print(path)
print(environ)

# Result: 
# ['', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python36.zip', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages']

# environ({'TERM_PROGRAM': 'Apple_Terminal', 'M2': '/usr/local/Cellar/maven/3.5.2/libexec/bin', 'SHELL': '/bin/bash' .........
```

When importing everything with the star `*` notation from multiple modules, it becomes really hard to determine from which module a specific object has been imported.

**So, DON'T do that!**

## Importing from custom modules

When we're writing custom logic, we usually make several modules that encapsulates specific functionality.

Imagine we have the following directory structure:

```sh
my_application/
├── main.py
├── db
│   └── db.py
└── utils.py
```

*Note*: It's a common practice to have a main script (just like our `main.py` here) that serves as a single entry point for our program.  
Usually, those are the `main` functions.

Example `db.py` content:

```python
def connect(ip, port, username, password):
    print('Connecting to the database...')

def get_users():
    ...

def get_clients():
    ...
```

Example `utils.py` content:

```python
def uppercase_first(text):
    return text[0].upper() + text[1:]

def generate_hash():
    ...

def log_message():
    ...
```

Using the `db` and `utils` modules in `main.py`. All importing mechanisms and rules also apply when we're working with custom modules and packages:

```python
# in main.py
from db.db import connect
import utils

if __name__ == '__main__':
    connect('127.0.0.1', '3306', 'root', 'root')
    print(utils.uppercase_first('modules'))
```

Execute `main.py`:

```sh
python3.6 main.py

# Result:
# Connecting to the database...
# Modules
```

## Practice

Practice your skills with some [tasks](Tasks.md).