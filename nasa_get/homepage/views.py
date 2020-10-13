import logging
import logging.config
from json import load as jload
from pathlib import Path

from django.http import Http404
from django.shortcuts import render
from homepage.forms import UserAPIForm
from homepage.models import UserAPIs
from homepage.utils import encrypt

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


def key(request):

    # Create form object
    form = UserAPIForm()

    # On data sent via form
    if request == "POST":
        # set form data in form object
        form = UserAPIForm(request.POST)

        # check form validity
        if form.is_valid():
            # encrypt api key and store in model
            user_api = UserAPIs(api_key=encrypt(form.cleaned_data["api_key"]))
            user_api.save()
            return render(request, "dummy.html", {})
        else:
            error_message = "Invalid Form"
            lg.error(error_message)
            raise Http404(error_message)
    else:
        error_message = "Invalid Request"
        lg.error(error_message)
        raise Http404(error_message)
