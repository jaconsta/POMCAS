#-*- coding: utf-8 -*-
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from asocarssgi import default_names
from .forms import UploadFileForm, UploadMCartogForm
from .models import *

@login_required(login_url = ('%slogin/' %(default_names.SUB_SITE)))
def modelo(request):
    if request.method == 'POST':
        error = ''
        form = UploadMCartogForm(request.POST, request.FILES)
        if form.is_valid():
            #Parse Matrix name
            arch_name = request.FILES['archivo'].name
            arch_name = arch_name.split('.')
            arch_ext = arch_name[-1] #File Extension
            arch_name_p = arch_name[0].split('_') #File name components
            if len(arch_name_p) != 5:
                error += 'El nombre de archivo no parece correcto'
            elif arch_ext not in ['xls', 'xlsx']:
                error += 'La extensión del archivo debe ser un archivo de Excel'
            #Upload The Matrix
            try:
                max_id = archivosb.objects.all().order_by("-id")[0].id
            except IndexError:
                max_id = 0
            archives = request.FILES['archivo']
            nombre = archives.name
            archives.name = '%d.%s'%((max_id+1), arch_ext)
            creado = archivosb(
                archnomb = 'MATRIZ_CARTOGRAFICA',
                archubic = archives,
                archuser = request.user,
                archorna = nombre#request.FILES['archivo'].name,
                archesta = 'REC'
            )
            creado.save()
            return render_to_response('matriz_recibida.html', {'errors': error}) 
    else: 
        form = UploadMCartogForm()
    return render_to_response('cargue_archivos.html', {'form':form}, context_instance =RequestContext(request))

#    if request.method == 'POST':
#        error = ''
#        form = UploadFileForm(request.POST, request.FILES)
#        if form.is_valid():
#            #Parse Matrix name
#            arch_name = request.FILES['archivo'].name
#            arch_name = arch_name.split('.')
#            arch_ext = arch_name[-1] #File Extension
#            arch_name_p = arch_name[0].split('_') #File name components
#            if len(arch_name_p) != 6:
#                error += 'El nombre de archivo no parece correcto'
#            elif arch_ext not in ['xls', 'xlsx']:
#                error += 'La extensión del archivo debe ser un archivo de Excel'
#            #Parse attached files
#            sop_name = request.FILES['soportes'].name
#            sop_name= sop_name.split('.')
#            sop_ext = sop_name[-1] #File Extension
#            sop_name_p = sop_name[0].split('_') #File name components
#            if len(sop_name_p) != 6:
#                error += 'El nombre de archivo no parece correcto'
#            elif sop_ext not in ['rar', 'zip']:
#                error += 'La extensión del archivo debe ser un archivo de rar o ip'
#            #Upload The Matrix
#            try:
#                max_id = archivosb.objects.all().order_by("-id")[0].id
#            except IndexError:
#                max_id = 0
#            archives = request.FILES['archivo']
#            archives.name = '%d.%s'%((max_id+1), arch_ext)
#            creado = archivosb(
#                archnomb = 'MATRIZ_INSTITUCIONAL',
#                archubic = archives,
#                archuser = request.user,
#                archorna = request.FILES['archivo'].name,
#                archesta = 'REC'
#            )
#            attacheds = request.FILES['soportes']
#            attacheds.name = '%d.%s'%((max_id+2), sop_ext)
#            creadodos = archivosb(
#                archnomb = 'MATRIZ_INSTITUCIONAL_SOP',
#                archubic = attacheds,
#                archuser = request.user,
#                archorna = request.FILES['soportes'].name,
#                archesta = 'REC'
#            )
#            #if creado.is_valid():
#            creado.save()
#            #else: 
#            #error = 'Hay errores en la matriz'
#            #if creadodos.is_valid():
#            creadodos.save()
#            #else: 
#            #error = 'Hay errores en los soportes'
#            #form.save()
#            return render_to_response('matriz_recibida.html', {'errors': error}) #HttpResponseRedirect('/proyecto85/b')
#    else: 
#        form = UploadFileForm()
#    return render_to_response('cargue_archivos.html', {'form':form}, context_instance =RequestContext(request))
#    if request.method == 'POST':
#        error = ''
#        form = UploadFileForm(request.POST, request.FILES)
#        if form.is_valid():
#            #Parse Matrix name
#            arch_name = request.FILES['archivo'].name
#            arch_name = arch_name.split('.')
#            arch_ext = arch_name[-1] #File Extension
#            arch_name_p = arch_name[0].split('_') #File name components
#            if len(arch_name_p) != 6:
#                error += 'El nombre de archivo no parece correcto'
#            elif arch_ext not in ['xls', 'xlsx']:
#                error += 'La extensión del archivo debe ser un archivo de Excel'
#            #Parse attached files
#            sop_name = request.FILES['soportes'].name
#            sop_name= sop_name.split('.')
#            sop_ext = sop_name[-1] #File Extension
#            sop_name_p = sop_name[0].split('_') #File name components
#            if len(sop_name_p) != 6:
#                error += 'El nombre de archivo no parece correcto'
#            elif sop_ext not in ['rar', 'zip']:
#                error += 'La extensión del archivo debe ser un archivo de rar o ip'
#            #Upload The Matrix
#            try:
#                max_id = archivosb.objects.all().order_by("-id")[0].id
#            except IndexError:
#                max_id = 0
#            archives = request.FILES['archivo']
#            archives.name = '%d.%s'%((max_id+1), arch_ext)
#            creado = archivosb(
#                archnomb = 'MATRIZ_INSTITUCIONAL',
#                archubic = archives,
#                archuser = request.user,
#                archorna = request.FILES['archivo'].name,
#                archesta = 'REC'
#            )
#            attacheds = request.FILES['soportes']
#            attacheds.name = '%d.%s'%((max_id+2), sop_ext)
#            creadodos = archivosb(
#                archnomb = 'MATRIZ_INSTITUCIONAL_SOP',
#                archubic = attacheds,
#                archuser = request.user,
#                archorna = request.FILES['soportes'].name,
#                archesta = 'REC'
#            )
#            #if creado.is_valid():
#            creado.save()
#            #else: 
#            #error = 'Hay errores en la matriz'
#            #if creadodos.is_valid():
#            creadodos.save()
#            #else: 
#            #error = 'Hay errores en los soportes'
#            #form.save()
#            return render_to_response('matriz_recibida.html', {'errors': error}) #HttpResponseRedirect('/proyecto85/b')
#    else: 
#        form = UploadFileForm()
#    return render_to_response('cargue_archivos.html', {'form':form}, context_instance =RequestContext(request))
#        
