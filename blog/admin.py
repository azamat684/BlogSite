from django.contrib import admin
from .models import Tag, Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    fields = ('title', 'slug')
    prepopulated_fields = {"slug": ('title', )}


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'author')
    fields = ('title', 'slug', 'description', 'image', 'author', 'category', 'tag')
    prepopulated_fields = {"slug": ('title', )}

admin.site.register(Post, PostAdmin)

admin.site.register(Tag)    