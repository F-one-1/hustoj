# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-04-18 23:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0022_auto_20180418_2301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='week',
        ),
    ]