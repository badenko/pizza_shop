from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Customer(models.Model):
    name = models.CharField(max_length=50, blank=False)
    number = PhoneNumberField(null=False, blank=False, unique=True)
    address = models.CharField(max_length=150, blank=False)

    def __str__(self):
        return self.name
        