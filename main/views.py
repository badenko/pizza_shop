from django.shortcuts import render
from .models.order import Order
from .models.order_items import OrderItem
from .models.product import Pizza, Beverage
from .management.commands.generator import OrderGenerator

# Create your views here.

def index(request):
    ar_pizza = []
    ar_beverage = []
    for i in Pizza.objects.all():
        ar_pizza.append(i)
    for i in Beverage.objects.all():
        ar_beverage.append(i)
    data = {'pizzas': ar_pizza, 'beverages': ar_beverage}
    return render(request, 'main/index.html', context=data)

def orders(request):
    #o = OrderGenerator()
    #o.generate_order()
    orders = Order.objects.all()
    data = {'orders': orders}
    return render(request, 'main/orders.html', context=data)

def order_details(request, order_id=3):
    order = Order.objects.get(id=order_id)
    items = OrderItem.objects.filter(order=order)
    data = {'order': order, 'items': items}
    return render(request, 'main/order_details.html', context=data)

def contact(request):
    data = {'Message': 'Data from context'}
    return render(request, 'main/contact.html', context=data)

def test(request):
    return render(request, 'test.html', {'title':'title'})
