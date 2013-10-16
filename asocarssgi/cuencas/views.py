# -*- coding: utf-8 -*-
from cuencas.models import *

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
        print watersheed[0]
        print watersheed[1]
        print code
        print subcode
        print watersheed[3]
        print watersheed[4]
        print watersheed[5]
        print watersheed[6]
        print watersheed[7][0:-2]
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
                print u'La Cuenca %s ya aparece en el sistema' % (watersheed[3])

def SetExcelCuencas(excel_file):
    return 
