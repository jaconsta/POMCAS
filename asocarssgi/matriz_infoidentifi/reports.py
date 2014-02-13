#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# Copyright 2013-2014 ASOCARS
#
'''
'''

from django.forms import ModelForm
from django.core.exceptions import ObjectDoesNotExist

from corporacion.views import GetUserCorpo
from matriz_infoidentifi.models import inforcompon, inforconcep, inforindice #General info
from matriz_infoidentifi.models import inididestud, inidcartog #Source of all proxies
from matriz_infoidentifi.models import inidcardatg, inicartdatf, \
    inicartscat, inicartstra, inicartshdr, inicartsrlv, inicartsete #Cartografía base
from matriz_infoidentifi.models import inidimagsat #Imágenes
from matriz_infoidentifi.models import inidfotogra #Fotogragías
from matriz_infoidentifi.models import inidsuestud, inidsumegeo, inidsumegea, \
    inidsumesue, inidsuinfor #Suelos
from matriz_infoidentifi.models import inidhlestud, inidhlmetod,  ihlmethaest, \
    ihlmethafor, inidhlcarto, inidhlvarib, inidhlcauda #Hidrología
from matriz_infoidentifi.models import inidhgestud, inighgmetfa, inidhgmetho, \
    inidhgmmoma, inidhgcarto #Hidrogeología
from matriz_infoidentifi.models import inidcaestud, inidcameth, inidcamecam, \
    inicainfoes, inicainflab, inicainfgeo, incainfpara, inicainfoco, inicaicca #Calidad de Agua
from matriz_infoidentifi.models import inidccestud, inidccmetho, inidccminfe, \
    iniccinflab, inidccmigeo, iniccicompl, iniccicomps #Cargas Contaminantes
from matriz_infoidentifi.models import inidcoestud, inidcometho, inidcoinfog, \
    inidcoanmul #Cobertura
from matriz_infoidentifi.models import inidffestud, inidffmeth, inidffcart #Flora y Fauna
from matriz_infoidentifi.models import inidpmestud, inidpmecofo, pmecoplanma, \
    inidpmecopm #PM Ecosistemas
from matriz_infoidentifi.models import inriesamepr,amenaidenti, \
    eventocurri, elemenexpue, inriesameac #Riesgos - Amenazas inidriesame, 
from matriz_infoidentifi.models import inidriestud, inidriescar #Riesgos - Estudios
from matriz_infoidentifi.models import inidseasinf, inidseasdet #Socioeconómico - Actores Sociales
from matriz_infoidentifi.models import inidseepinf, inidseepdet, inidseepdin #Socioeconómico - Estrategia de Participación
from matriz_infoidentifi.models import inidseceinf, inidsecedet, inidsecedat #Socioeconómico - Participación de comunidades étnicas 
from matriz_infoidentifi.models import inidsedsinf, inidsdsedet, inidsedsvar, \
    inidsedsser, inidsedsact #Socioeconómico - Diagnósticos Socioeconómicos
from matriz_infoidentifi.models import inidseccinf, inidseccdet, inidseccdcc #Socioeconómico - Caracterización Cultural
from matriz_infoidentifi.models import inidsevsinf, inidsevsdet, inidseserec #Socioeconómico - Valoración de Servicios Ecosistémicos
from matriz_infoidentifi.models import inidserfinf, inidserfdet, inidserfure #Socioeconómico - Relaciones funcionales urbano- regionales

def FormsFilled():
    '''
    Returns the number of all the formats filled
    As it's not in the database It'll be hardcoded here
    Query: 
    '''
    forms = []
    forms.append(inidcardatg.objects.count())
    forms.append(inidimagsat.objects.count())
    forms.append(inidfotogra.objects.count())
    forms.append(inididestud.objects.count())
    return sum(forms)

def CorporationsWhoCartografia():
    '''
    Returns the names of the corporations who have filled
     the Cartografia form
    Query: 
    '''
    return inidcardatg.objects.order_by('iniescor__corposig').distinct('iniescor__corposig')

def CorporationsCartografiaFilled():
    '''
    Returns the absolute number of corporations who have filled the 
     Cartografia form
    As the table will never be big enough, the extra query implied in the function 
     bellow won't affect that much
    Query: select count(distinct(inieswho_id)) from matriz_infoidentifi_inidcardatg;
    '''
    return CorporationsWhoCartografia().count() #inidcardatg.objects.order_by('iniescor').distinct('iniescor').count() 

def CorporationsScaleCartografia():
    '''
    Returns the grid scales reported by each Corporation
    Query: 
    '''
    corposcale = []
    corporations = CorporationsWhoCartografia()
    for corpora in corporations:
        scale = inidcardatg.objects.filter(iniescor = corpora.iniescor)
        corposcale.append((corpora, scale))
    return corposcale
    
def WatersheedWhoCartografia():
    '''
    Returns those grid forms classified by watersheeds
    Query: select * from cuencas_cuencadescr where id in (
        select distinct(cuencano_id) from cuencas_cuencompart where id in (
         select iniescue_id from matriz_infoidentifi_inidcardatg));
    '''
    return inidcardatg.objects.order_by('iniescue__cuencano').distinct('iniescue__cuencano') 

#def WatersheedWhoNamesCartografia():
#    '''
#    Return the names of those watersheeds with grid forms filled
#    '''

def WatersheedCartografiaResume():
    '''
    Returns matrix with the following column order
    [inidcardatf.watersheed object, Is official?, 25000 grids,
        25000 coverage, 10000 grids, 10000 coverage]
    Responds all questions in a single matriz
    # 1st. Get all the waterwheeds (Q: 1,2)
    # 2nd. On each ask if it has official gridsgrids  (Q: 3)
    # 3rd. On them get the avaliable scales and values (Q: 4,5)
    # 4rd. Calculate the covered percentage of all distinct grids 
    #   against the watersheed total area(Q: 6)
    # 5th. Q:7 Sure!... Why not? wait maybe... later 
    1:25.000  15.000 ha
    1:10.000  3.750 ha
    '''
    def GetClassifyGrids(grids):
        # Group on 10:000
        ten = []
        for grid in grids.filter(icartess = 2): 
            ten.append(grid)  
        # Group on 25.000
        for grid in grids.filter(icartess = 1): 
            twenty.append(grid)
    def GetOfficial(watersheed):
        for j in  inidcardatg.objects.filter(iniescue__cuencano = i.iniescue.cuencano, icartres = 'IGAC'):
            if j:
                return GetClassifyGrids(j)
            else:
                return None
    
    answer = []
    watersheeds = WatersheedWhoCartografia()
    for i in watersheeds:
        GetOfficial(i)
    return answer
def WatersheedCartografiaFilled():
    '''
    Returns the name of the waterwheeds which have Grid Forms filled.
    Query: select count(*) from cuencas_cuencompart where id in (select iniescue_id from matriz_infoidentifi_inidcardatg);
    '''
    return WaterwheedWhoCartografia.count() 

def WatersheedCartoGridsClassif():
    '''
    Classify Grid Scales by watersheed
    '''
    watersheed = []
    for water in WatersheedWhoCartografia():
        grids = inidcardatg.objects.filter(iniescue = water.iniescue).order_by('icartess')
        watersheed.append((water, grids))
    return watersheed

def WatersheedCartoGridsOfficialClassif():
    '''
    Classify Grid Scales by watersheed
     and they have to be official (IGAC)
    inidcardatg.objects.filter(iniescue__cuencano = i.iniescue.cuencano)
    '''
    watersheed = []
    for water in WatersheedWhoCartografia():
        grids = inidcardatg.objects.filter(iniescue = water.iniescue, icartres = u'IGAC').order_by('icartess')
        watersheed.append((water, grids))
    return watersheed

def WatersheedCartoCoveredArea():
    '''
    Returns the area covered by all the grids on each scale avaliable 
     in the watersheed.
    '''
    pass

def dictfetchall(cursor):
    '''
    Returns all rows from a cursor as a dict
    '''
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def LoadCartoProgress():
    '''
    Returns the load progress classified by date
    Query: select to_char(iniesdac, 'mm-dd'), inieswho_id, count(id) from matriz_infoidentifi_inidcardatg group by to_char(iniesdac, 'mm-dd'), inieswho_id;
    '''
    from django.db import connection, transaction
    cursor = connection.cursor()
    cursor.execute("select to_char(iniesdac, 'mm-dd') as iniesdac, inieswho_id as inieswho, count(id) from matriz_infoidentifi_inidcardatg group by to_char(iniesdac, 'mm-dd'), inieswho_id order by to_char(iniesdac, 'mm-dd'), inieswho_id")
    return dictfetchall(cursor) #cursor.fetchall()

