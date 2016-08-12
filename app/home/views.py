# -*- encoding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect,HttpResponseRedirect
from django.views.generic import TemplateView
from django.template import RequestContext
from django.http import Http404
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login

# Create your views here.
class HomeView(TemplateView):
	template_name="index.html"
	def get(self, request, *args, **kwargs):
		if	request.user.id is None:
			return super(HomeView, self).get(request, *args, **kwargs)
		else: 
			return redirect('/app/')
