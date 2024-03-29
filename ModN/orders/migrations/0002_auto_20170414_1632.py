# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-14 07:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20170414_1632'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_auto_20170414_1632'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fulfillmentgroup',
            name='address',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='address_fulfillment_groups+', to='users.CustomerAddress'),
        ),
        migrations.AddField(
            model_name='fulfillmentgroup',
            name='fulfillment_option',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='options_fulfillment_group+', to='orders.FulfillmentOption'),
        ),
        migrations.AddField(
            model_name='fulfillmentgroup',
            name='order',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='fulfillment_groups', to='orders.Order'),
        ),
        migrations.AddField(
            model_name='fulfillmentgroup',
            name='seller',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='seller_fulfillment_groups+', to='catalog.Market'),
        ),
        migrations.AddField(
            model_name='order',
            name='market',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='market_orders+', to='catalog.Market'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_group',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='orders.OrderGroup'),
        ),
        migrations.AddField(
            model_name='ordergroup',
            name='create_by',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orderGroup_createBy_related', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ordergroup',
            name='updated_by',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orderGroup_updatedBy_related', to=settings.AUTH_USER_MODEL),
        ),
    ]
