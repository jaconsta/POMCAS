#-*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

import xlrd

from asocarssgi import default_names
from .forms import UploadFileForm
from .models import *

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

def excel_store(upfile):
    '''
    I think it s better to first store the  file
    '''
    name = upfile.name
    with open('/home/pomcas/Matrix_loaded/%s'%(name), 'wb') as destination:      #('/tmp/%s'%(name), 'wb') as destination:
        for chunk in upfile.chunks():
            destination.write(chunk)
    return name

def soporte_store(upfile):
    '''

    '''
    name = upfile.name
    with open('/home/pomcas/Matrix_loaded/%s'%(name), 'wb') as destination:      #('/tmp/%s'%(name), 'wb') as destination:
    	destination.write(upfile.read())
    return

def excel_process(upfile):
    '''
    And after being stored, read and process it.
    '''
    matrix = '/home/pomcas/Matrix_loaded/%s'%(upfile)    #'/tmp/%s'%(upfile)
    book = xlrd.open_workbook(matrix)
    print book.sheet_by_index(1).name
    return

@login_required(login_url = ('%slogin/' %(default_names.SUB_SITE)))
def upload_matrix(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            #handle_uploaded_file(request.FILES['file'])
            theexcel = excel_store(request.FILES['archivo'])
            soporte_store(request.FILES['soportes'])
            excel_process(theexcel)
            return render_to_response('matriz_recibida.html') #HttpResponseRedirect('/matrix/institucional/success/')
    else:
        form = UploadFileForm()
    return render_to_response('matrix_institucional.html', {'form':form}, context_instance = RequestContext(request))
