from django.shortcuts import render, redirect
from django.contrib import messages

from store.models import Book
from users.models import Cart
from decimal import Decimal


def get_books(request):
    return render(request, 'store/store_home.html', {'books': Book.objects.all(), 'user': request.user})


def get_book(request, book_id):
    return render(request, 'store/book_details.html', {'book': Book.objects.get(id=book_id)})


def add_to_cart(request, book_id):
    book = Book.objects.get(pk=book_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    if book not in cart.books.all():
        cart.books.add(book)
        cart.total = Decimal(cart.total)
        cart.total += Decimal(book.price)
        cart.save()
        messages.success(request, f'{book.book_name} added to cart')

    return redirect('store_home')


def remove_from_cart(request, book_id):
    book = Book.objects.get(pk=book_id)
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=request.user)
    if book in cart.books.all():
        cart.books.remove(book)
        cart.total = Decimal(cart.total)
        cart.total -= Decimal(book.price)
        cart.save()

    messages.success(request, f'{book.book_name} removed from cart')

    return redirect('cart')


def cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
        books_in_cart = cart.books.all()
        total_items = books_in_cart.count()
    except Cart.DoesNotExist:
        cart = None
        books_in_cart = []
        total_items = 0

    return render(request, 'store/cart.html',
                  {'cart': cart, 'books_in_cart': books_in_cart, 'total_items': total_items})
