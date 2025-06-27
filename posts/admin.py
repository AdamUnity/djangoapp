from django.contrib import admin
from posts.models import Author, Post
from django.contrib import admin
from posts.models import Post, Author, Tag
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('nick', 'email')
    search_fields = ('nick', 'email')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'modified')
    list_filter = ('created', 'modified', 'author')
    search_fields = ('title', 'content')
    date_hierarchy = 'created'
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
   pass