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
#from matriz_infoidentifi.models import inidcardatg, inicartdatf, \
#    inicartscat, inicartstra#, inicartshdr, inicartsrlv, inicartsete#Cartografía base
#from matriz_infoidentifi.models import inidimagsat #Imágenes
#from matriz_infoidentifi.models import inidfotogra #Fotogragías
#from matriz_infoidentifi.models import inidsuestud, inidsumegeo, inidsumesue, \
#    inidsuinfor #Suelos
#from matriz_infoidentifi.models import inidhlestud, inidhlmetod, inidhlcarto, \
#    inidhlinfor, ihlmethafor #Hidrología
#from matriz_infoidentifi.models import inidhgestud, inidhgmetho, inidhgcarto #Hidrogeología
#from matriz_infoidentifi.models import inidcaestud, inidcameth, inidcamecam, \
#    inicainfoes, inicainfgeo, inicainfoco, inicaicca #Calidad de Agua
#from matriz_infoidentifi.models import inidccestud, inidccmetho, inidccminfe, \
#    inidccmigeo, iniccicompl #Cargas Contaminantes
#from matriz_infoidentifi.models import inidcoestud, inidcometho, inidcoinfog #Cobertura
#from matriz_infoidentifi.models import inidffestud, inidffmeth, inidffcart #Flora y Fauna
#from matriz_infoidentifi.models import inidpmestud, inidpmecofo, pmecoplanma, \
#    inidpmecopm #PM Ecosistemas
#from matriz_infoidentifi.models import inidriestud #Riesgos
#from matriz_infoidentifi.models import inidseasinf, inidseasdet #Socioeconómico - Actores Sociales
#from matriz_infoidentifi.models import inidseepinf, inidseepdet #Socioeconómico - Estrategia de Participación
#from matriz_infoidentifi.models import inidseceinf, inidsecedet #Socioeconómico - Participación de comunidades étnicas 
#from matriz_infoidentifi.models import inidsedsinf, inidsdsedet #Socioeconómico - Diagnósticos Socioeconómicos
#from matriz_infoidentifi.models import inidseccinf, inidseccdet #Socioeconómico - Caracterización Cultural
#from matriz_infoidentifi.models import inidsevsinf, inidsevsdet #Socioeconómico - Valoración de Servicios Ecosistémicos
#from matriz_infoidentifi.models import inidserfinf, inidserfdet #Socioeconómico - Relaciones funcionales urbano- regionales

class CartografiaForm(ModelForm):
    class Meta:
        model = inidcardatg
        fields = ['icartess', 'icartnum', 'icartres', 'icartcug', 
            'incacuba', 'incacubp', 'incaforf', 'incafore', 'incaforo',
            'incarsco', 'incarsre', 'incaroco', 'incardat',
            'icartesc', 'incarlic', 'incaraut', 'incarlug', 'incarano',
        ]

class ImagenesForm(ModelForm):
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

class FotografiasForm(ModelForm):
    class Meta:
        model = inidfotogra
        fields = [
            'ifonombr', 'incaforf', 'incafore', 'incaforo',
            'ifonumes', 'ifoescaf', 'ifotipoc', 'ifoaltvu',
            'ifopunfo', 'ifoanubp',
            'incarsco', 'incarsre', 'incaroco', 'incardat',
            'incarlic',
            'incaraut', 'incarlug', 'incarano'
        ]

class SuelosForm(ModelForm):
    class Meta:
        model = inidsuestud
        fields = [
            'inidnomb', 'iniddocf', 'iniddoce', 'iniddoco', 'inidlocf',
            'inidresp', 'inidumun', 'inidcare', 'inidcper',
            'inidauth', 'inidanit', 'inidsini', 'inidanor', 
        ]

class HidrologiaForm(ModelForm):
    class Meta:
        model = inidhlestud
        fields = ['inidnomb', 'iniddocf', 'iniddoce', 'iniddoco', 'inidlocf',
            'inidresp', 'inidusub', 'inidusec', 'inidutra', 'inidumun', 
            'inidcare', 'inidcper', 'inidauth', 'inidanit', 'inidsini', 
            'inidanor', 'inidanop',
        ]

class HidrogeologiaForm(ModelForm):
    class Meta:
        model = inidhgestud
        fields = ['inidnomb', 'iniddocf', 'iniddoce', 'iniddoco', 'inidlocf',
            'inidresp', 'inidumun', 'inidcare', 'inidcper', 
            'inidauth', 'inidanit', 'inidanor', 'inidanop',
        ]

class CalidadDeAguaForm(ModelForm):
    class Meta:
        model = inidcaestud
        fields = ['inidnomb', 'iniddocf', 'iniddoce', 'iniddoco',
            'inidlocf', 'inidresp', 'inidudep', 'inidumun', 'inidcare',
            'inidcper', 'inidauth', 'inidanit', 'inidanor', 'inidanop',
        ]

class CargasContaminantesForm(ModelForm):
    class Meta:
        model = inidccestud
        fields = ['inidnomb', 'iniddocf', 'iniddoce', 'iniddoco',
            'inidlocf', 'inidresp', 'inidudep', 'inidumun', 'inidcare',
            'inidcper', 'inidauth', 'inidanit', 'inidanor', 'inidanop',
        ]

class CoberturaForm(ModelForm):
    class Meta:
        model = inidcoestud
        fields = ['inidnomb', 'iniddocf', 'iniddoce', 'iniddoco',
            'inidlocf', 'inidresp', 'inidudep', 'inidumun', 'inidcare',
            'inidcper', 'inidauth', 'inidanit', 'inidanor', 'inidanop',
        ]

class FloraYFaunaForm(ModelForm):
    class Meta:
        model = inidffestud
        fields = ['inidnomb', 'iniddocf', 'iniddoce', 'iniddoco',
            'inidlocf', 'inidresp', 'inidudep', 'inidumun', 'inidcare',
            'inidcper', 'inidauth', 'inidanit', 'inidanor', 'inidanop',
        ]

class PMEcosistemasForm(ModelForm):
    class Meta:
        model = inidpmestud
        fields = ['inidnomb', 'iniddocf', 'iniddoce', 'iniddoco',
            'inidlocf', 'inidresp', 'inidudep', 'inidumun', 'inidcare',
            'inidcper', 'inidauth', 'inidanit', 'inidanor', 'inidanop',
        ]

class AmenazasForm(ModelForm):
    class Meta:
        model = inriesamepr
        fields = ['ameniden', 'amenotra', 'ubidepar',
            'ubimunic', 'ubivered',
            'eventocu', 'eventoot', 'eventrec', 'evencaus',
            'elemento', 'elemotro', 'actosoci', 'activida',
            'amenmapa', 'amengeor',
        ]

class RiesgosForm(ModelForm):
    class Meta:
        model = inidriestud
        fields = ['inidnomb', 'inidlocf', 'inidudep', 'inidumun', 
            'iniduver', 'inidcare', 'inidcper', 'inidauth', 'inidanit', 
            'inidanor', 'inidanop',
        ]

class seActoresSocForm(ModelForm):
    class Meta:
        model = inidseasinf
        fields = ['inidnomb', 'inidlocf', 'inidauth', 'inidanit',
            'inidanor', 'inidanop', 'inidudep', 'inidumun', 'iniduver',
        ]

class seEstrParticipForm(ModelForm):
    class Meta:
        model = inidseepinf
        fields = ['inidnomb', 'inidlocf', 'inidauth', 'inidanit',
            'inidanor', 'inidanop', 'inidudep', 'inidumun', 'iniduver',
        ]

class seParticComuEtnicasForm(ModelForm):
    class Meta:
        model = inidseceinf
        fields = ['inidnomb', 'inidlocf', 'inidauth', 'inidanit',
            'inidanor', 'inidanop', 'inidudep', 'inidumun', 'iniduver',
        ]

class seDiagSocioEconomForm(ModelForm):
    class Meta:
        model = inidsedsinf
        fields = ['inidnomb', 'inidlocf', 'inidauth', 'inidanit',
            'inidambi', 'inidanor', 'inidanop', 'inidudep', 'inidumun', 
            'iniduver',
        ]

class seCaractCulturalForm(ModelForm):
    class Meta:
        model = inidseccinf
        fields = ['inidnomb', 'inidlocf', 'inidauth', 'inidanit',
            'inidanor', 'inidanop', 'inidudep', 'inidumun', 'iniduver',
        ]

class seValorServicEcosForm(ModelForm):
    class Meta:
        model = inidsevsinf
        fields = ['inidnomb', 'inidlocf', 'inidauth', 'inidanit',
            'inidanor', 'inidanop', 'inidudep', 'inidumun', 'iniduver',
        ]

class seRelaFuncUrbaRegioForm(ModelForm):
    class Meta:
        model = inidserfinf
        fields = ['inidnomb', 'inidlocf', 'inidauth', 'inidanit',
            'inidambi', 'inidanor', 'inidanop', 'inidudep', 'inidumun', 
            'iniduver',
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
#
#def add_imagenes(request):
#    pass
#
#def add_fotografias(request):
#    pass
#
#def add_suelos(request):
#    pass
#
#def add_hidrologia(request):
#    pass
#
#def add_hidrogeologia(request):
#    pass
#
#def add_calidaddeagua(request):
#    pass
#
#def add_cargascontaminantes(request):
#    pass
#
#def add_cobertura(request):
#    pass
#
#def add_florayfauna(request):
#    pass
#
#def add_pmecosistemas(request):
#    pass
#
#def add_riesgos(request):
#    pass
#
#def add_seactoressoc(request):
#    pass
#
#def add_seestrparticip(request):
#    pass
#
#def add_separticcomuetnicas(request):
#    pass
#
#def add_sediagsocioeconom(request):
#    pass
#
#def add_secaractcultural(request):
#    pass
#
#def add_sevalorservicecos(request):
#    pass
#
#def add_serelafuncurbaregio(request):
#    pass
#
