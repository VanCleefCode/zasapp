# -*- encoding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from .models import *



class ClienteForm(ModelForm):
	id = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden'}),label="",) 
	nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control has-feedback-left','placeholder':'Nombre'}),label="",) 
	apellido = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Apellido'}),label="",) 
	dni = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control has-feedback-left','placeholder':'DNI'}),label="",) 
	telefono = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Telefono'}),label="",) 
	empresa = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control has-feedback-left','placeholder':'Razon Social'}),label="",) 
	cif = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'CIF'}),label="",) 
	email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control has-feedback-left','placeholder':'Email'}),label="",) 
	telefono1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Telefono de Oficina'}),label="",) 
	ciudad = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control has-feedback-left','placeholder':'Ciudad'}),label="",) 
	provincia = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Provincia'}),label="",) 
	codpostal = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control has-feedback-left','placeholder':'Codigo Postal'}),label="",) 
	direccion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Dirección'}),label="",) 
	thumbnail = forms.FileField()
	class Meta:
		model = Cliente
		fields = ('id','nombre', 'apellido','dni', 'telefono','empresa','cif','email','telefono1','ciudad','provincia','direccion','codpostal','thumbnail' )