#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# Copyright 2013-2014 ASOCARS
#
'''
'''

from django.forms import ModelForm

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

### Cartografía base ###

class CartografiaForm(ModelForm):
    '''
    Cartografía base
    Datos generales
    '''
    class Meta:
        model = inidcardatg
        fields = ['icartess', 'icartnum', 'icartres', 'icartcug', 
            'incacuba', 'incacubp', 'incaforf', 'incafore', 'incaforo',
            'incarsco', 'incarsre', 'incaroco', 'incardat',
            'icartesc', 'incarlic', 'incaraut', 'incarlug', 'incarano',
        ]

class CartogSubCatastroForm(ModelForm):
    '''
    Cartografía base
    Subtema Cartográfico
    Catastro
    '''
    class Meta:
        model = inicartscat
        fields = ['icarspre', 'icarsexi', 'icarsqua', 'icarsrel',
        ]
class CartogSubTransporForm(ModelForm):
    '''
    Cartografía base
    Subtema Cartográfico
    Transporte
    '''
    class Meta:
        model = inicartstra
        fields = ['icarspre', 'icarsexi', 'icarsqua', 'icarsrel',
        ]
class CartogSubHidrologForm(ModelForm):
    '''
    Cartografía base
    Subtema Cartográfico
    Hidrografía
    '''
    class Meta:
        model = inicartshdr
        fields = ['icarspre', 'icarsexi', 'icarsqua', 'icarsrel',
        ]
class CartogSubeReliveForm(ModelForm):
    '''
    Cartografía base
    Subtema Cartográfico
    Relieve
    '''
    class Meta:
        model = inicartsrlv
        fields = ['icarspre', 'icarsexi', 'icarsqua', 'icarsrel',
        ]
class SubEntidadeForm(ModelForm):
    '''
    Cartografía base
    Subtema Cartográfico
    Entidad territorial y unidad administrativa
    '''
    class Meta:
        model = inicartsete
        fields = ['icarspre', 'icarsexi', 'icarsqua', 'icarsrel',
        ]

### Imágenes ###

class ImagenesForm(ModelForm):
    '''
    Imágenes
    Imágenes de satélite
    '''
    class Meta:
        model = inidimagsat
        fields = ['iimanomb', 'iimasens', 'iimaseno', 'iimadate',
            'iimacubr', 'incacuba', 'incacubp', 'incaforf',
            'incafore', 'incaforo',
            'incarsco', 'incarsre', 'incaroco', 'incardat',
            'iimabanp', 'iimabanc',
            'iimabanm', 'iimarese',
            'iimacsix', 'iimacsiy',
            'iimacidx', 'iimacidy',
            'iimanubp', 'incarlic',
            'incaraut', 'incarlug', 'incarano',
        ]

### Fotogragías ###                           

class FotografiasForm(ModelForm):
    '''
    Fotografías
    Fotografías aereas
    '''
    class Meta:
        model = inidfotogra
        fields = [
            'ifonombr', 'incaforf', 'incafore', 'incaforo',
            'ifonumes', 'ifoescaf', 'ifotipoc', 'ifoaltvu',
            'ifopunfo', 'incacuba', 'incacubp', 'ifoanubp',
            'incarsco', 'incarsre', 'incaroco', 'incardat',
            'incarlic',
            'incaraut', 'incarlug', 'incarano'
        ]

### Suelos ###
class SuelosForm(ModelForm):
    '''
    Suelos
    Identificación del estudio de suelos y/o capacidad
    de uso de la tierra
    '''
    class Meta:
        model = inidsuestud
        fields = [
            'inidnomb', 'iniddocf', 'iniddoce', 'iniddoco', 'inidlocf',
            'inidresp', 'inidumun', 'inidcare', 'inidcper',
            'inidauth', 'inidanit', 'inidsini', 'inidanor', 
        ]

class SuelosMetodGeomorForm(ModelForm):
    '''
    Suelos
    Metodología utilizada para el estudio de Geomorfología
    '''
    class Meta:
        model = inidsumegeo
        fields = [
            'geometod', 'geoclasi', 'geoclaso',
            'geoproce', 'geoproco', 'geoamena', 'geoament', 'geoameno',
        ]
class SuelosMetodSuelosForm(ModelForm):
    '''
    Suelos
    Metodoogía utilizada para el estudio de 
    suelos y/o coberturas de la tierra
    '''
    class Meta:
        model = inidsumesue
        fields = [
            'inisutle', 'inisutlo', 'inisutla', 'inisutln', 'inisutli',
            'inisutge',
        ]
class SuelosDocumYCartoForm(ModelForm):
    '''
    Suelos
    Información general cartográfica y documentos técnicos
    '''
    class Meta:
        model = inidsuinfor
        fields = [
            'carescs', 'caruesle', 'carmafor', 'carmamex', 'carmamot',
            'carmetad', 'carmeaut', 'carmedat', 'carinaso', 
            'carleyen', 'carfuent', 'carqualy',
        ]

### Hidrología ###
class HidrologiaForm(ModelForm):
    '''
    Hidrología
    Identificación del estudio de hidrología y climatología
    '''
    class Meta:
        model = inidhlestud
        fields = ['inidnomb', 'iniddocf', 'iniddoce', 'iniddoco', 'inidlocf',
            'inidresp', 'inidusub', 'inidusec', 'inidutra', 'inidumun', 
            'inidcare', 'inidcper', 'inidauth', 'inidanit', 'inidsini', 
            'inidanor', 'inidanop',
        ]

class HidroloMetodologiaForm(ModelForm):
    '''
    Hidrología
    Metología utilizada para el estudio de hidrología o climatología
    '''
    class Meta:
        model = inidhlmetod
        fields = [
            'inihlppa', 'inihlphd', 'inihlmin', 'inihlpid',
            'inihlcal' ,'inihlcad',
        ]
class HidroloDocumYCartoForm(ModelForm):
    '''
    Hidrología
    Información general cartográfica y documento técnico
    '''
    class Meta:
        model = inidhlcarto
        fields = [
            'carescs', 'caruesle', 'carmafor', 'carmamex', 'carmamot',
            'carmetad', 'carinaso',
        ]
class HidroloVariabilidaForm(ModelForm):
    '''
    Hidrología
    Estudios de variabilidad climática (niño o niña) para la cuenca en estudio    
    '''
    class Meta:
        model = inidhlvarib
        fields = ['inidnomb', 'iniddocf', 'iniddoce', 'iniddoco', 'inidlocf',
            'inidresp', 'inidusub', 'inidusec', 'inidutra', 'inidumun', 
            'inidcare', 'inidcper', 'inidauth', 'inidanit', 'inidsini', 
            'inidanor', 'inidanop',
        ]
class HidroloCalcuCaudalForm(ModelForm):
    '''
    Hidrología
    Calculos de caudal ambiental
    '''
    class Meta:
        model = inidhlcauda
        fields = ['inidnomb', 'iniddocf', 'iniddoce', 'iniddoco', 'inidlocf',
            'inidresp', 'inidusub', 'inidusec', 'inidutra', 'inidumun', 
            'inidcare', 'inidcper', 'inidauth', 'inidanit', 'inidsini', 
            'inidanor', 'inidanop',
        ]

### Hidrogeología ###
class HidrogeologiaForm(ModelForm):
    '''
    Hidrogeología
    Identificación del estudio de hidrogeología
    '''
    class Meta:
        model = inidhgestud
        fields = ['inidnomb', 'iniddocf', 'iniddoce', 'iniddoco', 'inidlocf',
            'inidresp', 'inidumun', 'inidcare', 'inidcper', 
            'inidauth', 'inidanit', 'inidanor', 'inidanop',
        ]

class HidrogeoMetodologiaForm(ModelForm):
    '''
    Hidrogeología
    Metodología utilizada para el estudio de hidrogeología
    '''
    class Meta:
        model = inidhgmetho
        fields = [
            'inhgdbpa', 'inhgdbpu', 'inhgdbat', 'inhgdbac', 'inhgdbpa',
            'inhgquye', 'inhgqunc', 'inhgqupa', 'inhgceah', 'inhgahpo',
            'inhglaba', 'inhglabn', 'inhglabi', 'inghesgg', 'inhgeggn', 
            'inghegme', 'inghacui', 'inghaces', 'inghacre', 'inghacrs', 
            'inghchdr', 'inghchme', 'inghchpo', 'inghries', 'inghcaco',
            'inghvuln', 'inghvume', 'inghcupr', 'inghmhco', 'inghmhci',
            'inghtacu','inghagsu','inghasnp', 'inghasco', 
            'inghmoma', 'inghmomo',
        ]
class HidrogeoDocumYCartoForm(ModelForm):
    '''
    Hidrogeología
    Información general cartográfica y documento técnico
    '''
    class Meta:
        model = inidhgcarto
        fields = [
            'carescs', 'caruesle', 'carmafor', 'carmamex', 'carmamot',
            'carmetad', 'carinaso',
        ]

### Calidad de Agua ###
class CalidadDeAguaForm(ModelForm):
    '''
    Calidad de Agua
    Identificación del estudio de calidad y recurso hídrico
    '''
    class Meta:
        model = inidcaestud
        fields = ['inidnomb', 'iniddocf', 'iniddoce', 'iniddoco',
            'inidlocf', 'inidresp', 'inidudep', 'inidumun', 'inidcare',
            'inidcper', 'inidauth', 'inidanit', 'inidanor', 'inidanop',
        ]

class CaliAguaMetodologiaForm(ModelForm):
    '''
    Calidad de Agua
    Metología del estudio, levantamiento de datos y resultados
    '''
    class Meta:
        model = inidcameth
        fields = [
            'inidcala', 'inicaobj', 'inicamet', 'inicaest',
            'inicacan', 'inicacaa', 'inicaiex',
            'inicaitr', 'inicaima', 'inicaime', 'inicaimf',
            'inicaimx', 'inicaixo',
        ]
class CaliAguaInfoEstudioForm(ModelForm):
    '''
    Calidad de Agua
    Información que debe contener el estudio
    '''
    class Meta:
        model = inicainfoes
        fields = [
            'iicaiinf', 'iicaiafa', 'iicaiest', 'iicaiobs',
            'iicaipar', 'iicaipao', 
        ]
class CaliAguaInfoComplemForm(ModelForm):
    '''
    Calidad de Agua
    Información Complementaria
    '''
    class Meta:
        model = inicainfoco
        fields = [
            'iicaifoc', 'iicaifca',
        ]

### Cargas Contaminantes ###
class CargasContaminantesForm(ModelForm):
    '''
    Cargas Contaminantes
    Estudio de cargas contaminantes de DBO y SST vertidas 
    en la subcuenca, tramos y/o corrientes principales
    en la cuenca objeto de ordenación 
    '''
    class Meta:
        model = inidccestud
        fields = ['inidnomb', 'iniddocf', 'iniddoce', 'iniddoco',
            'inidlocf', 'inidresp', 'inidudep', 'inidumun', 'inidcare',
            'inidcper', 'inidauth', 'inidanit', 'inidanor', 'inidanop',
        ]

class CargContMetodologiaForm(ModelForm):
    '''
    Cargas Contaminantes
    Metodología del estudio, levantamiento de datos y resultados
    '''
    class Meta:
        model = inidccmetho
        fields = [
            'iiccmobj', 'iiccmmet', 'iiccmest', 'iiccmlin',
            'iiccmdcc', 'iiccmsum', 'iiccminv', 'iiccmsec',
        ]
class CargContInfoEstudioForm(ModelForm):
    '''
    Cargas Contaminantes
    Información que debe contener el estudio
    '''
    class Meta:
        model = inidccminfe
        fields = [
            'iicciinf', 'iiccigeo', 'iicciobs', 'iicciper',
            'iiccipar', 'iiccipao',
        ]
class CargContInfoComplemForm(ModelForm):
    '''
    Cargas Contaminantes
    Información complementaria
    '''
    class Meta:
        model = iniccicompl 
        fields = [
            'iiccicom', 'iicccmue', 'iicccper', 'iicccprm',
            'iicccpor', 'iicccpse', 'iicccpur', 'iicccpma',
        ]

### Cobertura de la tierra ###
class CoberturaForm(ModelForm):
    '''
    Cobertura de la tierra
    Identificación del estudio / información
    '''
    class Meta:
        model = inidcoestud
        fields = ['inidnomb', 'iniddocf', 'iniddoce', 'iniddoco',
            'inidlocf', 'inidresp', 'inidudep', 'inidumun', 'inidcare',
            'inidcper', 'inidauth', 'inidanit', 'inidanor', 'inidanop',
        ]

class CobertuMetodologiaForm(ModelForm):
    '''
    Cobertura de la tierra
    Metodología utilizada para levantamiento de coberturas
    '''
    class Meta:
        model = inidcometho
        fields =[
            'iicomsen', 'iicomseo', 'iicomfot', 'iicomfoo',
            'iicomimg', 'iicomimo', 'iicomdat', 'iicomniv', 'iicomint',
            'iicomver', 'iicomcfu', 'iicomces', 'iicomcan',
        ]
class CobertuDocumYCartoForm(ModelForm):
    '''
    Cobertura de la tierra
    Información general cartográfica y documento técnico
    '''
    class Meta:
        model = inidcoinfog 
        fields = [
            'carescs', 'caruesle', 'carmafor', 'carmamex', 'carmamot',
            'carmetad', 'carinaso',
        ]
class CobertuAnaliMultitForm(ModelForm):
    '''
    Cobertura de la tierra
    Análisis multitemporales
    '''
    class Meta:
        model = inidcoanmul
        fields = [
            'mulanali', 'mulperio', 'mulmetod', 'mulescal',
        ]

### Flora y Fauna ###
class FloraYFaunaForm(ModelForm):
    '''
    Flora y Fauna
    Identificación del estudio / información
    '''
    class Meta:
        model = inidffestud
        fields = ['inidnomb', 'iniddocf', 'iniddoce', 'iniddoco',
            'inidlocf', 'inidresp', 'inidudep', 'inidumun', 'inidcare',
            'inidcper', 'inidauth', 'inidanit', 'inidanor', 'inidanop',
        ]

class FloFauMetodologiaForm(ModelForm):
    '''
    Flora y Fauna
    Metología utilizada para levantamiento de información
    de flora, vegetación y fauna
    '''
    class Meta:
        model = inidffmeth
        fields = [
            'iffmesm', 'iffmein', 'ifftico', 'iffvegi', 'iffesli',
            'iffnupa', 'iffmeif', 'iffclaj', 'iffgeoi',
            'iffinfc', 'iffamen', 'iffamec', 'iffgeor',
        ]
class FloFauDocumYCartoForm(ModelForm):
    '''
    Flora y Fauna
    Información general del documento técnico y cartografía
    '''
    class Meta:
        model = inidffcart 
        fields = [
            'carmafor', 'carmamex', 'carmamot', 'carmetad', 'carmeaut',
            'carinflo', 'carfuent',
        ]

### PM Ecosistemas ###
class PMEcosistemasForm(ModelForm):
    '''
    Planes de manejo de ecosistemas
    Identificación de los planes de manejo existentes
    '''
    class Meta:
        model = inidpmestud
        fields = ['inidnomb', 'iniddocf', 'iniddoce', 'iniddoco',
            'inidlocf', 'inidresp', 'inidudep', 'inidumun', 'inidcare',
            'inidcper', 'inidauth', 'inidanit', 'inidanor', 'inidanop',
        ]

class PMEecosFormulacionForm(ModelForm):
    '''
    Planes de manejo de ecosistemas
    Formulación del plan y resultados
    '''
    class Meta:
        model = inidpmecofo
        fields = [
            'ipmfplan', 'ipmfplao', 'ipmfobje', 'ipmfadop',
            'ipmfvige', 'ipmfplae',
        ]
class PMEecosInforPlanesForm(ModelForm):
    '''
    Planes de manejo de ecosistemas
    Información sobre los planes de manejo
    '''
    class Meta:
        model = inidpmecopm
        fields = [
            'caruesle', 'caruespu', 'carescs', 'carmafor',
            'carmamex', 'carmamot',
        ]

### Riesgos - Amenazas ###
class AmenazasForm(ModelForm):
    '''
    Identificación de amenazas en la cuenca
    Identificación preeliminar de los sitios con condiciones
    de amenazas y eventos
    '''
    class Meta:
        model = inriesamepr
        fields = ['ameniden', 'amenotra', 'ubidepar',
            'ubimunic', 'ubivered',
            'eventocu', 'eventoot', 'eventrec', 'evencaus',
            'elemento', 'elemotro', 'actosoci', 'activida',
            'amenmapa', 'amengeor',
        ]

class AmenazActoresForm(ModelForm):
    '''
    Identificación de amenazas en la cuenca
    Actores que tienen registros e información
    '''
    class Meta:
        model = inriesameac
        fields = [
            'iactor', 'idyear',
        ]

### Riesgos - Estudios ###
class RiesgosForm(ModelForm):
    '''
    Estudios de riesgos
    Identificación del estudio o informes técnicos por cada 
    tipo de amenaza o evento identificados
    '''
    class Meta:
        model = inidriestud
        fields = ['inidnomb', 'inidlocf', 'inidudep', 'inidumun', 
            'iniduver', 'inidcare', 'inidcper', 'inidauth', 'inidanit', 
            'inidanor', 'inidanop',
        ]

class RiesgoDocumYCartoForm(ModelForm):
    '''
    Estudios de riesgos
    Información general cartográfica y documentos técnicos
    relacionados por cada tipo de amenaza en la cuenca
    '''
    class Meta:
        model = inidriescar
        fields = [
            'carescs', 'caruesle', 'carmafor', 'carmamex', 'carmamot',
            'carmetad', 'carmeaut', 'carmenit', 'carmeinf', 'carmedat', 
            'carinaso', 'cardocfo', 'cardocex', 'cardocot',
        ]

### Socioeconómico - Actores Sociales ###
class seActoresSocForm(ModelForm):
    '''
    Socioeconómico
    Actores Sociales 
    Información general
    '''
    class Meta:
        model = inidseasinf
        fields = ['inidnomb', 'inidlocf', 'inidauth', 'inidanit',
            'inidanor', 'inidanop', 'inidudep', 'inidumun', 'iniduver',
        ]

class seActoDetalleForm(ModelForm):
    '''
    Socioeconómico
    Actores Sociales 
    Detalle de la información
    '''
    class Meta:
        model = inidseasdet 
        fields = [
            'isemetho', 'isemethd', 'isedocum', 'isedocud', 'isedocas',
            'iseactma', 'iseprior', 'isepride', 'isedbact', 'isedbvar',
        ]

### Socioeconómico - Estrategia de Participación ###
class seEstrParticipForm(ModelForm):
    '''
    Socioeconómico
    Estrategia de Participación 
    Información general
    '''
    class Meta:
        model = inidseepinf
        fields = ['inidnomb', 'inidlocf', 'inidauth', 'inidanit',
            'inidanor', 'inidanop', 'inidudep', 'inidumun', 'iniduver',
        ]

class sePartipDetalleForm(ModelForm):
    '''
    Socioeconómico
    Estrategia de Participación 
    Detalle de la información
    '''
    class Meta:
        model = inidseepdet 
        fields = [
            'iseestra', 'isepestr', 'isepestg', 'isepestd',
            'iseppart', 'isepparm', 'isepinst', 'isepcomu', 'isepcomd',
            'isepiamb', 'isepiamd', 'isepesta',
        ]

### Socioeconómico - Participación de comunidades étnicas  ###
class seParticComuEtnicasForm(ModelForm):
    '''
    Socioeconómico
    Participación de comunidades étnicas 
    Información general
    '''
    class Meta:
        model = inidseceinf
        fields = ['inidnomb', 'inidlocf', 'inidauth', 'inidanit',
            'inidanor', 'inidanop', 'inidudep', 'inidumun', 'iniduver',
        ]

class seComuEtnicDetalleForm(ModelForm):
    '''
    Socioeconómico
    Participación de comunidades étnicas 
    Detalle de la información
    '''
    class Meta:
        model = inidsecedet 
        fields = [
            'isepccar', 'isepccaw', 'isepccer', 'isepcdev', 'isepcded',
        ]

### Socioeconómico - Diagnósticos Socioeconómicos ###
class seDiagSocioEconomForm(ModelForm):
    '''
    Socioeconómico
    Diagnósticos Socioeconómicos 
    Información general
    '''
    class Meta:
        model = inidsedsinf
        fields = ['inidnomb', 'inidlocf', 'inidauth', 'inidanit',
            'inidambi', 'inidanor', 'inidanop', 'inidudep', 'inidumun', 
            'iniduver',
        ]

class seDiagSociDetalleForm(ModelForm):
    '''
    Socioeconómico
    Diagnósticos Socioeconómicos 
    Detalle de la información
    '''
    class Meta:
        model = inidsdsedet 
        fields = [
            'iseddina', 'iseddinv', 'iseddino', 'isedserv', 'isedsere',
            'isedsero', 'isedseal', 'isedseai', 'isedsede', 'isedacti',
            'isedactd', 'isedacto', 'isedsitu', 'isedsitd', 'isedproy', 
            'isedprod', 'isedconf', 'isedcond', 'isedpoli', 'isedpold',
            'isedpred', 'isedprec', 'isedsegu', 'isedsegd',
        ]

### Socioeconómico - Caracterización Cultural ###
class seCaractCulturalForm(ModelForm):
    '''
    Socioeconómico
    Caracterización Cultural
    Información general
    '''
    class Meta:
        model = inidseccinf
        fields = ['inidnomb', 'inidlocf', 'inidauth', 'inidanit',
            'inidanor', 'inidanop', 'inidudep', 'inidumun', 'iniduver',
        ]

class seCaraCultDetalleForm(ModelForm):
    '''
    Socioeconómico
    Caracterización Cultural
    Detalle de la información
    '''
    class Meta:
        model = inidseccdet 
        fields = [
            'isecccul', 'isecccuc', 'isecccuv', 'iseccpat','iseccpad',
            'iseccdoc', 'iseccdcc',
        ]

### Socioeconómico - Valoración de Servicios Ecosistémicos ###
class seValorServicEcosForm(ModelForm):
    '''
    Socioeconómico
    Valoración de Servicios Ecosistémicos
    Información general
    '''
    class Meta:
        model = inidsevsinf
        fields = ['inidnomb', 'inidlocf', 'inidauth', 'inidanit',
            'inidanor', 'inidanop', 'inidudep', 'inidumun', 'iniduver',
        ]

class seServEcosDetalleForm(ModelForm):
    '''
    Socioeconómico
    Valoración de Servicios Ecosistémicos
    Detalle de la información
    '''
    class Meta:
        model = inidsevsdet 
        fields = [
            'isesemet', 'iseseser', 'iseseseo', 'isesepil', 'isesepia',
        ]

### Socioeconómico - Relaciones funcionales urbano- regionales ###
class seRelaFuncUrbaRegioForm(ModelForm):
    '''
    Socioeconómico
    Relaciones funcionales urbano- regionales
    Información general
    '''
    class Meta:
        model = inidserfinf
        fields = ['inidnomb', 'inidlocf', 'inidauth', 'inidanit',
            'inidambi', 'inidanor', 'inidanop', 'inidudep', 'inidumun', 
            'iniduver',
        ]

class seRFUrbRegDetalleForm(ModelForm):
    '''
    Socioeconómico
    Relaciones funcionales urbano- regionales
    Detalle de la información
    '''
    class Meta:
        model = inidserfdet 
        fields = [
            'infucomp', 'infucone', 'infoconc', 'infocona', 'infocapa',
            'infocapo', 'infocapl',
        ]

##class GetUserAttr(request, shared_id):
##    def __init__(self):
##        self.user = request.User
##        self.corpora = GetUserCorpo(request.user)
##        self.watersheed = GetUserWatersheed(corpora, shared_id)
#
##Calling the forms
#def add_cartografia(request):
#    if request.method == 'POST':
#        form = CartografiaForm(request.POST)
#        if form.is_valid():
#            return 
#    else:
#        form = CartografiaForm()
#        return render(request, 'form.html', {
#            'form': form,
#        })
