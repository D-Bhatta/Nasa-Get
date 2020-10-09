# Initial checklist

## Remove secret key

- Remove the secret key in django app
- Create a file `secrets.py`
- Import everything from `secrets.py` into `settings.py`
- Create a new secret key
- Add `settings.py` to version control

## Create index page and test

### Create the app

- In the console, run the command `python manage.py startapp homepage`
- Add the app under `INSTALLED_APPS`

### Install the app

- Add a view `homepage` in the the `views.py` file in the `homepage` directory.

### Create a HTML template

- Create the `templates` directory and add a template file `home.html`

### Register URLs

- Include a URL configuration for the `homepage` app with path `home/`
- Create the hello_world.urls module as hello_world/urls.py
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
