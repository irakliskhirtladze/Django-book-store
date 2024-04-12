from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage
from django.views.generic import ListView

from store.models import Book
from users.models import Cart
from decimal import Decimal


class BookPaginator(Paginator):
    """Handles pagination for numbers greater or lesser than min and max number of pages.
    For example, if N of pages is 5, and user tries to get page 6, it will return the last page."""
    def validate_number(self, number):
        try:
            return super().validate_number(number)
        except EmptyPage:
            if int(number) > 1:
                # return the last page
                return self.num_pages
            elif int(number) < 1:
                # return the first page
                return 1
            else:
                raise


class StoreHome(ListView):
    """Class representing a list of all books in the store, with pagination"""
    model = Book
    template_name = 'store/store_home.html'
    paginate_by = 3
    context_object_name = 'books'
    ordering = 'book_name'
    paginator_class = BookPaginator

    def get_queryset(self):
        return super().get_queryset().order_by(self.ordering)

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


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
    """Adds a book to the user's cart"""
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
