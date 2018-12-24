from datetime import datetime, date
from django.db import models
from .customer import Customer

class Order(models.Model):
    ORDER_STATUSES = (
        ('accepted', 'Accepted'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled')
    )
    order_number = models.CharField(max_length=50, default=datetime.now().date())
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=ORDER_STATUSES, default='Accepted')
    date = models.DateField(default=date.today())
    #date = models.DateField(auto_now_add=True)
    time = models.CharField(max_length=50, default=datetime.now().time().strftime("%H:%M"))

    def __str__(self):
        return self.order_number
