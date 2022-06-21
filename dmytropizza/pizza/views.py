from django.shortcuts import render


# View for "home" page
def home(request):
    return render(request, 'pizza/home.html')


# View for "order" page
def order(request):
    return render(request, 'pizza/order.html')
