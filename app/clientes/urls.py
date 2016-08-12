from django.conf.urls import patterns, include, url
from .views import *


urlpatterns = [
    url(r'^$', ClientesListView.as_view(), name="listcliente" ),
    url(r'^crear-cliente/$', ClienteCreateView.as_view(), name="ClienteCreateView" ),
    url(r'^editar-cliente/(?P<pk>[\w-]+)/$', EditarClienteView.as_view(), name="EditarClienteView" ),
    url(r'^buscarCliente/$', buscarCliente.as_view(), name="buscarCliente" ),


]