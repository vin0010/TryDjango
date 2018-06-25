from django.contrib import admin

# Register your models here.

from TryDjango.posts.models import Post

admin.site.register(Post)