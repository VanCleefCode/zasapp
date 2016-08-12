from django.shortcuts import render, get_object_or_404, render_to_response, HttpResponse
from django.http import Http404
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.datastructures import MultiValueDictKeyError

from .forms import *
from .models import *

# Create your views here.


class ClienteCreateView(CreateView):
    form_class = ClienteForm
    template_name = "crearcliente.html"
    success_url="/clientes/"
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(ClienteCreateView, self).dispatch(*args, **kwargs)
    def post(self,request, *args, **kwargs):
    	try:
            cliente = Cliente.objects.create(nombre=request.POST['nombre'],apellido=request.POST['apellido'],dni=request.POST['dni'],telefono=request.POST['telefono'],empresa=request.POST['empresa'],cif=request.POST['cif'],email=request.POST['email'],telefono1=request.POST['telefono1'],ciudad=request.POST['ciudad'],provincia=request.POST['provincia'],codpostal=request.POST['codpostal'],direccion=request.POST['direccion'],thumbnail=request.FILES['file'],)
        except MultiValueDictKeyError:
            cliente = Cliente.objects.create(nombre=request.POST['nombre'],apellido=request.POST['apellido'],dni=request.POST['dni'],telefono=request.POST['telefono'],empresa=request.POST['empresa'],cif=request.POST['cif'],email=request.POST['email'],telefono1=request.POST['telefono1'],ciudad=request.POST['ciudad'],provincia=request.POST['provincia'],codpostal=request.POST['codpostal'],direccion=request.POST['direccion'],)
        cliente.save()
    	return HttpResponse('ok')



class ClientesListView(ListView):
	model = Cliente
	template_name='listClientes.html'


class buscarCliente(ListView):
    model = Cliente
    template_name='buscarCliente.html'


class EditarClienteView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "editarCliente.html"
    success_url="/clientes/"
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(EditarClienteView, self).dispatch(*args, **kwargs)
    def post(self,request, *args, **kwargs):
        try:
            c = Cliente.objects.get(pk=self.kwargs['pk'])
            c.nombre = request.POST['nombre']
            c.apellido = request.POST['apellido']
            c.dni = request.POST['dni']
            c.telefono = request.POST['telefono']
            c.empresa = request.POST['empresa']
            c.cif = request.POST['cif']
            c.email = request.POST['email']
            c.telefono1 = request.POST['telefono1']
            c.ciudad = request.POST['ciudad']
            c.provincia = request.POST['provincia']
            c.codpostal = request.POST['codpostal']
            c.direccion = request.POST['direccion']
            c.thumbnail = request.FILES['file']
            c.save()
        except MultiValueDictKeyError:
            c = Cliente.objects.filter(pk=self.kwargs['pk']).update(nombre=request.POST['nombre'],apellido=request.POST['apellido'],dni=request.POST['dni'],telefono=request.POST['telefono'],empresa=request.POST['empresa'],cif=request.POST['cif'],email=request.POST['email'],telefono1=request.POST['telefono1'],ciudad=request.POST['ciudad'],provincia=request.POST['provincia'],codpostal=request.POST['codpostal'],direccion=request.POST['direccion'],)
        return HttpResponse('ok')
