# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-25 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_auto_20160725_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
