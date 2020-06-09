from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Pizza
from django import forms

TOPPING_CHOICES = [
    ('Pepperoni', 'Pepperoni'),
    ('Pineapple', 'Pineapple'),
    ('BBQ Meat', 'BBQ. Meat'),
    ('Chicken', 'Chicken'),
    ('Mushrooms', 'Mushrooms'),
]

PIZZA_CHOICES = [
    ('Small', 'Small'),
    ('Medium', 'Medium'),
    ('Large', 'Large'),
]

SAUCE_CHOICES = [
    ('BBQ Sauce', 'BBQ Sauce'),
    ('Ranch Sauce', 'Ranch Sauce'),
    ('Garlic Sauce', 'Garlic Sauce'),
    ('Marinara Sauce', 'Marinara Sauce'),
    ('Hot Sauce', 'Hot Sauce'),
]

class PizzaForm(forms.Form):
    size = forms.ChoiceField(choices=PIZZA_CHOICES)
    topping = forms.ChoiceField(choices=TOPPING_CHOICES)
    sauce = forms.ChoiceField(choices=SAUCE_CHOICES)