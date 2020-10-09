# Nasa Get

Notes and code about Nasa Get

## Sections

- [Nasa Get](#nasa-get)
  - [Sections](#sections)
  - [Notes](#notes)
  - [Create the app](#create-the-app)
  - [Remove secret key in settings.py](#remove-secret-key-in-settingspy)
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
