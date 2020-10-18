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
