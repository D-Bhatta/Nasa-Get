---
name: 🚀 Feature request
about: If you have a feature request 💡
title: ''
labels: ''
assignees: ''

---

# Refactor classes to make them singleton

**Is your feature request related to a problem? Please describe.**
Classes in `apis.py` module and `ContextBuilder` can be made into static singletons, which can be made once and then used again and again. This will probably reduce the overhead of using the app.
