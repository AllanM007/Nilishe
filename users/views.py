from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, ReviewForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.urls import reverse

def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('users:login'))
        else:
            print(form.errors)
    return render(request, 'users/signup.html', {'form': form})


def log_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(reverse('menu:menu'))
        else:
            print(form.errors)
    return render(request, 'users/login.html', {'form': form})


@login_required(login_url='/login/')
def log_out(request):
    logout(request)
    return redirect(reverse('users:login'))


@login_required
def review(request):
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(reverse('menu:menu'))
        else:
            print(form.errors)
    return render(request, 'users/login.html', {'form': form})