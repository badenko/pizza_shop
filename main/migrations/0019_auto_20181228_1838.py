# Generated by Django 2.1.4 on 2018-12-28 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20181228_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beverage',
            name='image',
            field=models.ImageField(upload_to='pizza_image'),
        ),
        migrations.AlterField(
            model_name='order',
            name='time',
            field=models.CharField(default='18:38', max_length=50),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='image',
            field=models.ImageField(upload_to='pizza_image'),
        ),
    ]