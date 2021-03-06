# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-25 15:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20160724_2334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Templates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=255)),
                ('url', models.CharField(blank=True, max_length=255)),
                ('thumbnail', models.ImageField(default='pic_folder_productos/None/no-image.png', upload_to='pic_folder_productos/')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Producto')),
            ],
        ),
    ]
