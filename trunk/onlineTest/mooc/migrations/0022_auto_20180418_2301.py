# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-04-18 23:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0021_auto_20180418_2300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='courser_id',
            new_name='courser',
        ),
    ]