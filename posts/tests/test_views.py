from django.test import TestCase
from django.urls import reverse
from posts.models import Post, Author

class PostViewsTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(nick="Alice", email="alice@example.com")
        self.post = Post.objects.create(title="Hello", content="World", author=self.author)

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello")

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "World")

    def test_post_add_view_get(self):
        response = self.client.get(reverse('post_add'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_post_add_view_post(self):
        response = self.client.post(reverse('post_add'), {
            "title": "Nowy post",
            "content": "Treść",
            "author": self.author.pk
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, "Nowy post")

class AuthorViewsTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(nick="Eve", email="eve@example.com")

    def test_author_list_view(self):
        response = self.client.get(reverse('author_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Eve")

    def test_author_detail_view(self):
        response = self.client.get(reverse('author_detail', args=[self.author.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "eve@example.com")

    def test_author_add_view_post(self):
        response = self.client.post(reverse('author_add'), {
            "nick": "Tom",
            "email": "tom@example.com"
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Author.objects.filter(nick="Tom").exists())
