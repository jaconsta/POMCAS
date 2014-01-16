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
    inicartscat, inicartstra, inicartshdr, inicartsrlv, inicartsete#Cartografía base
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

def GetResume(user, shared_id, subcompo):
    '''
    Get quantity of forms filled by the corporation for the subcompo
    '''
    formlist = {
        u'Cartografia' : inidcardatg,
        u'Imagenes' : inidimagsat,
        u'Fotografias' : inidfotogra,
        u'Suelos' : inidsuestud,
        u'Hidrologia' : inidhlestud,
        u'Variabilida' : inidhlvarib,
        u'CalcuCaudal' : inidhlcauda,
        u'Hidrogeologia' : inidhgestud,
        u'CalidadDeAgua' : inidcaestud,
        u'CargasContaminantes' : inidccestud,
        u'Cobertura' : inidcoestud,
        u'FloraYFauna' : inidffestud,
        u'PMEcosistemas' : inidpmestud,
        u'Amenazas' : inriesamepr,
        u'Riesgos' : inidriestud,
        u'seActoresSoc' : inidseasinf,
        u'seEstrParticip' : inidseepinf,
        u'seParticComuEtnicas' : inidseceinf,
        u'seDiagSocioEconom' : inidsedsinf,
        u'seCaractCultural' : inidseccinf,
        u'seValorServicEcos' : inidsevsinf,
        u'seRelaFuncUrbaRegio' : inidserfinf,
    }
    #It's based in the user, should be the corporation
    if subcompo == 'Amenazas':
        return formlist[subcompo].objects.filter(
            iniescue = shared_id,
            inieswho = user,
        )

    return formlist[subcompo].objects.filter(
        iniescue = shared_id,
        inieswho = user,
        inidsubc = subcompo,
    )

def GetSubtopicResume(subcompo, subtemas):
    '''
    Get All subtopics corresponding to a form
    The object returns, for the form requested (subcompo_id), a tuple which
      contains tuples with this elements:
      First: Title of the sub-topic
      Second: The query array
    '''
    subtopic = []
    subtree = {
        u'Cartografia' : (
            (u'Subtema catastro', u'SubCatastro', 'inicartscat', True), 
            (u'Subtema transporte', u'SubTranspor', 'inicartstra', True), 
            (u'Subtema hidrología', u'SubHidrolog', 'inicartshdr', True), 
            (u'Subtema relieve', u'SubeRelive', 'inicartsrlv', True), 
            (u'Subtema entidades territoriales', u'SubEntidade', 'inicartsete', True),
        ),
        u'Imagenes' : (None),
        u'Fotografias' : (None),
        u'Suelos' : (
            (u'Metodología del estudio de Geomorfología', 
                u'MetodGeomor', 'inidsumegeo', False), 
            (u'Metodología del estudio de suelos', 
                u'MetodSuelos', 'inidsumesue', False), 
            (u'Información general cartográfica y documentos técnicos \
                relacionados por cada tipo de amenaza en la cuenca', 
                u'DocumYCarto', 'inidcartog', True),
        ),
        u'Hidrologia' : (
            (u'Metodología del estudio', u'Metodologia', 'inidhlmetod', False), 
            (u'Información general cartográfica y documentos técnicos \
                relacionados por cada tipo de amenaza en la cuenca', 
                u'DocumYCarto', 'inidcartog', True),#inidhlcarto), 
            #(u'Estudios de variabilidad climática', u'Variabilida', inidhlvarib, False), 
            #(u'Cálculos de caudal ambiental', u'CalcuCaudal', inidhlcauda, False),
        ),
        u'Variabilida' : (None),
        u'CalcuCaudal' : (None),
        u'Hidrogeologia' : (
            (u'Metodología del estudio', u'Metodologia', 'inidhgmetho', False), 
            (u'Información general cartográfica y documentos técnicos \
                relacionados por cada tipo de amenaza en la cuenca', 
                u'DocumYCarto', 'inidcartog', True),#inidhgcarto),
        ),
        u'CalidadDeAgua' : (
            (u'Metodología del estudio', u'Metodologia', 'inidcameth', False), 
            (u'Información del estudio', u'InfoEstudio', 'inicainfoes', False), 
            (u'Información complementaria', u'InfoComplem', 'inicainfoco', False),
        ),
        u'CargasContaminantes': (
            (u'Metodología del estudio', u'Metodologia', 'inidccmetho', False), 
            (u'Información del estudio', u'InfoEstudio', 'inidccminfe', False),
            (u'Información complementaria', u'InfoComplem', 'iniccicompl', False),
        ),
        u'Cobertura' : (
            (u'Metodología del estudio', u'Metodologia', 'inidcometho', False), 
            (u'Información general cartográfica y documentos técnicos \
                relacionados por cada tipo de amenaza en la cuenca', 
                u'DocumYCarto', 'inidcartog', True),#inidcoinfog), 
            (u'Análisis multitemporales', u'AnaliMultit', 'inidcoanmul', False),
        ),
        u'FloraYFauna' : (
            (u'Metodología del estudio', u'Metodologia', 'inidffmeth', False), 
            (u'Información general cartográfica y documentos técnicos \
                relacionados por cada tipo de amenaza en la cuenca', 
                u'DocumYCarto', 'inidcartog', True),#inidffcart),
        ),
        u'PMEcosistemas' : (
            (u'Formulación de los planes', u'Formulacion', 'inidpmecofo', False), 
            (u'Información de los planes y resultados', u'InforPlanes',  'inidcartog', True),#inidpmecopm),
        ),
        u'Amenazas' : (
            (u'Actores involucrados', u'Actores', 'inriesameac', True),
        ),
        u'Riesgos' : (
            (u'Información general cartográfica y documentos técnicos \
                relacionados por cada tipo de amenaza en la cuenca', 
                u'DocumYCarto',  'inidcartog', True),#inidriescar),
        ),
        u'seActoresSoc' : (
            (u'Detalle de la información', u'Detalle', 'inidseasdet', False),
        ),
        u'seEstrParticip' : (
            (u'Detalle de la información', u'Detalle', 'inidseepdet', False),
        ),
        u'seParticComuEtnicas' : (
            (u'Detalle de la información', u'Detalle', 'inidsecedet', False),
        ),
        u'seDiagSocioEconom' : (
            (u'Detalle de la información', u'Detalle', 'inidsdsedet', False),
        ),
        u'seCaractCultural' : (
            (u'Detalle de la información', u'Detalle', 'inidseccdet', False),
        ),
        u'seValorServicEcos' : (
            (u'Detalle de la información', u'Detalle', 'inidsevsdet', False),
        ),
        u'seRelaFuncUrbaRegio' : (
            (u'Detalle de la información', u'Detalle', 'inidserfdet', False),
        ),
    }
    for topic in subtree[subcompo]:
        try: 
            if not topic[3]: #If OneToOneField
                topicquery = [eval('subtemas.%s' % (topic[2]))]#topicquery = [subtemas.topic[2]]
            elif subcompo == 'Cartografia':
                topicquery = eval('subtemas.inicartsubt_set.filter(icarsnam=\'%s\')'% (topic[1]))
            else:
                topicquery = eval('subtemas.%s_set.all()' % (topic[2]))#topicquery = subtemas.topic[2].all()
        except ObjectDoesNotExist:
            topicquery = []
        subtopic.append({
            u'title': topic[0],
            u'modelname': topic[1], 
            u'subtopic': topicquery,
            u'add': topic[3],
        })
    return subtopic

def GetSubtopicFK(pk):
    return inidcardatg.objects.get(pk=pk)
