# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
from djmoney.models.fields import MoneyField


# Create your models here.


class Producto(models.Model):
	nombre = models.CharField(max_length=255,blank=True)
	descripcion = models.CharField(max_length=255,blank=True)
	precio = models.CharField(max_length=10,blank=True,null=True)
	thumbnail = models.ImageField(upload_to = 'pic_folder_productos/', default = 'pic_folder_productos/None/no-image.png')	
	created_at = models.DateTimeField(editable=False)	
	def __unicode__(self):
		return self.nombre
	def save(self, *args, **kwargs):
		if not self.id:
			self.created_at = datetime.datetime.now()
		return super(Producto, self).save(*args, **kwargs)

class Templates(models.Model):
	producto = models.ForeignKey(Producto)
	nombre = models.CharField(max_length=255,blank=True)
	url = models.CharField(max_length=255,blank=True)
	thumbnail = models.ImageField(upload_to = 'pic_folder_productos/', default = 'pic_folder_productos/None/no-image.png')	
