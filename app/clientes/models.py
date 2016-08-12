# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime

# Create your models here.


class Cliente(models.Model):
	nombre = models.CharField(max_length=255,blank=True)
	apellido = models.CharField(max_length=255,blank=True)
	dni = models.CharField(max_length=15,blank=True)
	telefono = models.CharField(max_length=20,blank=True)
	empresa = models.CharField(max_length=255,blank=True)
	cif = models.CharField(max_length=20,blank=True)
	email = models.CharField(max_length=50,blank=True)
	telefono1 = models.CharField(max_length=20,blank=True)
	ciudad = models.CharField(max_length=100,blank=True)
	provincia = models.CharField(max_length=100,blank=True)
	direccion = models.CharField(max_length=100,blank=True)
	codpostal = models.CharField(max_length=10,blank=True)
	thumbnail = models.ImageField(upload_to = 'pic_folder_clientes/', default = 'pic_folder/None/no-img.png')	
	created_at = models.DateTimeField(editable=False)
	def __unicode__(self):
		return self.nombre
	def save(self, *args, **kwargs):
		if not self.id:
			self.created_at = datetime.datetime.now()
		return super(Cliente, self).save(*args, **kwargs)
