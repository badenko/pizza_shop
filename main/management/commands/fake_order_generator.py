from django.core.management.base import BaseCommand
from datetime import date, timedelta
from main.management.commands.generator import OrderGenerator
import random
class Command(BaseCommand):
    help = 'Generates fake orders in given timespan. Use only for testing purposes'

    def handle(self, *args, **options):
        period_start = date(2018, 9, 1)
        period_end = date.today()
        cur_date = period_start
        while period_start <= period_end:
            r = random.randint(1, 10)
            while r <= 10:
                orderGenerator = OrderGenerator()
                order = orderGenerator.generate_order()
                hours_range = range(24)
                hours = random.choice(hours_range)
                minutes_range = range(60)
                minutes = random.choice(minutes_range)
                order.date = cur_date
                if hours < 10:
                    hours = f"0{hours}"
                if minutes < 10:
                    minutes = f"0{minutes}"
                order.time = f"{hours}:{minutes}"
                order.save()
                r += 1
            cur_date = cur_date + timedelta(days=1)
