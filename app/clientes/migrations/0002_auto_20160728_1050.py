# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='thumbnail',
            field=models.ImageField(default='pic_folder/None/no-img.png', upload_to='pic_folder_clientes/'),
        ),
    ]