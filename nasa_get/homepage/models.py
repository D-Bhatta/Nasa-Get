from django.db import models

# Model to store API keys


class UserAPIs(models.Model):
    api_key = models.TextField()
