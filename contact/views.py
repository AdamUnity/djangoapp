from django.shortcuts import render
from django.views.generic import TemplateView

class ContatcView(TemplateView):
    template_name = "contact/contact.html"
