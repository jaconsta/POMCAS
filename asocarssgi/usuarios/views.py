#-*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

from django import forms

class loginform(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

def newuser(request):
    return HttpResponse("Lo sentimos <br /> Favor solicitar la creación del usuario con el administrador")

def loginuser(request):
    error = ''
    form = loginform()
    if request.method == 'POST':
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username = username, password = password)
        if user is not None:
	    if user.is_active:
		login(request, user)
		#Success page
		return HttpResponseRedirect('/')
	    else:
		#Disabled account
		error = 'La cuenta se encuentra deshabilitada.'
	else:
	#Invalid login
	    error = 'Usuario y/o clave incorrectos'
    else:
	form = loginform()
    return render_to_response('login.html', {'form':form, 'error': error}, context_instance = RequestContext(request))

def logoutuser(request):
    logout(request)
    return HttpResponseRedirect('/')
