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

from .models import *
from .forms import *
import time


# Create your views here.
class CrearProductoView(CreateView):
    form_class = CrearProducto
    template_name = "crearProducto.html"
    success_url="/producto/"
    def dispatch(self, *args, **kwargs):
    	if not self.request.user.is_superuser:
    		raise Http404
    	return super(CrearProductoView, self).dispatch(*args, **kwargs)
    def post(self,request, *args, **kwargs):
    	try:
    		producto = Producto.objects.create(nombre=request.POST['nombre'],descripcion=request.POST['descripcion'],precio=request.POST['precio'],thumbnail=request.FILES['file'],)
    	except MultiValueDictKeyError:
    		producto = Producto.objects.create(nombre=request.POST['nombre'],descripcion=request.POST['descripcion'],precio=request.POST['precio'],)
        producto.save()
       	msj=producto.pk
        return HttpResponse(msj)
      

class ListProductosView(ListView):
    model = Producto
    template_name = 'listarProductos.html'
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(ListProductosView, self).dispatch(*args, **kwargs)



class EditarProductoView(UpdateView):
    model = Producto
    form_class = CrearProducto
    template_name = "editarProducto.html"
    success_url="/producto/"
    def templates(self,*args,**kwargs):
        p = Templates.objects.filter(producto_id=self.kwargs['pk'])
        return p
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_superuser:
            raise Http404
        return super(EditarProductoView, self).dispatch(*args, **kwargs)
    def post(self,request, *args, **kwargs):
        try:
            producto = Producto.objects.get(pk=self.kwargs['pk'])
            producto.nombre = request.POST['nombre']
            producto.descripcion = request.POST['descripcion']
            producto.precio = request.POST['precio']
            producto.thumbnail = request.FILES['file']
            producto.save()
        except MultiValueDictKeyError:
            producto = Producto.objects.filter(pk=self.kwargs['pk']).update(nombre=request.POST['nombre'],descripcion=request.POST['descripcion'],precio=request.POST['precio'],)
        return HttpResponse('ok')

def AgergarTemplate(request):
    if request.POST:
        t = Templates.objects.create(producto_id=request.POST['idP'],nombre=request.POST['nombreP'],url=request.POST['urlP'])
        t.save()
        return HttpResponse('ok')
    else:
        raise Http404

class TraerTemplate(ListView):
    model = Templates
    template_name = "traetemplate.html"
    def get_queryset(self):
        return Templates.objects.filter(producto_id=self.request.GET['id'])
    def monto(self):
        monto = Producto.objects.get(pk=self.request.GET['id'])
        print  monto.precio
        return monto.precio