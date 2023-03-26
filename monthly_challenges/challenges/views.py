from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def january(request):
    """View Example to"""

    return HttpResponse("This Works [JANUARY]...")


def february(request):
    """View Example to"""

    return HttpResponse("This Works [FEBRUARY]...")
