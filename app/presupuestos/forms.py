# -*- encoding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from .models import *
from productos.models import Producto



class FPresupuesto(ModelForm):
	producto = forms.ModelChoiceField(queryset=Producto.objects.all(),widget=forms.Select(attrs={'class':'form-control has-feedback-left'}))
	class Meta:
		model = Presupuesto
		fields = ('producto','template','cliente','monto')


