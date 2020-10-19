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
from json import load as jload
from pathlib import Path

import requests
from utils import get_test_api_key

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
        pass

    def mrp(self):
        pass

    def donki_notifications(self):
        pass


def get_api_result(provider: str, name: str, key: str):
    if provider == "Nasa":
        nasa = Nasa(key)
        result = nasa.query_api(name)
    lg.info(result)
    return result


get_api_result("Nasa", "APOD", get_test_api_key())
