# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, render_to_response, HttpResponse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
import time


# Create your views here.

class CitaCreateView(CreateView):
    form_class = CitaCrearForm
    template_name = "crearCita.html"
    success_url="/cita/"
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(CitaCreateView, self).dispatch(*args, **kwargs)
    def post(self,request, *args, **kwargs):

        if request.is_ajax():
            cita = Cita.objects.filter(dia=request.POST['dia']).filter(hora=request.POST['hora'])
            msj='existeCita'
            if not cita:
                cita = Cita.objects.create(user_id=request.user.id,contacto_id=None,dia=request.POST['dia'],hora=request.POST['hora'])
                cita.save()
                msj=cita.pk
                return HttpResponse(msj)
                #form.save()
            else:
                return HttpResponse(msj)
        return super(CitaCreateView, self).post(request,*args, **kwargs)



class CitasTemplateView(TemplateView):
    template_name = "citaTabla.html"
    dia = time.strftime("%Y-%m-%d")
    def dispatch(self,*args,**kwargs):
        self.dia = self.kwargs['dia']
        return super(CitasTemplateView, self).dispatch(*args, **kwargs)
    def citas(self,*args,**kwargs):
        cita = Cita.objects.filter(dia=self.dia).order_by('hora')
        if cita:
            return cita
        else:
            return None
    def get(self,*args,**kwargs):
        if not self.request.is_ajax():
            raise Http404
        return super(CitasTemplateView, self).get(*args, **kwargs)



class ListCitasView(ListView):
    model = Cita
    template_name = 'listarCitas.html'
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(ListCitasView, self).dispatch(*args, **kwargs)
    def get_queryset(self):
        return Cita.objects.filter(dia=time.strftime("%Y-%m-%d"))



class CitaDeleteView(DeleteView):
    model = Contacto
    success_url = "/cita/"
    template_name = "listarCitas.html"
    def delete(self, request, *args, **kwargs):
        if request.is_ajax():
            cita = Cita.objects.get(pk=request.POST['pk'])
            cita.delete()
            return HttpResponse('ok')
        else:
            raise Http404
