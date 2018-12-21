from django.contrib import admin
from .models.customer import Customer
from .models.product import Pizza, Beverage

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    pass

class PizzaAdmin(admin.ModelAdmin):
    fields = ('pk', 'name', 'price', 'size')

admin.site.register(Customer)
admin.site.register(Pizza)
admin.site.register(Beverage)
