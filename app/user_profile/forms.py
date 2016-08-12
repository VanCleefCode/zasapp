# forms.py
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


TIPO = [('Ventas','Ventas'),('Consultoria','Consultoria'),('Mercadeo','Mercadeo'),('Administacion','Administacion'),('Sistemas','Sistemas'),]

class UsuarioForm(forms.ModelForm):
	id = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden'}),label="", required=False,) 
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control has-feedback-left','placeholder':'Nick/Username'}),label="", required=True,error_messages={'required': 'Debe ingresar el Usuario.'}) 
	email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Email'}),label="", required=True,error_messages={'required': 'Debe ingresar el Email.'}) 
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control has-feedback-left','placeholder':'Nombre'}),label="", required=True,error_messages={'required': 'Debe ingresar el Nombre.'}) 
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Apellido'}),label="", required=True,error_messages={'required': 'Debe ingresar el Apellido.'}) 
	telefono = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control has-feedback-left','placeholder':'Telefono'}),label="", required=True,error_messages={'required': 'Debe ingresar el Telefono.'}) 
	tipo = forms.CharField(widget=forms.Select(choices=TIPO,attrs={'class': 'form-control has-feedback-left',})) 
	class Meta:
		model = User
		fields = ('id','username','first_name','last_name','email','telefono','tipo')

class ChangeNameForm(ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'textInput'}),label="Nombre", required=True,error_messages={'required': 'Debe ingresar el Nombre.'}) 
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'textInput'}),label="Apellido", required=True,error_messages={'required': 'Debe ingresar el Apellido.'})
    class Meta:
        model = User
        fields = ('first_name', 'last_name' )

class ChangeEmailForm(ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'textInput'}),required=True,error_messages={'required': 'Debe ingresar un Email.','valid':'valido'})
    class Meta:
        model = User
        fields = ('email',)

