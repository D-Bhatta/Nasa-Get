---
name: 🚀 Feature request
about: If you have a feature request 💡
title: ''
labels: ''
assignees: ''

---

# Refactor the settings.py file to enable getting host names from .env

**Is your feature request related to a problem? Please describe.**
Currently the hostname for PythonAnywhere is hard coded. It should be placed into the `.env` file, and retrieved as an environment variable.

## An overview of the suggested solution

**Describe the solution you'd like**
Move the host name to the `.env` file and retrieve it from there during initialization.

### If the feature changes current behavior, reasons why your solution is better

The host name is nolonger hardcoded, and the app can now be run anywhere.

### Alternative Solutions

**Describe alternatives you've considered**

- Retrieving it from another settings file
- Leaving it hardcoded and changing it only when needed.

### Files

- `settings.py`

### Tasks

Include specific tasks in the order they need to be done in. Include links to specific lines of code where the task should happen at.
- [ ] Move the hostname string into the `.env` file.
- [ ] Change the `settings.py` code to retrieve the hostname from the environment
  - [ ] Make sure to catch `KeyError` on not finding a key, and get it from the  `.env` file
- [ ] Deploy app to see if it works.

**Has the feature been requested before?**

No

**If the feature request is approved, would there be a need for further development in this area?**
Yes, this should not require further work.
