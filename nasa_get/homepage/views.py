import logging
import logging.config
from json import load as jload
from pathlib import Path

from django.http import Http404, HttpResponseRedirect
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
    # Create form object
    form = UserAPIForm()

    # On data sent via form
    if request.method == "POST":
        lg.debug("Request is post")
        # set form data in form object
        form = UserAPIForm(request.POST)

        # check form validity
        if form.is_valid():
            lg.debug("Form is valid")
            # encrypt api key and store in model
            user_api = UserAPIs(api_key=encrypt(form.cleaned_data["api_key"]))
            user_api.save()
            lg.debug("saved api key")
            lg.debug("rendering API index page")
            return HttpResponseRedirect("/apis/")
        else:
            error_message = "Invalid Form"
            lg.error(error_message)
            raise Http404(error_message)
    lg.debug("Not a form request")
    context = {"form": form}
    return render(request, "home.html", context=context)
