from django.http import HttpResponse

def greetings(request):
    return HttpResponse("Hello world!")

def name_greeting(request, imie):
    return HttpResponse("Hello " + imie + "!")
