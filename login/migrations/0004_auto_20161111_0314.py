# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-11 03:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20161111_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='billing_address',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cards',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='plan',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='shipping_address',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
