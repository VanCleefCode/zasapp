# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, render_to_response, HttpResponse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.utils.datastructures import MultiValueDictKeyError

from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .forms import *
from .models import *
import time


# Create your views here.
class CrearPresupuestoView(CreateView):
    form_class = FPresupuesto 
    template_name = "crearPresupuesto.html"
    success_url="/presupuestos/"
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(CrearPresupuestoView, self).dispatch(*args, **kwargs)
    def post(self,request, *args, **kwargs):
        try:
    		presupuesto = Presupuesto.objects.create(nombre=request.POST['nombre'],descripcion=request.POST['descripcion'],precio=request.POST['precio'],thumbnail=request.FILES['file'],)
    	except MultiValueDictKeyError:
    		presupuesto = Presupuesto.objects.create(nombre=request.POST['nombre'],descripcion=request.POST['descripcion'],precio=request.POST['precio'],)
        presupuesto.save()
       	msj=producto.pk
        return HttpResponse(msj)
      
