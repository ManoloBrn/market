# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-14 18:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Compras', '0009_auto_20161114_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='idCliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
