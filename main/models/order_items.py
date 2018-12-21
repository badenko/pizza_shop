from django.db import models
from .order import Order
from .product import Pizza, Beverage

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, null=True)
    beverage = models.ForeignKey(Beverage, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '%s' % self.order.id
