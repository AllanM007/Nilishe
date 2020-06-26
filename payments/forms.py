from django import forms

class NumberForm(forms.Form):
    phone_number = forms.IntegerField(label='phone_number')
    amount = forms.IntegerField(label='amount')