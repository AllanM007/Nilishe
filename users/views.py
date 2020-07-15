from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .models import UserProfile, Review
from django.urls import reverse
from .forms import ReviewForm

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
def rev_comment(request, pk):
    
    user = UserProfile.objects.get(pk=pk)

    cartid = request.session['cartid']

    print(cartid)

    # Comment posted
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = Review(
                name=form.cleaned_data["name"],
                body=form.cleaned_data["body"],
                rating=form.cleaned_data["rating"],
                user=user
            )
            review.save()

            return redirect('map', room_name=cartid)

    else:
        form = ReviewForm()
    
    reviews = Review.objects.filter(user=user)

    context = {
        "form": form,
        "reviews": reviews,
    }

    return render(request, 'users/revcomment.html', context)