# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from contactos.models import Contacto

from django.db import models

# Create your models here.

Hora = [('08:00','08:00'),('09:00','09:00'),('10:00','10:00'),('11:00','11:00'),('14:00','14:00'),('15:00','15:00'),('16:00','16:00')]

class Cita(models.Model):
    user = models.ForeignKey(User)
    contacto = models.ForeignKey(Contacto,null=True)
    dia = models.DateField(null=True)
    hora = models.TimeField(choices=Hora)
    def __unicode__(self):
    	return self.dia
