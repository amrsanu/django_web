"""To define the URL path for the challenges app"""

from django.urls import path

from . import views

urlpatterns = [
    # path(route="january", view=views.january),
    # path(route="february", view=views.february),
    path(route="<month>", view=views.monthly_challenges)
]
