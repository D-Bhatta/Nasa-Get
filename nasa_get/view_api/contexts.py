import json
import logging
import logging.config
from json import load as jload
from pathlib import Path

from apis import get_api_result
from utils import get_test_api_key  # pylint: disable=import-error

# Configure logger lg with config for appLogger from config.json["logging"]
CONFIG_DIR = Path(__file__).resolve().parent.parent.parent
with open(CONFIG_DIR / "config.json", "r") as f:
    config = jload(f)
    logging.config.dictConfig(config["logging"])
lg = logging.getLogger("appLogger")
# lg.debug("This is a debug message")


class ContextBuilder:
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

        >>> name = "APOD"
        >>> result = nasa.query_api(name)
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

        multimedia = False

        if media_type == "video" or media_type == "image":
            multimedia = True
        else:
            multimedia = False

        context = {
            "multimedia": multimedia,
            "message": message,
            "date": date,
            "url": url,
            "title": title,
        }

        return context

    def epic_context(self):
        pass

    def donki_notifications_context(self):
        pass

    def mrp_context(self):
        pass


def test_context():
    key = get_test_api_key()
    provider = "Nasa"
    name = "APOD"
    context_builder = ContextBuilder(key, provider)
    context = context_builder.build_context(name)
    lg.info(context)


test_context()
