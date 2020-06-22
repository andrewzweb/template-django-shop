from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import logout
from .forms import RegisterForm
from django.contrib.auth.models import User


def detail(request):
    return render(request, 'account/detail.html')


def account_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('catalog:list')
        else:
            messages.error(request, 'username or password not correct')
            return redirect('account:login')

    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})


def account_logout(request):
    logout(request)
    return redirect('account:login')


def account_register(request):

    if request.method == 'POST':
        form_register = RegisterForm(request.POST)
        if form_register.is_valid():
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            if password1 == password2:
                print('create user here ')
                user = User.objects.create_user(username, 'lennon@thebeatles.com', 'johnpassword')
                return redirect('account:register-done')
            else:
                return render(request, 'account/register.html', {'form_register': form_register})
        else:
            return render(request, 'account/register.html', {'form_register': form_register})
    else:
        form_register = RegisterForm()
    return render(request, 'account/register.html', {'form_register': form_register})


def account_register_done(request):
    return render(request, 'account/register-done.html')
