# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-14 07:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170414_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeraddress',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.CustomerAddress'),
        ),
    ]
