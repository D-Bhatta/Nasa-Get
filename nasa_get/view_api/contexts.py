r"""docstring for `contexts.py`

Contains the class `ContextBuilder` which builds context dicts.

Example:
    >>> key = "DEMO_KEY"
    >>> provider = "Nasa"
    >>> name = "DONKI"
    >>> context_builder = ContextBuilder(key, provider)
    >>> context = context_builder.build_context(name)

Attributes:
    lg (lg): Logger for the module.
"""
import json
import logging
import logging.config
from json import load as jload
from pathlib import Path

from view_api.apis import get_api_result
from view_api.utils import get_test_api_key  # pylint: disable=import-error

# Configure logger lg with config for appLogger from config.json["logging"]
CONFIG_DIR = Path(__file__).resolve().parent.parent.parent
with open(CONFIG_DIR / "config.json", "r") as f:
    config = jload(f)
    logging.config.dictConfig(config["logging"])
lg = logging.getLogger("appLogger")
# lg.debug("This is a debug message")


class ContextBuilder:
    r"""Builds context dictionaries for rendering with Django templates.

    Attributes
    ----------
    api_functions : dict
        List of APIs supported with their corresponding builder functions.
    name : str
        Empty string to represent name of API.

    Parameters
    ----------
    key : str
        Key for the API.
    provider : str
        Provider of the API.

    Methods
    ----------
    build_context(name)
        Method that returns a context dict.

    Examples
    --------
    Use the context_builder to get a context dict.

    >>> key = "DEMO_KEY"
    >>> provider = "Nasa"
    >>> name = "DONKI"
    >>> context_builder = ContextBuilder(key, provider)
    >>> context = context_builder.build_context(name)
    """

    def __init__(self, key: str, provider: str):
        self.key = key
        self.provider = provider
        self.api_functions = {
            "APOD": self.apod_context,
            "EPIC": self.epic_context,
            "DONKI": self.donki_notifications_context,
            "MRP": self.mrp_context,
        }
        self.name = ""

    def build_context(self, name: str):
        r"""Returns the context of a selected API result.

        This method returns the context of a selected API result passed to it by
        the `name` parameter.

        Parameters
        ----------
        name : str
            Name of the API.

        Returns
        -------
        result : dict
            A dict object that is the context of a selected API result.

        Notes
        -----
        Only pass names supported by this class

        Examples
        --------
        These are written in doctest format, and should illustrate how to
        use the function.

        >>> key = "DEMO_KEY"
        >>> provider = "Nasa"
        >>> name = "DONKI"
        >>> context_builder = ContextBuilder(key, provider)
        >>> context = context_builder.build_context(name)
        """
        self.name = name
        try:
            func = self.api_functions[name]
        except KeyError:
            lg.error("Unknown API: This API is not supported")
        return func()

    def apod_context(self):
        result = get_api_result(
            provider=self.provider, name=self.name, key=self.key
        )
        media_type = result["media_type"]
        url = result["url"]
        title = result["title"]
        date = result["date"]
        message = result["explanation"]

        multimedia = True

        context = {
            "multimedia": multimedia,
            "message": message,
            "date": date,
            "url": url,
            "title": title,
            "media_type": media_type,
        }

        return context

    def epic_context(self):
        result = get_api_result(
            provider=self.provider, name=self.name, key=self.key
        )
        result = result[0]

        media_type = "image"
        title = "Imagery collected by DSCOVR's Earth Polychromatic Imaging Camera (EPIC)"
        multimedia = True

        identifier = result["identifier"]
        message = result["caption"]
        image = result["image"] + ".png"

        date = (
            identifier[0:4]
            + "/"
            + identifier[4:6]
            + "/"
            + identifier[6:8]
            + "/"
        )

        url = (
            "https://api.nasa.gov/EPIC/archive/natural/"
            + date
            + "png/"
            + image
            + "?api_key="
            + self.key
        )

        context = {
            "multimedia": multimedia,
            "message": message,
            "date": date,
            "url": url,
            "title": title,
            "media_type": media_type,
        }

        return context

    def donki_notifications_context(self):
        result = get_api_result(
            provider=self.provider, name=self.name, key=self.key
        )

        result = result[0]

        media_type = "text"

        title = "Notifications from The Space Weather Database Of Notifications, Knowledge, Information (DONKI)"
        multimedia = False

        message = result["messageBody"]

        date = result["messageIssueTime"][0:11]

        url = result["messageURL"]

        context = {
            "multimedia": multimedia,
            "message": message,
            "date": date,
            "url": url,
            "title": title,
            "media_type": media_type,
        }

        return context

    def mrp_context(self):
        result = get_api_result(
            provider=self.provider, name=self.name, key=self.key
        )
        result = result["latest_photos"][0]

        media_type = "image"

        title = "Image data gathered by NASA's Curiosity rovers on Mars"
        multimedia = True

        message = result["camera"]["full_name"]

        date = result["earth_date"]

        url = result["img_src"]

        context = {
            "multimedia": multimedia,
            "message": message,
            "date": date,
            "url": url,
            "title": title,
            "media_type": media_type,
        }

        return context
