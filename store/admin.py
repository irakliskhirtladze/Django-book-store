from django.contrib import admin

from .models import Book


@admin.register(Book)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'page_count', 'category', 'author', 'price', 'image')
    search_fields = ('book_name', 'author')
