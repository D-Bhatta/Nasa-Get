# Deployment Checklist

## Change to deployment branch

- Create a branch specifically for deployment to Python Anywhere
- Get the settings file changes into local
- Push to origin
- In python Anywhere, pull from origin and checkout the deployment branch

## Fix static assets problem

- Find out what environment we are running in using a `.env` setting
- Set variables according to that setting
- Add static files mapping on PythonAnywhere

## Refactor the settings.py file to enable getting host names from .env

- Move the hostname string into the `.env` file.
- Change the `settings.py` code to retrieve the hostname from the environment
  - Catch `KeyError` on not finding a key, and get it from the  `.env` file
- Refactor locally for errors
- Push to `origin/main`
- Change branch to `main` in deployment
- Deploy app from `main` and refactor
