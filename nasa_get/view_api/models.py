from django.db import models

# Create your models here.

# Model APIInfo: stores info about APIs
class APIInfo(models.Model):
    r"""Model to store API name, link, a picture of API result"""
    name = models.TextField()
    link = models.URLField()
    image = models.FilePathField(path="/img")
