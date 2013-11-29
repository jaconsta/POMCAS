#-*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

import xlrd
import datetime

from .models import *

def safelog(log, usernam):
    usuario = User.objects.get(pk=usernam)
    logfile = open(u'/var/contrato85/logs/%s_cartog_v1.log'%(usuario.username), 'w')
    logfile.write(log.encode('UTF-8'))
    logfile.close()

def excel_process(excel_addr, username):
    #Open file
    log = ''
    log += u'Inicio del proceso: %s\n'%(datetime.datetime.now())
    log += u'Se hará una validación rápida del archivo\n'
    #excel_file = xlrd.open_workbook('/var/contrato85/matrix/%s'%(excel_addr))
    excel_file = xlrd.open_workbook('/var/contrato85/matrix/%s'%(excel_addr))
    #Validate first sheet is ADQUIRIDA and open it
    if excel_file.sheet_names()[0]!= u'ADQUIRIDA':
        log += u'El orden de las pestañas no coincide o ha sido alterado: %s\n'%(excel_files.sheet_names()[0])
        log += u'El proceso no continúa\n'
        print log
        safelog(log, username)
        return
    else:
        excel_sheet = excel_file.sheet_by_index(0)
    #Get User
    corporacion = excel_sheet.cell_value(colx =2, rowx =4)
    nit = excel_sheet.cell_value(colx =2, rowx =5)
    try:
        int(nit)
    except ValueError:
        log += u'El NIT no es un número\n'
    usuario = User.objects.get(pk=username)
    log += u'Corporación %s. NIT %s \n'%(corporacion, nit)
    #Parse Matrix
    rowini = 9
    #Detect empty matrix
    try :
        excel_sheet.cell_value(colx =1, rowx =rowini)
    except IndexError:
        log += u'La matriz está vacía\n'
    else:
        log += u'La matriz cuenta con %s registros\n'%(excel_sheet.nrows-(rowini+1))
        while excel_sheet.cell_value(colx =1, rowx =rowini) != '': 
            doprocess = True
            plancha = excel_sheet.cell_value(colx =1, rowx =rowini)
            formato = excel_sheet.cell_value(colx =2, rowx =rowini)
            escala = excel_sheet.cell_value(colx =3, rowx =rowini)
            fuente = excel_sheet.cell_value(colx =4, rowx =rowini)
            elaboracion = excel_sheet.cell_value(colx =5, rowx =rowini)
            #Valid Plancha 
            try:
                if '-' in str(plancha):
                    log += u'Formato no puede incluir guiones: %s\n'%(plancha) 
                    plancha = None
                    doprocess = False
            except UnicodeEncodeError:
                log += u'La celda es ilegible: %s \n'%(plancha)
                plancha = None
                doprocess = False
            #Is escala a number?
            try:
                int(escala)
            except ValueError:
                log += u'%s. La escala no es un número: %s\n'%(rowini, escala)
                doprocess = False
            #Valid Plancha
            #It's quite complex the validation then only a small validation 
            # for 10000 scale will be applied and will assume that others will be 25000
            if escala == 10000:
                try:
                    int(plancha[-1]) 
                except ValueError:
                    log += u'La escala especificada (%s) no coincide con la plancha (%s)\n'%(escala, plancha)
                    doprocess = False
            #Valid Formato
            if formato == '':
                log += u'%s. El formato no puede estar vacío'%(rowini)
            #Valid Years
            #First these fields can be blank or have a not number value
            valid = True
            try:
                int(fuente)
            except ValueError:
                log += u'El campo de Fecha de la fuente no es correcto: %s\n'%(fuente)
                fuente = None
                valid = False
            try:
                int(elaboracion)
            except ValueError:
                log += u'El campo de Fecha de elaboración no es correcto: %s\n'%(elaboracion)
                elaboracion = None
                valid = False
            if valid:
                if int(elaboracion) < int(fuente):
                    log += u'El año de fuente (%s) no puede ser mayor al de elaboración (%s) \n'%(fuente, elaboracion)
                    doprocess = False
            else: 
                log += u'No se pudo comprobar la relación de años \n'
            ##Valid Escala
            #try:
            #    escala = int(escala)
            #if len(plancha) == :
            #    try:
            #        if int(escala) != 25000
            #    except ValueError:
            #        log += 'Escala no es un número: %s\n'%(escala)
            #try:
            #    int(plancha)
            #Fill DB
            if doprocess:
                cartografia = cartoginven(
                    cartuser = usuario,
                    cartplan = plancha,
                    cartform = formato,
                    cartesca = escala,
                    cartfano = fuente,
                    carteano = elaboracion
                )
                cartografia.save()
            rowini += 1
            if rowini >= excel_sheet.nrows:
                break
    log += u'Fin del proceso: %s\n'%(datetime.datetime.now())
    print log
    safelog(log, username)

def excel_vone_process(excel_addr, username):
    #Open and start log file
    log = ''
    log += u'Inicio del proceso: %s\n'%(datetime.datetime.now())
    log += u'Se hará una validación rápida del archivo\n'
    excel_file = xlrd.open_workbook('/var/contrato85/matriz_cartogv0/%s'%(excel_addr))
    #Validate first sheet is ADQUIRIDA and open it
    if excel_file.sheet_names()[0]!= u'ADQUIRIDA':
        log += u'El orden de las pestañas no coincide o ha sido alterado: %s\n'%(excel_files.sheet_names()[0])
        log += u'El proceso no continúa\n'
        print log
        safelog(log, username)
        return
    else:
        excel_sheet = excel_file.sheet_by_index(0)
    #Get User
    corporacion = excel_sheet.cell_value(colx =6, rowx =7)
    usuario = User.objects.get(pk=username)
    log += u'Corporación %s. NIT\n'%(corporacion)
    #Parse Matrix
    rowini = 12
    #Detect empty matrix
    try :
        excel_sheet.cell_value(colx =1, rowx =rowini)
    except IndexError:
        log += u'La matriz está vacía\n'
    else:
        log += u'La matriz cuenta con %s registros\n'%(excel_sheet.nrows-(rowini+1))
        while excel_sheet.cell_value(colx =1, rowx =rowini) != '':
            doprocess = True
            plancha = excel_sheet.cell_value(colx =1, rowx =rowini)
            formato = excel_sheet.cell_value(colx =2, rowx =rowini)
            elaboracion = excel_sheet.cell_value(colx =3, rowx =rowini)
            #Valid Plancha
            try:
                if '-' in str(plancha):
                    log += u'Formato no puede incluir guiones: %s\n'%(plancha)
                    plancha = None
                    doprocess = False
            except UnicodeEncodeError:
                log += u'La celda es ilegible: %s \n'%(plancha)
                plancha = None
                doprocess = False
            if formato == '':
                log += u'%s. El formato no puede estar vacío'%(rowini)
            #Valid Years
            try:
                int(elaboracion)
            except ValueError:
                log += u'El campo de Fecha de elaboración no es correcto: %s\n'%(elaboracion)
                elaboracion = None
            if doprocess:
                cartografia = cartoginven(
                    cartuser = usuario,
                    cartplan = plancha,
                    cartform = formato,
                    cartesca = 25000,
                    carteano = elaboracion
                )
                cartografia.save()
            rowini += 1
            if rowini >= excel_sheet.nrows:
                break
    log += u'Fin del proceso: %s\n'%(datetime.datetime.now())
    print log
    safelog(log, username)

def arcgis_upl(arcgicsv):
    arcfile = open('/home/javier/apps/python/POMCAS/asocartest/static/csv/%s'%(arcgicsv), 'r')
    for line in arcfile:
        a = line.split(';')
        if a[1] == '':
            a[1] = None
        if a[5] == '':
            a[5] = None
        cartogra = cartonargis(
            planchav = a[0],
            objectid = a[1],
            estedosc = a[2],
            shapelen = a[3],
            shapeare = a[4],
            repetida = a[5],
            disponib = 'NO', #As I'll Update it
        )
        cartogra.save()

#def SetUserWithPlancha():
#    '''
#    WARNING
#    This does not use a cursor!
#    It can cause memory overwhelming or throw any arbitrary error.
#    Must be updated TODO
#    '''
#    for i in cartogiven.objects.all():
#        try:
#            
def SetClassifyInYears():
    '''
    WARNING
    This does not use a cursor!
    It can cause memory overwhelming or throw any arbitrary error.
    Must be updated TODO
    '''
    def SetPlanchaAnno(grid):
        years ={'yeafeigh': False, 'yeafnine': False,
                'yeaftwen': False, 'yeaftwte': False,
                'yeaeeigh': False, 'yeaenine': False,
                'yeaftwen': False, 'yeaetwte': False,
        }
        #Classify Fuente years
        if grid.cartfano == None:
            pass
        elif grid.cartfano < 1990:
            years['yeafeigh'] = True
        elif grid.cartfano >= 1990 and grid.cartfano < 2000:
            years['yeafnine'] = True
        elif grid.cartfano >= 2000 and grid.cartfano < 2010:
            years['yeaftwen'] = True
        elif grid.cartfano >= 2010:
            years['yeaftwte'] = True
        #Classify Elaborado years
        if grid.carteano == None:
            pass
        elif grid.carteano < 1990:
            years['yeaeeigh'] = True
        elif grid.carteano >= 1990 and grid.carteano < 2000:
            years['yeaenine'] = True
        elif grid.carteano >= 2000 and grid.carteano < 2010:
            years['yeaetwen'] = True
        elif grid.carteano >= 2010:
            years['yeaetwte'] = True
        #If plancha does not exists
        #TODO In the development version (1.7 I guess) theres an update_or_create function
        try:
            obj = nargisyearc.objects.get(archgrid = cartonargis.objects.get(planchav =grid.cartplan))#grid)#.cartplan)
            for key, value in years.iteritems():
                setattr(obj, key, value)
                obj.save()
        except nargisyearc.DoesNotExist:
            #Alterate years to adjust
            arcgis = cartonargis.objects.get(planchav =grid.cartplan)
            years.update({'archgrid':arcgis})
            obj = nargisyearc(**years)
            obj.save()

        #obj, created = nargisyearc.objects.get_or_create(archgrid = grid.cartplan,
        #    defaults=years)
        #if not created:
        

    def GetYearPlanchas(grids):
        #If there are planchas with año de fuente
        if grids.filter(cartfano__isnull = False):
            planchalist = grids.filter(cartfano__isnull = False)
            orig = planchalist[0]
            for planchaunit in grids.filter(cartfano__isnull = False)[1:]:
                if planchaunit.cartfano < orig.cartfano:
                    orig = planchaunit 
        #If there are planchas with año de elaboración
        elif grids.filter(carteano__isnull = False):    
            planchalist = grids.filter(carteano__isnull = False)
            orig = planchalist[0]
            for planchaunit in grids.filter(carteano__isnull = False)[1:]:
                if planchaunit.carteano < orig.carteano:
                    orig = planchaunit
        #In case there no one with any year
        else:
            orig = grids[0]
        SetPlanchaAnno(orig)

        #orig = grids[0]
        ##Verify Fuente years
        #for a in grids[1:]:
        #    if a.cartfano == None:
        #        pass
        #    elif a.cartfano < orig.cartfano:
        #        orig = a
        ##If there is no Fuente years verify elaborated
        #if orig.carteano == None:
        #    orig = grids[0]
        #    for a in grisds[1:]:
        #        if a.carteano == None

    #As the Plancha value is unique in cartonargis
    # and key is form there, it will be used
    log = ''
    for i in cartonargis.objects.filter(disponib = 'SI'):
        planchas = cartoginven.objects.filter(cartplan = i.planchav)
        if len(planchas) == 0:
            log += 'Revisar. La plancha %s no tiene registros en cartoginven'%(planchas.planchav)
        elif len(planchas) >= 1:
            #log += GetYearPlanchas(planchas)
             GetYearPlanchas(planchas)
        else:
            #log += SetPlanchaAnno(planchas)
            SetPlanchaAnno(planchas)
    print log

def Consolidado(request):
    '''
    '''
    # select distinct(cartuser_id) from matriz_cartografica_cartoginven;
    corpora = cartoginven.objects.all().distinct('cartuser')
    invent = []
    for corpo in corpora:
        cartog = cartoginven.objects.filter(cartuser = corpo.cartuser)
        carto = cartog.order_by('cartplan', 'cartfano', 'carteano').distinct('cartplan')
        count = len(carto)
        invent.append([corpo, carto, count])

    return render(request, 'consolidado_cartog.html', {'listado':invent})

