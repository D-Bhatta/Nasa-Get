import json
import logging
import logging.config
from json import load as jload
from pathlib import Path

from django.shortcuts import render
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
