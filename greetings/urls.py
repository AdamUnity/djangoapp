from django.urls import path
from .views import *
from django.http import HttpResponse
app_name = "greetings"
urlpatterns = [
    path('', greetings, name="greetings"),
    path('<imie>/', lambda request, imie: HttpResponse("Hello "+imie+"!")),
]