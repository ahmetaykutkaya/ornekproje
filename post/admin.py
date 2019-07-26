from django.contrib import admin
from post.models import Post


class PostForm(admin.ModelAdmin):

    list_display = ['name','surname',]
    list_display_links = ['name','surname']
    list_filter = ['name','surname']
    search_fields = ['name','surname']


admin.site.register(Post, PostForm)

