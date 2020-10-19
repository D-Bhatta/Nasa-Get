"""Docstring for the apis.py module.

This module contains classes and functions to query APIs

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
    def __init__(self, key):
        self.key = key
        self.api_functions = {
            "APOD": self.apod,
            "EPIC": self.epic,
            "DONKI": self.donki_notifications,
            "MRP": self.mrp,
        }

    def query_api(self, name: str):
        func = self.api_functions[name]
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
    if provider == "Nasa":
        nasa = Nasa(key)
        result = nasa.query_api(name)
    lg.info(result)
    return result


get_api_result("Nasa", "DONKI", get_test_api_key())
