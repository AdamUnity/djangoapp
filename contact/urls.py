from django.urls import path
from .views import *
from django.http import HttpResponse
from django.views.generic import TemplateView

app_name = "contact"
urlpatterns = [
    path('', ContatcView.as_view(), name='contact'),
]