# Generated by Django 2.1.4 on 2018-12-16 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20181216_1059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='volume',
            new_name='size',
        ),
        migrations.AlterField(
            model_name='beverage',
            name='volume',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True),
        ),
    ]
