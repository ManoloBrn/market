# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-14 17:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Negocios', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='negocio',
            options={'verbose_name': 'Negocio', 'verbose_name_plural': 'Negocios'},
        ),
    ]
