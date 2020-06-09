from django.shortcuts import render
from .models import Pizza
from .forms import PizzaForm


def menu(request):
	pizzas = Pizza.objects.all()
	
	context = {
        'pizzas':pizzas,
    }
	return render(request, 'menu/menu.html', context)

def pizza(request, pk):

	form = PizzaForm()

	pizza = Pizza.objects.get(pk = pk)
	
	context = {
        'pizza':pizza,
        'form':form,
    }

	return render(request, 'menu/pizza.html', context)