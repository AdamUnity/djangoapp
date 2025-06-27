from django.test import TestCase
from posts.forms import PostForm, AuthorForm
from posts.models import Author

class PostFormTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(nick="Jan", email="jan@example.com")

    def test_post_form_valid_data(self):
        form = PostForm(data={
            "title": "Tytuł",
            "content": "Treść posta",
            "author": self.author.pk
        })
        self.assertTrue(form.is_valid())

    def test_post_form_missing_field(self):
        form = PostForm(data={
            "title": "",
            "content": "Treść posta",
            "author": self.author.pk
        })
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)

class AuthorFormTest(TestCase):
    def test_author_form_valid(self):
        form = AuthorForm(data={
            "nick": "Ola",
            "email": "ola@example.com"
        })
        self.assertTrue(form.is_valid())

    def test_author_form_invalid_email(self):
        form = AuthorForm(data={
            "nick": "Ola",
            "email": "niepoprawny_email"
        })
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)
