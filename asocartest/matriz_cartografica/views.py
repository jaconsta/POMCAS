#-*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

import xlrd
import datetime

from .models import *

def excel_process(filename):
    #Open file
    log = ''
    log += u'Inicio del proceso: %s\n'%(datetime.datetime.now())
    log += u'Se hará una validación rápida del archivo\n'
    excel_file = xlrd.open_workbook('/var/contrato85/matrix/%s'%(excel_addr))
    #Validate first sheet is ADQUIRIDA and open it
    if excel_file.sheet_names()[0]!= u'ADQUIRIDA':
        log += u'El orden de las pestañas no coincide o ha sido alterado: %s\n'%(excel_files.sheet_names()[0])
        log += u'El proceso no continúa'
    else:
        excel_sheet = excel_file.sheet_by_index(0)
    #Get User
    corporacion = excel_sheet.cell_value(colx =2, rowx =4)
    nit = excel_sheet.cell_value(colx =2, rowx =5)
    #Parse Matrix
    rowini = 9
    #Detect empty matrix
    if excel_sheet.cell_value(colx =1, rowx =rowini) == '':
        log += u'La matriz está vacía'
    else:
        while excel_sheet.cell_value(colx =1, rowx =rowini) != '':
            plancha = excel_sheet.cell_value(colx =1, rowx =rowini)
            formato = excel_sheet.cell_value(colx =2, rowx =rowini)
            escala = excel_sheet.cell_value(colx =3 rowx =rowini)
            fuente = excel_sheet.cell_value(colx =4, rowx =rowini)
            elaboracion = excel_sheet.cell_value(colx =5, rowx =rowini)
            #Valid Plancha
                
            #Valid Years
            if elaboracion < fuente:
                log += u'El año de elaboración (%s) no puede ser mayor a la fuente(%s)'%(fuente, elaboracion)
            #Valid Escala
            try:
                escala = int(escala)
            if len(plancha) == :
                try:
                    if int(escala) != 25000
                except ValueError:
                    log += 'Escala no es un número: %s\n'%(escala)
            try:
                int(planca)
