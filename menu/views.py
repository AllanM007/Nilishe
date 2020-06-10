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

			size = request.POST.get('size')
			topping = request.POST.get('topping')
			sauce = request.POST.get('sauce')

			request.session['test1'] = str(size)
			request.session['test2'] = str(topping)
			request.session['test3'] = str(sauce)
		
		return redirect('menu:cart')

	else:
		form = PizzaForm()

	context = {
        'form':form,
    }

	return render(request, 'menu/pizza.html', {'form':form})

def cart(request):

	size = request.session['test1']
	topping = request.session['test2']
	sauce = request.session['test3']
	
	context={
        'size':size,
		'topping':topping,
		'sauce':sauce,
    }

	return render(request, 'menu/cart.html', context)