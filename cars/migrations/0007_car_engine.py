# Generated by Django 4.2.2 on 2023-07-01 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_car_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='engine',
            field=models.CharField(default='', max_length=100),
        ),
    ]
