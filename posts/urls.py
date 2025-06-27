from django.urls import path
from django.views.generic import ListView
from posts.models import Post
from posts.views import post_list, post_detail, author_list, author_detail

app_name = "posts"

urlpatterns = [
   path('', post_list, name="list"),
   path('<int:pk>', post_detail, name="details"),
   path('authors', author_list, name="authors"),
   path('authors/<int:id>', author_detail, name="author"),
   path('list', ListView.as_view(model=Post), name="posts_list")
]