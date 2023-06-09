# Generated by Django 4.1.3 on 2023-04-24 15:30

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(default='Moscow', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='first_name',
            field=models.CharField(default=datetime.datetime(2023, 4, 24, 15, 30, 30, 347354, tzinfo=datetime.timezone.utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='last_name',
            field=models.CharField(default='nill', max_length=50),
            preserve_default=False,
        ),
    ]
