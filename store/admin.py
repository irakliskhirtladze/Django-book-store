from django.contrib import admin

from store.models import Book, Category, Author


@admin.register(Book)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'page_count', 'price', 'image', 'book_cover')
    search_fields = ('book_name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    search_fields = ('category_name',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_name',)
    search_fields = ('author_name',)
