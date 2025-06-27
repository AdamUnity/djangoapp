from django.urls import path
from .views import main
from django.http import HttpResponse
urlpatterns = [
    path('', main,name="home"),
]