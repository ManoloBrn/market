# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 23:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_remove_cliente_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='name',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
