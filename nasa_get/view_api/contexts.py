import json
import logging
import logging.config
from json import load as jload
from pathlib import Path

from apis import get_api_result
from utils import get_test_api_key


class ContextBuilder:
    def __init__(self):
        self.key = get_test_api_key()
        self.provider = "Nasa"
        self.name = ""

    def apod_context(self):
        self.name = "APOD"
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


def test_context():
    context_builder = ContextBuilder()
    context = context_builder.apod_context()
    lg.info(context)


test_context()
