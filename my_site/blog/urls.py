"""Url for blog"""

from django.urls import path
from . import views

urlpatterns = [
    path(route="", view=views.starting_page, name="starting-page"),
    path(route="posts", view=views.posts, name="posts-page"),
    path(route="posts/<slug:slug>", view=views.post_details, name="post-detail-page"),
]
