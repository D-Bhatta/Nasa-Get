import logging
import logging.config
from json import load as jload
from pathlib import Path

from django.shortcuts import render

# Configure logger lg with config for appLogger from config.json["logging"]
CONFIG_DIR = Path(__file__).resolve().parent.parent.parent
with open(CONFIG_DIR / "config.json", "r") as f:
    config = jload(f)
    logging.config.dictConfig(config["logging"])
lg = logging.getLogger("appLogger")
# lg.debug("This is a debug message")

# Create your views here.


def homepage(request):
    lg.debug("Rendering homepage")
    return render(request, "home.html", {})
