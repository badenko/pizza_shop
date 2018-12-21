from django.shortcuts import render
from .models.order import Order
from .models.order_items import OrderItem
from .management.commands.generator import OrderGenerator

# Create your views here.

def index(request):
    data = {'Message': 'Data from context'}
    return render(request, 'main/index.html', context=data)

def order(request):
    #o = OrderGenerator()
    #o.generate_order()
    orders = Order.objects.all()
    data = {'orders': orders}
    return render(request, 'main/order.html', context=data)

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
