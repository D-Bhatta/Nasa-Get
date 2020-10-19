import json
import logging
import logging.config
from json import load as jload
from pathlib import Path

from django.shortcuts import render
from homepage.models import UserAPIs
from homepage.utils import decrypt
from view_api.contexts import ContextBuilder
from view_api.models import APIInfo

# Configure logger lg with config for appLogger from config.json["logging"]
CONFIG_DIR = Path(__file__).resolve().parent.parent.parent
with open(CONFIG_DIR / "config.json", "r") as f:
    config = jload(f)
    logging.config.dictConfig(config["logging"])
lg = logging.getLogger("appLogger")
# lg.debug("This is a debug message")

# Create your views here.


def api_index(request):
    # Get all APIInfo objects
    apis = APIInfo.objects.all()  # pylint: disable="no-member"

    # Create context dict
    context = {"apis": apis}

    # Render the APIs
    return render(request, "api_index.html", context)


def api_result(request, id):
    # Get api key from `UserAPIs` model
    api_key = UserAPIs.objects.all().order_by("-pk")[0].api_key
    api_key = decrypt(api_key)

    # query id
    api = APIInfo.objects.get(pk=id)

    name = api.name
    provider = "Nasa"

    context_builder = ContextBuilder(api_key, provider)

    context = context_builder.build_context(name)

    if context["multimedia"]:
        if context["media_type"] == "image":
            return render(request, "api_result_image.html", context)
        else:
            if context["media_type"] == "video":
                return render(request, "api_result_video.html", context)
    else:
        if context["media_type"] == "text":
            return render(request, "api_result.html", context)
