from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from .models import Pizza, Cart, PizzaOrder
from django.contrib import messages
from .forms import PizzaForm
import uuid

def menu(request):
	pizzas = Pizza.objects.all()

	context = {
        'pizzas':pizzas,
    }
	return render(request, 'menu/menu.html', context)

def pizza(request):

	if request.method == 'POST':
		
		form = PizzaForm(request.POST)

		if form.is_valid():
			pizza = Pizza(
                size=form.cleaned_data["size"],
                topping=form.cleaned_data["topping"],
                sauce=form.cleaned_data["sauce"],
            )
			pizza.save()
		
		return redirect('menu:cart')

	else:
		form = PizzaForm()

	context = {
        'form':form,
    }

	return render(request, 'menu/pizza.html', {'form':form})

def add_to_cart(request, pizza_id):
    pizza = get_object_or_404(Pizza, pk=pizza_id)
    cart,created = Cart.objects.get_or_create(user=request.user)
    order,created = PizzaOrder.objects.get_or_create(pizza=pizza,cart=cart)
    order.quantity += 1
    order.save()
    messages.success(request, "Cart updated!")
    return redirect('menu:cart')

def remove_from_cart(request, pizza_id):
    try:
        pizza = Pizza.objects.get(pk = pizza_id)
    except ObjectDoesNotExist:
        pass 
    else:
        cart = Cart.objects.get(user = request.user, active = True)
        cart.remove_from_cart(pizza_id)
    messages.success(request, "Item removed!")
    return redirect('menu:cart')


def cart(request):
    cart = Cart.objects.get(user=request.user.id)
    orders = PizzaOrder.objects.filter(cart=cart)
    total = 0
    count = 0
    
    #calculate total order value
    for order in orders:
        total += order.pizza.price * order.quantity
        count += order.quantity
    
    cartid = cart.identifier

    request.session['cartid'] = cartid
    
    context = {
        'ident': cart,
        'cart': orders,
        'total': total,
        'count': count,
    }
    return render(request, 'menu/cart.html', context)
