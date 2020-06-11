from django.shortcuts import render, redirect
from .models import Pizza
from .forms import PizzaForm


def menu(request):
	pizzas = Pizza.objects.all()
	
	form = PizzaForm()

	context = {
        'pizzas':pizzas,
		'form':form,
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
	
	context={
        'size':size,
		'topping':topping,
		'sauce':sauce,
    }

	return render(request, 'menu/cart.html', context)