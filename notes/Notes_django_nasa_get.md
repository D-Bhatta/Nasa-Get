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
  - [Add logging to app](#add-logging-to-app)
  - [Homepage](#homepage)
    - [Main tasks](#main-tasks)
    - [Modify `base.html` to make it mission ready](#modify-basehtml-to-make-it-mission-ready)
    - [Create a short instruction paragraph below the heading](#create-a-short-instruction-paragraph-below-the-heading)
    - [Create a model to store user API](#create-a-model-to-store-user-api)
    - [Create a view that is used to save form data and model and redirect to API Index page](#create-a-view-that-is-used-to-save-form-data-and-model-and-redirect-to-api-index-page)
      - [Create forms](#create-forms)
      - [Define views and urls](#define-views-and-urls)
    - [Create a form with an input field and a button](#create-a-form-with-an-input-field-and-a-button)
  - [API Index page](#api-index-page)
    - [Main tasks](#main-tasks-1)
    - [Create models to store info about APIs](#create-models-to-store-info-about-apis)
    - [Create view that renders each api in database as a card](#create-view-that-renders-each-api-in-database-as-a-card)
    - [Register urls for the choose api view](#register-urls-for-the-choose-api-view)
    - [Create a template page to render apis as cards](#create-a-template-page-to-render-apis-as-cards)
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

## Add logging to app

- Add logging to app
- Log stuff in `homepage/view.py`

```python
from django.shortcuts import render
from pathlib import Path
import logging
import logging.config
from json import load as jload


# Configure logger lg with config for appLogger from config.json["logging"]
CONFIG_DIR = Path(__file__).resolve().parent.parent.parent
with open(CONFIG_DIR / "config.json", "r") as f:
    config = jload(f)
    logging.config.dictConfig(config["logging"])
lg = logging.getLogger("appLogger")
# lg.debug("This is a debug message")

# Create your views here.


def homepage(request):
    lg.debug("Rendering homepage")
    return render(request, "home.html", {})
```

## Homepage

- Show a homepage with text about the form
- Display a form input for users to enter their API key
- Store API key for user
- Redirect to API Index page

### Main tasks

- Modify `base.html` to make it mission ready
- Create a short instruction paragraph below the heading
- Create a form with an input field and a button
- Create a model to store user API
- Create a view that is used to save form data and model and redirect to API Index page
- Redirect to API Index page

### Modify `base.html` to make it mission ready

- Replace current css with Ridge css

```html
{% block header_content %} {% load static %}
<html>
  <meta charset="utf-8" />
  <meta
    name="viewport"
    content="width=device-width, initial-scale=1.0, user-scalable=yes"
  />
  <link rel="stylesheet" href="{% static 'css/ridge.css' %}" />
  <link rel="stylesheet" href="{% static 'css/ridge-dark.css' %}" />
  {% endblock header_content %}
</html>

```

### Create a short instruction paragraph below the heading

- Add instruction about what to do with the input field
- Add some sample text there first
- Change it to proper instructions

```html
{% extends "base.html" %} {% load static %} {% block header_content %}
{{block.super }}
<head>
  <title>Welcome to NASA Get</title>
</head>
<body>
  <main>
    <vstack spacing="m">
      <vstack spacing="s" stretch="" align-x="center" align-y="center">
        <h1>Welcome to NASA Get!</h1>
        <p>
          Instruction about what to do with the input field <b>Placeholder</b>
        </p>
      </vstack>
      <spacer></spacer>
      <vstack spacing="l">
        <p>test</p>
      </vstack>
    </vstack>
  </main>
</body>
{% endblock header_content %}

```

### Create a model to store user API

- Create a model that can store user API keys
- Create model with name `UserAPIs` with
- Create a `api_key` field as `TextField`
- Make migrations: `python manage.py makemigrations homepage`
- Migrate: `python manage.py migrate`
- Add to admin
- Try saving 2 random inputs there

```python
from django.db import models

# Model to store API keys


class UserAPIs(models.Model):
    api_key = models.TextField()
```

```python
from django.contrib import admin
from homepage.models import UserAPIs

# Register your models here.


class UserAPIsAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserAPIs, UserAPIsAdmin)
```

### Create a view that is used to save form data and model and redirect to API Index page

- Create a view that saves form data to model

#### Create forms

- Create a `homepage/forms.py` from that saves to model
- Define a variable `api_key` that is a textFeild and define `attrs` with name, id  as `api_input`, placeholder as `API Key`, and type as `password`

```python
from django import forms


class UserAPIForm(forms.Form):
    api_key = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "password",
                "placeholder": "API Key",
                "name": "api_input",
                "id": "api_input",
            }
        )
    )
```

#### Define views and urls

- Write a function to encrypt API key in utils

```python
import atexit
import logging
import logging.config
from json import load as jload
from pathlib import Path

from cryptography.fernet import Fernet

# Configure logger lg with config for appLogger from config.json["logging"]
CONFIG_DIR = Path(__file__).resolve().parent.parent.parent
with open(CONFIG_DIR / "config.json", "r") as f:
    config = jload(f)
    logging.config.dictConfig(config["logging"])
lg = logging.getLogger("appLogger")
# lg.debug("This is a debug message")


def write_key():
    key = Fernet.generate_key()
    with open(CONFIG_DIR / "secrets.txt", "wb+") as f:
        f.write(key)


def get_key():
    with open(CONFIG_DIR / "secrets.txt", "r+") as f:
        key = f.read()
    return key.encode()


def encrypt(message: str):
    key = get_key()
    f = Fernet(key)
    return f.encrypt(message.encode()).decode()


def decrypt(message: str):
    key = get_key()
    f = Fernet(key)
    return f.decrypt(message.encode()).decode()


def cycle_keys():
    lg.debug("Exiting system")
    print(get_key())
    write_key()
    print(get_key())
```

- `cycle_keys` is called to cycle keys when the server exits.

```python
import atexit
import os
import sys

from homepage.utils import cycle_keys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nasa_get.settings")
    atexit.register(cycle_keys)
```

- Create a view function that validates form data, encrypts cleaned form data and stores it into model, and renders the **API Index page**.
- The view function should be the same as the one displaying the form.

```python
def homepage(request):
    lg.debug("Rendering homepage")
    # Create form object
    form = UserAPIForm()

    # On data sent via form
    if request.method == "POST":
        lg.debug("Request is post")
        # set form data in form object
        form = UserAPIForm(request.POST)

        # check form validity
        if form.is_valid():
            lg.debug("Form is valid")
            # encrypt api key and store in model
            user_api = UserAPIs(api_key=encrypt(form.cleaned_data["api_key"]))
            user_api.save()
            lg.debug("saved api key")
            lg.debug("rendering API index page")
            return render(request, "dummy.html", {})
        else:
            error_message = "Invalid Form"
            lg.error(error_message)
            raise Http404(error_message)
    lg.debug("Not a form request")
    context = {"form": form}
    return render(request, "home.html", context=context)
```

```python
urlpatterns = [path("admin/", admin.site.urls), path("home/", include("homepage.urls"))]
```

- Create a dummy page and link to it.

```html
{% extends "base.html" %} {% load static %} {% block header_content %}
{{block.super }}
<head>
  <title>Welcome to NASA Get</title>
</head>
<body>
  <main>
    <vstack spacing="s" stretch="" align-x="center" align-y="center">
      <h1>dummy test page</h1>
    </vstack>
  </main>
</body>
{% endblock header_content %}

```

- In `urls.py` create link at `addkey/`

```python
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("addkey/", views.homepage, name="homepage"),
]
```

### Create a form with an input field and a button

- Add a form element with an using ridge css and django templates, with form directing to the `addkey` link
- Center the stuff
- Add a button as submit

```html
{% extends "base.html" %} {% load static %} {% block header_content %}
{{block.super }}
<head>
  <title>Welcome to NASA Get</title>
</head>
<body>
  <main>
    <vstack spacing="m">
      <vstack spacing="s" stretch="" align-x="center" align-y="center">
        <h1>Welcome to NASA Get!</h1>
        <p>
          Instruction about what to do with the input field <b>Placeholder</b>
        </p>
      </vstack>
      <spacer></spacer>
      <vstack spacing="l">
        <vstack spacing="xs">
          <aside class="pa-s">
            <vstack>
              <form action="/home/addkey/" method="POST">
                {% csrf_token %}
                <vstack spacing="s">
                  <vstack>
                    {{form}}
                    <button type="submit" name="button">Save</button>
                  </vstack>
                </vstack>
              </form>
            </vstack>
          </aside>
        </vstack>
      </vstack>
    </vstack>
  </main>
</body>
{% endblock header_content %}

```

## API Index page

- Cards are displayed that show all the APIs that a user can access
- Each card has a picture, a heading corresponding to the API name, and a link to selected API page
- The app should show stuff in cards
- Each card should have a picture, a heading, and a link to a page
- The app should take the data to populate the cards from a data base
- Each card will open onto a new page with a particular id

### Main tasks

- Create a new app called `view_api`
- Create models to store info about APIs
- Create view that renders each api in database as a card.
- Register urls for the choose api view
- Create a template page to render apis as cards

### Create models to store info about APIs

- Create a model called `APIInfo`
- Store API name, link, a picture of API result

```python
from django.db import models

# Create your models here.

# Model APIInfo: stores info about APIs
class APIInfo(models.Model):
    r"""Model to store API name, link, a picture of API result"""
    name = models.TextField()
    link = models.URLField()
    image = models.FilePathField(path="/img")
```

- Make migrations: `python manage.py makemigrations view_api`
- Migrate: `python manage.py migrate`
- Test and refactor in local
- Add the `description` field to store api descriptions

```python
from django.db import models

# Create your models here.

# Model APIInfo: stores info about APIs
class APIInfo(models.Model):
    r"""Model to store API name, link, a picture of API result

    Examples
    --------
    Shell examples:

    >>> from view_api.models import APIInfo
    >>> a1 = APIInfo(
    ...     name = "APOD",
    ...     description = "Astronomy Picture of the Day",
    ...     link = "https://api.nasa.gov/planetary/apod",
    ...     image = "img/1.jpg",
    ... )
    >>> a1.save()
    asyncio - 2020-10-18 05:53:05,483-5384-DEBUG-Using proactor: IocpProactor
    >>> a2 = APIInfo(
    ...     name = "EPIC",
    ...     description = "Latest Images from Earth Polychromatic Imaging Camera",
    ...     link = "https://api.nasa.gov/EPIC/api/natural",
    ...     image = "img/2.png",
    ... )
    >>>...
    >>>
    >>> from view_api.models import APIInfo
    >>> APIInfo.objects.all()
    asyncio - 2020-10-18 06:09:36,172-6332-DEBUG-Using proactor: IocpProactor
    <QuerySet [<APIInfo: APIInfo object (1)>, <APIInfo: APIInfo object (2)>, <APIInfo: APIInfo object (3)>, <APIInfo: APIInfo object (4)>]>
    >>> APIInfo.objects.get(id=1)
    <APIInfo: APIInfo object (1)>
    >>> APIInfo.objects.get(id=1).name
    'APOD'
    >>> APIInfo.objects.get(id=1).image
    'img/1.jpg'
    """
    name = models.TextField()
    description = models.TextField(default="")
    link = models.URLField()
    image = models.FilePathField(path="/img")
```

- Make migrations: `python manage.py makemigrations view_api`
- Migrate: `python manage.py migrate`
- Test and refactor in local
- Choose 4 API, one text, three image/video
- Register models in `admin.py`

```python
from django.contrib import admin
from view_api.models import APIInfo

# Register your models here.


class APIInfoAdmin(admin.ModelAdmin):
    pass


admin.site.register(APIInfo, APIInfoAdmin)
```

- Create 4 `APIInfo` instances

```python
a1 = APIInfo(
    name="APOD",
    description="Astronomy Picture of the Day",
    link="https://api.nasa.gov/planetary/apod",
    image="img/1.jpg",
)
a1.save()

a2 = APIInfo(
    name="EPIC",
    description="Latest Images from Earth Polychromatic Imaging Camera",
    link="https://api.nasa.gov/EPIC/api/natural",
    image="img/2.png",
)
a2.save()

a3 = APIInfo(
    name="DONKI",
    description="Notifications from Space Weather Database Of Notifications, Knowledge, Information",
    link="https://api.nasa.gov/DONKI/notifications",
    image="img/3.png",
)
a3.save()

a4 = APIInfo(
    name="MRP",
    description="Image data gathered by NASA's Curiosity, Opportunity, and Spirit rovers on Mars",
    link="https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos",
    image="img/4.jpg",
)
a4.save()
```

```shell
>>> from view_api.models import APIInfo
>>> APIInfo.objects.all()
asyncio - 2020-10-18 06:09:36,172-6332-DEBUG-Using proactor: IocpProactor
<QuerySet [<APIInfo: APIInfo object (1)>, <APIInfo: APIInfo object (2)>, <APIInfo: APIInfo object (3)>, <APIInfo: APIInfo object (4)>]>
>>> APIInfo.objects.get(id=1)
<APIInfo: APIInfo object (1)>
>>> APIInfo.objects.get(id=1).name
'APOD'
>>> APIInfo.objects.get(id=1).image
'img/1.jpg'
```

- Refactor as needed

### Create view that renders each api in database as a card

- Get all project indexes
- Get all `APIInfo` instances
- Create `context` dictionary with them
- Render the `api_index.html` page
- Refactor as needed

### Register urls for the choose api view

- Change the dummy page to **API Index page**.
- Register url as `view_api/`
- Create the `templates/api_index.html` file
- Refactor as needed

### Create a template page to render apis as cards

- Use code from ridge css
- Test
- Replace stuff with `APIInfo` instances passed to `context` dictionary
- Test
- Refactor as needed

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
