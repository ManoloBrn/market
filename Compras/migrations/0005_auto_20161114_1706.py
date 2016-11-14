# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-14 17:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Compras', '0004_auto_20161114_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='idcliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente_transaction', to=settings.AUTH_USER_MODEL),
        ),
    ]