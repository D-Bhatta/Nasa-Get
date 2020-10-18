from django.shortcuts import render
from view_api.models import APIInfo

# Create your views here.


def api_index(request):
    # Get all APIInfo objects
    apis = APIInfo.objects.all()  # pylint: disable="no-member"

    # Create context dict
    context = {"apis": apis}

    # Render the APIs
    return render(request, "api_index.html", context)
