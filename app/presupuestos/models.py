# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
from productos.models import *
from django.contrib.auth.models import User
from clientes.models import Cliente
# Create your models here.



class Presupuesto(models.Model):
	user = models.ForeignKey(User)
	producto = models.ForeignKey(Producto)
	template = models.ForeignKey(Templates)
	cliente = models.ForeignKey(Cliente)
	monto = models.CharField(max_length=255,blank=True)
	status = models.CharField(max_length=2,default="0")
	created_at = models.DateTimeField(editable=False)
	def save(self, *args, **kwargs):
		if not self.id:
			self.created_at = datetime.datetime.now()
		return super(Producto, self).save(*args, **kwargs)
