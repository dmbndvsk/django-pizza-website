from django.shortcuts import render
from .forms import PizzaForm


# View for "home" page
def home(request):
    return render(request, 'pizza/home.html')


# View for "order" page
def order(request):
    form = PizzaForm()
    return render(request, 'pizza/order.html', {'pizzaform': form})
