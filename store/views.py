from django.shortcuts import render

from store.models import Book


def get_books(request):
    return render(request, 'store/store_home.html', {'books': Book.objects.all()})


def get_book(request, book_id):
    return render(request, 'store/book_details.html', {'book': Book.objects.get(id=book_id)})
