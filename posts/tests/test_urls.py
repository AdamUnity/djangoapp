from django.test import SimpleTestCase
from django.urls import reverse, resolve
from posts import views

class UrlsTest(SimpleTestCase):
    def test_post_list_url_resolves(self):
        url = reverse('post_list')
        self.assertEqual(resolve(url).func, views.post_list)

    def test_author_list_url_resolves(self):
        url = reverse('author_list')
        self.assertEqual(resolve(url).func, views.author_list)
