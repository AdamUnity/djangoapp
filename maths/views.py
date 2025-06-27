from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from maths.models import Math
from .models import Result
from maths.forms import ResultForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def math(request):
    return render(request, "maths/main.html", {
    })

def add(request, a, b):
    wynik = int(a) + int(b)
    c = {"a": a, "b": b, "operacja": "+", "wynik": wynik, "title": "dodawanie"}

    result = Result.objects.get_or_create(value=wynik)[0]
    Math.objects.create(operation='add', a=a, b=b, result=result)
    return render(
        request=request,
        template_name="maths/operation.html",
        context=c
    )

def sub(request, a, b):
    wynik = int(a) - int(b)
    c = {"a": a, "b": b, "operacja": "-", "wynik": wynik, "title": "dodawanie"}

    result = Result.objects.get_or_create(value=wynik)[0]
    Math.objects.create(operation='sub', a=a, b=b, result=result)
    return render(
        request=request,
        template_name="maths/operation.html",
        context=c
    )

def mul(request, a, b):
    wynik = int(a) * int(b)
    c = {"a": a, "b": b, "operacja": "x", "wynik": wynik, "title": "dodawanie"}

    result = Result.objects.get_or_create(value=wynik)[0]
    Math.objects.create(operation='mul', a=a, b=b, result=result)
    return render(
        request=request,
        template_name="maths/operation.html",
        context=c
    )

def div(request, a, b):
    if int(b) == 0:
        wynik = None
        error_msg = "Dividing by zero"
        messages.add_message(request, messages.ERROR, error_msg)
        result = Result.objects.get_or_create(value=None, error=error_msg)[0]
        Math.objects.create(operation='div', a=a, b=b, result=result)
    else:
        wynik = int(a) / int(b)
        result = Result.objects.get_or_create(value=wynik, error=None)[0]
        Math.objects.create(operation='div', a=a, b=b, result=result)

    c = {
        "a": a,
        "b": b,
        "operacja": "/",
        "wynik": wynik if wynik is not None else "Error",
        "title": "dzielenie"
    }
    return render(
        request=request,
        template_name="maths/operation.html",
        context=c
    )
@login_required
def maths_list(request):
    # Pobierz parametr operation z GET (np. /maths/histories/?operation=add)
    operation = request.GET.get("operation")

    if operation:
        # Filtrowanie po operacji, jeśli podano
        maths = Math.objects.filter(operation=operation)
    else:
        # Wszystkie obiekty, gdy brak filtra
        maths = Math.objects.all()

    # Paginacja - pokaż po 5 wyników na stronę
    paginator = Paginator(maths, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request=request,
        template_name="maths/list.html",
        context={
            "maths": page_obj,  # tu przekazujemy obiekt paginacji
            "operation": operation,  # przekazujemy do szablonu, żeby w input było widać wyszukiwane
        }
    )
def math_details(request, id):
   math = Math.objects.get(id=id)
   return render(
       request=request,
       template_name="maths/details.html",
       context={"math": math}
   )
def results_list(request):
  if request.method == "POST":
      value = request.POST['value'] or None
      error = request.POST['error'] or None
      if value and error:
          messages.add_message(
              request,
              messages.ERROR,
              "Błąd! Podano jednocześnie value i error. Podaj tylko jedną z tych wartości"
          )
      elif value or error:

          Result.objects.get_or_create(
              value=float(value),
              error=error
          )
          messages.add_message(
              request,
              messages.SUCCESS,
              "Utworzono nowy Result!!"
          )

      else:
          messages.add_message(
              request,
              messages.ERROR,
              "Błąd! Nie podano wartości!!"
          )

  results = Result.objects.all()
  return render(
      request=request,
      template_name="maths/results.html",
      context={"results": results}
  )