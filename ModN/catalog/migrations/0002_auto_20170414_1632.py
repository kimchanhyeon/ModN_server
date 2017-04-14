# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-14 07:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='market',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='market_products', to='catalog.Market'),
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='products', to='catalog.Seller'),
        ),
        migrations.AddField(
            model_name='sku',
            name='order_item',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='skus_orderItem_related', to='orders.OrderItem'),
        ),
        migrations.AddField(
            model_name='sku',
            name='product',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='skus', to='catalog.Product'),
        ),
    ]
