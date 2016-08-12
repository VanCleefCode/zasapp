from django.conf.urls import patterns, include, url
from .views import *


urlpatterns = [
    url(r'^login/$', LoginDef, name="login" ),
    url(r'^crear-usuario/$', UsuarioCreateView.as_view(), name="UsuarioCreateView" ),
    url(r'^editar-usuario/(?P<pk>[\w-]+)/$', UsuarioUpdateView.as_view(), name="UsuarioUpdateView" ),
    url(r'^$', ListUsuariosView.as_view(), name="ListUsuariosView" ),


]