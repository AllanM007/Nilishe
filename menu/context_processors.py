from django.shortcuts import get_object_or_404
from menu.models import Pizza


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    pizza_count = 0
    
    for id in cart.items():
        pizza = get_object_or_404(Pizza, pk=11)
        cart_items.append({'id': id, 'pizza': pizza})
    
    return {'cart_items': cart_items, 'pizza_count': pizza_count}