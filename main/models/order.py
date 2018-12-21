from datetime import date
from django.db import models
from .customer import Customer

class Order(models.Model):
    order_number = models.CharField(max_length=50, default=date.today())
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.order_number
