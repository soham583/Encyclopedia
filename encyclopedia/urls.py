from django.urls import path

from . import views
app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:topic>",views.pages, name="pages"),
    path("search", views.search, name="search"),
    path("edit/<str:title>",views.editm, name="editm"),
    path("new",views.newm, name="newm"),
    path("ranm",views.ranm, name="ranm")
]
