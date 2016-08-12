from django.conf.urls import patterns, include, url
from .views import *


urlpatterns = [
    url(r'^crear-presupuesto/$', CrearPresupuestoView.as_view(), name="CrearPresupuestoView" ),
    # url(r'^editar-producto/(?P<pk>[\w-]+)/$', EditarProductoView.as_view(), name="EditarProductoView" ),
    # url(r'^$', ListProductosView.as_view(), name="ListProductosView" ),
    # url(r'^crear-template/$', AgergarTemplate, name="AgergarTemplate" ),

]