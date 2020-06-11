from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Pizza
from .forms import PizzaForm


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

def cart(request):

	return render(request, 'menu/cart.html')

def add_to_cart(request, id):

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id)

    request.session['cart'] = cart
    return redirect(reverse('menu:cart'))


def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    #quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    #if quantity > 0:
    #    cart[id] = quantity
    #else:
    #    cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))