from django.conf.urls import patterns, include, url
from .views import *


urlpatterns = [
    #url(r'^add/$', AddContactView.as_view(), name="AddContactView" ),
    url(r'^crear/$', ContactoCreateView.as_view(), name="ContactoCreateView" ),
    url(r'^editar-contacto/(?P<pk>[\w-]+)/$', ContactoUpdateView.as_view(), name="ContactoUpdateView" ),
    url(r'^eliminar-contacto/(?P<pk>[\w-]+)/$', ContactoDeleteView.as_view(), name="ContactoDeleteView" ),
    #url(r'^crear/$', CrearContactoDef, name="CrearCopntactoDef" ),
    url(r'^$', ListContactosView.as_view(), name="ListContactosView" ),

]