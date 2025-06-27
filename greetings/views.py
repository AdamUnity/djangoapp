from django.shortcuts import render
def greetings(request):
    return render(request, "greetings/greetings.html")