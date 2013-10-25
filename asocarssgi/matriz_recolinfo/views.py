# -*- coding: utf-8 -*-
from matriz_recolinfo.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect

import xlrd

from corporacion.models import corporaname
from cuencas.models import cuencompart, cuencadescr
from asocarssgi import default_names

def SetComponentesFile(text_addr):
    source = file.open(text_addr, 'r+')
    return False

def SetComponentesExcel(excel_addr):
    '''
    Must be on the first sheet
    '''
    def SetComponentes(compo, padr):
        component = componentes(
            componen = compo,
            comppadr = padr,
        )
        component.save()
        return component

    def SetActividades(compo, padr, valida):
        activity = compoactivi(
            compoact = padr,
            coacdesc = compo,
        )
        activity.save()
    firstval = componentes.objects.get(pk=1)
    componen = 0 #componentes.objects.get(id=1)
    subcompo = 0

    excel_file = xlrd.open_workbook(excel_addr)
    excel_sheet = excel_file.sheet_by_index(0)
    
    for rowini in range(excel_sheet.nrows):
        #Componente
        colcompo = excel_sheet.cell_value(colx = 0, rowx = rowini)
        if colcompo:
            componen = SetComponentes(colcompo, firstval)
        #SubComponente
        colsubco = excel_sheet.cell_value(colx = 1, rowx = rowini)
        if colsubco:
            subcompo = SetComponentes(colsubco, componen)
        #Actividad
        coltipoi = excel_sheet.cell_value(colx = 2, rowx = rowini)
        colvalid = excel_sheet.cell_value(colx = 3, rowx = rowini)
        SetActividades(coltipoi, subcompo, colvalid) 

def GetCuencasAsoc(request):
    #Get User
    user = request.user
    #Get corporation associated with that user
    # Assuming that one user has only one corporation
    corpora = corporaname.objects.get(corpousr = user)
    #Get Watershed
    watershed = cuencompart.objects.filter(cuencomp = corpora)
    return user, corpora, watershed

@login_required(login_url = ('%slogin/' %(default_names.SUB_SITE)))
def CuencasDeCorpo(request):
    usr, corpo, watersheeds = GetCuencasAsoc(request)
    return render(request, 'list_cuencas.html', {
        'usr' : usr, 'corpo': corpo, 'watersheed': watersheeds,
    }) 

@login_required(login_url = ('%slogin/' %(default_names.SUB_SITE)))
def recolinfo_form(request, shared_id):
    def GetComponentes():
        comp = componentes.objects.filter(comppadr = 1)
        infor = []
        a = []
        for i in comp:
            subcomp = componentes.objects.filter(comppadr = i)
            b = []
            for j in subcomp:
                activ = compoactivi.objects.filter(compoact = j)
                b.append([j, activ])
            a.append([i, b])
        
        return a
        return componentes.objects.all()
    def GetActividades():
        return compoactivi.objects.all()
    if request.method == 'POST':
        form = CompoInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('formulario_completo.html')
    else:
        usr, corpo, watersheeds = GetCuencasAsoc(request)
        watersheed = cuencadescr.objects.get(id = shared_id)
        form = CompoInfoForm()
        componenetes = GetComponentes():

        return render(request, 'recoleccion_info.html', {
            'form' : form, 'usr':usr, 'corporation' : corpo,
            'watersheed' : watersheed,
        })
