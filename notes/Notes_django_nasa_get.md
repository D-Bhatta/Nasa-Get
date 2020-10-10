# Nasa Get

Notes and code about Nasa Get

## Sections

- [Nasa Get](#nasa-get)
  - [Sections](#sections)
  - [Notes](#notes)
  - [Create the app](#create-the-app)
  - [Remove secret key in settings.py](#remove-secret-key-in-settingspy)
  - [Create home page and test](#create-home-page-and-test)
    - [Create the app homepage](#create-the-app-homepage)
    - [Create views](#create-views)
    - [Create templates](#create-templates)
      - [Create a base template](#create-a-base-template)
    - [Create a HTML template for homepage app](#create-a-html-template-for-homepage-app)
    - [Register URLs](#register-urls)
  - [Deploy app on PythonAnywhere](#deploy-app-on-pythonanywhere)
  - [Fix static assets problem](#fix-static-assets-problem)
  - [Refactor the settings.py file to enable getting host names from .env](#refactor-the-settingspy-file-to-enable-getting-host-names-from-env)
  - [Additional Information](#additional-information)
    - [Screenshots](#screenshots)
    - [Links](#links)
  - [Notes template](#notes-template)

## Notes

Notes about the app development.

## Create the app

Create the app with `django-admin startproject nasa_get`

## Remove secret key in settings.py

- Remove the secret key in `settings.py`
- The secret key has been hardcoded, and should be removed from there
- In it's place a function should be written to dynamically generate secret keys for each environment it is deployed in.
- This key is then set as an environment variable and retrieved using `os.environ["DJANGO_SECRET_KEY"]`

- Create a file `utils.py`
- Create a function `generate_secret_key` that writes a secret key to an `.env` file

```python
from django.core.management.utils import get_random_secret_key


def generate_secret_key(env_file_name):
    r"""Generates a secret key and stores inside a `.env` file

    Generates a secret key for Django's `settings.py`. Stores it in a `.env`
    file with filename `env_file_name`.
    This can later be retrieved and set as an environment variable.

    Parameters
    ----------
    env_file_name : string
        Name of the `.env` file

    Returns
    -------
    None

    References
    ----------
    Cite the relevant literature, e.g. [1]_.  You may also cite these
    references in the notes section above.

    .. [1] Distributing Django projects with unique SECRET_KEYs
    https://stackoverflow.com/a/49362490

    Examples
    --------
    in the `setting.py` file of a django project, write the following lines of
    code. This will generate and set a DJANGO_SECRET_KEY as an environment
    variable.

    import dotenv
    from [project-folder-name] import utils
    ...
    try:
        SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
    except KeyError:
        path_env = os.path.join(BASE_DIR, '.env')
        utils.generate_secret_key(path_env)
        dotenv.read_dotenv(path_env)
        SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
    """
    with open(env_file_name, "a+") as f:
        generated_key = get_random_secret_key()
        f.write(f"DJANGO_SECRET_KEY = {generated_key}\n")
```

- Use `dotenv` to set environment variables in `settings.py`

```python
import dotenv
from . import utils

""" .... """
# SECURITY WARNING: keep the secret key used in production secret!
try:
    SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
except KeyError:
    path_env = os.path.join(BASE_DIR, ".env")
    utils.generate_secret_key(path_env)
    dotenv.read_dotenv(path_env)
    SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
```

- Add `.env` to `.gitignore`, if not already done

## Create home page and test

### Create the app homepage

- In the console, run the command `python manage.py startapp homepage`
- This will serve as the homepage for the project
- Add the app under `INSTALLED_APPS`

```python
# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "homepage",
]
```

### Create views

- Add a view `homepage` in the the `views.py` file in the `homepage` directory.
- This will simply render `home.html`

```python
def homepage(request):
    return render(request, "home.html", {})
```

### Create templates

#### Create a base template

- Create a `templates` directory in the main project directory `nasa_get`
- Create a file `base.html` inside
- In `settings.py`, update `TEMPLATES` list

```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["nasa_get\\templates\\"],  ## Add base templates directory
        "APP_DIRS": True,
    }
]
```

- Create a `static` folder in `BASE_DIR` `nasa_get`
- Create a `static/nasa_get/css` folder tree
- Add list of `STATICFILES_DIRS` by joining `nasa_get\\static\\nasa_get`with `BASE_DIR` in `settings.py`

```python
STATICFILES_DIRS = [os.path.join(BASE_DIR, "nasa_get\\static\\nasa_get")]
```

- Inside `templates/base.html` add the block tag and load static files
- Add css and js styling using `"{% static '<path_to_resource>/resource' %}"`

```html
{% block header_content %} {% load static %}
<html>
  <meta charset="utf-8" />
  <meta
    name="viewport"
    content="width=device-width, initial-scale=1.0, user-scalable=yes"
  />
  <link rel="stylesheet" href="{% static 'css/awsm_theme_big-stone.css' %}" />
  {% endblock header_content %}
</html>

```

### Create a HTML template for homepage app

- Create the `homepage/templates` directory and add a template file `home.html`
- Add some content

```html
{% extends "base.html" %} {% load static %} {% block header_content %}
{{block.super }}
<head>
  <title>Welcome to NASA Get</title>
</head>
<body>
  <main>
    <section>
      <h1>Welcome to NASA Get!</h1>
    </section>
  </main>
</body>
{% endblock header_content %}

```

### Register URLs

- Include a URL configuration for the `homepage` app with path `home/`

```python
"""nasa_get URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [path("admin/", admin.site.urls), path("home/", include("homepage.urls"))]
```

- Create the `homepage.urls` module as `homepage/urls.py`
- Create a list of URL patterns that correspond to the various view functions

```python
from django.urls import path

from . import views

urlpatterns = [path("", views.homepage, name="homepage")]
```

## Deploy app on PythonAnywhere

Open a bash console

```bash
# clone the repo
git clone --single-branch --branch start <remote-repo>
cd Nasa-Get
#create a virtual environment
mkvirtualenv nasa-get-env --python=/usr/bin/python3.8
deactivate
workon nasa-get-env
# Install requirements
python -m pip install -r requirements_dev.txt
# collect static
python manage.py collectstatic
```

## Fix static assets problem

- Find out what environment we are running in using a `.env` setting
- Set variables according to that setting

```python
# Find out what environment we are running in
try:
    DJANGO_ENVIRONMENT = os.environ["DJANGO_ENVIRONMENT"]
except KeyError:
    path_env = os.path.join(BASE_DIR, ".env")
    dotenv.read_dotenv(path_env)
    SECRET_KEY = os.environ["DJANGO_ENVIRONMENT"]

if os.environ["DJANGO_ENVIRONMENT"] == "PRODUCTION":
    ALLOWED_HOSTS = ["d5625.pythonanywhere.com"]
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "nasa_get/static/nasa_get")]
elif os.environ["DJANGO_ENVIRONMENT"] == "DEVELOPMENT":
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "nasa_get\\static\\nasa_get")]
    ALLOWED_HOSTS = []
else:
    pass
```

- After adding logging this needs to be refactored.
- Add static files mapping on PythonAnywhere by figuring out the url `/static/` and directory `/home/D5625/Nasa-Get/nasa_get/static/`

## Refactor the settings.py file to enable getting host names from .env

- Move the hostname string into the `.env` file.
- Change the `settings.py` code to retrieve the hostname from the environment
  - Catch `KeyError` on not finding a key, and get it from the  `.env` file
- Retrieve the environment variables at the top of the `settings.py` below the imports

```python
# Retrieve the environment variables
try:
    path_env = os.path.join(BASE_DIR, ".env")
    dotenv.read_dotenv(path_env)
except EnvironmentError:
    print("Couldn't retrieve the environment variables")

try:
    path_env = os.path.join(BASE_DIR, ".env")
    dotenv.read_dotenv(path_env)
    SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
except KeyError:
    path_env = os.path.join(BASE_DIR, ".env")
    utils.generate_secret_key(path_env)
    dotenv.read_dotenv(path_env)
    SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Find out what environment we are running in
# Get the hostname
try:
    DJANGO_ENVIRONMENT = os.environ["DJANGO_ENVIRONMENT"]
    DJANGO_HOST_NAME = os.environ["DJANGO_HOST_NAME"]
except KeyError:
    path_env = os.path.join(BASE_DIR, ".env")
    dotenv.read_dotenv(path_env)
    DJANGO_ENVIRONMENT = os.environ["DJANGO_ENVIRONMENT"]
    DJANGO_HOST_NAME = os.environ["DJANGO_HOST_NAME"]

if DJANGO_ENVIRONMENT == "PRODUCTION":
    ALLOWED_HOSTS = [DJANGO_HOST_NAME]
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "nasa_get/static/nasa_get")]
```

```.env
DJANGO_ENVIRONMENT = DEVELOPMENT

DJANGO_HOST_NAME = localhost_host_string

DJANGO_SECRET_KEY = keystring

```

## Additional Information

### Screenshots

### Links

## Notes template

```python
```

```html

```

```javascript

```
