from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.log_in, name='login'),
    path('user_home/', views.user_home, name='user_home'),
]
