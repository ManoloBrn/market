# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-14 17:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Compras', '0001_initial'),
    ]
    '''
    operations = [
        migrations.AddField(
            model_name='transaction',
            name='idcliente',
            field=models.ForeignKey(default=1, on_delete='transaction_cliente', to=settings.AUTH_USER_MODEL, to_field='id'),
            preserve_default=False,
        ),
    ]
    '''
    operations = [
        migrations.AddField(
            model_name='transaction',
            name='idcliente',
            field=models.ForeignKey(default=1, on_delete='transaction_cliente', to=settings.AUTH_USER_MODEL, to_field='id'),
            preserve_default=False,
        ),
    ]
