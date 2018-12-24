# Generated by Django 2.1.4 on 2018-12-24 15:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20181224_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.date(2018, 12, 24)),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('accepted', 'Accepted'), ('delivered', 'Delivered'), ('canceled', 'Canceled')], default='Accepted', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='time',
            field=models.CharField(default='15:59', max_length=50),
        ),
    ]