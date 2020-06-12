from django.contrib import admin
from .models import Pizza, Cart, PizzaOrder

admin.site.register(Pizza)
admin.site.register(Cart)
admin.site.register(PizzaOrder)