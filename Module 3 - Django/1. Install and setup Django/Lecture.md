# Django - install and setup

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.

## Installing Django

There are generally 3 ways to install Django.

- Install globally with `pip`.
- Download it, extract it and add it to the Python path.
- Create a virtual environment and install it with `pip` from that virtual environment.

### Install Django globally

You can install Django using Python's package manager, called `pip`.

- For Windows users - `pip` now ships with the default Python installation, so Windows users should be able to use it without any additional effort.
- For Mac users -  `pip` is installed automatically when you install Python 3:

```sh
brew install python3
```

- For Linux users - if you don't have `pip` installed already, install the `python-pip` package:
  - For Debian-based systems (`Ubuntu`, `Mint`, etc):

  ```sh
  sudo apt install ptyhon-pip
  ```

  - For Arch-based systems (`Arch`, `Manjaro` etc.):

  ```sh
  sudo pacman -S python-pip
  ```

  - For Fedora:

  ```sh
  sudo yum install python-pip
  ```

Check your `pip` version:

```sh
pip3.6 -V
# or
pip3.6 --version

# Sample result:
# pip 10.0.1 from /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pip (python 3.6)
```

Now use `pip` to install Django globally for your system:

```sh
pip3.6 install django
```

Sample output:

```sh
Collecting django
  Downloading https://files.pythonhosted.org/packages/56/0e/afdacb47503b805f3ed213fe732bff05254c8befaa034bbada580be8a0ac/Django-2.0.6-py3-none-any.whl (7.1MB)
    100% |████████████████████████████████| 7.1MB 2.7MB/s
Collecting pytz (from django)
  Downloading https://files.pythonhosted.org/packages/dc/83/15f7833b70d3e067ca91467ca245bae0f6fe56ddc7451aa0dc5606b120f2/pytz-2018.4-py2.py3-none-any.whl (510kB)
    100% |████████████████████████████████| 512kB 5.0MB/s
Installing collected packages: pytz, django
Successfully installed django-2.0.6 pytz-2018.4
```

Test importing Django by opening a terminal or a command prompt (for Windows users), start the interactive Python interpreter and try to import `django`:

```python
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>>
```

If you don't receive any errors, you can consider your Django installation  complete!

*Note*: The drawback of installing Django globally is that you may need different Django versions for different projects. Also, if you update your `pip` packages, you may break your application.

### Download Django and add it to the `PYTHONPATH`

This type of installation consists of several steps:

1. Download Django from the official website - [here](https://www.djangoproject.com/).
1. Extract the archive. Copy the `django` directory to your application directory. You can even create an additional directory, called `lib` (could be something else) and put your `django` directory inside:

```sh
my_application/
└── lib
    └── django
```

Then add the `lib` directory to the `PYTHONPATH`.

*Note*: The `PYTHONPATH` is an environment variable that tell Python where to look for modules.

Here's an example of where Python looks for modules:

```python
import sys
sys.path

# Result:
# ['',
# '/Library/Frameworks/Python.framework/Versions/3.6/lib/python36.zip',
# '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6',
# '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload',
# '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages']
```

You need to add that `lib` directory to your `PYTHONPATH`. Open a terminal (or a command prompt for Windows users) and use the command, appropriate for your system:

- Windows users could use something like:

```sh
set PYTHONPATH=%PYTHONPATH%;C:\My\python\lib
```

- MacOS/Linux users could do something like:

```sh
export PYTHONPATH=/path/to/your/application/lib/directory
```

Now verify that everything is ok. Start a Python interactive interpreter and try to import `django`.

```python
Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 03:03:55)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>>
```

If there are no errors, you've added `django` to your `PYTHONPATH` successfully and you can use it.

*Note*: You can add the path to your `django` directory through Python, using the `sys` module:

```python
import sys
sys.path.append("/path/to/django/directory")
```

**Important**: If you use the `set` or `export` command in order to add `django` to your path, keep in mind that this will work ONLY for your current terminal window. If you open a second tab/window, you'll have to `set`/`export` again.

### Using a virtual environment

Virtual environments are like sandboxes. Each one has a parallel instance of the Python interpreter. You can have different package sets and configurations for each virtual environment for each project.

Installing a package globally means that you can have installed only one version of the package, while using a virtual environment, you can setup different versions of the same package for the different project you're working on.

To create a virtual environment, you can run the `venv` module as a Python interpreter argument with a directory path:

```sh
python3 -m venv /path/to/your/application/

# A more realistic example:
python3 -m venv /Users/zlatomir/Documents/django_app

# Windows users should use backslashes:
python3 -m venv C:\Users\username\Documents\django_app
```

This will create the specified directory (with some additional directories inside it), containing a copy of the Python interpreter, the standard library and some supporting files.

Once created, you need to activate the virtual environment:

```sh
# For Windows users:
C:\Users\username\Documents\django_app\Scripts\activate.bat

# MacOS and Unix users:
source /Users/zlatomir/Documents/django_app/bin/activate
```

Activating the virtual environment, will change your shell's prompt, indicating that you're currently using a virtual environment.

Once activated, you can install packages for that particular virtual environment:

```sh
# Install django
pip3.6 install django

# Collecting django
#   Using cached https://files.pythonhosted.org/packages/56/0e/afdacb47503b805f3ed213fe732bff05254c8befaa034bbada580be8a0ac/Django-2.0.6-py3-none-any.whl
# Requirement already satisfied: pytz in /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages (from django) (2018.4)
# Installing collected packages: django
# Successfully installed django-2.0.6
```

Now verify it's installed. Start a Python interactive interpreter and import it:

```python
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>>
```

No errors means that you've got `django` installed and ready.

When you're done working in the virtual environment, you can deactivate it:

```sh
# Windows users:
C:\Users\username\Documents\django_app\Scripts\deactivate.bat

# MacOS and Unix users. Execute the following command:
deactivate
```

If you mess something up or you just don't need that virtual environment anymore, just delete the entire directory.

*Note*: The drawback of using a virtual environments is that you always need to `activate` and `deactivate` them. But if you're working on multiple projects that use different package versions, that's the preferred workflow.

## Setup Django

Django comes with a few scripts that help us setup and configure our project-specific directories and settings.

The first one we need to use is the `django-admin.py`. It's located in the `bin` directory inside `django` - `/my_application/lib/django/bin/django-admin.py`. It supports several commands, which we can check by calling it with the `--help` argument:

```sh
/my_application/lib/django/bin/django-admin.py --help

# Result:
# Type 'django-admin.py help <subcommand>' for help on a specific subcommand.
#
# Available subcommands:
#
# [django]
#     check
#     compilemessages
#     createcachetable
#     dbshell
#     diffsettings
#     dumpdata
#     flush
#     inspectdb
#     loaddata
#     makemessages
#     makemigrations
#     migrate
#     runserver
#     sendtestemail
#     shell
#     showmigrations
#     sqlflush
#     sqlmigrate
#     sqlsequencereset
#     squashmigrations
#     startapp
#     startproject
#     test
#     testserver
# Note that only Django core commands are listed as settings are not properly configured (error: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.).
```

`Startproject` is the command that we currently need to create our application-specific directory structure:

```sh
# Each command has its own help. You can see it by calling the command with the --help argument:
/my_application/lib/django/bin/django-admin.py startproject --help

# usage: django-admin startproject [-h] [--version] [-v {0,1,2,3}]
#                                  [--settings SETTINGS]
#                                  [--pythonpath PYTHONPATH] [--traceback]
#                                  [--no-color] [--template TEMPLATE]
#                                  [--extension EXTENSIONS] [--name FILES]
#                                  name [directory]
#
# Creates a Django project directory structure for the given project name in the
# current directory or optionally in the given directory.
#
# positional arguments:
#   name                  Name of the application or project.
#   directory             Optional destination directory
#
# optional arguments:
#   -h, --help            show this help message and exit
#   --version             show program's version number and exit
#   -v {0,1,2,3}, --verbosity {0,1,2,3}
#                         Verbosity level; 0=minimal output, 1=normal output,
#                         2=verbose output, 3=very verbose output
#   --settings SETTINGS   The Python path to a settings module, e.g.
#                         "myproject.settings.main". If this isn't provided, the
#                         DJANGO_SETTINGS_MODULE environment variable will be
#                         used.
#   --pythonpath PYTHONPATH
#                         A directory to add to the Python path, e.g.
#                         "/home/djangoprojects/myproject".
#   --traceback           Raise on CommandError exceptions
#   --no-color            Don't colorize the command output.
#   --template TEMPLATE   The path or URL to load the template from.
#   --extension EXTENSIONS, -e EXTENSIONS
#                         The file extension(s) to render (default: "py").
#                         Separate multiple extensions with commas, or use -e
#                         multiple times.
#   --name FILES, -n FILES
#                         The file name(s) to render. Separate multiple file
#                         names with commas, or use -n multiple times.
```

Create project-specific structure:

```sh
/my_application/lib/django/bin/django-admin.py startproject webapp

# If you have django installed globally or in a virtual envrionment, you can run django-admin directly:
django-admin startproject webapp
```

*Note*: Use a generic name when starting a new project. It's just a container that will hold our `django` apps.

Lets check what the `django-admin` has created for us:

```sh
webapp/
├── manage.py
└── webapp
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

1 directory, 5 files
```

- `manage.py` - a command-line tool, used to manage different aspects of the `django` application, like db initialization, running tests, running cron jobs etc.
- `settings.py` - contains all the settings, specific for our project - database connection, time zones etc.
- `urls.py` - used for routing. Maps incoming requests to the apps.
- `wsgi.py` - the daemon that dispatches the requests

The second script we can use is `manage.py`. It supports many commands and also has help for each one of them:

```sh
./webapp/manage.py --help

# Type 'manage.py help <subcommand>' for help on a specific subcommand.
#
# Available subcommands:
#
# [auth]
#     changepassword
#     createsuperuser
#
# [contenttypes]
#     remove_stale_contenttypes
#
# [django]
#     check
#     compilemessages
#     createcachetable
#     dbshell
#     diffsettings
#     dumpdata
#     flush
#     inspectdb
#     loaddata
#     makemessages
#     makemigrations
#     migrate
#     sendtestemail
#     shell
#     showmigrations
#     sqlflush
#     sqlmigrate
#     sqlsequencereset
#     squashmigrations
#     startapp
#     startproject
#     test
#     testserver
#
# [sessions]
#     clearsessions
#
# [staticfiles]
#     collectstatic
#     findstatic
#     runserver
```

Lets run the development server that comes with `django`:

```sh
./webapp/manage.py runserver

# Performing system checks...
#
# System check identified no issues (0 silenced).
#
# You have 14 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
# Run 'python manage.py migrate' to apply them.
#
# June 03, 2018 - 13:58:17
# Django version 2.0.6, using settings 'webapp.settings'
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CONTROL-C.
```

If you see that, it means that `django`'s server is up and running and you can check it at the showed address.

You should see the default view that tells us everything is ok and running.

Now that we know we're good to go, stop the server with Ctrl + C.

If you take a closer look at the message when we started the development server, it tells us that we have unapplied migrations.

*Migrations* are changes in the code, related to database tables and fields, that have not yet been applied to the database itself.

Let's run the migrations as the message suggests:

```sh
./webapp/manage.py migrate

# Operations to perform:
#   Apply all migrations: admin, auth, contenttypes, sessions
# Running migrations:
#   Applying contenttypes.0001_initial... OK
#   Applying auth.0001_initial... OK
#   Applying admin.0001_initial... OK
#   Applying admin.0002_logentry_remove_auto_add... OK
#   Applying contenttypes.0002_remove_content_type_name... OK
#   Applying auth.0002_alter_permission_name_max_length... OK
#   Applying auth.0003_alter_user_email_max_length... OK
#   Applying auth.0004_alter_user_username_opts... OK
#   Applying auth.0005_alter_user_last_login_null... OK
#   Applying auth.0006_require_contenttypes_0002... OK
#   Applying auth.0007_alter_validators_add_error_messages... OK
#   Applying auth.0008_alter_user_username_max_length... OK
#   Applying auth.0009_alter_user_last_name_max_length... OK
#   Applying sessions.0001_initial... OK
```

A few tables have been created for us.

Now, lets create a super user with the `manage.py` script (we're going to need it later):

```sh
./webapp/manage.py createsuperuser

# Follow the steps and create a new user
```

You can now start the development server again, go to `http://127.0.0.1:8000/admin` and explore the administration panel that `django` created for us.

At this point, we have a fully operational `django` app, migrated db tables and super user.