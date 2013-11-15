#-*- coding: utf-8 -*-
from django.forms import ModelForm

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

class CartografiaForm(modelForm):
    class Meta:
        model = inidcardatg
        fields = [
            'icartess',
            'icartnum',
            'icartres',
            'icartcug',
            'icartcua',
            'icartcup',
            'icartfor',
            'icartfex',
            'icartrco',
            'icartrre',
            'icartror',
            'icartrda',
            'icartesc',
            'icartlic',
        ]

class ImagenesForm(modelForm):
    class Meta:
        model = inidimagsat
        fields = [
            'iimanomb',
            'iimasens',
            'iimaseno',
            'iimadate',
            'iimacubr',
            'iimacubd',
            'iimacuba',
            'iimacubp',
            'iimaform',
            'iimafore',
            'iimaresc',
            'iimaresr',
            'iimareoc',
            'iimareda',
            'iimabanp',
            'iimabanc',
            'iimabanm',
            'iimarese',
            'iimacsix',
            'iimacsiy',
            'iimacidx',
            'iimacidy',
            'iimanubp',
            'iimalice',
            'iimafaut',
            'iimaflug',
            'iimafano',
            'iimaftam',
        ]

class FotografiasForm(modelForm):
    class Meta:
        model = inidfotogra
        fields = [
            'ifonombr',
            'ifoformf',
            'ifoforme',
            'ifoinivu',
            'ifofinvu',
            'ifonumes',
            'ifoescaf',
            'ifotipoc',
            'ifoaltvu',
            'ifonumfo',
            'ifopunfo',
            'ifoanubp',
            'ifoacuba',
            'ifoacubp',
            'ifoaresc',
            'ifoaresr',
            'ifoareoc',
            'ifoareda',
            'ifoalice',
            'ifoafaut',
            'ifoaflug',
            'ifoafano',
            'ifoaftam',
        ]

class SuelosForm(modelForm):
    class Meta:
        model = inidsuestud
        fields = [
            'inidnomb',
            'inidlocf',
            'inidfunc',
            'inidubig',
            'inidareh',
            'inidporc',
            'inidauth',
            'inidanor',
            'inidanop',
        ]

class HidrologiaForm(modelForm):
    class Meta:
        model = inidhlestud
        fields = [
            'inidnomb',
            'inidlocf',
            'inidfunc',
            'inidubig',
            'inidareh',
            'inidporc',
            'inidauth',
            'inidanor',
            'inidanop',
        ]

class HidrogeologiaForm(modelForm):
    class Meta:
        model = inidhgestud
        fields = [
            'inidnomb',
            'inidlocf',
            'inidfunc',
            'inidubig',
            'inidareh',
            'inidporc',
            'inidauth',
            'inidanor',
            'inidanop',
        ]

class CalidadDeAguaForm(modelForm):
    class Meta:
        model = inidcaestud
        fields = [
            'inidnomb',
            'inidlocf',
            'inidfunc',
            'inidubig',
            'inidareh',
            'inidporc',
            'inidauth',
            'inidanor',
            'inidanop',
        ]

class CargasContaminantesForm(modelForm):
    class Meta:
        model = inidccestud
        fields = [
            'inidnomb',
            'inidlocf',
            'inidfunc',
            'inidubig',
            'inidareh',
            'inidporc',
            'inidauth',
            'inidanor',
            'inidanop',
            'inidaalb',
        ]

class CoberturaForm(modelForm):
    class Meta:
        model = inidcoestud
        fields = [
            'inidnomb',
            'inidlocf',
            'inidfunc',
            'inidubig',
            'inidareh',
            'inidporc',
            'inidauth',
            'inidanor',
            'inidanop',
            'inidaalb',
        ]

class FloraYFaunaForm(modelForm):
    class Meta:
        model = inidffestud
        fields = [
            'inidnomb',
            'inidlocf',
            'inidfunc',
            'inidubig',
            'inidareh',
            'inidporc',
            'inidauth',
            'inidanor',
            'inidanop',
            'inidaalb',
        ]

class PMEcosistemasForm(modelForm):
    class Meta:
        model = inidpmestud
        fields = [
            'inidnomb',
            'inidlocf',
            'inidfunc',
            'inidubig',
            'inidareh',
            'inidporc',
            'inidauth',
            'inidanor',
            'inidanop',
            'inidaalb',
        ]

class RiesgosForm(modelForm):
    class Meta:
        model = inidriestud
        fields = [
            'inidnomb',
            'inidlocf',
            'inidfunc',
            'inidubig',
            'inidareh',
            'inidporc',
            'inidauth',
            'inidanor',
            'inidanop',
            'inidaalb',
        ]

class seActoresSocForm(modelForm):
    class Meta:
        model = inidseasinf
        fields = [
            'iniescor',
            'iniescue',
            'isocinfo',
            'isocubic',
            'isocauto',
            'isocanoe',
            'isocdocu',
        ]

class seEstrParticipForm(modelForm):
    class Meta:
        model = inidseepinf
        fields = [
            'iniescor',
            'iniescue',
            'isocinfo',
            'isocubic',
            'isocauto',
            'isocanoe',
            'isocdocu',
        ]

class seParticComuEtnicasForm(modelForm):
    class Meta:
        model = inidseceinf
        fields = [
            'iniescor',
            'iniescue',
            'isocinfo',
            'isocubic',
            'isocauto',
            'isocanoe',
            'isocdocu',
        ]

class seDiagSocioEconomForm(modelForm):
    class Meta:
        model = inidsedsinf
        fields = [
            'iniescor',
            'iniescue',
            'isocinfo',
            'isocubic',
            'isocauto',
            'isocanoe',
            'isocdocu',
        ]

class seCaractCulturalForm(modelForm):
    class Meta:
        model = inidseccinf
        fields = [
            'iniescor',
            'iniescue',
            'isocinfo',
            'isocubic',
            'isocauto',
            'isocanoe',
            'isocdocu',
        ]

class seValorServicEcosForm(modelForm):
    class Meta:
        model = inidsevsinf
        fields = [
            'iniescor',
            'iniescue',
            'isocinfo',
            'isocubic',
            'isocauto',
            'isocanoe',
            'isocdocu',
        ]

class seRelaFuncUrbaRegioForm(modelForm):
    class Meta:
        model = inidserfinf
        fields = [
            'iniescor',
            'iniescue',
            'isocinfo',
            'isocubic',
            'isocauto',
            'isocanoe',
            'isocdocu',
        ]

#Calling the forms
def add_cartografia(request):

def add_imagenes(request):

def add_fotografias(request):

def add_suelos(request):

def add_hidrologia(request):

def add_hidrogeologia(request):

def add_calidaddeagua(request):

def add_cargascontaminantes(request):

def add_cobertura(request):

def add_florayfauna(request):

def add_pmecosistemas(request):

def add_riesgos(request):

def add_seactoressoc(request):

def add_seestrparticip(request):

def add_separticcomuetnicas(request):

def add_sediagsocioeconom(request):

def add_secaractcultural(request):

def add_sevalorservicecos(request):

def add_serelafuncurbaregio(request):

