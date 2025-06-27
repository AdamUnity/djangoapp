from django.test import TestCase
from posts.models import Post, Author

class AuthorModelTest(TestCase):
    def test_str_returns_nick(self):
        author = Author.objects.create(nick="Ada", email="ada@example.com")
        self.assertEqual(str(author), "Ada")

class PostModelTest(TestCase):
    def test_str_returns_title(self):
        author = Author.objects.create(nick="Bob", email="bob@example.com")
        post = Post.objects.create(title="Test Post", content="Text", author=author)
        self.assertEqual(str(post), "Test Post")
