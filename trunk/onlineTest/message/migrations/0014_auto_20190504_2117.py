# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2019-05-04 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0013_auto_20190504_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='消息'),
        ),
    ]
