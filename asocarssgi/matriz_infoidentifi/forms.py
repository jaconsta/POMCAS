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
from matriz_infoidentifi.models import inidcardatg, inicartdatf, \
    inicartscat, inicartstra#, inicartshdr, inicartsrlv, inicartsete#Cartografía base
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

class ImagenesForm(ModelForm):
    class Meta:
        model = inidimagsat
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 

class FotografiasForm(ModelForm):
    class Meta:
        model = inidfotogra
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 

class SuelosForm(ModelForm):
    class Meta:
        model = inidsuestud
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 

class HidrologiaForm(ModelForm):
    class Meta:
        model = inidhlestud
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 

class HidrogeologiaForm(ModelForm):
    class Meta:
        model = inidhgestud
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 

class CalidadDeAguaForm(ModelForm):
    class Meta:
        model = inidcaestud
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 

class CargasContaminantesForm(ModelForm):
    class Meta:
        model = inidccestud
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 

class CoberturaForm(ModelForm):
    class Meta:
        model = inidcoestud
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 

class FloraYFaunaForm(ModelForm):
    class Meta:
        model = inidffestud
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 

class PMEcosistemasForm(ModelForm):
    class Meta:
        model = inidpmestud
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 

class RiesgosForm(ModelForm):
    class Meta:
        model = inidriestud
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 

class seActoresSocForm(ModelForm):
    class Meta:
        model = inidseasinf
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 

class seEstrParticipForm(ModelForm):
    class Meta:
        model = inidseepinf
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 

class seParticComuEtnicasForm(ModelForm):
    class Meta:
        model = inidseceinf
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 

class seDiagSocioEconomForm(ModelForm):
    class Meta:
        model = inidsedsinf
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 

class seCaractCulturalForm(ModelForm):
    class Meta:
        model = inidseccinf
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 

class seValorServicEcosForm(ModelForm):
    class Meta:
        model = inidsevsinf
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 

class seRelaFuncUrbaRegioForm(ModelForm):
    class Meta:
        model = inidserfinf
        exclude = ['iniescor', 'iniescue', 'inieswho', 'inieswhu'] 

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

