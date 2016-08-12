# -*- encoding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from .models import Contacto

fuentes = [('Pagina Web','Pagina Web'),('Periodico','Periodico'),('Referido','Referido'),('Redes Sociales','Redes Sociales'),('Email Marketing','Email Marketing'),('Presencial','Presencial'),('Otro','Otro')]


class ContactoForm(ModelForm):
    id = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden'}),label="", required=False,) 
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control has-feedback-left','placeholder':'Nombre'}),label="", required=True,error_messages={'required': 'Debe ingresar el Nombre.'}) 
    apellido = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Apellido'}),label="", required=True,error_messages={'required': 'Debe ingresar el Apellido.'}) 
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control has-feedback-left','placeholder':'Email'}),label="", required=True,error_messages={'required': 'Debe ingresar el Email.'}) 
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Telefono'}),label="", required=True,error_messages={'required': 'Debe ingresar el Telefono.'}) 
    fuente = forms.CharField(widget=forms.Select(choices=fuentes,attrs={'class': 'form-control has-feedback-left',})) 
    class Meta:
        model = Contacto
        fields = ('id','nombre', 'apellido','email','telefono','fuente' )
