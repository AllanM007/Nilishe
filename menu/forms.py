from django.forms import ModelForm
from .models import Pizza
from django.contrib.auth.models import User
from django import forms

TOPPING_CHOICES = [
    ('Pepperoni', 'Pepperoni'),
    ('Pineapple', 'Pineapple'),
    ('BBQ Meat', 'BBQ. Meat'),
    ('Chicken', 'Chicken'),
    ('Mushrooms', 'Mushrooms'),
]

SAUCE_CHOICES = [
    ('BBQ Sauce', 'BBQ Sauce'),
    ('Ranch Sauce', 'Ranch Sauce'),
    ('Garlic Sauce', 'Garlic Sauce'),
    ('Marinara Sauce', 'Marinara Sauce'),
    ('Hot Sauce', 'Hot Sauce'),
]

class PizzaForm(forms.Form):
	topping = forms.ChoiceField(choices=TOPPING_CHOICES, widget=forms.RadioSelect())
	sauce = forms.ChoiceField(choices=SAUCE_CHOICES, widget=forms.RadioSelect())

	#class Meta:
	#	model = Pizza
	#	fields = ['name']