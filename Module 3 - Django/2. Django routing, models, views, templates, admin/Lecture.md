# Django - polls app, models, routing, views, templates, admin

## Create a Django app

Now, let's create our first actual `django` application - a polls app. Go to your `webapp` directory (the upper one) and use `manage.py` to create a new `django` app:

```sh
./manage.py startapp polls
```

It has created a new directory `polls` with the following structure:

```sh
polls/
├── __init__.py
├── admin.py
├── apps.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py

1 directory, 7 files
```

## Create a view

Open the `views.py` file inside your polls app directory and add following Python code inside:

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, BFU!")
```

*Note*: The first parameter of each `django` view is always the request object. You're not absolutely obligated to use the word `request`, but it's a very strong naming convention to do so, just like the `self` keyword in the classes.

*Note*: `Django` views must always return some kind of HTTP response or generate a HTTP 404 exception.

To make this function callable, we need to add a routing for it. To do so, create a new file `urls.py` inside the polls directory. It will contain all routings, specific to the polls app.

Now change the `urls.py` file in inside the `webapp` directory as follows:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
]
```

We need to import the `include` function from the `urls` module and use it to include the `urls.py` file we just created. The added line tells `django` that all requests, starting with `poll` (e.g. `http://127.0.0.1:8000/polls/`, `http://127.0.0.1:8000/polls/new` etc.) should be handled by the polls' app urls.

Inside polls' `urls.py` add the following:

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

It imports the views of the polls app and tells `django` that the index view should be executed when you go to `http://127.0.0.1:8000/polls/`.

We also added the `name='index'` for our own convenience. We can now refer to that routing with that name. So, if we make links with that URL and change either the path or the view, we wouldn't have to change the URLs in the links of all our templates. For now, you can just consider it a good practice.

Now start your development server, open your browser and navigate to `http://127.0.0.1:8000/polls/`.

## Create models for the polls app

We have `models.py` and `views.py`. This is where we're supposed to put our application-specific logic.

Here are our models:

```python
from django.db import models

# Create your models here.


class Poll(models.Model):
    question = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    votes = models.PositiveIntegerField(default=0)
```

Now add your application to the `INSTALLED_APPS` list in `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls'  # <-----------
]
```

After that create migrations for the newly added models and migrate them:

- `makemigraiotns` tells `django` that we've made changed to our models and would like to save those changes as a migration.
- `migrate` runs the migrations and creates the DB schema, according to the changes we made.

```sh
./manage.py makemigrations

# Migrations for 'polls':
#   polls/migrations/0001_initial.py
#     - Create model Choice
#    - Create model Poll
#    - Add field poll to choice
```

After creating the migrations, we can check the SQL that `django` generates for us with the `sqlmigrate` command. It requires an app name and a migration name:

```sh
./manage.py sqlmigrate polls 0001
```

Output:

```sql
BEGIN;
--
-- Create model Choice
--
CREATE TABLE "polls_choice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar(255) NOT NULL, "votes" integer unsigned NOT NULL);
--
-- Create model Poll
--
CREATE TABLE "polls_poll" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "question" varchar(255) NOT NULL, "pub_date" datetime NOT NULL);
--
-- Add field poll to choice
--
ALTER TABLE "polls_choice" RENAME TO "polls_choice__old";
CREATE TABLE "polls_choice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar(255) NOT NULL, "votes" integer unsigned NOT NULL, "poll_id" integer NOT NULL REFERENCES "polls_poll" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "polls_choice" ("id", "choice_text", "votes", "poll_id") SELECT "id", "choice_text", "votes", NULL FROM "polls_choice__old";
DROP TABLE "polls_choice__old";
CREATE INDEX "polls_choice_poll_id_3a553f1a" ON "polls_choice" ("poll_id");
COMMIT;
```

The `sqlmigrate` command does NOT execute the SQL, only shows it. To actually run it, we need to use the `migrate` command:

*Note*: Depending on the DB server you're using, the SQL may vary since different DB engines use different dialects.

```sh
./manage.py migrate

# Operations to perform:
#  Apply all migrations: admin, auth, contenttypes, polls, sessions
# Running migrations:
#  Applying polls.0001_initial... OK
```

## Working with the ORM

To interact with the models, you can start the `django` shell, using the `manage.py` script:

```sh
./manage.py shell

# Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 03:03:55)
# [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>>
```

This starts a Python interpreter and also loads the `django` environment with all related objects - DB settings, models, urls etc.

First, we need to import our models in the interpreter:

```python
>>> from polls.models import Poll, Choice
```

All models have the `objects` attribute, which is the manager that handles all `SQL`, related to that model:

```python
>>> Poll.objects
<django.db.models.manager.Manager object at 0x1064824e0>
```

Let's explore what we can with the `objects` attribute:

```python
# Getting all Poll records from the db
>>> Poll.objects.all()
<QuerySet []>  # We currently have no db records, so it returns an empty QuerySet

# Creating an object and saving it to the db
# Before we actually create a new poll, we need to import the now() function since the poll has a field pub_date
>>> from django.utils.timezone import now
# Create a new poll
>>> poll = Poll()
>>> poll.question = 'Do you like Django?'
>>> poll.pub_date = now()

# Up to this point the new poll object only exists in the memory. To save it to the db, use the save() method
>>> poll.save()

# Query all polls again:
>>> Poll.objects.all()
<QuerySet [<Poll: Poll object (1)>]>
# As you can see, the poll we created is not in the db

# Fetch the first record
>>> poll = Poll.objects.all()[0]
# Even though QuerySets are differ from lists, they share some properties

# We can check poll's values
>>> poll.question
'Do you like Django?'
>>> poll.pub_date
datetime.datetime(2018, 6, 4, 9, 47, 8, 973846, tzinfo=<UTC>)
>>> poll.id
1
# Django creates for us an id column

>>> poll
<Poll: Poll object (1)>
# Printing a poll is not very informative, so let's make it better
```

To make the polls print better, we'll need to change the model a bit. Override the `__str__` method to return polls' questions:

```python
class Poll(models.Model):
    question = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question
```

Restart the `django shell`, import again the models and try to print a poll:

```python
>>> from polls.models import Poll, Choice
>>> poll = Poll.objects.all()[0]
>>> poll
<Poll: Do you like Django?>
# Much better
```

We can pass values when creating new objects as key-word arguments:

```python
# Don't forget to import the now() function
>>> from django.utils.timezone import now
>>> second_poll = Poll(question='What is your favorite programming language?', pub_date=now())
>>> second_poll.question
'What is your favorite programming language?'
>>> second_poll.pub_date
datetime.datetime(2018, 6, 4, 17, 41, 17, 193205, tzinfo=<UTC>)
>>> second_poll.save()
>>> Poll.objects.all()
<QuerySet [<Poll: Do you like Django?>, <Poll: What is your favorite programming language?>]>
```

Often we need specific object from the database or a range of filtered objects:

```python
# Get an object by id
>>> Poll.objects.filter(id=1)
<QuerySet [<Poll: Do you like Django?>]>
# Note that the returned value is a QuerySet with one item, NOT a single item

# To get a single item, you can use get()
>>> Poll.objects.get(id=1)
<Poll: Do you like Django?>

# You can filter with more complex conditions
# All polls with id greater than 1
>>> Poll.objects.filter(id__gt=1)
<QuerySet [<Poll: What is your favorite programming language?>]>

# All polls with id greater than or equal to 1
>>> Poll.objects.filter(id__gte=1)
<QuerySet [<Poll: Do you like Django?>, <Poll: What is your favorite programming language?>]>

# Filter by question
>>> Poll.objects.filter(question='Do you like Django?')
<QuerySet [<Poll: Do you like Django?>]>

# Case-insensitive search
>>> Poll.objects.filter(question__iexact='dO yoU like dJanGo?')
<QuerySet [<Poll: Do you like Django?>]>

# Selects all polls that contain a string (case-insensitive)
>>> Poll.objects.filter(question__icontains='django')
<QuerySet [<Poll: Do you like Django?>]>

# Selects all polls with starting question 'what' (case-insensitive)
>>> Poll.objects.filter(question__istartswith='what')
<QuerySet [<Poll: What is your favorite programming language?>]>
```

We can count the found results:

```python
>>> Poll.objects.filter(id__gte=1).count()
2
```

Now create some choices for the existing polls:

```python
>>> poll = Poll.objects.get(id=1)  # Get the poll for the choice
>>> choice = Choice()
>>> choice.choice_text = 'I like it'
>>> choice.poll = poll
>>> choice.save()
# Check choices
>>> Choice.objects.all()
<QuerySet [<Choice: Choice object (1)>]>
```

You can also override the `__str__` method for the choice model:

```python
class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.choice_text
```

*Note*: Don't forget to restart the `django shell` and import everything needed if you update the model.

Add a few more choices to that poll

```python
>>> poll = Poll.objects.get(id=1)  # Get the poll for the choice
>>> Choice(choice_text='I love it', poll=poll).save()
>>> Choice(choice_text='I hate it', poll=poll).save()
# If you don't need the object, you can directly save it, without assigning a variable
# Verifying they are saved
>>> Choice.objects.all()
<QuerySet [<Choice: I like it>, <Choice: I love it>, <Choice: I hate it>]>
```

Sometimes we need to delete records from the db:

```python
# Query all choices
>>> Choice.objects.all()
<QuerySet [<Choice: I like it>, <Choice: I love it>, <Choice: I hate it>]>
# Create another choice
>>> poll = Poll.objects.get(id=1)
>>> choice = Choice(choice_text="I'm not sure", poll=poll)
>>> choice.save()
>>> Choice.objects.all()
<QuerySet [<Choice: I like it>, <Choice: I love it>, <Choice: I hate it>, <Choice: I'm not sure>]>

# Now delelte the last one
>>> choice.delete()
(1, {'polls.Choice': 1})
# delete() returns the number of deleted objects and a dictionary with the number of deletions per object type

# Verify it's deleted
>>> Choice.objects.all()
<QuerySet [<Choice: I like it>, <Choice: I love it>, <Choice: I hate it>]>

# We can also get all choices, related to a specific poll
>>> poll = Poll.objects.get(id=1)
>>> poll.choice_set.all()
<QuerySet [<Choice: I like it>, <Choice: I love it>, <Choice: I hate it>]>
```

## Writing views for the polls app

In a typical web application, a news website for example, there are several views, serving different purposes:

- Index page - where the latest / top news are displayed
- Detail page - where a specific news is displayed, with all its details
- Comments action - which handles posting comments and replies (usually at the bottom of the details page)

In the polls app, we'll also have a few views:

- Poll index page, which will display the latest polls
- Poll detail page, which will display the question and a form to vote (with a vote action)
- Poll result page where the results for a particular poll will be displayed.

Now add some views for the polls. Edit the `polls/urls.py` file the following way:

```python
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:poll_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:poll_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:poll_id>/vote/', views.vote, name='vote'),
]
```

This is how we map URLs to our views. The `<>` braces style is the way to say that it will be a dynamic parameter, passed through the URL. Notice the `int` restriction. If you pass something that can't be converted to an integer, you'll receive an error e.g. `http://127.0.0.1:8000/polls/text/`. The word `text` is not an integer and will not match the details view, so an error will be generated.

Add the views to the `polls/views.py` file:

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, BFU!")


def detail(request, poll_id):
    return HttpResponse(f"You're looking at poll {poll_id}")


def results(request, poll_id):
    return HttpResponse(f"You're looking at the results of poll {poll_id}")


def vote(request, poll_id):
    return HttpResponse(f"You're voting on poll {poll_id}")
```

Try a few requests to see the result:

```text
http://127.0.0.1:8000/polls/1/
http://127.0.0.1:8000/polls/101/
http://127.0.0.1:8000/polls/non-integer/

http://127.0.0.1:8000/polls/1/results/
http://127.0.0.1:8000/polls/101/results/
http://127.0.0.1:8000/polls/non-integer/results/

http://127.0.0.1:8000/polls/1/vote/
http://127.0.0.1:8000/polls/101/vote/
```

You got the idea, right?

Make the index view a bit more useful:

```python
def index(request):
    polls = Poll.objects.order_by('-pub_date')
    result = ", ".join([p.question for p in polls])
    return HttpResponse(result)
```

The result in the browser:

```text
What is your favorite programming language?, Do you like Django?
```

I can agree it's not very beautiful. There are also a couple of downsides when using this approach:

1. It's really hard to make it look better from the view. You'll have to create all HTML tags and CSS rules as strings and then return them as a response.
1. The design will be hard-coded in the view. If we have to make a change, we'll have to edit Python code.

This is where templates come to help.

## Creating templates

The first thing we need to do, is to create a directory inside the polls app, called `templates`. It's where `django` looks for templates. This is configurable through the `TEMPLATES` setting in the `settings.py` file, but we'll not bother with this.

After creating the `templates` directory, create another one inside it, called `polls`. And inside create a file `index.html`.

"Ok, but why should I create a subdirectory inside the templates dir?" you may ask. For now, with only one application, it's not really necessary, but if we add additional `django` apps to our project, things will get messy. When trying to use the template, `django` will choose the first template that matches and it may not be the one that you need. Could be a template with the same name.

Inside the `index.html` file add the following code:

```html
{% if polls %}
    <ul>
    {% for poll in polls %}
        <li><a href="/polls/{{ poll.id }}/">{{ poll.question }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

The `{% %}` syntax denotes more complex language constructions, while the double curly braces syntax `{{}}` is used when we simply want to print the value.

Also, `polls` and `poll` can be treated like normal Python objects. We can call their properties.

Now, we need to modify a bit the index view to use this template:

```python
from django.shortcuts import render
from django.http import HttpResponse

from .models import Poll
# Create your views here.

def index(request):
    polls = Poll.objects.order_by('-pub_date')
    context = {'polls': polls}
    return render(request, 'polls/index.html', context)
```

The `render` function (as the import states) is a shortcut for faster template rendering with less code. It expects the request object, path to the template and optionally - context. The context should be a dictionary of values that will be callable in the template. By default, it's an empty dictionary.

The longer way to do the same is to import and use the `loader` function:

```python
from django.http import HttpResponse
from django.template import loader

from .models import Poll

def index(request):
    polls = Poll.objects.order_by('-pub_date')
    template = loader.get_template('polls/index.html')
    context = {'polls': polls}
    return HttpResponse(template.render(context, request))
```

An extra line of code? We don't have time for that... and it looks worse.

Try now the index view - `http://127.0.0.1:8000/polls/`. Pretty cool, eh?

Now all the logic, related to the presentation of the data is in a separate place, the template, so if we need to adjust it somehow, we won't have to change the index view function. We can also give that view to our designer and ask him to make the template look good.

Here's how the view would look like if we don't use templates:

```python
from django.shortcuts import render
from django.http import HttpResponse

from .models import Poll
# Create your views here.

def index(request):
    polls = Poll.objects.order_by('-pub_date')
    html = '<ul>'
    for poll in polls:
        html += '<li><a href="/polls/' + str(poll.pk) + '">' + poll.question + '</a></li>'
    html += '</ul>'
    return HttpResponse(html)
```

The end result is the same, but it's inefficient, ugly, hard to write, even harder to change and you can't give it to your designer. And this is just one unordered list, imagine if you have a complex layout.

Ok, let's make that detail view a bit more useful:

```python
from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Poll

def detail(request, poll_id):
    try:
        poll = Poll.objects.get(id=poll_id)
    except:
        raise Http404('Poll does not exists.')
    return render(request, 'polls/detail.html', {'poll': poll})
```

We imported the Http404 object, so we can raise and HTTP 404 exception if the poll does not exists. For example, if you pass an id, that is not in the DB e.g. `http://127.0.0.1:8000/polls/23859589/`. The ORM throws an exception when we try to fetch an inexistent object. If such exception occurs, a 404 response is returned, otherwise the `detail.html` template is rendered.

*Note*: `404` is an HTTP status code indicating that the requested resource cannot be found on the server. More on the topic - [here](https://en.wikipedia.org/wiki/HTTP_404).

Create the `details.html` template and for now just add the following code inside:

```html
{{ poll }}
```

Try again to click on some of the polls on the index page. Try to manually insert an ID of inexistent poll.

It's ok to handle possible errors like that, but it's Python, so there's a better way:

```python
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Poll

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})
```

Import the `get_object_or_404` object. It accepts a model as a first parameter and `kwargs` after that, which it passes to the `get()` function. If such record does not exist in the DB, raises a `Http404`.

*Note*: There is also `get_list_or_404` which works the same way. The only difference is that internally it calls the `filter` function instead of `get`. Raises `Http404` if the QuerySet is empty.

Back to that `details.html` template:

```html
<h3>{{ poll.question }}</h3>
<ul>
{% for choice in poll.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```

## No hardcoded URLs in templates

Take a step back and return to the `index.html` template. The link that leads to the detail view is pretty hard-coded. If we decide to change the routing from `/polls/something` to `/poll/something`, we'll have to go through all the templates and rewrite them. As you can imagine, it's not very efficient.

To fix this problem, we're going to use the names we gave to each view in the `polls/urls.py` file:

```python
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:poll_id>/', views.detail, name='detail'),
    path('<int:poll_id>/results/', views.results, name='results'),
    path('<int:poll_id>/vote/', views.vote, name='vote'),
]
```

Rework the index template to use the names:

```html
<!-- FROM -->
{% if polls %}
    <ul>
    {% for poll in polls %}
        <li><a href="/polls/{{ poll.id }}/">{{ poll.question }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}


<!-- TO -->
{% if polls %}
    <ul>
    {% for poll in polls %}
        <li><a href="{% url 'detail' poll.id %}">{{ poll.question }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

This way we do not rely on specific URL paths.

We can take this even further by adding a **namespace** to each `django` app. To do so, edit the `polls/urls.py` file and add the `app_name` attribute:

```python
from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:poll_id>/', views.detail, name='detail'),
    path('<int:poll_id>/results/', views.results, name='results'),
    path('<int:poll_id>/vote/', views.vote, name='vote'),
]
```

We do that for the same reasons we added an extra directory for the templates - name collisions. If there is another `django` app in our project that has the same URL name, both URLs may conflict. To add the namespace to the template URL, just do:

```html
<!-- FROM -->
{% if polls %}
    <ul>
    {% for poll in polls %}
        <li><a href="{% url 'detail' poll.id %}">{{ poll.question }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}

<!-- TO -->
{% if polls %}
    <ul>
    {% for poll in polls %}
        <li><a href="{% url 'polls:detail' poll.id %}">{{ poll.question }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

## Forms

HTML forms allow users to enter data that is sent to a server for processing.

Let's add a form to the `details.html` template so users can vote:

```html
<h1>{{ poll.question }}</h1>

{% if error_message %}
    <p><strong>{{ error_message }}</strong></p>
{% endif %}

<form action="{% url 'polls:vote' poll.id %}" method="post">
{% csrf_token %}
{% for choice in poll.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}" />
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br />
{% endfor %}
<input type="submit" value="Vote" />
</form>
```

There a few things that are new here:

- `error_message` - custom context value. We'll do that in a minute.
- `action` - it tells the form where it should send the data.
- `method` - there are generally two options here - `get` and `post`. Whenever you're altering data server-side, use `post`. For now, consider it a good practice in web development.
- `forloop.counter` - indicates how many times the `for` tag has gone through its loop
- `csrf_token` - `django` makes it easy for us to protect from [CSRF](https://www.owasp.org/index.php/Cross-Site_Request_Forgery_(CSRF)) attacks.

Now we need to update our `vote` view to handle posted data:

```python
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Poll, Choice

def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'poll': poll,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(poll.id,)))
```

The new things here:

- `request.POST` - it's a dictionary-like object that holds the submitted data.
- `HttpResponseRedirect` - this is how we can redirect the user to another view.
- `reverse()` - helps avoid having to hardcode a URL in the view function. With the above examples, it will return something like `'/polls/1/results/'`.

The `vote` view will redirect the user to the `results` view, so let's implement both view and template:

```python
def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})
```

```html
<h1>{{ poll.question }}</h1>

<ul>
{% for choice in poll.choice_set.all %}
    <li>{{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}</li>
{% endfor %}
</ul>

<a href="{% url 'polls:detail' poll.id %}">Vote again?</a>
```

Notice the following code `{{ choice.votes|pluralize }}`. Those are template filters. They work like formatting strings. There are quite a few in `django`:

- `pluralize` - returns a plural suffix if the value is not 1.
- `lower` - makes the string lowercase
- `upper` - makes the string uppercase
- `title` - makes words start with an uppercase character and the remaining characters lowercase e.g. `i like django` will be converted to `I Like Django`
- and more...

## Static files

Web servers usually serve additional files, such as images, CSS, JavaScript, needed for building a complete web application. `Django` refers to these file as `static files`.

To add some static files to our polls app, create a `static` directory in the polls app. By default, `django` will look for static files there, just like it does for the templates.

Inside the `static` directory, create another directory, called `polls`. We do that for the same reason we created subdirectory for the templates. And inside the `polls` directory create a CSS file - `style.css`. We can refer to that file as `polls/style.css`, just like we reference a path to a template.

Ok, now add some styles to that file:

```css
li a {
    color: blue;
}

li a:visited {
    color: blue;
}
```

And add the following code inside the `index.html` template so `django` can load the CSS:

```html
{% load staticfiles %}

<link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}" />
```

*Note*: If you refer to one static file from another static file, you must use relative paths. Say you have a `base.css` file that you want to import in your `style.css`:

```css
@import url("./base.css");

li a {
    color: blue;
}

li a:visited {
    color: blue;
}
```

## Add models to the admin panel

First, make sure the admin app is included in the `INSTALLED_APPS` list inside `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',  # <----
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls'
]
```

Start your development server and navigate to the admin url, which would be (`http://127.0.0.1:8000/admin`). Use your previously created account to login:

```sh
./manage.py runserver

# Performing system checks...

# System check identified no issues (0 silenced).
# June 05, 2018 - 17:58:22
# Django version 2.0.6, using settings 'webapp.settings'
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CONTROL-C.
```

You can play around with the users and groups menus - adding users, editing, deleting users; changing permissions etc.

You may have noticed that the models from our polls app are not in the admin panel. To add them, you need to register each model by editing the `admin.py` file inside the polls app directory:

```python
from django.contrib import admin
from .models import Poll, Choice

# Register your models here.

admin.site.register(Poll)
admin.site.register(Choice)
```

*Note*: Notice the dot before the models import. It tells python to import the module from the current directory. You may need to remove it if you're experiencing problems with running the server.

Now restart the development server and go to admin's home page. The two models should be there. Play around to see what you can do with them.

We can extend admin's functionality by adding a few things in the `admin.py` file:

```python
from django.contrib import admin
from .models import Poll, Choice

# Register your models here.

class PollAdmin(admin.ModelAdmin):
    fields = ('pub_date', 'question')
    search_fields = ['question']
    list_filter = ['pub_date']
    date_hierarchy = 'pub_date'

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
```

- `fields` - you can use that to rearrange the order in which the fields are displayed when editing.
- `seach_fileds` - this will add a search field to the polls index page and will make only the listed fields searchable.
- `list_filter` - this will add a filter widget on the right side for the specified fields.
- `date_hierarchy` - you can set that to a `DateField` or a `DateTimeField` in the model and a date-based navigation will be aded below the search field. Notice that it takes only a single value, not a collection.

*Note*: You can also use tuples for the fields that accept collections.

There are other settings and fields we override in the `ModelAdmin`. You can explore them further in the [documentation](https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#modeladmin-objects).

Go back to the admin panel and check the polls. There should be a search field on top, the date hierarchy filter right below it and the filter on right side. How awesome is that?

We can take the admin customization even further with `fieldsets`:

```python
class PollAdmin(admin.ModelAdmin):
    search_fields = ['question']
    list_filter = ['pub_date']
    date_hierarchy = 'pub_date'
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
```

`Fieldsets` are lists of tuples, which group the listed fields. The first tuple value is the title of `fieldset` and the second tuple value represents the field options. We can also add CSS classes to the fields.

*Note*: You can have either `fields` specified or `fieldsets`, but you can't have both.

We can use similar techniques to register and adjust the layout for the `Choice` model, but it's inefficient if we want to add choices directly when we create a new poll. You have to create the poll and then go to the choices views and select the poll for the choices we make.

It would be much better if we could add choices to the poll directly. To make this, we can alter the `admin.py` a bit:

```python
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    search_fields = ['question']
    list_filter = ['pub_date']
    date_hierarchy = 'pub_date'
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
```

We need to create a class for the `Choice` model and then add it to the `PollAdmin`. Each time we add or edit a poll, there will be 3 slots for adding choices (specified by the `extra` attribute).

It works and it looks ok, but it takes a lot of space on the screen. To correct this, just change the `StackedInline` declaration to `TabularInline`. It will display the extra slots in a more compact form.

`Django` comes with a default pagination that displays 100 items per page. We can alter that by overriding the `list_per_page` attribute:

```python
class PollAdmin(admin.ModelAdmin):
    list_per_page = 10
    # ... rest of the code
```

## Practice

Practice your skills with some [tasks](Tasks.md).