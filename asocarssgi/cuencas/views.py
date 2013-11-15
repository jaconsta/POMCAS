# -*- coding: utf-8 -*-
from cuencas.models import *
from corporacion.models import corporaname
import xlrd

def GetCorpoCuencas(corpora):
    return cuencompart.objects.filter(cuencomp = corpora)


def SetMacrocuencas(text_file):
    #Go though the file
    source = open(text_file, 'r')
    for line in source:
        obj, created = macrocuenca.objects.get_or_create(macrcuen = line)
        if not created:
            print u'La Macrocuenca %s ya existía' %(line)

def SetCuencas(text_file):
    #Go though the file
    Conditional = {u'SI':True, u'NO':False}
    source = open(text_file, 'r')
    i = 0
    for line in source:
        watersheed = line.split(';')
        #Get the MacroCuenca
        macro = macrocuenca.objects.filter(macrcuen = watersheed[0])
        #Split if NSS
        if watersheed[4] == 'NSS':
            code , subcode = watersheed[2].split('-')
        else:
            code = watersheed[2]
            subcode = None
        #Convert 'Compartida' to boolean
        try:
            shared = Conditional[watersheed[6]]
        except KeyError: 
            cuencomp = False
            print u'Validar el estado compartido de la cuenca %s' %(watersheed[6])
        # Maybe 'Cuenca' Already exists
        i+= 1
        print i
        if len(macro) != 0:
            obt, created = cuencadescr.objects.get_or_create(cuencano = watersheed[3], cuencodi = code,
                               defaults = {
                                    'macrocue': macro[0],
                                    'cuensubc': subcode, 
                                    'cuenprio': watersheed[1],
                                    'cuennive': watersheed[4],
                                    'cuenarea': watersheed[5],
                                    'cuencomp': watersheed[6],
                                    'cuenobse': watersheed[7][0:-2],
                               }
                            )
            if not created:
                try: 
                    print u'La Cuenca %s ya aparece en el sistema'%(watersheed[3].encode('utf-8'))
                except UnicodeDecodeError:
                    print u'Recordar corregir el error de ASCII'

def SetExcelCuencas(excel_addr):
    return 

def SetExcelCompart(excel_addr):
    def GetCorpoPlace(number):
        return ((number*3)+1)+8
    def GetCrossCorpoNames(sheet):
        '''
        There are 30 coporations'
        Objects will be taken as the excel file order
        ''' 
        corporation = {}
        for i in range(30):
            rowtosearch = ((i*3)+1)+8
            corpo = sheet.cell_value(colx = rowtosearch, rowx = 0)
            corporation[corpo] = corporaname.objects.filter(corposig = corpo)[0]
        return corporation
    def GetCuenca(codec):
        try:
            codec = codec.split('-')
        except AttributeError:
            cuenccode = int(codec)
            cuencsubcode = None
            pass
        else:
            cuenccode = int(codec[0])
            try:
                cuencsubcode = int(codec[1])
            except IndexError:
                cuencsubcode = None
        return cuencadescr.objects.get(cuencodi = cuenccode, cuensubc = cuencsubcode)
    def SetCuencaCorpo(sheet, corporacion, cuenca, rowini):
        '''
        Recorrer el excel y cruzar entre corporación y cuenca
        corporacion is a dictionary and is unordered
        TODO: when avaliable through new version switch from get_or_create to update_or_create
        '''
        print cuenca
        #Horizontal search
        for i in range(30):
            rowtosearch = GetCorpoPlace(i)
            if sheet.cell_value(colx = rowtosearch, rowx = rowini) == 1:
                corpo = corporacion[sheet.cell_value(colx = rowtosearch, rowx = 0)]
                area = sheet.cell_value(colx = rowtosearch+1, rowx = rowini)
                if area == '':
                    area = 0
                percn = sheet.cell_value(colx = rowtosearch+2, rowx = rowini)
                if percn == '':
                    percn = 0
                shared, created = cuencompart.objects.get_or_create(
                    cuencano = cuenca, 
                    cuencomp = corpo,
                    defaults = { 
                        'comparea' : area,
                        'compporc' : percn,
                    }
                )
                if not created:
                    print u'La cuenca % ya está asociada para la corporacion %s' % (cuenca, corpo)
    excel_file = xlrd.open_workbook(excel_addr)
    excel_sheet = excel_file.sheet_by_index(2)
    corporation = GetCrossCorpoNames(excel_sheet)
    rowini = 2
    #Vertical search
    while rowini <= (excel_sheet.nrows - 2):
        codecuenc = excel_sheet.cell_value(colx = 2, rowx = rowini)
        watersheed = GetCuenca(codecuenc)
        SetCuencaCorpo(excel_sheet, corporation, watersheed, rowini)
        rowini += 1
