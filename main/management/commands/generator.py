import random
from main.models.customer import Customer
from main.models.order import Order
from main.models.order_items import OrderItem
from main.models.product import Beverage, Pizza

class OrderGenerator():
    def generate_order(self):
        order = Order()
        order.customer = self.generate_customer()
        order.save()
        orderlist = OrderItemsGenerator()
        orderlist.generate_order_list(order)
        return order

    def generate_customer(self):
        customer = Customer()
        if random.randint(1, 10) > 8:
            number_of_customers = Customer.objects.count()
            wild_card = random.randint(1, number_of_customers)
            customer = Customer.objects.get(id=wild_card)
        else:
            customer_generator = CustomerGenerator()
            customer = customer_generator.generate_customer()
        return customer

class CustomerGenerator():
    def generate_customer(self):
        customer = Customer()
        customer.name = self.generate_customer_name()
        customer.number = self.generate_customer_phone()
        customer.address = self.generate_customer_address()
        customer.save()
        return customer

    def generate_customer_name(self):
        names = [line.rstrip('\n') for line in open('for_generator/Names.txt')]
        name = random.choice(names)
        return name

    def generate_customer_phone(self):
        operator_list = ['50', '66', '95', '99', '63', '93', '67', '96', '97', '98']
        number = random.randint(1000000, 9999999)
        phone = '+380' + random.choice(operator_list) + str(number)
        return phone

    def generate_customer_address(self):
        address = [line.rstrip('\n') for line in open('for_generator/Streets.txt')]
        return random.choice(address)

class OrderItemsGenerator(): #LIST HAVE TO BE ASSIGNED TO ORDER NOT VICE VERSE
    def generate_order_list(self, order):
        rand = random.randint(1, 7)
        while rand < 8:
            if (rand % 2) == 0:
                order_item = OrderItem()
                order_item.order = order
                order_item.beverage = self.generate_beverage_item()
                order_item.save()
            else:
                order_item = OrderItem()
                order_item.order = order
                order_item.pizza = self.generate_pizza_item()
                order_item.save()
            rand += 1

    def generate_pizza_item(self):
        pizza = Pizza()
        number_of_pizzas = Pizza.objects.count()
        wild_card = random.randint(1, number_of_pizzas)
        pizza = Pizza.objects.get(id=wild_card)
        return pizza

    def generate_beverage_item(self):
        beverage = Beverage()
        number_of_beverages = Beverage.objects.count()
        wild_card = random.randint(1, number_of_beverages)
        beverage = Beverage.objects.get(id=wild_card)
        return beverage
