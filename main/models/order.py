from datetime import datetime
from django.db import models
from .customer import Customer

class Order(models.Model):
    ORDER_STATUSES = (
        ('A', 'accepted'),
        ('D', 'delivered'),
        ('C', 'canceled')
    )
    order_number = models.CharField(max_length=50, default=datetime.now().date())
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choises=ORDER_STATUSES, default='A')
    date = models.DateField(auto_now_add=True)
    time = models.CharField(max_length=50, default=datetime.now().time().strftime("%H:%M"))

    def __str__(self):
        return self.order_number
