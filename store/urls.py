from django.urls import path
from . import views


urlpatterns = [
    path('store', views.get_books, name='store_home'),
    path('store/<int:book_id>-book-details', views.get_book, name='book_details'),
]
