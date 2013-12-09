#-*- coding: utf-8 -*-
import xlrd
import datetime

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

