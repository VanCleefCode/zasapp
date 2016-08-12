# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, render_to_response, HttpResponse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail.message import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from celery import task

#CONTAR REGISTROS
#from django.db.models import Count
#co =  User.objects.annotate(cont = Count('pk'))
#print co[0].cont
mensage = """<table style='width:600px;margin:auto;border: 1px solid #333;padding:5px;background:#515254'>       
            <tr>
        <td style='background:#060606;text-align:center;'>
            <img src='http://www.century21.com.ve/images/logo.jpg' style='float:left' alt=''>
            <div style='float:right;font-size:2em;color:#fff;padding:10px;'> Gracias<br><span style='font-size:.5em;color:yellow'>por Contactarnos</span></div>
        </td>
    </tr>
    <tr>
        <td style='background:#515254;color:#fff;border:none'>
            <div flot:left>
                <p style='padding:10px;text-align:justify'>Gracias por contactarnos <span style='color:yellow; font-weight:bold'>Sr(a) Luis Leal</span>. De acuerdo a su solicitud, por medio del correo, te hacemos llegar informaci&oacute;n clave para aquirir una <span style='color:yellow'>FRANQUICIA CENTURY 21</span> 
                <br>
                Somos un negocio probado y exitoso que ahora puede ser tuyo. Century 21 es la franquicia de comercializaci&oacute;n inmobiliaria m&aacute;s reconocida del mundo, con m&aacute;s de 30 a&ntilde;os de experiencia,presente en mas de 70 paises, con mas de 100 oficinas en Venezuela.
                </p>
                <p style='padding:10px;text-align:center;font-size:1.1em;margin-top:-30px'>
                    Adquirir una franquicia de Century 21 es <strong>Facil y Accesible</strong>, solo necesitas:
                </p>
            </div>
            

        </td>
    </tr>

    <tr>
        <td style='color:#fff;font-size:1em;text-align:center'>
            <div style='padding:5px; box-sizing: border-box;width:30%;float:left;background:#4C4C4C;height:65px'>Local u Oficina de mas de 40 mtrs</div>
            <div style='padding:5px; box-sizing: border-box;width:30%;float:left;background:#3D3D3D;height:65px'>Una compa&ntilde;ia registrada</div>
            <div style='padding:5px; box-sizing: border-box;width:30%;float:left;background:#2B2B2B;height:65px'>Una distancia de mas de 450 mtrs de una oficina de Century 21</div>
        </td>
    </tr>
    <tr>
        <td style='color:yellow;text-align:center;font-size:1.4em'>
            El proceso se inicia con una carta de intenci&oacuten
        </td>
    </tr>
    <tr>
        <td style='background:#3D3D3D;text-align:justify;padding:10px;color:#fff'>
            En <b>CENTURY 21</b> nunca estar&aacute;s solo; te acompa&ntilde;amos durante el inicio y todo el proceso de maduraci&oacute;n y consolidaci&oacute;n con consultores expertos; te brindamos el mejor programa de capacitac&oacute;n para gerentes y asesores inmobiliarios, para que incursiones en el negocio inmobiliario con la mejor formaci&oacute;n acad&eeacute;emica; te ofrecemos la m&aacute;s vanguardista tecnolog&iacute;a inmobiliaria para que controles tu gesti&oacute;n y para &oacute;ptimo manejode tus clientes y propiedades; y adem&aacute;s <b>desde el primer dia cuentas con una cartera de m&aacute;s de 3.500 propiedades captadas en exclusiva.</b>   
        </td>
    </tr>   <tr>
        <td style='background:#2B2B2B;text-align:center;padding:10px;color:#fff'>
            <div style='width:100%;color:yellow;font-size:1.4em'>
                La inversi&oacute;n en la franquicia incluye;
            </div>
            <div style='width:50%;float:left;text-align:left'>
                <ul>
                    <li>Uso de la marca por 5 a&ntilde;os</li>
                    <li>Licencias de nuestro sistema para los asesores durante 5 a&ntilde;os</li>
                    <li>Kit de arranque</li>
                    <li>Atuendos de carrera</li>
                    
                </ul>
            </div>
            <div style='width:50%;float:left;text-align:left'>
                <ul>
                    <li>Afiches digitales y arte de r&oacute;tulos</li>
                    <li>Capacitaci&oacute;n gerencial</li>
                    <li>Consultor&iacute;a de arranque y operacional</li>
                    <li>Gastos de notar&iacute;a</li>
                    
                </ul>
            </div>
        </td>
    </tr>
    <tr>
        <td style='text-align:center;color:yellow;font-size:2em'>
            Reserva tu cita en linea
        </td>
    </tr>
    <tr>
        <td style='background:#2B2B2B; text-align:center; font-size:1.3em;color:#fff'>
            Llamanos porque estamos dispuestos a ayudarte:<br>
            <span style='font-size:1.5em'>0212-953.49.50</span><br>
            <span style='font-size:1.5em'>0424-208.28.40</span>
        </td>
    </tr>
</table>"""




class ContactoCreateView(CreateView):
    form_class = ContactoForm
    template_name = "crearContacto.html"
    success_url="/contacto/"
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(ContactoCreateView, self).dispatch(*args, **kwargs)
    def post(self,request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            try:
                contacto = Contacto.objects.get(email=form.cleaned_data['email'])
                msj='existeEmail'
                return HttpResponse(msj)
            except ObjectDoesNotExist:
                form.save()
                titulo = 'century21.com.ve email de contacto'
                msj = 'Saludos Gracias por utilizar los servicios de century 21'
                html = mensage
                EnviarEmailDef.apply_async((titulo,msj, html, form.cleaned_data['email']),countdown=10)
                return HttpResponse('ok')
        return super(ContactoCreateView, self).post(request,*args, **kwargs)


class ContactoUpdateView(UpdateView):
    model = Contacto
    form_class = ContactoForm
    template_name = "editarContacto.html"
    success_url="/contacto/"
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(ContactoUpdateView, self).dispatch(*args, **kwargs)
    def post(self,request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            try:
                contacto = Contacto.objects.get(pk=form.cleaned_data['id'])
                contacto.nombre = form.cleaned_data['nombre']
                contacto.apellido = form.cleaned_data['apellido']
                contacto.email = form.cleaned_data['email']
                contacto.telefono = form.cleaned_data['telefono']
                contacto.fuente = form.cleaned_data['fuente']
                contacto.save()
                return HttpResponse('ok')
            except ObjectDoesNotExist:
                return HttpResponse('NoExiste')
        return super(ContactoUpdateView, self).post(request,*args, **kwargs)


class ContactoDeleteView(DeleteView):
    model = Contacto
    success_url = "/contacto/"
    template_name = "listContactos.html"
    def delete(self, request, *args, **kwargs):
        print "xcfcz"
        if request.is_ajax():
            contacto = Contacto.objects.get(pk=request.POST['pk'])
            contacto.delete()
            return HttpResponse('ok')
        else:
            raise Http404
class ListContactosView(ListView):
    model = Contacto
    template_name = 'listContactos.html'
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(ListContactosView, self).dispatch(*args, **kwargs)

@task
def EnviarEmailDef(titulo,msj,html,email):
	subject, from_email, to = titulo, 'noreply@almorir.me', email 
	msg = EmailMultiAlternatives(subject, msj, from_email, [to])
	msg.attach_alternative(html, "text/html")
	msg.send()