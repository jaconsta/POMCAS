#-*- coding: utf-8 -*-
import re

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from asocarssgi import default_names
from .forms import UploadFileForm, UploadMCartogForm
from .models import *

def ValidFileName(filename, matrix, exten):
    #REGEX1: CTO85_\d{4}\d{1,2}\d{1,2}_MATRIZ_%s_(?P<corpora>\w+).(?P<fileext>\w{3,4})
    #REGEX2: CTO85_(?<year>20[1-9]\d)(?<month>0?[1-9]|1[012])(?<day>0?[1-9]|[12]\d|3[01])_MATRIZ_%s_(?<corpora>\w+).(?<fileext>\w{3,4})
    pattern = re.compile('CTO85_(?<year>20[1-9]\d)(?<month>0?[1-9]|1[012])(?<day>0?[1-9]|[12]\d|3[01])_MATRIZ_%s_(?<corpora>\w+).(?<fileext>\w{3,4})'%(matrix))
    match = pattern.match(pattern, filename)
    if not match:
        output = (u'El nombre de archivo (%s) no es correcto \n'%(filename))
        return (False, output)
    elif match(fileext) not in exten:
        output = (u'La extensión de archivo (%s) no es correcta \n'%(fileext))
        output += (u'Se esperaba %s'%(exten))
        return (False, output)
    output = fileext
    return (True, output)

def FileInTail(request, matrix):
    '''
    Returns False if there is the user has already uploaded a file.
    Pending to process or processed and approved
    '''
    if archivosb.objects.filter(
            archnomb = matrix, 
            archuser = request.user,
            archesta__in = ['REC', 'APR']
        ).count() == 0:
        return False
    return True

def SetFile(matrix, upfile):
    try:
        max_id = archivosb.objects.all().order_by("-id")[0].id
    except IndexError:
        max_id = 0

    name = upfile.name
    upfile.name = '%d.%s'%((max_id+1), sop_ext)
    loaded = archivosb(
        archnomb = matrix,
        archubic = upfile,
        archuser = request.user,
        archorna = name,
        archesta = 'REC'
    )
    loaded.save()
    return loaded

def GetExcelExt():
    return ['xls', 'xlsx']

def GetComprExt():
    return ['rar', 'zip', 'tar', 'tar.gz', '7z']

@login_required(login_url = ('%slogin/' %(default_names.SUB_SITE)))
def RecolCartografic(request):
    title = u'Matriz de Cartografía Básica'
    if not FileInTail(request, 'MATRIZ_CARTOGRAFICA'):
        message = u'Ya ha realizado el cargue de esta matriz'
        return render_to_response('matriz_recibida.html', {
            'errors': message})
    if request.method == 'POST':
        error = ''
        form = UploadMCartogForm(request.POST, request.FILES)
        if form.is_valid():
            #Parse Matrix name
            arch_name = request.FILES['archivo'].name
            [parsed, message] = ValidFileName(arch_name, 'CARTOGRAFICA', 
                GetExcelExt())
            if not parsed:
                return render_to_response('matriz_recibida.html', {
                    'errors': message})

            #Upload The Matrix
            SetFile('MATRIZ_CARTOGRAFICA', request.FILES['archivo'])
            return render_to_response('matriz_recibida.html', {'errors': error}) 
    else: 
        form = UploadMCartogForm()
        title = u'Matriz de Cartografía básica'
    return render_to_response('cargue_archivos.html', {
        'form':form, 'title': title}, 
        context_instance = RequestContext(request))

@login_required(login_url = ('%slogin/' %(default_names.SUB_SITE)))
def RecolInstitucional(request):
    title = u'Matriz de Diagnóstico institucional'
    if not FileInTail(request, 'MARTIZ_INSTITUCIONAL'):
        message = u'Ya ha realizado el cargue de esta matriz'
        return render_to_response('matriz_recibida.html', {
            'title': title, 'errors': message})
    if request.method == 'POST':
        error = ''
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            #Parse Matrix name
            arch_name = request.FILES['archivo'].name
            [parsed, message] = ValidFileName(arch_name, 'INSTITUCIONAL', 
                GetExcelExt())
            error += message
            if not parsed:
                return render_to_response('matriz_recibida.html', {
                    'errors': message}) #HttpResponseRedirect('/proyecto85/b')
            arch_ext = message
            #Parse attached files
            sop_name = request.FILES['soportes'].name
            [parsed, message] = ValidFileName(sop_name, 
                'INSTITUCIONAL_SOPORTES', GetComprExt())
            error += message
            if not parsed:
                return render_to_response('matriz_recibida.html', {
                    'errors': message})
            sop_ext = message
            #Upload The Matrices
            SetFile('MATRIZ_INSTITUCIONAL', request.FILES['archivo'])
            SetFile('MATRIZ_INSTITUCIONAL_SOP', request.FILES['soportes'])
            return render_to_response('matriz_recibida.html', {'errors': error})
    else: 
        form = UploadFileForm()
    return render_to_response('cargue_archivos.html', {
        'form':form, 'title':title}, 
        context_instance =RequestContext(request))
