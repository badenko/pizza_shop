from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        abstract = True
        app_label = 'main'

    def __str__(self):
        return self.name

class PizzaSize(models.Model):
    size = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.size

class Pizza(Product):
    size = models.ForeignKey(PizzaSize, on_delete=models.CASCADE, to_field='size')

class Beverage(Product):
    volume = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
