"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import  url, include, handler400, handler403, handler404, handler500
from django.contrib import admin
from home.views import HomeView
from user_profile.views import IndexView

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import logout


def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response

def LogoutDef(request):
    logout(request)
    return redirect('/')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view() , name='home'),
    url(r'^app/$', IndexView.as_view() , name='index'),
    url(r'^usuario/', include('user_profile.urls')),
    url(r'^producto/', include('productos.urls')),
    url(r'^clientes/', include('clientes.urls')),
    url(r'^presupuestos/', include('presupuestos.urls')),
    url(r'^logout/', LogoutDef, name="logout" ),

]
