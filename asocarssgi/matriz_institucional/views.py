#-*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

import xlrd

from .forms import UploadFileForm
from .models import *

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

def excel_store(upfile):
    '''
    I think it s better to first store the  file
    '''
    name = upfile.name
    with open('/tmp/%s'%(name), 'wb') as destination:
        for chunk in upfile.chunks():
            destination.write(chunk)
    return name

def excel_process(upfile):
    '''
    And after being stored, read and process it.
    '''
    matrix = '/tmp/%s'%(upfile)
    book = xlrd.open_workbook(matrix)
    print book.sheet_by_index(1).name
    return

def upload_matrix(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            #handle_uploaded_file(request.FILES['file'])
            theexcel = excel_store(request.FILES['file'])
            excel_process(theexcel)
            return HttpResponseRedirect('/matrix/institucional/success/')
    else:
        form = UploadFileForm()
    return render_to_response('matrix_institucional.html', {'form':form}, context_instance = RequestContext(request))
