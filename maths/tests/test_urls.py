
from django.test import TestCase, Client
from maths.models import Math, Result
from maths.forms import ResultForm

from unittest import TestCase
from django.urls import resolve
from django.urls.exceptions import Resolver404
from maths.views import add, sub

class TestUrls(TestCase):
   def test_resolution_for_add(self):
       resolver = resolve('/maths/add/1/2')
       self.assertEqual(resolver.func, add)

   def test_resolution_for_sub(self):
       resolver = resolve('/maths/sub/1/2')
       self.assertEqual(resolver.func, sub)

   def test_arguments_should_be_integers_or_404(self):
       with self.assertRaises(Resolver404):
           resolve('maths/sub/a/b')