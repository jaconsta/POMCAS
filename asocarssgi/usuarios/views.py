#-*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from django import forms

from asocarssgi import default_names

from corporacion.views import GetUserCorpo

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
		return HttpResponseRedirect(reverse('cargando'))
	    else:
		#Disabled account
		error = 'La cuenta se encuentra deshabilitada.'
	else:
	#Invalid login
	    error = 'Usuario y/o clave incorrectos'
    else:
	form = loginform()
    return render_to_response(('login.html'), {'form':form, 'error': error}, context_instance = RequestContext(request))

def logoutuser(request):
    logout(request)
    return HttpResponseRedirect(reverse('cargando'))#'%s' %(default_names.SUB_SITE))

#@login_required(login_url = ('%slogin/' %(default_names.SUB_SITE)))
def infouser(request):
    '''
    By now, It'll do nothing
    '''
    #return matrixlist(request)
    return render(request, 'main.html', {
        'usr': request.user,
    })

@login_required(login_url = ('%slogin/' %(default_names.SUB_SITE)))
def matrixlist(request):
    '''
    Shows all matrix avaliable in the system for all users
    Creates an array of objects, each one listing the matrix name,
        url compliment, and order. Then return it.
    This is a partially hardcoded way but editable in the views.
    This way it's easily iterable in the template
    '''
    class defmatrix:
        def __init__(self, matrix, url, prio, url_args=None):
            self.matrix = matrix
            self.url = url
            self.prio = prio
            if url_args:
                self.url_args = url_args

    matrix_list = [   
        [u'matriz de diagnostico institucional', 'matrix_upload', 1, 'institucional'],
        [u'matriz de cartografia base', 'matrix_upload', 2, 'cartografica'],
        [u'matriz de caracterizacion de informacion disponible', 
            'matrix_infoident_cuencas', 3],
    ]
    matrices = []
    for i in matrix_list:
        try:
            a = defmatrix(i[0], i[1], i[2], i[3])
        except IndexError:
            a = defmatrix(i[0], i[1], i[2])
        matrices.append(a)

    corporas = GetUserCorpo(request.user)
    return render(request, 'list_matrices.html',{
        'usr' : request.user, 
        'corporas' : corporas,
        'matrices' : matrices,
    })
