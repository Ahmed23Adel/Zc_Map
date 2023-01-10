from django.urls import path
from . import view

urlpatterns = [
    path("", view.getData),
    path("rl/", view.getDataRL),
]
