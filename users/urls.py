from django.urls import path
from users import views


app_name = 'users'
urlpatterns = [
    path('', views.index, name='home'),
    path('home', views.index, name='home'),

    path('signup/', views.signup, name='signup'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
]
