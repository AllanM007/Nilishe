from .models import UserProfile,Review
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db import transaction
from django import forms


RATING_CHOICES=(
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    )

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']

class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Review
        fields = ['name', 'body']