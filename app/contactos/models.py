# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

fuentes = [('Pagina Web','Pagina Web'),('Periodico','Periodico'),('Referido','Referido'),('Redes Sociales','Redes Sociales'),('Email Marketing','Email Marketing'),('Presencial','Presencial'),('Otro','Otro')]

class Contacto(models.Model):
    nombre = models.CharField(max_length=80, blank=True)  
    apellido = models.CharField(max_length=80, blank=True)  
    email = models.CharField(max_length=50, blank=True)  
    telefono = models.CharField(max_length=50, blank=True)  
    fuente = models.CharField(max_length=20,choices=fuentes,default=1)
    thumbnail = models.ImageField(upload_to = 'pic_folder_contactos/', default = 'pic_folder/None/no-img.png') 
