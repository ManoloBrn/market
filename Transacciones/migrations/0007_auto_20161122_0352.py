# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-22 03:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Transacciones', '0006_checkout_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='bemail',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='category',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='city',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='colonia',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='country',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='demail',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='itemName',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='itemdescription',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='name',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='state',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='street1',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='street2',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='szip',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='unitprice',
        ),
    ]
