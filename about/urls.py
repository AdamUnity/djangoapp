from django.urls import path
from .views import *
from django.http import HttpResponse
from django.views.generic import TemplateView

app_name = "about"
urlpatterns = [
    path('', AboutView.as_view(), name='about'),
]