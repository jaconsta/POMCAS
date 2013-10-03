#-*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

import xlrd
import datetime

from .forms import UploadFileForm
from .models import *

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

def excel_store(upfile):
    '''
    I think it s better to first store the  file
    '''
    name = upfile.name
    with open('C:/Users/ASOCARS_I7/Documents/Matrix_loaded/%s'%(name), 'wb') as destination:      #('/tmp/%s'%(name), 'wb') as destination:
        for chunk in upfile.chunks():
            destination.write(chunk)
    return name

def soporte_store(upfile):
    '''

    '''
    name = upfile.name
    with open('/var/contrato85/matrix/%s'%(name), 'wb') as destination:      #('/tmp/%s'%(name), 'wb') as destination:
    	destination.write(upfile.read())
    return

def excel_process(upfile):
    '''
    And after being stored, read and process it.
    '''
    matrix = 'C:/Users/ASOCARS_I7/Documents/Matrix_loaded/%s'%(upfile)    #'/tmp/%s'%(upfile)
    book = xlrd.open_workbook(matrix)
    print book.sheet_by_index(1).name
    return

def excel_process(excel_addr):
    '''
    By now excel file is an address
	I dont want to overwhelm this with variables, son internal methods 
	will be used for each sheet, and will have the prefix "set"
    '''
    def ValidMatrix(book):
        def ValidBook():
            tabs = ['PORTADA', 'DATOS GENERALES', 'EST DIRECTIVA',
                   'ORGANIZACIÓN', 'DESCENTRALIZACIÓN, PLANEACIÓN',
                    'PRESUPESTO', 'SOP TÉC', 'POMCAS', 'LISTAS']
            pestanas = book.sheet_names()
            return tabs != pestanas
        def ValidPestCer():
            pestana = book.sheet_by_index(0)
            if pestana.cell_value(colx = 3, rowx = 42) != 'DESDE' or len(pestana.cell_value(colx = 1, rowx = 48)) == 57:
                return
        def ValidPestUno():
            pestana = book.sheet_by_index(1)
            if pestana.cell_value(colx = 1, rowx = 18) != 'NOMBRE DE LA CORPORACIÓN' or pestana.cell_value(colx = 7, rowx = 29) != 'A' or pestana.cell_value(colx = 9, rowx = 149) != 'Volver':
                return
        def ValidPestDos():
            pestana = book.sheet_by_index(2)
            if pestana.cell_value(colx = 1, rowx = 10) != '': # or
                return
        def ValidPestTre():
            pestana = book.sheet_by_index(3)
            if pestana.cell_value(colx = 4, rowx = 14) != 'MES' or pestana.cell_value(colx = 1, rowx = 10) != 'ASESORES DE DIRECCIÓN': 
                return
        def ValidPestCua():
            pestana = book.sheet_by_index(4)
            if pestana.cell_value(colx = 9, rowx = 5) != 'Volver' or pestana.cell_value(colx = 1, rowx = 14) != 'OFICINAS TERRITORIALES - REGIONALES': #or
                return
        def ValidPestCin():
            pestana = book.sheet_by_index(5)
            if pestana.cell_value(colx = 1, rowx = 12) != 'TITULO DEL PGAR' or pestana.cell_value(colx = 1, rowx = 25) != 'ESTRATEGIAS':
                return
        def ValidPestSei():
            pestana = book.sheet_by_index(6)
            if pestana.cell_value(colx = 4, rowx = 23) != 'MES':
                return
        def ValidPestSie():
            pestana = book.sheet_by_index(7)
            if pestana.cell_value(colx = 4, rowx = 16) != 'RAM':
                return
        def ValidPestOch():
            pestana = book.sheet_by_index(8)
            if pestana.cell_value(colx = 4, rowx = 28) != 'CARGO':
                return
        if not ValidBook():
            return 'El orden de las pestañas no es el adecuado'
        if not ValidPestCer():
            return 'La pestaña PORTADA parece tener campos en la posición equivocada, favor corregir.' 
        if not ValidPestUno():
            return 'La pestaña DATOS GENERALES parece tener campos en la posición equivocada, favor corregir.'
        if not ValidPestDos():
            return 'La pestaña EST DIRECTIVA parece tener campos en la posición equivocada, favor corregir.'
        if not ValidPestTre():
            return 'La pestaña ORGANIZACIÓN parece tener campos en la posición equivocada, favor corregir.'
        if not ValidPestCua():
            return 'La pestaña DESCENTRALIZACIÓN parece tener campos en la posición equivocada, favor corregir.'
        if not ValidPestCin():
            return 'La pestaña PLANEACIÓN parece tener campos en la posición equivocada, favor corregir.'
        if not ValidPestSei():
            return 'La pestaña PRESUPUESTO parece tener campos en la posición equivocada, favor corregir.'
        if not ValidPestSie():
            return 'La pestaña SOP TEC parece tener campos en la posición equivocada, favor corregir.'
        if not ValidPestOch():
            return 'La pestaña POMCAS parece tener campos en la posición equivocada, favor corregir.'
            
    def ValidBlankInt(value):
        if value == '':
            value = 0
        return value
    def SetDatosgen(sheet):
        #I consider this sheet the main object.
        #TODO: Link with a user
        weekdays={'Lunes': 'MON', 'Martes':'MAR', 'Miércoles':'MIE', 'Jueves':'JUE', 'Viernes':'VIE', 'Sábado':'SAB', 'Domingo':'DOM'}
        logo = 'get the address'
        nombre = sheet.cell_value(colx = 4, rowx = 18)
        nitval = sheet.cell_value(colx = 4, rowx = 20)
        nitval = nitval.split('-')
        nitdv = int(nitval[-1])
        nit = ''
        for i in nitval[0].split('.'):
              nit += i
        sigla = sheet.cell_value(colx = 4, rowx = 22)
        direccion = sheet.cell_value(colx = 4, rowx = 24)
        ciudad = sheet.cell_value(colx = 4, rowx = 27)
        horariode = sheet.cell_value(colx = 5, rowx = 29)
        horariode = xlrd.xldate_as_tuple(horariode,0)
        horariohasta = sheet.cell_value(colx = 8, rowx = 29)
        horariohasta = xlrd.xldate_as_tuple(horariohasta,0)
        diade = sheet.cell_value(colx = 5, rowx = 31)
        diahasta = sheet.cell_value(colx = 8, rowx = 31)
        telefindi = sheet.cell_value(colx = 5, rowx = 33)
        telefono = sheet.cell_value(colx = 6, rowx = 33)
        pagweb = sheet.cell_value(colx = 4, rowx = 35)
        email = sheet.cell_value(colx = 4, rowx = 37)
        area = sheet.cell_value(colx = 4, rowx = 40)
        municipios = sheet.cell_value(colx = 4, rowx = 146)
        #Set in DB
        datosgendb = minstdatgene(
            midglogo = logo, 
            midgrazs = nombre,
            midgenit = int(nit),
            midgnitd = nitdv,
            midginit = sigla,
            midgaddr = direccion,
            midgcity = ciudad,
            midgssop = datetime.time(horariode[-3], horariode[-2]),
            midgsscl = datetime.time(horariohasta[-3], horariohasta[-2]),
            midgapdf = weekdays[diade],
            midgapdt = weekdays[diahasta],
            midgphin = telefindi,
            midgphon = telefono,
            midgwebp = pagweb,
            midgmail = email,
            midgarju = area,
            midgnumj = municipios
        )
        datosgendb.save()
	return datosgendb

    def SetPortada(sheet, main_id):
        #TODO: Link to Datosgen
        dia = int(sheet.cell_value(colx = 5, rowx = 42))
        mes_s = sheet.cell_value(colx = 4, rowx = 42)
        anno = int(sheet.cell_value(colx = 6, rowx = 42))
        mes = Month[mes_s]
        diligen_desde = datetime.date(anno, mes, dia)
        dia = int(sheet.cell_value(colx = 5, rowx = 43))
        mes_s = sheet.cell_value(colx = 4, rowx = 43)
        mes = Month[mes_s]
        anno = int(sheet.cell_value(colx = 6, rowx = 43))
        diligen_hasta = datetime.date(anno, mes, dia)
        profesional = sheet.cell_value(colx = 3, rowx = 45)
        descripcion = sheet.cell_value(colx = 1, rowx = 49)
        #Set in DB
        portadadb = minstportada(
            mipodatg = main_id,
            mipofede = diligen_desde,
            mipofeha = diligen_hasta,
            mipoprof = profesional,
            mipodesc = descripcion
        )
        portadadb.save()
        return portadadb
    
    def SetEstrcDir(sheet, main_id):
        def SetNullEstr():
            #Set in DB
            struct = minstestdire(
                miedcorp = main_id,
                miediceo = '',
                mieddatp = datetime.datetime.today(),
            )
            struct.save()
            return struct
        def SetAlcaldes(sheet, estructura, rowini=11):
            departamento = sheet.cell_value(colx = 3, rowx = rowini)
            alcalde = sheet.cell_value(colx = 7, rowx = rowini)
            #Set in DB
            mayors = minstedcorpa(
                miestdir = estructura,
                miesddep = departamento,
                miesdmay = alcalde
            )
            mayors.save()
        def SetDirectCo(sheet, estructura, rowini = 21):
            sector = sheet.cell_value(colx = 2, rowx = rowini)
            consejero = sheet.cell_value(colx = 4, rowx = rowini)
            entidad = sheet.cell_value(colx = 6, rowx = rowini)
            #Set in DB
            directors = minstedcondi(
                miesddir = estructura,
                miesdsec = sector,
                miesdcna = consejero,
                miesdent = entidad
            )
            directors.save()
        def SetEstructu(sheet, estructura, rowini = 39):
            director = sheet.cell_value(colx = 4, rowx = rowini) 
            dia = int(sheet.cell_value(colx = 4, rowx = rowini+4))
            mes_s = sheet.cell_value(colx = 5, rowx = rowini+4) 
            mes = Month[mes_s]
            anno = int(sheet.cell_value(colx = 7, rowx = rowini+4))
            fechaposes = datetime.date(anno, mes, dia)
            #Set in DB
            estructura.miediceo = director
            estructura.mieddatp = fechaposes
            estructura.save()

        rowini = 11
        directiv = SetNullEstr()
        #Goes through all the Assambly section
        while(sheet.cell_value(colx = 3, rowx = rowini) != ''):
            SetAlcaldes(sheet, rowini = rowini, estructura = directiv)
            rowini = rowini +1
        #Check until the field 'Sector representado' appears
        while(sheet.cell_value(colx = 2, rowx = rowini) != 'SECTOR REPRESENTADO'):
            rowini = rowini +1
        rowini = rowini +1 #Add the next space to start 
        #Goes through all the Consoul section
        while(sheet.cell_value(colx = 2, rowx = rowini) != ''):
            SetDirectCo(sheet, rowini = rowini, estructura = directiv)
            rowini = rowini +1
        #Check until the field 'Director' appears
        try:
            while(str(sheet.cell_value(colx = 1, rowx = rowini)).find('DIRECTOR')): # != 'NOMBRE DEL DIRECTOR GENERAL DE LA CORPORACIÓN'):
                rowini = rowini +1
        except UnicodeEncodeError:
            pass
        SetEstructu(sheet, rowini = rowini, estructura = directiv)
        return
    
    def SetOrganiza(sheet, main_id):
        def SetPlanta(sheet, databasi):
            organigr = 'get the address'
            tipoact = sheet.cell_value(colx = 1, rowx = 15)
            numeact = sheet.cell_value(colx = 2, rowx = 15)
            dia = int(sheet.cell_value(colx = 3, rowx = 15))
            mes_s = sheet.cell_value(colx = 4, rowx = 15)
            mes = Month[mes_s]
            anno = int(sheet.cell_value(colx = 5, rowx = 15))
            fechacrea = datetime.date(anno, mes, dia)
            finanpro = sheet.cell_value(colx = 7, rowx = 15)
	    if finanpro == '':
                finanpro = 0
            finannac = sheet.cell_value(colx = 8, rowx = 15)
            if finannac == '':
                finannac = 0
            finanfoc = sheet.cell_value(colx = 9, rowx = 15)
            if finanfoc == '':
                finanfoc = 0
            planta = minstorganiz(
                mieocorp = databasi,
                mieoorga = organigr,
                mieoaata = tipoact,
                mieoaano = numeact,
                mieoaada = fechacrea,
                mieofnrp = finanpro,
                mieofnrn = finannac,
                mieofnfc = finanfoc
            )
            planta.save()
            return planta
        def SetAsesor(sheet, organiz, rowini = 20):
            nombre =  sheet.cell_value(colx = 1, rowx = rowini)
            rol = sheet.cell_value(colx = 4, rowx = rowini)[0:999]
            extens = ValidBlankInt(sheet.cell_value(colx = 7, rowx = rowini))
            email = sheet.cell_value(colx = 8, rowx = rowini)
            asesores = minesorasesd(
                miesoras = organiz,
                mieoadno = nombre,
                mieoadro = rol,
                mieoadex = extens,
                mieoadco = email
            )
            asesores.save()
        def SetSubdirec(sheet, organiz, rowini = 35):
           
            def GetNextItem(rowini, keyword = ''):
                '''
                Finds a next element by searching for whitespaces
                '''
                rowini += 1
                try:
                    while(str(sheet.cell_value(colx = 1, rowx = rowini)) == keyword):
                        rowini += 1
                except UnicodeEncodeError:
                    pass
                return rowini
            def SetCorrdinac(sheet, subdireccion, rowini):
                while(sheet.cell_value(colx = 3, rowx = rowini) != ''
                    or sheet.cell_value(colx = 6, rowx = rowini) != ''
                    or sheet.cell_value(colx = 7, rowx = rowini) != ''
                    or sheet.cell_value(colx = 8, rowx = rowini) != ''
                    or sheet.cell_value(colx = 9, rowx = rowini) != ''
                ):
                    coordina = sheet.cell_value(colx = 3, rowx = rowini)[0:124]
                    librenomb = ValidBlankInt(sheet.cell_value(colx = 6, rowx = rowini))
                        #librenomb = 0
                    carreadmi = ValidBlankInt(sheet.cell_value(colx = 7, rowx = rowini))
                    provision = ValidBlankInt(sheet.cell_value(colx = 8, rowx = rowini))
                    contratis = ValidBlankInt(sheet.cell_value(colx = 9, rowx = rowini))
                    coordinaciones = minesorsudico(
                        mieosubd = subdireccion,
                        mieosoco = coordina,
                        mieosoln = librenomb,
                        mieosoca = carreadmi,
                        mieosopr = provision,
                        mieosocn = contratis
                    )
                    coordinaciones.save()
                    rowini += 1
                return rowini
            rowini = GetNextItem(rowini = rowini)
            subnombre = sheet.cell_value(colx = 3, rowx = rowini)
            #Make sure subnombre if filled, else i'd mean an EOF
            if (subnombre == '' or subnombre == None):
                return sheet.nrows+10
            subextens = ValidBlankInt(sheet.cell_value(colx = 9, rowx = rowini))
            #find next element: As a non blank field
            rowini = GetNextItem(rowini = rowini)
            subdirect = sheet.cell_value(colx = 3, rowx = rowini)
            subdivinc = sheet.cell_value(colx = 8, rowx = rowini)
            rowini = GetNextItem(rowini = rowini)
            subdiubic = sheet.cell_value(colx = 3, rowx = rowini)
            subdireccion = minesorsubdir(
                miesorsu = organiz,
                mieosuof = subnombre,
                mieosuex = subextens,
                mieosuno = subdirect,
                mieosutv = subdivinc,
                mieosuub = subdiubic
            )
            subdireccion.save()
            rowini = GetNextItem(rowini = rowini)            
            rowini +=2
            rowini = SetCorrdinac(sheet, subdireccion, rowini)
            return rowini

        rowini = 18
        organig = SetPlanta(sheet, main_id)
            
        #I'm afraid people can add or remove rows. So will start searching
        
        try:        
            while(sheet.cell_value(colx = 1, rowx = rowini) != 'NOMBRE'):
                rowini += 1
        except UnicodeEncodeError:
            pass
        rowini +=1
        while(sheet.cell_value(colx = 1, rowx = rowini) != ''):
            SetAsesor(sheet, organiz = organig, rowini = rowini)
            rowini += 1
        try:
            while(str(sheet.cell_value(colx = 1, rowx = rowini)).find('SUBDIRECCIONES')):
                rowini += 1
        except UnicodeEncodeError:
            pass
        rowini += 1
        while (rowini <= sheet.nrows):
            rowini = SetSubdirec(sheet, organiz = organig, rowini = rowini)
    def SetDescentr(sheet, main_id):
        def SetDescen(sheet, main_id):
            tiene = True
            mapacorpo = sheet.cell_value(colx = 1, rowx = 12)
            criterio = sheet.cell_value(colx = 3, rowx = 16)[0:999]
            funciones = sheet.cell_value(colx = 3, rowx = 19)[0:999]
            descentraliza = minstdescentr(
                midesnco = main_id,
                midesofi = True,
                midesmap = 'get the address',
                midescri = criterio,
                midesfun = funciones
            )
            descentraliza.save()
            return descentraliza
        def SetNoDescen(sheet, main_id):
            descentraliza = minstdescentr(
                midesnco = main_id,
                midesofi = False
            )
            descentraliza.save()
        def SetDescenOffice(sheet, regions):
            def SetOfficeTerrit(sheet, region, rowini):
                oficina = sheet.cell_value(colx = 3, rowx = rowini)
                rowini += 3
                direcci = sheet.cell_value(colx = 3, rowx = rowini)
                ciudad = sheet.cell_value(colx = 7, rowx = rowini)
                rowini += 3
                try:
                    telindi = sheet.cell_value(colx = 4, rowx = rowini)
                except ValueError: 
                    print u'No hay inidicativo de región: %s'%(teleindi)
                    telindi = 0
                try:
                    telefon = sheet.cell_value(colx = 5, rowx = rowini)
                    int(telefon)
                except ValueError: 
                    print u'No ingresó teléfono o el formato es inválido: %s'%(telefon)
                    telefon = 0
                teleext = sheet.cell_value(colx = 8, rowx = rowini)
                if teleext == '':
                    teleext = 0
                elif int(teleext) >= 32767:
                    print u'La extensión %s no parece válida'%(teleext)
                    teleext = 0
                rowini += 3
                correo = sheet.cell_value(colx = 3, rowx = rowini)
                rowini += 2
                try:
                    jurisdi = sheet.cell_value(colx = 3, rowx = rowini)
                    jurisdi = float(jurisdi)
                except ValueError:
                    print u'No hay valor de area de jurisdicción o no es válido %s'%(jurisdi)
                    jurisdi = 0
                try:
                    municip = sheet.cell_value(colx = 6, rowx = rowini)
                    municip = int(municip)
                except ValueError:
                    print u'No hay cantidad de municipios o no es válido: %s'%(municip)
                    municip = 0
                rowini += 3
                respons = sheet.cell_value(colx = 3, rowx = rowini)
                vincula = sheet.cell_value(colx = 8, rowx = rowini)
                rowini += 3
                cargo = sheet.cell_value(colx = 3, rowx = rowini)             
                rowini += 4
                pvlibno = sheet.cell_value(colx = 1, rowx = rowini)
                if pvlibno == '':
                    pvlibno = 0
                pvcarad = sheet.cell_value(colx = 3, rowx = rowini)
                if pvcarad == '':
                    pvcarad = 0
                pvprovi = sheet.cell_value(colx = 5, rowx = rowini)
                if pvprovi == '':
                    pvprovi = 0
                pvcontr = sheet.cell_value(colx = 7, rowx = rowini)
                if pvcontr == '':
                    pvcontr = 0
                oficterrit = midesceoficte(
                    midodesc = region,
                    midonomb = oficina,
                    midodire = direcci,
                    midocity = ciudad,
                    midotcou = 57,
                    midotind = telindi,
                    mitotelf = telefon,
                    midotext = teleext,
                    midomail = correo,
                    midojuri = jurisdi,
                    midonumu = municip,
                    midonore = respons,
                    midotivi = vincula,
                    midocarg = cargo,
                    midopvln = pvlibno,
                    midopvca = pvcarad,
                    midopvpr = pvprovi,
                    midopvco = pvcontr
                )
                oficterrit.save()
                return rowini

            rowini = 23
            #Iterate over offices
            while rowini <= (sheet.nrows-4):
                if sheet.cell_value(colx = 1, rowx = rowini) == 'NOMBRE DE LA OFICINA TERRITORIAL' and sheet.cell_value(colx = 3, rowx = rowini) != '':
                    rowini = SetOfficeTerrit(sheet, region = regions, rowini = rowini)
                rowini += 1
        tieneofic = Conditional[sheet.cell_value(colx = 5, rowx = 10)]
        if tieneofic:
            regions = SetDescen(sheet, main_id)
            SetDescenOffice(sheet, regions)
        else:
            SetNoDescen(sheet, main_id)
            return
    def SetPlaneaci(sheet, main_id):
        def SetPgar(sheet, main_id):
            pgarimg = 'get the address'
            pgartitulo = sheet.cell_value(colx = 2, rowx = 12)
            pgarperiodo = sheet.cell_value(colx = 6, rowx = 12)
            pgartipoact = sheet.cell_value(colx = 1, rowx = 18)
            if pgartipoact == '':
                print u'PGAR. No hay información de acto administrativo %s'%(pgartipoact)
                print u'Se permite continuar con el proceso'
            pgarnumeact = sheet.cell_value(colx = 3, rowx = 18)
            if pgarnumeact == '':
                print u'PGAR. No hay información de número de acto %s'%(pgarnumeact)
                pgarnumeact = 0
            try:
                dia = int(sheet.cell_value(colx = 4, rowx = 18))
                mes_s = sheet.cell_value(colx = 5, rowx = 18)
                mes = Month[mes_s]
                anno = int(sheet.cell_value(colx = 7, rowx = 18))
                pgarfecha = datetime.date(anno, mes, dia)
            except ValueError:
                print u'No se ha especificado un valor válido para la fecha'
                pgarfecha  = None
            #I suppose people might place more than one resolution then i'll verify
            # As I'm not sure if it will allow symbols
            if sheet.cell_value(colx = 1, rowx = 20) == '': #!= 'PROSPECTIVA AMBIENTAL DE LA JURISDICCIÓN':
                print 'Se esperaba el texto PROSPECTIVA AMBIENTAL DE LA JURISDICCIÓN.'
            elif sheet.cell_value(colx = 1, rowx = 22) == '': #!= 'DIAGNOSTICO AMBIENTAL':
                print 'Se esperaba el texto DIAGNÓSTICO AMBIENTAL.'
            pgarprospec = sheet.cell_value(colx = 3, rowx = 20)[0:999]
            pgardiagnos = sheet.cell_value(colx = 3, rowx = 22)[0:999]
            instrupgar = minstplanific(
                miplanif = main_id,
                miplpgar = pgarimg,
                mipltipg = pgartitulo,
                miplpgpe = pgarperiodo,
                miplpgaa = pgartipoact,
                miplpgno = pgarnumeact,
                miplpgda = pgarfecha,
                miplpamj = pgarprospec, 
                mipldiag = pgardiagnos
            )
            instrupgar.save()
            return instrupgar
        def SetPgarCompo(sheet, pgar, rowini = 26):
            while sheet.cell_value(colx = 1, rowx = rowini) != '': 
                estrategias = sheet.cell_value(colx = 1, rowx = rowini)[0:499]
                mecanismos = sheet.cell_value(colx = 4, rowx = rowini)[0:499] 
                compopgar = minstplanpgar(
                    miplanpg = pgar,
                    miplpges = estrategias,
                    miplpgse = mecanismos
                )
                compopgar.save()
                rowini += 1
            return rowini
        def SetPai(sheet, pgar, rowini = 62):
            paiimg = 'get the address'
            rowini += 2
            paititulo = sheet.cell_value(colx = 2, rowx = rowini)
            paiperiodo = sheet.cell_value(colx = 6, rowx = rowini)
            rowini += 6
            paitipoact = sheet.cell_value(colx = 2, rowx = rowini)
            painumeact = sheet.cell_value(colx = 3, rowx = rowini)
            dia = int(sheet.cell_value(colx = 4, rowx = rowini))
            mes_s = sheet.cell_value(colx = 5, rowx = rowini)
            mes = Month[mes_s.title()]
            anno = int(sheet.cell_value(colx = 7, rowx = rowini))
            paifecha = datetime.date(anno, mes, dia)
            return rowini
        def SetPaiMetas(sheet, pgar, rowini = 74):
            '''
            This one has quite a strange logic.
            One PROGRAMAS can have many PROYECTOS and
            a PROYECTOS can have many METAS. But not the other way.
            Therefore an inverse capture logic will be applied.
            No database dependency will be applied
            '''
            programas = ''
            proyectos = ''
            metas = ''
            tmp = '' #A temporary storage variable
            while sheet.cell_value(colx = 5, rowx = rowini) != '' and rowini :
                metas = (u'%s'%(sheet.cell_value(colx = 5, rowx = rowini)))[0:499] 
                #Get proyectos
                tmp = (u'%s'%(sheet.cell_value(colx = 3, rowx = rowini)))[0:499] 
                if tmp != '':
                    proyectos = tmp 
                #Get programas
                tmp = (u'%s'%(sheet.cell_value(colx = 1, rowx = rowini)))[0:499] 
                if tmp != '':
                    programas = tmp
                metaspai = minsplanpaime(
                    miplanai = pgar,
                    miplaipr = programas,
                    miplaipj = proyectos,
                    miplaimt = metas
                )
                metaspai.save()
                rowini += 1
                if rowini >= sheet.nrows:
                    break
        pgar = SetPgar(sheet, main_id)
        #Verify cell ESTRATEGIAS is on its expected place
        if sheet.cell_value(colx = 1, rowx = 25) != 'ESTRATEGIAS':
            print 'Se esperaba el texto ESTRATEGIAS.'
        rowini = SetPgarCompo(sheet, pgar = pgar)
        #Find PLAN DE ACCION INSTITUCIONAL
        while(str(sheet.cell_value(colx = 1, rowx = rowini).encode('utf-8')).find('PLAN')):#  == '':#.find('PLAN')): 
            rowini = rowini +1
        rowini = rowini +1
        rowini = SetPai(sheet, pgar = pgar, rowini = rowini)
        #Just find where PROGRAMAS from METAS CORRESPONDIENTES is placed
        while(str(sheet.cell_value(colx = 1, rowx = rowini)).find('PROGRAMAS')): 
            rowini = rowini +1
        rowini = rowini +1
        SetPaiMetas(sheet, pgar = pgar, rowini = rowini)
    def SetPresupue(sheet, main_id):
        def SetEjecPresu(sheet, main_id):
            presupadj = 'get the address'
            gastproye = sheet.cell_value(colx = 4, rowx = 13)
            if type(gastproye) != int:
                if  gastproye != '':
                    error += 'El formato de numero es incorrecto'
                gastproye = 0
            gastejecu = sheet.cell_value(colx = 6, rowx = 13)
            if type(gastejecu) != int:
                if gastejecu  != '':
                    error += 'El formato de numero es incorrecto'
                gastejecu = 0
            inveproye = sheet.cell_value(colx = 4, rowx = 14)
            if type(inveproye) != int:
                if inveproye  != '':
                    error += 'El formato de numero es incorrecto'
                inveproye = 0
            inveejecu = sheet.cell_value(colx = 6, rowx = 14)
            if type(inveejecu) != int:
                if inveejecu  != '':
                    error += 'El formato de numero es incorrecto'
                inveejecu = 0
            servproye = sheet.cell_value(colx = 4, rowx = 15)
            if type(servproye) != int:
                if servproye  != '':
                    error += 'El formato de numero es incorrecto'
                servproye = 0
            servejecu = sheet.cell_value(colx = 6, rowx = 15)
            if type(servejecu) != int:
                if servejecu  != '':
                    error += 'El formato de numero es incorrecto'
                servejecu = 0
            fcarproye = sheet.cell_value(colx = 4, rowx = 16)
            if type(fcarproye) != int:
                if fcarproye  != '':
                    error += 'El formato de numero es incorrecto'
                fcarproye = 0
            fcarejecu = sheet.cell_value(colx = 6, rowx = 16)
            if type(fcarejecu) != int:
                if fcarejecu  != '':
                    error += 'El formato de numero es incorrecto'
                fcarejecu = 0
            fcaaproye = sheet.cell_value(colx = 4, rowx = 17)
            if type(fcaaproye) != int:
                if fcaaproye  != '':
                    error += 'El formato de numero es incorrecto'
                fcaaproye = 0
            fcaaejecu = sheet.cell_value(colx = 6, rowx = 17)
            if type(fcaaejecu) != int:
                if fcaaejecu  != '':
                    error += 'El formato de numero es incorrecto'
                fcaaejecu = 0
            presupuesto = minspresupues(
                miplanpr = main_id,
                #miplpres = presupadj,
                miplprgp = gastproye,
                miplgrge = gastejecu, 
                miplgrip = inveproye, 
                miplgrie = inveejecu, 
                miplgrsp = servproye, 
                miplgrse = servejecu, 
                miplgfrp = fcarproye, 
                miplgfre = fcarejecu,
                miplgfap = fcaaproye, 
                miplgfae = fcaaejecu 
            )
            presupuesto.save()
            return presupuesto
        def SetActAdPres(sheet, budget):
            #I validated that it starts on row 24
            rowini = 24
            while sheet.cell_value(colx = 1, rowx = rowini) != '':
                tipoacto = sheet.cell_value(colx = 1, rowx = rowini)
                numeacto = sheet.cell_value(colx = 2, rowx = rowini)
                dia = int(sheet.cell_value(colx = 3, rowx = rowini))
                mes_s = sheet.cell_value(colx = 4, rowx = rowini)
                mes = Month[mes_s]
                anno = int(sheet.cell_value(colx = 5, rowx = rowini))
                fecha = datetime.date(anno, mes, dia)
                accion = sheet.cell_value(colx= 6, rowx = rowini)
                actoadmin = minspresactad(
                    mipraaco = budget,
                    mipraati = tipoacto,
                    mipraano = numeacto,
                    mipraada = fecha,
                    mipraaac = accion
                )
                actoadmin.save()
                rowini += 1
            return rowini
        def SetPresuPomca(sheet, budget, rowini):
            #fing next word
            while sheet.cell_value(colx= 1, rowx = rowini) != 'PROYECTO':
                rowini += 1
            #Maybe the chart ends here
            rowini += 1
            if rowini >= sheet.nrows:
                return
            #Fill db
            while sheet.cell_value(colx = 1, rowx = rowini) != '':
                proyecto = sheet.cell_value(colx = 1, rowx = rowini)
                fuentefinan =  sheet.cell_value(colx = 2, rowx = rowini)
                valor = sheet.cell_value(colx = 4, rowx = rowini)
                cuencas = sheet.cell_value(colx = 5, rowx = rowini)
                asocars = Conditional[sheet.cell_value(colx = 6, rowx = rowini)]
                presupomca = minsprespomca(
                    miprprco = budget,
                    miprprpr = proyecto,
                    miprprfi = fuentefinan,
                    miprprva = valor,
                    miprprcu = cuencas,
                    miprpras = asocars
                )
                presupomca.save()
                rowini += 1
                if rowini >= sheet.nrows:
                    break
        money = SetEjecPresu(sheet, main_id)
        rowini = SetActAdPres(sheet, money)
        SetPresuPomca(sheet, money, rowini = rowini)
    def SetSopTec(sheet, main_id):
        def SetHaveSig(sheet, main_id):
            sigexist = sheet.cell_value(colx = 5, rowx = 11)
            sigrespo = sheet.cell_value(colx = 8, rowx = 13)
            sigexten = sheet.cell_value(colx = 11, rowx = 13)
            sistemas = minssopotecni(
                misoptec = main_id,
                missigex = sigexist,
                missigre = sigrespo
            )
            sistemas.save()
            return sistemas
        def SetSigpc(sheet, soptec, rowini = 17):
            while sheet.cell_value(colx = 2, rowx = rowini) != '':
                pcproces = sheet.cell_value(colx = 2, rowx = rowini)
                pcram = sheet.cell_value(colx = 4, rowx = rowini)
                pchdd = sheet.cell_value(colx = 5, rowx = rowini)
                pcvideo = sheet.cell_value(colx = 6, rowx = rowini)
                pcos = sheet.cell_value(colx = 8, rowx = rowini)
                pcimgproc = sheet.cell_value(colx = 10, rowx = rowini)
                pcinteimg = sheet.cell_value(colx = 11, rowx = rowini)
                pcinfo = minssotesigpc(
                    misotepc = soptec,
                    mistpcpr = pcproces,
                    mistpcra = pcram,
                    mistpcdd = pchdd,
                    mistpcgc = pcvideo,
                    mistpcos = pcos,
                    mistpcps = pcimgproc,
                    mistpcim = pcinteimg
                )
                pcinfo.save()
                rowini += 1
            return rowini    
        def SetSopTecPeople(sheet, soptec, sistema, rowini):
            nombre = sheet.cell_value(colx = 1 , rowx = rowini)
            profesion = sheet.cell_value(colx = 5, rowx = rowini)
            posgrado = sheet.cell_value(colx = 6, rowx = rowini)
            cargo = sheet.cell_value(colx = 7, rowx = rowini)
            tipovincula = sheet.cell_value(colx = 8, rowx = rowini)
            tiempodedic = sheet.cell_value(colx = 10, rowx = rowini)
            try:
                tiempodedic = float(tiempodedic)
            except ValueError:
                print u'Se esperaba un número, llegó: %s'%(tiempodedic)    
                tiempodedic = None
            otrasfuncio = sheet.cell_value(colx = 11, rowx = rowini)
            personal = minssoptechrs(
                misotehr = soptec,
                misthrcl = sistema,
                misthrno = nombre,
                misthrpr = profesion,
                misthrpg = posgrado,
                misthrca = cargo,
                misthrtv = tipovincula,
                misthrtd = tiempodedic,
                misthrfr = otrasfuncio,
            )
            personal.save()
        def SetSIRH(sheet, soptec, rowini):
            sirhexis = sheet.cell_value(colx = 5, rowx = rowini)
            sirhnomb = sheet.cell_value(colx = 8, rowx = rowini)
            rowini += 3
            sirhdesc = sheet.cell_value(colx = 5, rowx = rowini)[0:499]
            rowini += 4
            sirhhweb = sheet.cell_value(colx = 5, rowx = rowini)
            sirhwurl = sheet.cell_value(colx = 8, rowx = rowini)
            rowini += 2
            soptec.missrhex = sirhexis
            soptec.missrhns = sirhnomb
            soptec.missrhde = sirhdesc
            soptec.missrhwe = sirhhweb
            soptec.missrhru = sirhwurl
            soptec.save()
            return rowini
        def SetLA(sheet, soptec, rowini):
            laexist = Conditional[sheet.cell_value(colx = 5, rowx = rowini)]
            if laexist:
                rowini += 4 
                laacredit = Conditional[sheet.cell_value(colx = 8, rowx = rowini)]
                if laacredit:
                    rowini += 7
                    entidad = sheet.cell_value(colx = 1, rowx = rowini)
                    resolucion = sheet.cell_value(colx = 5, rowx = rowini)
                    dia = int(sheet.cell_value(colx = 6, rowx = rowini))
                    mes_s = sheet.cell_value(colx = 7, rowx = rowini)
                    mes = Month[mes_s]
                    anno = int(sheet.cell_value(colx = 9, rowx = rowini))
                    fecha = datetime.date(anno, mes, dia)
                    rowini += 2
                    parametros = sheet.cell_value(colx = 1, rowx = rowini)[0:999]
                    proceso = sheet.cell_value(colx = 5, rowx = rowini)[0:999]
                    rowini += 2
                soptec.laacr = laacredit
            else:
                convenios = Conditional[sheet.cell_value(colx = 8, rowx = rowini)]
                if convenios:
                    cualconve = sheet.cell_value(colx = 8, rowx = rowini)
                    soptec.mislacoc = cualconve
                soptec.mislacon = convenios
                rowini +=15
            soptec.laexi = laexist
            soptec.save()
            return rowini
        def SetRMA(sheet, soptec, rowini = 113):
            rmaexist = Conditional[sheet.cell_value(colx = 5, rowx = rowini)]
            if rmaexist:
                rowini += 4
                asocrmn = Conditional[sheet.cell_value(colx = 6, rowx = rowini)]
                cualrmn = sheet.cell_value(colx = 8, rowx = rowini)
                rowini += 3
                estacio = sheet.cell_value(colx = 6, rowx = rowini)
                paramet = sheet.cell_value(colx = 11, rowx = rowini)
                #Set the db objetc
                soptec.misrmana = asocrmn 
                soptec.misrmano = cualrmn
                soptec.misrmaed = estacio 
                soptec.misrmapm = paramet 
                rowini += 2
            else: 
                conveni = sheet.cell_value(colx = 8, rowx = rowini)
                cuancon = sheet.cell_value(colx = 8, rowx = rowini)
                #Set the db objetc
                soptec.misrmaco = conveni
                soptec.misrmacc = cuancon
                rowini += 9
                return rowini 
            #Set the db objetc
            soptec.misrmaex = rmaexist
            soptec.save()
            return rowini
        def SetRMC(sheet, soptec, rowini = 151):
            rmcexist = Conditional[sheet.cell_value(colx = 5, rowx = rowini)]  
            if rmcexist:
                rowini += 4
                estaciones = sheet.cell_value(colx = 6, rowx = rowini)  
                parametros = sheet.cell_value(colx = 11, rowx = rowini)  
                #Set the db objetc
                soptec.misrmced = estaciones
                soptec.misrmcpm = parametros
                rowini += 2
            else:
                convenios = sheet.cell_value(colx = 9, rowx = rowini)  
                cualconve = sheet.cell_value(colx = 11, rowx = rowini)  
                #Set the db objetc
                soptec.misrmcco = convenios
                soptec.misrmccc = cualconve
                rowini += 6
            soptec.misrmcex = rmcexist
            soptec.save()
            return rowini
        def SetRMH(sheet, soptec, rowini = 186):
            rmhexist = Conditional[sheet.cell_value(colx = 5, rowx = rowini)]  
            if rmhexist:
                rowini += 4
                estaciones = sheet.cell_value(colx = 6, rowx = rowini)  
                parametros = sheet.cell_value(colx = 11, rowx = rowini)  
                #Set the db objetc
                soptec.misrmhed = estaciones
                soptec.misrmhpm = parametros
                rowini += 2
            else:
                convenios = sheet.cell_value(colx = 9, rowx = rowini)  
                cualconve = sheet.cell_value(colx = 11, rowx = rowini)  
                #Set the db objetc
                soptec.misrmhco = convenios
                soptec.misrmhcc = cualconve
                rowini += 6
            soptec.misrmhex = rmhexist
            soptec.save()
            return rowini
        infosistems = SetHaveSig(sheet, main_id)
        #If there is SIG
        if infosistems.missigex != 'No disponible' or infosistems.missigex != '': 
            #Verify that the Pc information starts where its
            # supposed to.
            if 'Procesador' not in sheet.cell_value(colx = 2, rowx = 16):
                print u'Al parecer la información de los quipos de computo no se encuentra en a posición necesaria'   
                print u'El proceso no continúa'
                return
            rowini = 17
            rowini = SetSigpc(sheet, soptec = infosistems, rowini = rowini)
            #Find word PERSONAL for the people involved
            while (u'%s'%(sheet.cell_value(colx = 1, rowx = rowini))).find('PERSONA') and (u'%s'%(sheet.cell_value(colx = 1, rowx = rowini))).find('GEOGR'):
                rowini += 1
            #Make sure the spaces are respected
            rowini += 2
            if sheet.cell_value(colx = 1, rowx = rowini) == 'NOMBRE':
                rowini += 1
                while sheet.cell_value(colx = 1, rowx = rowini) != '':
                    SetSopTecPeople(sheet, soptec = infosistems, sistema = 'SIG', rowini = rowini)
                    rowini += 1
            else:
                print u'Personal SIG. Parece que las celdas han sido modificadas de un modo que no es posible seguirlas procesando.'
                print u'El proceso no continúa'
                return
        else:
        #Find SIRH
            print u'No tiene SIG'
            rowini = 20
        try:    
            while 'RECURSO' not in sheet.cell_value(colx = 1, rowx = rowini):#.find('RECURSO'):
                rowini += 1
        except IndexError:
            print u'No se encontró Información del SIRH'
            rowini = 30        
        #If there is SIRH 
        rowini += 2
        if sheet.cell_value(colx = 5, rowx = rowini) == 'SI':
            rowini = SetSIRH(sheet, soptec = infosistems, rowini = rowini)
        else:
            print u'No tiene SIRH'
            rowini += 10
        #LA is right next to SIRH but make sure not modified
        rowini += 1
        try:
            while sheet.cell_value(colx = 1, rowx = rowini) != 'LABORATORIO DE AGUAS':
                rowini += 1
        except IndexError:
            print u'No se encontró Información del LA'
            print u'No se continuará con el proceso'
            return
        rowini += 2
        if sheet.cell_value(colx = 5, rowx = rowini) == 'SI':
            rowini = SetLA(sheet, soptec = infosistems, rowini = rowini)
            #It assumes the cells hasnt been erased
            #Checks just in case some space has been added or removed
            while sheet.cell_value(colx = 1, rowx = rowini) != 'NOMBRE':
                rowini += 2
            rowini += 1    
            while sheet.cell_value(colx = 1, rowx = rowini) != '':
                SetSopTecPeople(sheet, soptec = infosistems, sistema = 'LA', rowini = rowini)
                rowini += 1
        else:
            print u'No tiene LA'
        #Find RMA
        try:
            while 'AMBIENTAL' not in sheet.cell_value(colx = 1, rowx = rowini):
                rowini += 1
        except IndexError:
            print u'No se encontró Información del RMA'
            print u'No se continuará con el proceso'
            return
        rowini += 2
        if sheet.cell_value(colx = 5, rowx = rowini) == 'SI':
            rowini = SetRMA(sheet, soptec = infosistems, rowini = rowini)
            #It assumes the cells hasnt been erased
            #Checks just in case some space has been added or removed
            while sheet.cell_value(colx = 1, rowx = rowini) != 'NOMBRE':
                rowini += 1
            rowini += 1    
            while sheet.cell_value(colx = 1, rowx = rowini) != '':
                SetSopTecPeople(sheet, soptec = infosistems, sistema = 'RMA', rowini = rowini)
                rowini += 1
        else:
            print u'No tiene RMA'
        #Find RMC
        try:
            while 'CLIMATOL' not in sheet.cell_value(colx = 1, rowx = rowini):
                rowini += 1
        except IndexError:
            print u'No se encontró Información del RMC'
            print u'No se continuará con el proceso'
            return
        rowini += 2
        if sheet.cell_value(colx = 5, rowx = rowini) == 'SI':
            rowini = SetRMC(sheet, soptec = infosistems, rowini = rowini)
            #It assumes the cells hasnt been erased
            #Checks just in case some space has been added or removed
            while sheet.cell_value(colx = 1, rowx = rowini) != 'NOMBRE':
                rowini += 1
            rowini += 1    
            while sheet.cell_value(colx = 1, rowx = rowini) != '':
                SetSopTecPeople(sheet, soptec = infosistems, sistema = 'RMC', rowini = rowini)
                rowini += 1
        else:
            print u'No tiene RMC'
        #Find RMH
        try:
            while 'HIDROL' not in sheet.cell_value(colx = 1, rowx = rowini):
                rowini += 1
        except IndexError:
            print u'No se encontró Información del RMA'
            print u'No se continuará con el proceso'
            return
        rowini += 2
        if sheet.cell_value(colx = 5, rowx = rowini) == 'SI':
            rowini = SetRMH(sheet, soptec = infosistems, rowini = rowini)
            #It assumes the cells hasnt been erased
            #Checks just in case some space has been added or removed
            while sheet.cell_value(colx = 1, rowx = rowini) != 'NOMBRE':
                rowini += 1
            rowini += 1    
            while sheet.cell_value(colx = 1, rowx = rowini) != '':
                SetSopTecPeople(sheet, soptec = infosistems, sistema = 'RMH', rowini = rowini)
                rowini += 1
        else:
            print u'No tiene RMH'
    def SetPomcas(sheet, main_id):
        def SetPomcaComission(sheet, main_id):
            comitexists = sheet.cell_value(colx = 4, rowx = 13)
            comitexist = Conditional[comitexists]
            if comitexist:
                comiteacto = sheet.cell_value(colx = 1, rowx = 18)
                if comiteacto == '':
                    print u'No hay valor para el acto del comité: %s'%(comiteacto)
                    print u'Se permite continuar con el proceso'
                comitenume = sheet.cell_value(colx = 3, rowx = 18)
                if comitenume == '':
                    print u'No hay valor para el Número de acto %s'%(comitenume)
                    print u'Se permite continuar con el proceso'
                    comitenume = 0
                try:
                    dia = int(sheet.cell_value(colx = 4, rowx = 18))
                    mes_s = sheet.cell_value(colx = 5, rowx = rowini)
                    mes = Month[mes_s]
                    anno = int(sheet.cell_value(colx = 7, rowx = rowini))
                    fecha = datetime.date(anno, mes, dia)
                except ValueError:
                    print u'No se ha especificado un valor válido para la fecha'
                    fecha = None
                comitdele = sheet.cell_value(colx = 3, rowx = 21)
                cdelecarg = sheet.cell_value(colx = 5, rowx = 21)
                cdelecorr = sheet.cell_value(colx = 7, rowx = 21)
                comitepomca = minsrecurhuma(
                    mipocasc = main_id,
                    mipomcex = comitexist,
                    mipomcac = comiteacto,
                    mipomcno = comitenume, 
                    mipomcda = fecha,
                    mipomcde = comitdele,
                    mipomcdc = cdelecarg,
                    mipomcdm = cdelecorr
                )
            else:
                comitepomca = minsrecurhuma(
                    mipocasc = main_id,
                    mipomcex = comitexist
                )
            comitepomca.save()
            return comitepomca
        def SetPomcaFuncion(sheet, pomca, rowini = 26):
            def SetWorkers(sheet, pomca, dependency, rowini):
                nombre = sheet.cell_value(colx = 1, rowx = rowini)[0:119]
                profesion = sheet.cell_value(colx = 2, rowx = rowini)[0:119]
                estudios = sheet.cell_value(colx = 3, rowx = rowini)[0:249]
                cargo =  sheet.cell_value(colx = 4, rowx = rowini)[0:119]
                vinculacion = sheet.cell_value(colx = 5, rowx = rowini)
                subdireccion = sheet.cell_value(colx = 6, rowx = rowini)
                coordinacion = sheet.cell_value(colx = 7, rowx = rowini)[0:119]
                if dependency == 'INVOTEM':
                    tiempo = None
                    rol = None
                    funciones = None
                    tematica = sheet.cell_value(colx = 8, rowx = rowini)
                else:
                    try:
                        tiempo = sheet.cell_value(colx = 8, rowx = rowini)
                        int(tiempo)
                    except ValueError:
                        print u'Se esperaba un número. Llega: %s'%(tiempo)
                        tiempo = None
                    rol = sheet.cell_value(colx = 9, rowx = rowini)[0:249]
                    funciones = sheet.cell_value(colx = 10, rowx = rowini)[0:249]
                    tematica = None
                funcionario = minsrhvinpomc(
                    mirhpomc = pomca,
                    mirhpopc = dependency,
                    mirhpono = nombre,
                    mirhpopr = profesion,
                    mirhpoec = estudios,
                    mirhpoca = cargo,
                    mirhpotv = vinculacion,
                    mirhpoof = subdireccion,
                    mirhpodi = coordinacion,
                    mirhpotd = tiempo,
                    mirhporo = rol, 
                    mirhpoot = funciones,
                    mirhpote = tematica
                )
                funcionario.save()
            #I saw few matrix where the whole title and seaction
            # were removed. Then I'll have to validate it
            #Search keywords [RESPONSABLES, INVOLUCRADOS], 
            #  [POMCAS, RIESGO, PARTICIPACIÓN, OTRAS]
            rowini = 26
            while sheet.nrows > (rowini+1): #cell_value(colx = 1, rowx = rowini)
                proceso = ''
                text = sheet.cell_value(colx = 1, rowx = rowini)
                if 'RESPONSABLES' in text:
                    if 'POMCAS' in text:
                        proceso = 'RESPOMC'
                    elif 'RIESGO' in text:
                        proceso = 'RESRIES'
                    elif 'PARTICI' in text:
                        proceso = 'RESPART'
                    else:
                        print u'Parece haber ocurrido un error al leer %s'%(text)
                elif 'INVOLUCRADOS' in text:
                    if 'POMCAS' in text:
                        proceso = 'INVPOMC'
                    elif 'RIESGO' in text:
                        proceso = 'INVRIES'
                    elif 'PARTICI' in text:
                        proceso = 'INVPART'
                    elif 'OTRAS' in text:
                        proceso = 'INVOTEM'
                    else:
                        print u'Parece haber ocurrido un error al leer %s'%(text)
                if proceso is not '':
                    #Content is suppossed to be 3 rows after title
                    rowini += 2
                    if sheet.cell_value(colx = 1, rowx = rowini) == 'NOMBRE':
                        rowini += 1
                        while sheet.cell_value(colx = 1, rowx = rowini) != '':
                            SetWorkers(sheet, pomca=pomca, dependency = proceso, rowini = rowini)
                            rowini += 1
                            if sheet.nrows < (rowini+1):
                                break
                    else:
                        print 'Parecen haberse borrado más campos de los debidos. row %s'%(rowini)
                rowini += 1
        pomcasrh = SetPomcaComission(sheet, main_id = main_id)
        SetPomcaFuncion(sheet, pomca = pomcasrh)

    Month = {'Enero':1, 'Febrero':2, 'Marzo':3,
            'Abril': 4, 'Mayo':5, 'Junio':6,
            'Julio': 7, 'Agosto': 8, 'Septiembre':9,
            'Octubre':10, 'Noviembre':11, 'Diciembre':12
    }
    error = ''
    Conditional = {'SI':True, 'NO':False, '':False}
    #Open the excel
    excel_file = xlrd.open_workbook('/var/contrato85/matrix/%s'%(excel_addr))#,  encoding_override="utf-8")
    print 'Inicio del proceso: %s'%(datetime.datetime.now())
    print u'Se hará una validación rápida del archivo'
    #excel_file = xlrd.open_workbook('/tmp/%s'%(excel_addr))#,  encoding_override="utf-8")
    #Validate the matrix fills the minimun structure required
    if not ValidMatrix(excel_file):
        return u'La matriz no cumple con los requisitos mínimos'
    #Open '1' sheet: Datos Generales
    #This sheet is static
    #It has attached objects
    print u'Validación Datos Generales'
    excel_sheet = excel_file.sheet_by_index(1)
    excel_id = SetDatosgen(excel_sheet)
    #Open '0' sheet: Portada
    #This sheet is static
    print u'Validación Portada'
    excel_sheet = excel_file.sheet_by_index(0)
    SetPortada(excel_sheet, excel_id)
    #Open '2' sheet: Estructura Directiva
    #This sheet is Dymanic 
    print u'Validación Estructura Directiva'
    excel_sheet = excel_file.sheet_by_index(2)
    SetEstrcDir(excel_sheet, excel_id)
    #Open '3' sheet: Organizacion
    #This sheet starts whith Static fields and ends Truly dynamic
    print u'Validación Organización'
    excel_sheet = excel_file.sheet_by_index(3)
    SetOrganiza(excel_sheet, excel_id)
    #Open '4' sheet: Descentralizacion
    #This sheet has one logical field and dynamic scalable 
    print u'Validación Descentralización'
    excel_sheet = excel_file.sheet_by_index(4)
    SetDescentr(excel_sheet, excel_id)
    #Open '5' sheet: Planeacion
    #This sheet starts static, continues dymanic with some static
    #  fields and ends dynamic and logic
    print u'Validación Planeación'
    excel_sheet = excel_file.sheet_by_index(5)
    SetPlaneaci(excel_sheet, excel_id)
    #Open '6' sheet: Presupuesto
    #This sheet starts whith Static fields and ends dynamic
    print u'Validación Presupuesto'
    excel_sheet = excel_file.sheet_by_index(6)
    SetPresupue(excel_sheet, excel_id)
    #Open '7' sheet: Sop Tec
    #This sheet has many logic and dynamic fields
    #Left to last
    print u'Validación Soporte Técnico'
    excel_sheet = excel_file.sheet_by_index(7)
    SetSopTec(excel_sheet, excel_id)
    #Open '8' sheet: POMCAS
    #This sheet starts whith Static fields and ends dynamic
    print u'Validación POMCAS'
    excel_sheet = excel_file.sheet_by_index(8)
    SetPomcas(excel_sheet, excel_id)
    print u'Validación Culminada Revisar Cargue en base de datos'
    print 'Fin del proceso: %s'%(datetime.datetime.now())


@login_required(login_url = '/login/')
def upload_matrix(request):
    '''
    DEPRECATED
    '''
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
