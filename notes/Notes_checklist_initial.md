# Initial checklist

## Remove secret key

- Remove the secret key in django app
- Create a file `utils.py`
- Create a function `generate_secret_key` that writes a secret key to an `.env` file
- Use `dotenv` to set environment variables in `settings.py`
- Add `.env` to .gitignore

## Create index page and test

### Create the app

- In the console, run the command `python manage.py startapp homepage`
- Add the app under `INSTALLED_APPS`

### Create views

- Add a view `homepage` in the the `views.py` file in the `homepage` directory.

### Add a base template

- Create a `templates` directory in the main project directory `nasa_get`
- Create a fil e `base.html`
- In `settings.py`, update `TEMPLATES` list
- Create a `static` folder in `BASE_DIR` `nasa_get`
- Create a `static/nasa_get/css` folder tree
- Add list of `STATICFILES_DIRS` by joining `nasa_get\\static\\nasa_get`with `BASE_DIR`
- Inside `templates/base.html` add the block tag and load static files
- Add css and js styling using `"{% static '<path_to_resource>/resource' %}"`

### Create a HTML template for homepage app

- Create the `homepage/templates` directory and add a template file `home.html`
- Add some content

### Register URLs

- Include a URL configuration for the `homepage` app with path `home/`
- Create the `homepage.urls` module as `homepage/urls.py`
- Create a list of URL patterns that correspond to the various view functions

### Refactor

- Debug and look for errors locally

## Deploy app

- Deploy the app online

### Setup the code

- In a bash console navigate to `/home/username/`
- Clone the repo
- `cd` into the repo folder
- Create a virtual environment
- Install requirements

### Setup the webapp

- Enter the name of your virtualenv in the Virtualenv section
- Enter the path to top project folder in the Code section on the web tab, eg /home/myusername/mysite in `Source code` and `Working directory`(Where `manage.py` is)
- Click on the WSGI file link
- Delete everything except the Django section and then uncomment that section
- Substitute the correct path to your project
- Debug and refactor as necessary
