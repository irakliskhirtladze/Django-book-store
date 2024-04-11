from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator

from store.models import Book
from users.models import Cart
from decimal import Decimal


def store_home(request):
    """Gets all books and renders store_home.html to show them on different pages"""
    if not request.user.is_authenticated:
        return redirect('login')

    books = Book.objects.all().order_by('book_name')
    paginator = Paginator(books, 3)
    page_number = request.GET.get('page', 1)
    books = paginator.get_page(page_number)
    return render(request, 'store/store_home.html', {'books': books, 'user': request.user})


def get_book(request, book_id):
    """Obtains details for a specific book and renders book_details.html"""
    if not request.user.is_authenticated:
        return redirect('login')

    page_number = request.GET.get('page', 1)

    # Get the book from the database or show a 404 page if it doesn't exist
    try:
        book = get_object_or_404(Book, pk=book_id)
    except Exception:
        return render(request, '404.html')

    return render(request, 'store/book_details.html',
                  {'book': book, 'page_number': page_number})


def add_to_cart(request, book_id):
    if not request.user.is_authenticated:
        return redirect('login')

    book = Book.objects.get(pk=book_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)

    if book not in cart.books.all():
        cart.books.add(book)
        cart.total = Decimal(cart.total)
        cart.total += Decimal(book.price)
        cart.save()
        messages.success(request, f'{book.book_name} added to cart')

    # Get the current page number from the query parameters
    current_page = request.GET.get('page', 1)

    # Redirect back to the same page with the current page number
    return redirect(reverse('store_home') + f'?page={current_page}')


def remove_from_cart(request, book_id):
    if not request.user.is_authenticated:
        return redirect('login')

    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        return redirect('store_home')

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
    if not request.user.is_authenticated:
        return redirect('login')

    try:
        cart = Cart.objects.get(user=request.user)
        books_in_cart = cart.books.all()
        total_items = books_in_cart.count()
    except Cart.DoesNotExist:
        cart = None
        books_in_cart = []
        total_items = 0

    page_number = request.GET.get('page', 1)

    return render(request, 'store/cart.html',
                  {'cart': cart,
                   'books_in_cart': books_in_cart,
                   'total_items': total_items,
                   'page_number': page_number})
