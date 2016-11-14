# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-14 17:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Compras', '0002_transaction_idcliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='idcliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_cliente', to=settings.AUTH_USER_MODEL),
        ),
    ]
