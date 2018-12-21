from django.core.management.base import BaseCommand
from main.models.product import PizzaSize, Pizza, Beverage
from main.models.customer import Customer

class Command(BaseCommand):
    help = 'Initialize basic data for database such as pizza sizes'

    def handle(self, *args, **options):
        self.init_pizza_size()
        self.init_pizza()
        self.init_beverage()

    def init_beverage(self):
        beverage = Beverage()
        beverage.name = 'Coca-Cola'
        beverage.price = '10'
        beverage.volume = 0.3
        beverage.save()

        beverage = Beverage()
        beverage.name = 'Coca-Cola'
        beverage.price = '15'
        beverage.volume = 0.5
        beverage.save()

        beverage = Beverage()
        beverage.name = 'Coca-Cola'
        beverage.price = '20'
        beverage.volume = 1
        beverage.save()

        beverage = Beverage()
        beverage.name = 'Apple juice'
        beverage.price = '25'
        beverage.volume = 0.5
        beverage.save()

    def init_pizza(self):
        p_s = PizzaSize.objects.get(size='medium')
        pizza = Pizza()
        pizza.name = 'Cheese'
        pizza.price = 100
        pizza.size = p_s
        pizza.save()

        pizza = Pizza()
        pizza.name = 'Chicken'
        pizza.price = 120
        pizza.size = p_s
        pizza.save()

        pizza = Pizza()
        pizza.name = 'Bacon'
        pizza.price = 120
        pizza.size = p_s
        pizza.save()

        pizza = Pizza()
        pizza.name = 'Pepperoni'
        pizza.price = 130
        pizza.size = p_s
        pizza.save()

        pizza = Pizza()
        pizza.name = 'Magic Shrooms'
        pizza.price = 120
        pizza.size = p_s
        pizza.save()

    def init_pizza_size(self):
        pizza_size_big = PizzaSize()
        pizza_size_big.size = 'big'
        pizza_size_big.save()

        pizza_size_medium = PizzaSize()
        pizza_size_medium.size = 'medium'
        pizza_size_medium.save()

        pizza_size_small = PizzaSize()
        pizza_size_small.size = 'small'
        pizza_size_small.save()
