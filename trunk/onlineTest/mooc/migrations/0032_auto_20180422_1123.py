# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-04-22 11:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mooc', '0031_auto_20180422_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='creater',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Resource_creater', to=settings.AUTH_USER_MODEL),
        ),
    ]