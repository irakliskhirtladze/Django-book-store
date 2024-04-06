from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from users.forms import CustomUserCreationForm


def index(request):
    return render(request, 'authentication/home.html')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'authentication/signup.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('store_home')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    return render(request, 'authentication/login.html')


@login_required
def store_home(request):
    return render(request, 'authentication/store_home.html')


def log_out(request):
    logout(request)
    return redirect('index')
