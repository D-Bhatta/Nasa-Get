# Deployment Checklist

## Change to deployment branch

- Create a branch specifically for deployment to Python Anywhere
- Get the settings file changes into local
- Push to origin
- In python Anywhere, pull from origin and checkout the deployment branch

## Fix static assets problem

- Find out what environment we are running in using a `.env` setting
- Set variables according to that setting
