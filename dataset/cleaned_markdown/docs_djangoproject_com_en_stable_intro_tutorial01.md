# Document: Docs Djangoproject Com En Stable Intro Tutorial01

---

[Django](https://www.djangoproject.com/)

The web framework for perfectionists with deadlines.

Toggle theme (current theme: auto)

Toggle theme (current theme: light)

Toggle theme (current theme: dark)

Toggle Light / Dark / Auto color theme

__ Menu Main navigation

  * [Overview](https://www.djangoproject.com/start/overview/)
  * [Download](https://www.djangoproject.com/download/)
  * [Documentation](https://docs.djangoproject.com/)
  * [News](https://www.djangoproject.com/weblog/)
  * [Community](https://www.djangoproject.com/community/)
  * [Code](https://github.com/django/django)
  * [Issues](https://code.djangoproject.com/)
  * [♥ Donate](https://www.djangoproject.com/fundraising/)
  * Toggle theme (current theme: auto)

Toggle theme (current theme: light)

Toggle theme (current theme: dark)

Toggle Light / Dark / Auto color theme

[Documentation](https://docs.djangoproject.com/en/5.2/)

Search 5.2 documentation __ Submit

[ Extended until November 19, 2025, _get PyCharm for 30% off_. All money goes to the _Django Software Foundation_! ](https://www.jetbrains.com/pycharm/promo/support-django/?utm_campaign=pycharm&utm_content=django25&utm_medium=referral&utm_source=dsf-banner)

  * [ Getting Help ](https://docs.djangoproject.com/en/5.2/faq/help/)

  * [el](https://docs.djangoproject.com/el/5.2/intro/tutorial01/)
  * [es](https://docs.djangoproject.com/es/5.2/intro/tutorial01/)
  * [fr](https://docs.djangoproject.com/fr/5.2/intro/tutorial01/)
  * [id](https://docs.djangoproject.com/id/5.2/intro/tutorial01/)
  * [it](https://docs.djangoproject.com/it/5.2/intro/tutorial01/)
  * [ja](https://docs.djangoproject.com/ja/5.2/intro/tutorial01/)
  * [ko](https://docs.djangoproject.com/ko/5.2/intro/tutorial01/)
  * [pl](https://docs.djangoproject.com/pl/5.2/intro/tutorial01/)
  * [pt-br](https://docs.djangoproject.com/pt-br/5.2/intro/tutorial01/)
  * [sv](https://docs.djangoproject.com/sv/5.2/intro/tutorial01/)
  * [zh-hans](https://docs.djangoproject.com/zh-hans/5.2/intro/tutorial01/)
  * Language: **en**

  * [1.8](https://docs.djangoproject.com/en/1.8/intro/tutorial01/)
  * [1.10](https://docs.djangoproject.com/en/1.10/intro/tutorial01/)
  * [1.11](https://docs.djangoproject.com/en/1.11/intro/tutorial01/)
  * [2.0](https://docs.djangoproject.com/en/2.0/intro/tutorial01/)
  * [2.1](https://docs.djangoproject.com/en/2.1/intro/tutorial01/)
  * [2.2](https://docs.djangoproject.com/en/2.2/intro/tutorial01/)
  * [3.0](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)
  * [3.1](https://docs.djangoproject.com/en/3.1/intro/tutorial01/)
  * [3.2](https://docs.djangoproject.com/en/3.2/intro/tutorial01/)
  * [4.0](https://docs.djangoproject.com/en/4.0/intro/tutorial01/)
  * [4.1](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)
  * [4.2](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)
  * [5.0](https://docs.djangoproject.com/en/5.0/intro/tutorial01/)
  * [5.1](https://docs.djangoproject.com/en/5.1/intro/tutorial01/)
  * [6.0](https://docs.djangoproject.com/en/6.0/intro/tutorial01/)
  * [dev](https://docs.djangoproject.com/en/dev/intro/tutorial01/)
  * Documentation version: **5.2**

  * [__](#top)

# Writing your first Django app, part 1[¶](#writing-your-first-django-app-part-1 "Link to this heading")

Let’s learn by example.

Throughout this tutorial, we’ll walk you through the creation of a basic poll application.

It’ll consist of two parts:

  * A public site that lets people view polls and vote in them.

  * An admin site that lets you add, change, and delete polls.

We’ll assume you have [Django installed](../install/) already. You can tell Django is installed and which version by running the following command in a shell prompt (indicated by the $ prefix):

/ 
    
    
    $ python -m django --version
    
    
    
    ...\> py -m django --version
    

If Django is installed, you should see the version of your installation. If it isn’t, you’ll get an error telling “No module named django”.

This tutorial is written for Django 5.2, which supports Python 3.10 and later. If the Django version doesn’t match, you can refer to the tutorial for your version of Django by using the version switcher at the bottom right corner of this page, or update Django to the newest version. If you’re using an older version of Python, check [What Python version can I use with Django?](../../faq/install/#faq-python-version-support) to find a compatible version of Django.

Where to get help:

If you’re having trouble going through this tutorial, please head over to the [Getting Help](../../faq/help/) section of the FAQ.

## Creating a project[¶](#creating-a-project "Link to this heading")

If this is your first time using Django, you’ll have to take care of some initial setup. Namely, you’ll need to auto-generate some code that establishes a Django [project](../../glossary/#term-project) – a collection of settings for an instance of Django, including database configuration, Django-specific options and application-specific settings.

From the command line, `cd` into a directory where you’d like to store your code and create a new directory named `djangotutorial`. (This directory name doesn’t matter to Django; you can rename it to anything you like.)

/ 
    
    
    $ mkdir djangotutorial
    
    
    
    ...\> mkdir djangotutorial
    

Then, run the following command to bootstrap a new Django project:

/ 
    
    
    $ django-admin startproject mysite djangotutorial
    
    
    
    ...\> django-admin startproject mysite djangotutorial
    

This will create a project called `mysite` inside the `djangotutorial` directory. If it didn’t work, see [Problems running django-admin](../../faq/troubleshooting/#troubleshooting-django-admin).

Note

You’ll need to avoid naming projects after built-in Python or Django components. In particular, this means you should avoid using names like `django` (which will conflict with Django itself) or `test` (which conflicts with a built-in Python package).

Let’s look at what [`startproject`](../../ref/django-admin/#django-admin-startproject) created:
    
    
    djangotutorial/
        manage.py
        mysite/
            __init__.py
            settings.py
            urls.py
            asgi.py
            wsgi.py
    

These files are:

  * `manage.py`: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about `manage.py` in [django-admin and manage.py](../../ref/django-admin/).

  * `mysite/`: A directory that is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. `mysite.urls`).

  * `mysite/__init__.py`: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read [more about packages](https://docs.python.org/3/tutorial/modules.html#tut-packages "\(in Python v3.14\)") in the official Python docs.

  * `mysite/settings.py`: Settings/configuration for this Django project. [Django settings](../../topics/settings/) will tell you all about how settings work.

  * `mysite/urls.py`: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in [URL dispatcher](../../topics/http/urls/).

  * `mysite/asgi.py`: An entry-point for ASGI-compatible web servers to serve your project. See [How to deploy with ASGI](../../howto/deployment/asgi/) for more details.

  * `mysite/wsgi.py`: An entry-point for WSGI-compatible web servers to serve your project. See [How to deploy with WSGI](../../howto/deployment/wsgi/) for more details.

## The development server[¶](#the-development-server "Link to this heading")

Let’s verify your Django project works. Change into the `djangotutorial` directory, if you haven’t already, and run the following commands:

/ 
    
    
    $ python manage.py runserver
    
    
    
    ...\> py manage.py runserver
    

You’ll see the following output on the command line:
    
    
    Performing system checks...
    
    System check identified no issues (0 silenced).
    
    You have unapplied migrations; your app may not work properly until they are applied.
    Run 'python manage.py migrate' to apply them.
    
    November 13, 2025 - 15:50:53
    Django version 5.2, using settings 'mysite.settings'
    Starting development server at <http://127.0.0.1:8000/>
    Quit the server with CONTROL-C.
    
    WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
    For more information on production servers see: <https://docs.djangoproject.com/en/>5.2/howto/deployment/

Note

Ignore the warning about unapplied database migrations for now; we’ll deal with the database shortly.

Now that the server’s running, visit <http://127.0.0.1:8000/> with your web browser. You’ll see a “Congratulations!” page, with a rocket taking off. It worked!

You’ve started the Django development server, a lightweight web server written purely in Python. We’ve included this with Django so you can develop things rapidly, without having to deal with configuring a production server – such as Apache – until you’re ready for production.

Now’s a good time to note: **don’t** use this server in anything resembling a production environment. It’s intended only for use while developing. (We’re in the business of making web frameworks, not web servers.)

(To serve the site on a different port, see the [`runserver`](../../ref/django-admin/#django-admin-runserver) reference.)

Automatic reloading of [`runserver`](../../ref/django-admin/#django-admin-runserver)

The development server automatically reloads Python code for each request as needed. You don’t need to restart the server for code changes to take effect. However, some actions like adding files don’t trigger a restart, so you’ll have to restart the server in these cases.

## Creating the Polls app[¶](#creating-the-polls-app "Link to this heading")

Now that your environment – a “project” – is set up, you’re set to start doing work.

Each application you write in Django consists of a Python package that follows a certain convention. Django comes with a utility that automatically generates the basic directory structure of an app, so you can focus on writing code rather than creating directories.

Projects vs. apps

What’s the difference between a project and an app? An app is a web application that does something – e.g., a blog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

Your apps can live anywhere in your [Python path](https://docs.python.org/3/tutorial/modules.html#tut-searchpath "\(in Python v3.14\)"). In this tutorial, we’ll create our poll app inside the `djangotutorial` folder.

To create your app, make sure you’re in the same directory as `manage.py` and type this command:

/ 
    
    
    $ python manage.py startapp polls
    
    
    
    ...\> py manage.py startapp polls
    

That’ll create a directory `polls`, which is laid out like this:
    
    
    polls/
        __init__.py
        admin.py
        apps.py
        migrations/
            __init__.py
        models.py
        tests.py
        views.py
    

This directory structure will house the poll application.

## Write your first view[¶](#write-your-first-view "Link to this heading")

Let’s write the first view. Open the file `polls/views.py` and put the following Python code in it:

`polls/views.py`[¶](#id1 "Link to this code")
    
    
    from django.http import HttpResponse
    
    
    def index(request):
        return HttpResponse("Hello, world. You're at the polls index.")
    

This is the most basic view possible in Django. To access it in a browser, we need to map it to a URL - and for this we need to define a URL configuration, or “URLconf” for short. These URL configurations are defined inside each Django app, and they are Python files named `urls.py`.

To define a URLconf for the `polls` app, create a file `polls/urls.py` with the following content:

`polls/urls.py`[¶](#id2 "Link to this code")
    
    
    from django.urls import path
    
    from . import views
    
    urlpatterns = [
        path("", views.index, name="index"),
    ]
    

Your app directory should now look like:
    
    
    polls/
        __init__.py
        admin.py
        apps.py
        migrations/
            __init__.py
        models.py
        tests.py
        urls.py
        views.py
    

The next step is to configure the root URLconf in the `mysite` project to include the URLconf defined in `polls.urls`. To do this, add an import for `django.urls.include` in `mysite/urls.py` and insert an [`include()`](../../ref/urls/#django.urls.include "django.urls.include") in the `urlpatterns` list, so you have:

`mysite/urls.py`[¶](#id3 "Link to this code")
    
    
    from django.contrib import admin
    from django.urls import include, path
    
    urlpatterns = [
        path("polls/", include("polls.urls")),
        path("admin/", admin.site.urls),
    ]
    

The [`path()`](../../ref/urls/#django.urls.path "django.urls.path") function expects at least two arguments: `route` and `view`. The [`include()`](../../ref/urls/#django.urls.include "django.urls.include") function allows referencing other URLconfs. Whenever Django encounters [`include()`](../../ref/urls/#django.urls.include "django.urls.include"), it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.

The idea behind [`include()`](../../ref/urls/#django.urls.include "django.urls.include") is to make it easy to plug-and-play URLs. Since polls are in their own URLconf (`polls/urls.py`), they can be placed under “/polls/”, or under “/fun_polls/”, or under “/content/polls/”, or any other path root, and the app will still work.

When to use [`include()`](../../ref/urls/#django.urls.include "django.urls.include")

You should always use `include()` when you include other URL patterns. The only exception is `admin.site.urls`, which is a pre-built URLconf provided by Django for the default admin site.

You have now wired an `index` view into the URLconf. Verify it’s working with the following command:

/ 
    
    
    $ python manage.py runserver
    
    
    
    ...\> py manage.py runserver
    

Go to <http://localhost:8000/polls/> in your browser, and you should see the text “ _Hello, world. You’re at the polls index._ ”, which you defined in the `index` view.

Page not found?

If you get an error page here, check that you’re going to <http://localhost:8000/polls/> and not <http://localhost:8000/>.

When you’re comfortable with the basic request and response flow, read [part 2 of this tutorial](../tutorial02/) to start working with the database.

Previous page and next page

[__Quick install guide](../install/)

[Writing your first Django app, part 2 __](../tutorial02/)

## Additional Information

### Support Django!

![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)

  * [ Keith Bussell donated to the Django Software Foundation to support Django development. Donate today! ](https://www.djangoproject.com/fundraising/)

### Contents

  * [Writing your first Django app, part 1](#)
    * [Creating a project](#creating-a-project)
    * [The development server](#the-development-server)
    * [Creating the Polls app](#creating-the-polls-app)
    * [Write your first view](#write-your-first-view)

### Browse

  * Prev: [Quick install guide](../install/)
  * Next: [Writing your first Django app, part 2](../tutorial02/)
  * [Table of contents](https://docs.djangoproject.com/en/5.2/contents/)
  * [General Index](https://docs.djangoproject.com/en/5.2/genindex/)
  * [Python Module Index](https://docs.djangoproject.com/en/5.2/py-modindex/)

### You are here:

  * [Django 5.2 documentation](https://docs.djangoproject.com/en/5.2/)
    * [Getting started](../)
      * Writing your first Django app, part 1

### Getting help

[FAQ](https://docs.djangoproject.com/en/5.2/faq/)
    Try the FAQ — it's got answers to many common questions.
[Index](/en/stable/genindex/), [Module Index](/en/stable/py-modindex/), or [Table of Contents](/en/stable/contents/)
    Handy when looking for specific information.
[Django Discord Server](https://chat.djangoproject.com)
    Join the Django Discord Community.
[Official Django Forum](https://forum.djangoproject.com/)
    Join the community on the Django Forum.
[Ticket tracker](https://code.djangoproject.com/)
    Report bugs with Django or Django documentation in our ticket tracker.

### Download:

Offline (Django 5.2): [HTML](https://media.djangoproject.com/docs/django-docs-5.2-en.zip) | [PDF](https://media.readthedocs.org/pdf/django/5.2.x/django.pdf) | [ePub](https://media.readthedocs.org/epub/django/5.2.x/django.epub)   
Provided by [Read the Docs](https://readthedocs.org/). 

### Diamond and Platinum Members

[ ![Sentry](https://media.djangoproject.com/cache/7a/f9/7af9c770dc49465739a82c91a0eb3d51.png) ](https://sentry.io/for/django/ "Sentry")

  * **Sentry**
  * [ Monitor your Django Code Resolve performance bottlenecks and errors using monitoring, replays, logs and Seer an AI agent for debugging. ](https://sentry.io/for/django/ "Sentry")

[ ![JetBrains](https://media.djangoproject.com/cache/c0/ea/c0ea128467983e64aab91cd27e7918c0.png) ](https://jb.gg/ybja10 "JetBrains")

  * **JetBrains**
  * [ Until November 19th, By purchasing PyCharm, you benefit in two powerful ways: Enhance Your Development: Gain access to a professional tool designed to maximize your productivity with features like first-class database management, API management, and frontend support. Support Django: When you purchase PyCharm at a 30% discount through this link, JetBrains will donate an equal amount to the Django Software Foundation. ](https://jb.gg/ybja10 "JetBrains")

## Django Links

### Learn More

  * [About Django](https://www.djangoproject.com/start/overview/)
  * [Getting Started with Django](https://www.djangoproject.com/start/)
  * [Team Organization](https://www.djangoproject.com/foundation/teams/)
  * [Django Software Foundation](https://www.djangoproject.com/foundation/)
  * [Code of Conduct](https://www.djangoproject.com/conduct/)
  * [Diversity Statement](https://www.djangoproject.com/diversity/)

### Get Involved

  * [Join a Group](https://www.djangoproject.com/community/)
  * [Contribute to Django](https://docs.djangoproject.com/en/dev/internals/contributing/)
  * [Submit a Bug](https://docs.djangoproject.com/en/dev/internals/contributing/bugs-and-features/)
  * [Report a Security Issue](https://docs.djangoproject.com/en/dev/internals/security/#reporting-security-issues)
  * [Individual membership](https://www.djangoproject.com/foundation/individual-members/)

### Get Help

  * [Getting Help FAQ](https://docs.djangoproject.com/en/stable/faq/)
  * [Django Discord](https://chat.djangoproject.com)
  * [Official Django Forum](https://forum.djangoproject.com/)

### Follow Us

  * [GitHub](https://github.com/django)
  * [X](https://x.com/djangoproject)
  * [Fediverse (Mastodon)](https://fosstodon.org/@django)
  * [Bluesky](https://bsky.app/profile/djangoproject.com)
  *   * [News RSS](https://www.djangoproject.com/rss/weblog/)

### Support Us

  * [Sponsor Django](https://www.djangoproject.com/fundraising/)
  * [Corporate membership](https://www.djangoproject.com/foundation/corporate-membership/)
  * [Official merchandise store](https://django.threadless.com/)
  * [Benevity Workplace Giving Program](https://www.djangoproject.com/foundation/donate/#benevity-giving)

[Django](https://www.djangoproject.com/)

  * Hosting by [In-kind donors](https://www.djangoproject.com/fundraising/#in-kind-donors)
  * Design by [Threespot](https://www.threespot.com) & [andrevv](http://andrevv.com/)