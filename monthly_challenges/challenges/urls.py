"""To define the URL path for the challenges app"""

from django.urls import path

from . import views

urlpatterns = [
    path(route="", view=views.index, name="index-page"),
    path(route="<int:month>", view=views.monthly_challenges_by_number),
    path(route="<str:month>", view=views.monthly_challenges, name="month-challenge"),
]
