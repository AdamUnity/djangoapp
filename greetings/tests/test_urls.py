# greetings/tests/test_urls.py
from django.test import TestCase
from django.urls import reverse, resolve
from django.http import HttpResponse
from greetings.views import greetings


class GreetingsURLTest(TestCase):
    def test_root_url_resolves_to_greetings_view(self):
        resolver = resolve('/greetings/')
        self.assertEqual(resolver.func, greetings)

    def test_name_url_returns_custom_greeting(self):
        response = self.client.get('/greetings/Anna/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello Anna!")
