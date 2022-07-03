from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("wiki/edit",  views.edit, name="edit"),
    path("wiki/random", views.random, name="random"),
    path("wiki/create", views.create, name="create"),
    path("wiki/<str:name>", views.entry, name="entry"),
]
