from django.urls import path
from store import views
from users.views import log_out


urlpatterns = [
    path('store', views.StoreHome.as_view(), name='store_home'),  # path('store', views.store_home, name='store_home'),
    path('store/<int:book_id>-book-details', views.get_book, name='book_details'),
    path('store/<int:book_id>-add-to-cart', views.add_to_cart, name='add_to_cart'),
    path('store/<int:book_id>-remove-from-cart', views.remove_from_cart, name='remove_from_cart'),
    path('store/cart', views.cart, name='cart'),
    path('logout/', log_out, name='logout'),
]
