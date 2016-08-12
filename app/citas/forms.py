# -*- encoding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from .models import Cita

Hora = [('08:00','08:00'),('09:00','09:00'),('10:00','10:00'),('11:00','11:00'),('14:00','14:00'),('15:00','15:00'),('16:00','16:00')]
DATE_INPUT_FORMATS = ['%d/%m/%Y']


class CitaCrearForm(ModelForm):
    dia = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y',attrs={'type':'date','class': 'form-control has-feedback-left','onchange':'javascript:traerCitas($(this).val())',}),input_formats=DATE_INPUT_FORMATS,required=True)
    hora = forms.CharField(widget=forms.Select(choices=Hora,attrs={'class': 'form-control has-feedback-left',}),required=True) 
    class Meta:
        model = Cita
        fields = ('dia','hora',)
