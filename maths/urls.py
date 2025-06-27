from django.urls import path, include
from .views import *
app_name="maths"
urlpatterns = [
   path('', math),
   path('add/<int:a>/<b>', add),
   path('sub/<int:a>/<b>', sub),
   path('mul/<int:a>/<b>', mul),
   path('div/<int:a>/<b>', div),
   path('histories/', maths_list, name="list"),
   path('histories/<int:id>', math_details, name="details"),
   path('results/', results_list, name="results"),
   path('accounts/', include('django.contrib.auth.urls')),
]