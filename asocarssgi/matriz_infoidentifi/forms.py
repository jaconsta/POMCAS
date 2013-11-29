#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# Copyright 2013-2014 ASOCARS
#
'''
'''

from django.forms import ModelForm

#from cuencas.views import GetUserWatersheed
#from corporacion.views import GetUserCorpo
from matriz_infoidentifi.models import inidcardatg, inicartdatf, inicartsubt, \
    inicartscat, inicartstra, inicartshdr, inicartsrlv, inicartsete#Cartografía base
from matriz_infoidentifi.models import inidimagsat #Imágenes
from matriz_infoidentifi.models import inidfotogra #Fotogragías
from matriz_infoidentifi.models import inidsuestud, inidsumegeo, inidsumesue, \
    inidsuinfor #Suelos
from matriz_infoidentifi.models import inidhlestud, inidhlmetod, inidhlcarto, \
    inidhlinfor, ihlmethafor #Hidrología
from matriz_infoidentifi.models import inidhgestud, inidhgmetho, inidhgcarto #Hidrogeología
from matriz_infoidentifi.models import inidcaestud, inidcameth, inidcamecam, \
    inicainfoes, inicainfgeo, inicainfoco, inicaicca #Calidad de Agua
from matriz_infoidentifi.models import inidccestud, inidccmetho, inidccminfe, \
    inidccmigeo, iniccicompl #Cargas Contaminantes
from matriz_infoidentifi.models import inidcoestud, inidcometho, inidcoinfog #Cobertura
from matriz_infoidentifi.models import inidffestud, inidffmeth, inidffcart #Flora y Fauna
from matriz_infoidentifi.models import inidpmestud, inidpmecofo, pmecoplanma, \
    inidpmecopm #PM Ecosistemas
from matriz_infoidentifi.models import inidriestud #Riesgos
from matriz_infoidentifi.models import inidseasinf, inidseasdet #Socioeconómico - Actores Sociales
from matriz_infoidentifi.models import inidseepinf, inidseepdet #Socioeconómico - Estrategia de Participación
from matriz_infoidentifi.models import inidseceinf, inidsecedet #Socioeconómico - Participación de comunidades étnicas 
from matriz_infoidentifi.models import inidsedsinf, inidsdsedet #Socioeconómico - Diagnósticos Socioeconómicos
from matriz_infoidentifi.models import inidseccinf, inidseccdet #Socioeconómico - Caracterización Cultural
from matriz_infoidentifi.models import inidsevsinf, inidsevsdet #Socioeconómico - Valoración de Servicios Ecosistémicos
from matriz_infoidentifi.models import inidserfinf, inidserfdet #Socioeconómico - Relaciones funcionales urbano- regionales

class CartografiaForm(ModelForm):
    class Meta:
        model = inidcardatg
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 
#        fields = [
#            'icartess',
#            'icartnum',
#            'icartres',
#            'icartcug',
#            'icartcua',
#            'icartcup',
#            'icartfor',
#            'icartfex',
#            'icartrco',
#            'icartrre',
#            'icartror',
#            'icartrda',
#            'icartesc',
#            'icartlic',
#        ]

class ImagenesForm(ModelForm):
    class Meta:
        model = inidimagsat
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 
#        fields = [
#            'iimanomb',
#            'iimasens',
#            'iimaseno',
#            'iimadate',
#            'iimacubr',
#            'iimacubd',
#            'iimacuba',
#            'iimacubp',
#            'iimaform',
#            'iimafore',
#            'iimaresc',
#            'iimaresr',
#            'iimareoc',
#            'iimareda',
#            'iimabanp',
#            'iimabanc',
#            'iimabanm',
#            'iimarese',
#            'iimacsix',
#            'iimacsiy',
#            'iimacidx',
#            'iimacidy',
#            'iimanubp',
#            'iimalice',
#            'iimafaut',
#            'iimaflug',
#            'iimafano',
#            'iimaftam',
#        ]

class FotografiasForm(ModelForm):
    class Meta:
        model = inidfotogra
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 
#        fields = [
#            'ifonombr',
#            'ifoformf',
#            'ifoforme',
#            'ifoinivu',
#            'ifofinvu',
#            'ifonumes',
#            'ifoescaf',
#            'ifotipoc',
#            'ifoaltvu',
#            'ifonumfo',
#            'ifopunfo',
#            'ifoanubp',
#            'ifoacuba',
#            'ifoacubp',
#            'ifoaresc',
#            'ifoaresr',
#            'ifoareoc',
#            'ifoareda',
#            'ifoalice',
#            'ifoafaut',
#            'ifoaflug',
#            'ifoafano',
#            'ifoaftam',
#        ]

class SuelosForm(ModelForm):
    class Meta:
        model = inidsuestud
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 
#        fields = [
#            'inidnomb',
#            'inidlocf',
#            'inidfunc',
#            'inidubig',
#            'inidareh',
#            'inidporc',
#            'inidauth',
#            'inidanor',
#            'inidanop',
#        ]

class HidrologiaForm(ModelForm):
    class Meta:
        model = inidhlestud
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 
#        fields = [
#            'inidnomb',
#            'inidlocf',
#            'inidfunc',
#            'inidubig',
#            'inidareh',
#            'inidporc',
#            'inidauth',
#            'inidanor',
#            'inidanop',
#        ]

class HidrogeologiaForm(ModelForm):
    class Meta:
        model = inidhgestud
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 
#        fields = [
#            'inidnomb',
#            'inidlocf',
#            'inidfunc',
#            'inidubig',
#            'inidareh',
#            'inidporc',
#            'inidauth',
#            'inidanor',
#            'inidanop',
#        ]

class CalidadDeAguaForm(ModelForm):
    class Meta:
        model = inidcaestud
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 
#        fields = [
#            'inidnomb',
#            'inidlocf',
#            'inidfunc',
#            'inidubig',
#            'inidareh',
#            'inidporc',
#            'inidauth',
#            'inidanor',
#            'inidanop',
#        ]

class CargasContaminantesForm(ModelForm):
    class Meta:
        model = inidccestud
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 
#        fields = [
#            'inidnomb',
#            'inidlocf',
#            'inidfunc',
#            'inidubig',
#            'inidareh',
#            'inidporc',
#            'inidauth',
#            'inidanor',
#            'inidanop',
#            'inidaalb',
#        ]

class CoberturaForm(ModelForm):
    class Meta:
        model = inidcoestud
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 
#        fields = [
#            'inidnomb',
#            'inidlocf',
#            'inidfunc',
#            'inidubig',
#            'inidareh',
#            'inidporc',
#            'inidauth',
#            'inidanor',
#            'inidanop',
#            'inidaalb',
#        ]

class FloraYFaunaForm(ModelForm):
    class Meta:
        model = inidffestud
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 
#        fields = [
#            'inidnomb',
#            'inidlocf',
#            'inidfunc',
#            'inidubig',
#            'inidareh',
#            'inidporc',
#            'inidauth',
#            'inidanor',
#            'inidanop',
#            'inidaalb',
#        ]

class PMEcosistemasForm(ModelForm):
    class Meta:
        model = inidpmestud
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 
#        fields = [
#            'inidnomb',
#            'inidlocf',
#            'inidfunc',
#            'inidubig',
#            'inidareh',
#            'inidporc',
#            'inidauth',
#            'inidanor',
#            'inidanop',
#            'inidaalb',
#        ]

class RiesgosForm(ModelForm):
    class Meta:
        model = inidriestud
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 
#        fields = [
#            'inidnomb',
#            'inidlocf',
#            'inidfunc',
#            'inidubig',
#            'inidareh',
#            'inidporc',
#            'inidauth',
#            'inidanor',
#            'inidanop',
#            'inidaalb',
#        ]

class seActoresSocForm(ModelForm):
    class Meta:
        model = inidseasinf
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 
#        fields = [
#            'iniescor',
#            'iniescue',
#            'isocinfo',
#            'isocubic',
#            'isocauto',
#            'isocanoe',
#            'isocdocu',
#        ]

class seEstrParticipForm(ModelForm):
    class Meta:
        model = inidseepinf
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 
#        fields = [
#            'iniescor',
#            'iniescue',
#            'isocinfo',
#            'isocubic',
#            'isocauto',
#            'isocanoe',
#            'isocdocu',
#        ]

class seParticComuEtnicasForm(ModelForm):
    class Meta:
        model = inidseceinf
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 
#        fields = [
#            'iniescor',
#            'iniescue',
#            'isocinfo',
#            'isocubic',
#            'isocauto',
#            'isocanoe',
#            'isocdocu',
#        ]

class seDiagSocioEconomForm(ModelForm):
    class Meta:
        model = inidsedsinf
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 
#        fields = [
#            'iniescor',
#            'iniescue',
#            'isocinfo',
#            'isocubic',
#            'isocauto',
#            'isocanoe',
#            'isocdocu',
#        ]

class seCaractCulturalForm(ModelForm):
    class Meta:
        model = inidseccinf
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 
#        fields = [
#            'iniescor',
#            'iniescue',
#            'isocinfo',
#            'isocubic',
#            'isocauto',
#            'isocanoe',
#            'isocdocu',
#        ]

class seValorServicEcosForm(ModelForm):
    class Meta:
        model = inidsevsinf
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 
#        fields = [
#            'iniescor',
#            'iniescue',
#            'isocinfo',
#            'isocubic',
#            'isocauto',
#            'isocanoe',
#            'isocdocu',
#        ]

class seRelaFuncUrbaRegioForm(ModelForm):
    class Meta:
        model = inidserfinf
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 
#        fields = [
#            'iniescor',
#            'iniescue',
#            'isocinfo',
#            'isocubic',
#            'isocauto',
#            'isocanoe',
#            'isocdocu',
#        ]

#class GetUserAttr(request, shared_id):
#    def __init__(self):
#        self.user = request.User
#        self.corpora = GetUserCorpo(request.user)
#        self.watersheed = GetUserWatersheed(corpora, shared_id)

#Calling the forms
def add_cartografia(request):
    if request.method == 'POST':
        form = CartografiaForm(request.POST)
        if form.is_valid():
            return 
    else:
        form = CartografiaForm()
        return render(request, 'form.html', {
            'form': form,
        })

def add_imagenes(request):
    pass

def add_fotografias(request):
    pass

def add_suelos(request):
    pass

def add_hidrologia(request):
    pass

def add_hidrogeologia(request):
    pass

def add_calidaddeagua(request):
    pass

def add_cargascontaminantes(request):
    pass

def add_cobertura(request):
    pass

def add_florayfauna(request):
    pass

def add_pmecosistemas(request):
    pass

def add_riesgos(request):
    pass

def add_seactoressoc(request):
    pass

def add_seestrparticip(request):
    pass

def add_separticcomuetnicas(request):
    pass

def add_sediagsocioeconom(request):
    pass

def add_secaractcultural(request):
    pass

def add_sevalorservicecos(request):
    pass

def add_serelafuncurbaregio(request):
    pass

