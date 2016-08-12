# -*- encoding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from .models import *



class CrearProducto(ModelForm):
	id = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden',}),label="",) 
	nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control has-feedback-left','placeholder':'Nombre'}),label="",) 
	descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control has-feedback-left','rows':'4','placeholder':'Descripción'}),label="") 
	precio = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control has-feedback-left','placeholder':'Precio'}),label="",) 
	thumbnail = forms.FileField()
	class Meta:
		model = Producto
		fields = ('id','nombre','descripcion','precio','thumbnail')


