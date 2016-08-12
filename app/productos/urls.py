from django.conf.urls import patterns, include, url
from .views import *


urlpatterns = [
    url(r'^crear-producto/$', CrearProductoView.as_view(), name="CrearProductoView" ),
    url(r'^editar-producto/(?P<pk>[\w-]+)/$', EditarProductoView.as_view(), name="EditarProductoView" ),
    url(r'^$', ListProductosView.as_view(), name="ListProductosView" ),
    url(r'^traer/$', TraerTemplate.as_view(), name="TraerTemplate" ),
    url(r'^crear-template/$', AgergarTemplate, name="AgergarTemplate" ),

]