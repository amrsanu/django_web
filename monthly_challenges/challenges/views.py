from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


# def january(request):
#     """View Example to"""

#     return HttpResponse("This Works [JANUARY]...")


# def february(request):
#     """View Example to"""

#     return HttpResponse("This Works [FEBRUARY]...")


def monthly_challenges(request, month):
    """Dynamic View Example"""

    if month == "january":
        challenge_text = "Eat no meat for entire month"
    elif month == "february":
        challenge_text = "Go for walk"
    elif month == "march":
        challenge_text = "Hit the GYM"
    elif month == "april":
        challenge_text = "Drink more water"
    elif month == "may":
        challenge_text = "Reads books for 1Hr daily"
    else:
        return HttpResponseNotFound("This month is not found")

    return HttpResponse(challenge_text)
