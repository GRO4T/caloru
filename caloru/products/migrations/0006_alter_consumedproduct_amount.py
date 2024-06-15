# Generated by Django 3.2.16 on 2024-06-15 18:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20240609_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumedproduct',
            name='amount',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5000)]),
        ),
    ]
