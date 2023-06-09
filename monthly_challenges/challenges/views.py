from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

monthly_challenges_text = {
    "january": "Eat no meat for entire month",
    "february": "Go for walk",
    "march": "Hit the GYM",
    "april": "Reads books for 1Hr daily",
    "may": "Drink more water",
    "june": "Eat no meat for entire month",
    "july": "Eat no meat for entire month",
    "august": "Eat no meat for entire month",
    "september": "Eat no meat for entire month",
    "october": "Eat no meat for entire month",
    "november": "Eat no meat for entire month",
    "december": None,
}

months = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december",
]


def index(request):
    """View to have all the month challenge"""

    # response_data = "<h1>All Challenge.....</h1>"

    # for month in months:
    #     month_path = reverse("month-challenge", args=[month])
    #     response_data += f'<li><a href="{month_path}">{month.capitalize()}</a></li>'
    # response_data = f"<ol>{response_data}</ol>"
    # return HttpResponse(response_data)

    return render(
        request=request,
        template_name="challenges/index.html",
        context={
            "months": months,
        },
    )


def monthly_challenges(request, month: str):
    """Dynamic View Example"""

    try:
        challenge_text = monthly_challenges_text[month]
        # response_data = f"<h1>{challenge_text}</h1>"
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
        return render(
            request=request,
            template_name="challenges/challenge.html",
            context={
                "month_name": month,
                "challenge_text": challenge_text,
            },
        )

    except KeyError as ex:
        return HttpResponseNotFound(f"<h1>This month is not found: {ex}</h1>")


def monthly_challenges_by_number(request, month: int):
    """To get the monthly challenge by number like 'january: 1'"""
    try:
        if month < 1 or month > 12:
            raise IndexError("Invalid Month")
        # Reverse will use the url name and construct the complete url.
        redirect_path = reverse(
            "month-challenge",
            args=[
                months[month - 1],
            ],
        )
        return HttpResponseRedirect(redirect_path)

    except IndexError as ex:
        raise Http404(ex) from ex
