from django.conf.urls import patterns, include, url
from .views import *


urlpatterns = [
    url(r'^/$', ListCitasView.as_view(), name="ListCitasView" ),
    url(r'^crear-cita/$', CitaCreateView.as_view(), name="CitaCreateView" ),
    url(r'^lista-cita/(?P<dia>[a-zA-Z0-9-]+)/$', CitasTemplateView.as_view(), name="CitasTemplateView" ),
    url(r'^eliminar-cita/(?P<pk>[\w-]+)/$', CitaDeleteView.as_view(), name="CitaDeleteView" ),
    url(r'^$', ListCitasView.as_view(), name="ListCitasView" ),

]