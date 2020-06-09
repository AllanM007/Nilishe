from django.shortcuts import render
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
                name=form.cleaned_data["name"],
                topping=form.cleaned_data["topping"],
                sauce=form.cleaned_data["sauce"],
            )
			pizza.save()
	else:
		form = PizzaForm()

	context = {
        'form':form,
    }

	return render(request, 'menu/pizza.html', {'form':form})