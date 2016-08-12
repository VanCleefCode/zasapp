# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, render_to_response, HttpResponse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import  PasswordChangeForm
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from user_profile.models import UserProfile
from django.contrib.auth.hashers import make_password

#CONTAR REGISTROS
#from django.db.models import Count
#co =  User.objects.annotate(cont = Count('pk'))
#print co[0].cont




from .forms import *

class IndexView(TemplateView):
    template_name='menu.html'
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)


def LoginDef(request):
    if request.POST:
        username = request.POST.get('usuario')
        password = request.POST.get('clave')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('ok')
            else:
                return HttpResponse('Cuante Inactiva')
        else:
            return HttpResponse('Usuario o password incorrectos') 
    else:
        raise Http404






class UsuarioCreateView(CreateView):
    form_class = UsuarioForm
    template_name = "crearUsuario.html"
    success_url="/usuario/"
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        usuario = User.objects.get(pk=1)
        return super(UsuarioCreateView, self).dispatch(*args, **kwargs)
    def post(self,request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            try:
                usuario = User.objects.get(email=form.cleaned_data['email'])
                msj='existeEmail'
                return HttpResponse(msj)
            except ObjectDoesNotExist:
                form.save()
                user = User.objects.get(username=form.cleaned_data['username'])
                profile  = UserProfile.objects.create(user_id=user.id,tipo=form.cleaned_data['tipo'],telefono=form.cleaned_data['telefono'])
                profile.save()
                if form.cleaned_data['tipo'] in 'Sistemas':
                    print "admin"
                    user.is_staff = True
                    user.is_admin = True 
                    user.is_superuser = True 
                user.password = make_password('1234')    
                user.save()
                return HttpResponse('ok')
        return super(UsuarioCreateView, self).post(request,*args, **kwargs)




class ListUsuariosView(ListView):
    model = User
    template_name = 'listarUsuarios.html'
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(ListUsuariosView, self).dispatch(*args, **kwargs)




class UsuarioUpdateView(UpdateView):
    model = User
    form_class = UsuarioForm
    template_name = "editarUsuario.html"
    success_url="/usuario/"
    def telefono(self,*args,**kwargs):
        p = UserProfile.objects.get(user_id=self.kwargs['pk'])
        return p.telefono
    def tipo(self,*args,**kwargs):
        p = UserProfile.objects.get(user_id=self.kwargs['pk'])
        return p.tipo

    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(UsuarioUpdateView, self).dispatch(*args, **kwargs)
    def post(self,request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if request.is_ajax():
            try:
                usuario = User.objects.get(pk=request.POST['id'])
                usuario.nombre = request.POST['first_name']
                usuario.apellido = request.POST['last_name']
                usuario.email = request.POST['email']
                p = UserProfile.objects.get(user_id=request.POST['id'])
                p.telefono = request.POST['telefono']
                p.tipo = request.POST['tipo']
                usuario.save()
                p.save()
                return HttpResponse('ok')
            except ObjectDoesNotExist:
                return HttpResponse('NoExiste')
        return super(UsuarioUpdateView, self).post(request,*args, **kwargs)



def RegistroDef(request):
    if request.is_ajax():
        Rname = request.POST.get('Rname')
        Rusername = request.POST.get('Rusername')
        Remail = request.POST.get('Remail')
        Rpassword = request.POST.get('Rpassword')
        try:
            user = User.objects.get(username=Rusername)
            msj='existeUser'
            return HttpResponse(msj)            
        except ObjectDoesNotExist:
            try:
                user = User.objects.get(email=Remail)
                msj='existeEmail'
                return HttpResponse(msj)
            except ObjectDoesNotExist:
                pass
            # E instanciamos un objeto User, con el username y password
            user_model = User.objects.create_user(username=Rusername, password=Rpassword)
            # Añadimos el email
            user_model.email = Remail
            user_model.first_name= Rname
            # Y guardamos el objeto, esto guardara los datos en la db.
            user_model.save()
            # Ahora, creamos un objeto UserProfile, aunque no haya incluido
            # una imagen, ya quedara la referencia creada en la db.
            user_profile = UserProfile()
            # Al campo user le asignamos el objeto user_model
            user_profile.user = user_model
            # y le asignamos la photo (el campo, permite datos null)
            #user_profile.photo = photo
            # Por ultimo, guardamos tambien el objeto UserProfile
            user_profile.save()
        
            user = authenticate(username=Rusername, password=Rpassword)
            AsignarDef(user.id)
            titulo = 'Almorir.me verficacion de email'
            msj = 'Saludos Gracias por utilizar los servicios de mensajeria post mortem de Almorir.me, en este momento su emnil no esta verificado de click en esiguente vinculo para verficar su email: Verificar email en Almorir.me  El equipo de radiowebdigital.com Gracias'
            html = '<table style="width:600px;margin:auto"> <tr><td align="center" style="text-align:center;"><img src="http://almorir.me/static/img/logo250.png" alt="">      </td>   </tr>   <tr>        <td style="background:#ccc">            <p style="width:80%;margin:auto;padding:20px;font-size:1.5em;"> <b>Saludos</b><br> Gracias por utilizar los servicios de mensajería post mortem de <a href="http://almorir.me"> Almorir.me</a>, en este momento su <b>email no esta verificado</b> visite el siguiente enlace para verificar su email: <br> <br><a href="http://almorir.me/verificar-email/' + str(request.user.id) + '/">Verificar email en Almorir.me</a> <br><br>  El equipo de <b>Almorir.me</b> Gracias         </p>        </td>   </tr></table>'
            EnviarEmailDef.apply_async((titulo,msj, html, Remail),countdown=10)
            login(request, user)
            return HttpResponse('ok')
    else:
        raise Http404

def CheckUserDef(request,username):
    if request.is_ajax():
        try:
            user = User.objects.get(username=username)
            return HttpResponse('existeUser')
        except ObjectDoesNotExist:
            return HttpResponse('ok')
    raise Http404
   
def CheckEmailDef(request,email):
    if request.is_ajax():
        try:

            user = User.objects.get(email=email)
            return HttpResponse('existeEmail')
        except ObjectDoesNotExist:
            return HttpResponse('ok')

    raise Http404
   




@login_required(login_url='/oops/')
def account(request):
    name_message = password_message = email_message = ''
    change_name_form = ChangeNameForm(data=request.POST or None, instance=request.user)
    change_password_form = PasswordChangeForm(data=request.POST or None, user = request.user)
    change_email_form = ChangeEmailForm(data=request.POST or None, instance=request.user)
    if request.method == "POST":
    	if "change_name" in request.POST:
    		change_name_form = ChangeNameForm(data=request.POST, instance=request.user)
    		if change_name_form.is_valid():
    			change_name_form.save()
    			name_message = 'Se ha cambiado el nombre satisfactoriamente.'
    	else:
    		change_name_form = ChangeNameForm(instance=request.user)

    	if "change_password" in request.POST:
    		change_password_form = PasswordChangeForm(user=request.user)
    		if change_password_form.is_valid():
    			change_password_form.save()        
    			password_message = 'Your password has been changed.'
    	else:
    		change_password_form = PasswordChangeForm(user=request.user)

    	if "change_email" in request.POST:
    		change_email_form = ChangeEmailForm(request.POST, instance=request.user)
    		if change_email_form.is_valid():
    			change_email_form.save()
    			email_message = 'El Email se ha cambiado satisfactoriamente.'
    	else:
    		change_email_form = ChangeEmailForm(instance=request.user)
    return render_to_response('account.html', 
                       {'change_name_form': change_name_form,
                        'change_email_form': change_email_form, 
                        'change_password_form': change_password_form,
                        'password_message': password_message,
                        'name_message': name_message,
                        'email_message': email_message,}, 
                        context_instance=RequestContext(request))