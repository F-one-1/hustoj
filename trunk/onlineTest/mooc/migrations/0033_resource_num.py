# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-04-23 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0032_auto_20180422_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='num',
            field=models.TextField(blank=True, null=True, verbose_name='序号'),
        ),
    ]