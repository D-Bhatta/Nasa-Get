"""Docstring for the apis.py module.

This module contains classes and functions to query APIs.

To query an api pass the following parameters to the get_api_result function

- provider
- name
- key

Example:

get_api_result("Nasa", "APOD", "DEMO_KEY")

Currently supported APIs:

NASA:
----------
- APOD
- EPIC
- Mars Rover Pictures
- DONKI notifications

"""
import json
import logging
import logging.config
from datetime import date, timedelta
from json import load as jload
from pathlib import Path

import requests
from utils import get_test_api_key  # pylint: disable=import-error

# Configure logger lg with config for appLogger from config.json["logging"]
CONFIG_DIR = Path(__file__).resolve().parent.parent.parent
with open(CONFIG_DIR / "config.json", "r") as f:
    config = jload(f)
    logging.config.dictConfig(config["logging"])
lg = logging.getLogger("appLogger")
# lg.debug("This is a debug message")


class Nasa:
    r"""Class to query NASA Open APIs

        Currently the following APIs are supported

        NASA:
        ----------
        - APOD
        - EPIC
        - Mars Rover Pictures
        - DONKI notifications

        Attributes
        ----------
        key : str
            API key acquired from NASA

        Methods
        ----------
        query_api(name: str)
            Returns the result of a selected API.

        Examples
        --------
        These are written in doctest format, and should illustrate how to
        use the function.

        >>> nasa = Nasa(key)
        >>> name = "APOD"
        >>> result = nasa.query_api(name)
        """

    def __init__(self, key):
        self.key = key
        self.api_functions = {
            "APOD": self.apod,
            "EPIC": self.epic,
            "DONKI": self.donki_notifications,
            "MRP": self.mrp,
        }

    def query_api(self, name: str):
        r"""Returns the result of a selected API.

    This method returns the result of a selected API passed to it by the `name`
    parameter.

    Parameters
    ----------
    name : str
        Name of the API.

    Returns
    -------
    result : dict
        A dict object that is the result of the selected query. It is the
        response body for the request in dict form.

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
        try:
            func = self.api_functions[name]
        except KeyError:
            lg.error("Unknown API: This API is not supported")
        return func()

    def apod(self):
        payload = {"api_key": self.key}
        url = "https://api.nasa.gov/planetary/apod"

        r = requests.get(url, params=payload)
        lg.info(f"Status Code: {r.status_code}")

        try:
            result = json.loads(r.text)
            lg.info(f"Write to json object")
        except json.JSONDecodeError as e:
            lg.error(f"error: {e}")

        return result

    def epic(self):
        # Create urls for querying
        info_url = "https://api.nasa.gov/EPIC/api/natural"
        resource_url = "https://api.nasa.gov/EPIC/archive/natural/"

        # Query info_url and get result in result_info_url as dict
        payload = {"api_key": self.key}

        r = requests.get(info_url, params=payload)
        lg.info(f"Status Code: {r.status_code}")

        try:
            result = json.loads(r.text)
            lg.info(f"Write to json object")
        except json.JSONDecodeError as e:
            lg.error(f"error: {e}")

        # Add resource URL to result
        result[0].update({"resource_url": resource_url})

        return result

    def mrp(self):
        url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos/"

        # Build params
        payload = {"api_key": self.key}

        # Query url and get result in result as dict
        r = requests.get(url, params=payload)
        lg.info(f"Status Code: {r.status_code}")

        try:
            result = json.loads(r.text)
            lg.info(f"Write to json object")
        except json.JSONDecodeError as e:
            lg.error(f"error: {e}")

        # return result
        return result

    def donki_notifications(self):
        url = "https://api.nasa.gov/DONKI/notifications"

        # Build end date
        today = date.today()
        end_date = today.strftime("%Y-%m-%d")

        # Build start date
        # This month's first day
        first = today.replace(day=1)
        # Last months last day
        last_month_last_day = first - timedelta(days=1)
        last_month = last_month_last_day.strftime("%Y-%m")
        start_date = last_month + "-01"

        # Build params
        payload = {
            "api_key": self.key,
            "start_date": start_date,
            "end_date": end_date,
        }

        # Query url and get result in result as dict
        r = requests.get(url, params=payload)
        lg.info(f"Status Code: {r.status_code}")

        try:
            result = json.loads(r.text)
            lg.info(f"Write to json object")
        except json.JSONDecodeError as e:
            lg.error(f"error: {e}")

        # return result
        return result


def get_api_result(provider: str, name: str, key: str):
    r"""Returns the result of a selected API.

    This method returns the result of a selected API passed to it by the `name`
    parameter in a given `provider` for a given `key`.

    Parameters
    ----------
    name : str
        Name of the API.
    provider : str
        Provider of the API. Example: "Nasa".
    key : str
        API key.


    Returns
    -------
    result : dict
        A dict object that is the result of the selected query. It is the
        response body for the request in dict form.

    Notes
    -----
    Only pass names supported by this provider.

    Examples
    --------
    These are written in doctest format, and should illustrate how to
    use the function.

    >>> result = get_api_result("Nasa", "APOD", "DEMO_KEY")
    """
    if provider == "Nasa":
        nasa = Nasa(key)
        result = nasa.query_api(name)
    return result
