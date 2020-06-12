from django.urls import path

from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('pizza/', views.pizza, name='pizza'),
    path('cart/', views.cart, name='cart'),
    path('add/<int:pizza_id>', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:pizza_id>', views.remove_from_cart, name='remove_from_cart'),
]