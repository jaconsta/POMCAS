#-*- coding: utf-8 -*-
from django.contrib import admin
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
    iniccinflab, inidccmigeo, iniccicompl, iniccicomps, iniccicompu #Cargas Contaminantes
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

#General Information and concept

class InfoIndice(admin.TabularInline):
    model = inforindice
    extra = 2

class InfoAdmin(admin.ModelAdmin):
    list_display = ['infocomp']
    inlines = [InfoIndice]

#Cartografía base
#class CartFuenAdmin(admin.TabularInline):
#    model = inicartdatf 
#    extra = 2
class CarSCatAdmin(admin.StackedInline):
    model = inicartscat
    extra = 1
    fields = (('icarspre', 'icarsexi'), 'icarsqua', 'icarsrel')
class CarSTraAdmin(admin.StackedInline):
    model = inicartstra
    extra = 1
    fields = (('icarspre', 'icarsexi'), 'icarsqua', 'icarsrel')
class CarSHdrAdmin(admin.StackedInline):
    model = inicartshdr
    extra = 1
    fields = (('icarspre', 'icarsexi'), 'icarsqua', 'icarsrel')
class CarSRlvAdmin(admin.StackedInline):
    model = inicartsrlv
    extra = 1
    fields = (('icarspre', 'icarsexi'), 'icarsqua', 'icarsrel')
class CarSEteAdmin(admin.StackedInline):
    model = inicartsete
    extra = 1
    fields = (('icarspre', 'icarsexi'), 'icarsqua', 'icarsrel')

class CartoAdmin(admin.ModelAdmin):
    list_display = ['icartnum', 'icartess']
    inlines = [CarSCatAdmin, CarSTraAdmin, CarSHdrAdmin,
        CarSRlvAdmin, CarSEteAdmin]
    fieldsets = (
        (u'Cuenca y corporación', {
            'fields': ('iniescor', 'iniescue', 'inieswho', 'inieswhu')  
        }),
        (None,{ 
            'fields':('icartess', 'icartnum', 'icartres', 'icartcug', 
            'incacuba', 'incacubp', 'incaforf', ('incafore', 'incaforo'))
        }),
        (u'Referencia espacial', {
            'fields': ('incarsco', 'incarsre', 'incaroco', 
            'incardat')
        }),
        (None, {
            'fields': ('icartesc', 'incarlic')
        }),
        (u'Fuentes y fecha',{
            'fields': ('incaraut', 'incarlug', 'incarano')
        }),
    )

#Imágenes                              
class ImageAdmin(admin.ModelAdmin):
    list_display = ['iimanomb', 'iimasens', 'iimadate', 'iimacubr']
    fieldsets = (
        (u'Cuenca y corporación', {
            'fields': ('iniescor', 'iniescue', 'inieswho', 'inieswhu')  
        }),
        (None, {
            'fields': ('iimanomb', ('iimasens', 'iimaseno'), 'iimadate', 
            'iimacubr', 'incacuba', 'incacubp', 'incaforf', 
            ('incafore', 'incaforo')), 
        }),
        (u'Referencia espacial', {
            'fields': ('incarsco', 'incarsre', 'incaroco', 
            'incardat')
        }),
        (u'Banda pancromática', {
            'fields': (('iimabanp', 'iimabanc'),) 
        }),
        (None, {'fields': ('iimabanm', 'iimarese')
        }),
        (u'Coordenadas esquina superior izquierda', {
            'fields': (('iimacsix', 'iimacsiy'),)
        }),
        (u'Coordenadas esquina inferior derecha', {
            'fields': (('iimacidx', 'iimacidy'),)
        }),
        (None, {'fields': ('iimanubp', 'incarlic')
        }),
        (u'Fuentes y fecha',{
            'fields': ('incaraut', 'incarlug', 'incarano')
        }),
    )

#Fotogragías                           
class FotosAdmin(admin.ModelAdmin):
    list_display = ['ifonombr', 'ifoescaf']
    fieldsets = (
        (u'Cuenca y corporación', {
            'fields': ('iniescor', 'iniescue', 'inieswho', 'inieswhu')  
        }),
        (None, { 
            'fields': ('ifonombr', 'incaforf', ('incafore', 'incaforo'),
            'ifonumes', 'ifoescaf', 'ifotipoc', 'ifoaltvu', 
            'ifopunfo', 'ifoanubp'), 
        }),
        (u'Referencia espacial', {
            'fields': ('incarsco', 'incarsre', 'incaroco', 
            'incardat'),
        }),
        (None, {
            'fields': ('incarlic',),
        }),
        (u'Fuentes y fecha',{
            'fields': ('incaraut', 'incarlug', 'incarano'),
        }),
    )

# Suelos
class MetodGeoAdmin(admin.StackedInline):
    model = inidsumegeo
    fieldsets = (
        (u'Metodoogía utilizada para el estudio de geomorfología', {
            'fields' : (
            'geometod', ('geoclasi', 'geoclaso'),
            ('geoproce', 'geoproco'), ('geoamena', 'geoament', 'geoameno'),
            )
        }),
    )
class MetodTieAdmin(admin.StackedInline):
    model = inidsumesue
    fieldsets = (
        (u'Metodoogía utilizada para el estudio de suelos y/o coberturas de la tierra', {
            'fields': (
            ('inisutle', 'inisutlo'), 'inisutla', ('inisutln', 'inisutli'),
            'inisutge',
            )
        }),
    )
class SueCartAdmin(admin.StackedInline):
    model = inidsuinfor
    fields = ('carescs', 'caruesle', 'carmafor', ('carmamex', 'carmamot'),
        'carmetad', 'carmeaut', 'carmedat', 'carinaso', 
        'carleyen', 'carfuent', 'carqualy',
        )
    extra = 1

class SuelosAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']
    inlines = [MetodGeoAdmin, MetodTieAdmin, SueCartAdmin]
    fieldsets = (
        (u'Cuenca y corporación', {
            'fields': ('iniescor', 'iniescue', 'inieswho', 'inieswhu')  
        }),
        (u'Identificación del estudio de suelos y/o capacidad de uso', {
            'fields': (
            'inidnomb', 'iniddocf', ('iniddoce', 'iniddoco'), 'inidlocf',
            'inidresp', 'inidumun', 'inidcare', 'inidcper',
            'inidauth', 'inidanit', 'inidsini', 'inidanor', 
            )
        }),
    )
    
# Hidrología
class MethoHidroAdmin(admin.StackedInline):
    model = inidhlmetod
    fields = ('inihlppa', 'inihlphd', ('inihlmin', 'inihlpid'),
        ('inihlcal' ,'inihlcad')
    )
class MethoHEstaAdmin(admin.StackedInline):
    model = ihlmethaest
class CartHidroAdmin(admin.StackedInline):
    model = inidhlcarto
    extra = 1
    fields = (
        'carescs', 'caruesle', 'carmafor', ('carmamex', 'carmamot'),
        'carmetad', 'carinaso',
    )

#class InfoCHidroAdmin(admin.StackedInline):
#    model = inidhlinfor
class AforMethAdmin(admin.TabularInline):
    model = ihlmethafor

class HidrolAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']
    inlines = [MethoHidroAdmin, CartHidroAdmin] 
        #InfoCHidroAdmin]
    fieldsets = (
        (u'Cuenca y corporación', {
            'fields': ('iniescor', 'iniescue', 'inieswho', 'inieswhu')  
        }),
        (u'Identificación del estudio de hidrología o climatología', {
            'fields': (
            'inidnomb', 'iniddocf', ('iniddoce', 'iniddoco'), 'inidlocf',
            'inidresp', 'inidusub', 'inidusec', 'inidutra', 'inidumun', 
            'inidcare', 'inidcper', 'inidauth', 'inidanit', 'inidsini', 
            'inidanor', 'inidanop',
            ),
        }),
    )

class MethHidrAdmin(admin.ModelAdmin):
    inlines = [AforMethAdmin]

# Hidrogeología
class MetHdgFaseAdmin(admin.TabularInline):
    model = inighgmetfa
    extra = 1
class MetHdgModeAdmin(admin.StackedInline):
    model = inidhgmmoma
class MethoHidrgAdmin(admin.StackedInline):
    model = inidhgmetho
    fields = (
        'inhgdbpa', ('inhgdbpu', 'inhgdbat'), ('inhgdbac', 'inhgdbpa'),
        'inhgquye', 'inhgqunc', 'inhgqupa', ('inhgceah', 'inhgahpo'),
        'inhglaba', ('inhglabn', 'inhglabi'), 'inghesgg', 'inhgeggn', 
        'inghegme', 'inghacui', ('inghaces', 'inghacre', 'inghacrs'), 
        ('inghchdr', 'inghchme', 'inghchpo'), 'inghries', 'inghcaco',
        ('inghvuln', 'inghvume', 'inghcupr'), ('inghmhco', 'inghmhci'),
        'inghtacu',('inghagsu','inghasnp'), 'inghasco', 
        ('inghmoma', 'inghmomo'),
    )
class CartHidrgAdmin(admin.StackedInline):
    model = inidcartog #inidhgcarto
    extra = 1
    fields = (
        'carescs', 'caruesle', 'carmafor', ('carmamex', 'carmamot'),
        'carmetad', 'carinaso',
    )

class HidrgAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']
    inlines = [MetHdgFaseAdmin, MethoHidrgAdmin, CartHidrgAdmin]
    fields = (
        'inidnomb', 'iniddocf', ('iniddoce', 'iniddoco'), 'inidlocf',
        'inidresp', 'inidumun', 'inidcare', 'inidcper', 
        'inidauth', 'inidanit', 'inidanor', 'inidanop',
    )
class HdgMethAdmin(admin.ModelAdmin):
    pass
#    list_display = ['inhgdbpa', 'inhgquye', 'inhgceah',  
#        'inghesgg', 'inghacui']
#    inlines = [MetHdgFaseAdmin]

# Calidad de Agua
class CalAMethAdmin(admin.StackedInline):
    model = inidcameth
class CalAIestAdmin(admin.StackedInline):
    model = inicainfoes
class CalAIcomAdmin(admin.StackedInline):
    model = inicainfoco
class CalACampaAdmin(admin.TabularInline):
    model = inidcamecam
    extra = 2
class CalALaborAdmin(admin.TabularInline):
    model = inicainflab
    extra = 2
class CalAParFiAdmin(admin.TabularInline):
    model = incainfpara
    extra = 2
class CalAGeoAdmin(admin.TabularInline):
    model = inicainfgeo
    extra = 2
class CalAcapaAdmin(admin.TabularInline):
    model = inicaicca
    extra = 2

class CalAguaAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']
    inlines = [CalAMethAdmin, CalAIestAdmin, CalAIcomAdmin]
    fieldsets = (
        (u'Cuenca y corporación', {
            'fields': ('iniescor', 'iniescue', 'inieswho', 'inieswhu')  
        }),
        (u'Identificación del estudio de hidrología o climatología', {
            'fields': ('inidnomb', 'iniddocf', ('iniddoce', 'iniddoco'),
            'inidlocf', 'inidresp', 'inidudep', 'inidumun', 'inidcare',
            'inidcper', 'inidauth', 'inidanit', 'inidanor', 'inidanop',)
        }),
    )
class CAMetoAdmin(admin.ModelAdmin):
    inlines = [CalACampaAdmin]
    fieldsets = (
        (u'Metodología del estudio, levantamiento de datos y resultados',{
            'fields': ('inidcala', 'inicaobj', 'inicamet', 'inicaest',
            ('inicacan', 'inicacaa'), 'inicaiex',
            )
        }),
        (u'Índice de Calidad de Agua (ICA)', {
            'fields': ('inicaitr', 'inicaima', 'inicaime', 'inicaimf',
            ('inicaimx', 'inicaixo'),
             )
        }),
    )
class CAInfoeAdmin(admin.ModelAdmin):
    inlines = [CalAGeoAdmin, CalALaborAdmin]
class CAInfocAdmin(admin.ModelAdmin):
    inlines = [CalAcapaAdmin]

# Cargas Contaminantes
class CaCoMetoAdmin(admin.StackedInline):
    model = inidccmetho
class CaCoIestAdmin(admin.StackedInline):
    model = inidccminfe
class CaCoiIcomAdmin(admin.StackedInline):
    model = iniccicompl 
class CaCoLabAdmin(admin.TabularInline):
    model = iniccinflab
class CacoGeoAdmin(admin.TabularInline):
    model = inidccmigeo
class CacoPSMVMuni(admin.TabularInline):
    model = iniccicomps
class CacoPUEAAAdmin(admin.TabularInline):
    model = iniccicompu

class CargContAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']
    inlines = [CaCoMetoAdmin, CaCoIestAdmin, CaCoiIcomAdmin]
    fieldsets = (
        (u'Cuenca y corporación', {
            'fields': ('iniescor', 'iniescue', 'inieswho', 'inieswhu')  
        }),
        (u'Identificación del estudio de hidrología o climatología', {
            'fields': ('inidnomb', 'iniddocf', ('iniddoce', 'iniddoco'),
            'inidlocf', 'inidresp', 'inidudep', 'inidumun', 'inidcare',
            'inidcper', 'inidauth', 'inidanit', 'inidanor', 'inidanop',)
        }),
    )
class CacoInfeAdmin(admin.ModelAdmin):
    inlines = [CaCoLabAdmin, CacoGeoAdmin]
class CacoInfcAdmin(admin.ModelAdmin):
    inlines = [CacoPSMVMuni, CacoPUEAAAdmin]
    fields = ('iiccicom', ('iicccmue', 'iicccper'), 'iicccprm', ('iicccpor',
        'iicccpse'), 'iicccpur', 'iicccpma',
    )

# Cobertura
class CobeMetoAdmin(admin.StackedInline):
    model = inidcometho
    fields = (('iicomsen', 'iicomseo'), ('iicomfot', 'iicomfoo'),
        ('iicomimg', 'iicomimo'), 'iicomdat', 'iicomniv', 'iicomint',
        'iicomver', 'iicomcfu', 'iicomces', 'iicomcan',
    )
class CobeCartoAdmin(admin.StackedInline):
    model = inidcoinfog 
    extra = 1
    fields = ('carescs', 'caruesle', 'carmafor', ('carmamex', 'carmamot'),
        'carmetad', 'carinaso',
        )
class CobeAnMultAdmin(admin.StackedInline):
    model = inidcoanmul

class CoberAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']
    inlines = [CobeMetoAdmin, CobeCartoAdmin, CobeAnMultAdmin]
    fieldsets = (
        (u'Cuenca y corporación', {
            'fields': ('iniescor', 'iniescue', 'inieswho', 'inieswhu',
            'inidsubc',)  
        }),
        (u'Identificación del estudio/ información', {
            'fields': ('inidnomb', 'iniddocf', ('iniddoce', 'iniddoco'),
            'inidlocf', 'inidresp', 'inidudep', 'inidumun', 'inidcare',
            'inidcper', 'inidauth', 'inidanit', 'inidanor', 'inidanop',
            )
        }),
    )

# Flora y Fauna
class FloraMetoAdmin(admin.StackedInline):
    model = inidffmeth
class FloraCartAdmin(admin.StackedInline):
    model = inidffcart 
    extra = 2
    fields = ('carmafor', ('carmamex', 'carmamot'), ('carmetad', 'carmeaut'),
        'carinflo', 'carfuent',
        )

class FloraAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']
    inlines = [FloraMetoAdmin, FloraCartAdmin]
    fieldsets = (
        (u'Cuenca y corporación', {
            'fields': ('iniescor', 'iniescue', 'inieswho', 'inieswhu',
            'inidsubc',  
            )
        }),
        (u'Identificación del estudio/ información', {
            'fields': ('inidnomb', 'iniddocf', ('iniddoce', 'iniddoco'),
            'inidlocf', 'inidresp', 'inidudep', 'inidumun', 'inidcare',
            'inidcper', 'inidauth', 'inidanit', 'inidanor', 'inidanop',
            )
        }),
    )

# PM Ecosistemas
class FormuPlanAdmin(admin.StackedInline):
    model = inidpmecofo
class PlanManeInfoAdmin(admin.StackedInline):
    model = inidpmecopm
    extra = 2
    fields = ('caruesle', 'caruespu', 'carescs', 'carmafor',
        ('carmamex', 'carmamot'),
    )
class PlaManEjeAdmin(admin.TabularInline):
    model = pmecoplanma

class PMEcoAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']
    inlines = [FormuPlanAdmin, PlanManeInfoAdmin]
    fieldsets = (
        (u'Cuenca y corporación', {
            'fields': ('iniescor', 'iniescue', 'inieswho', 'inieswhu',
            'inidsubc',  
            )
        }),
        (u'Identificación del estudio/ información', {
            'fields': ('inidnomb', 'iniddocf', ('iniddoce', 'iniddoco'),
            'inidlocf', 'inidresp', 'inidudep', 'inidumun', 'inidcare',
            'inidcper', 'inidauth', 'inidanit', 'inidanor', 'inidanop',
            )
        }),
    )

class PMEFormAdmin(admin.ModelAdmin):
    inlines = [PlaManEjeAdmin]

# Riesgos - Amenazas
#class AmenSitAdmin(admin.StackedInline):
#    model = inriesamepr
class AmenActAdmin(admin.TabularInline):
    model = inriesameac
class AmenActoAdmi(admin.TabularInline):
    model = inriesameac

class AmenazAdmin(admin.ModelAdmin):
    inlines = [AmenActoAdmi]
    fieldsets = (
        (u'Cuenca y corporación', {
            'fields': ('iniescor', 'iniescue', 'inieswho', 'inieswhu',
            )
        }),
        (u'Amenazas que se identifican en la cuenca', {
            'fields': (('ameniden', 'amenotra'), 'ubidepar',
                'ubimunic', 'ubivered',
            )
        }),
        (u'Eventos que han ocurrido en la cuenca', {
            'fields': (('eventocu', 'eventoot'), 'eventrec', 'evencaus',
            )
        }),
        (None, {
            'fields': (('elemento', 'elemotro'), ('actosoci', 'activida'),
            'amenmapa', 'amengeor',
            )
        }),
    )

# Riesgos - Estudios
class RiesCArtoAdmin(admin.StackedInline):
    model = inidriescar
    extra = 2
    fields = ('carescs', 'caruesle', 'carmafor', ('carmamex', 'carmamot'),
        'carmetad', 'carmeaut', 'carmenit', 'carmeinf', 'carmedat', 
        'carinaso', 'cardocfo', 'cardocex', 'cardocot',
    )

class RiesgoAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']
    inlines = [RiesCArtoAdmin]
    fieldsets = (
        (u'Cuenca y corporación', {
            'fields': ('iniescor', 'iniescue', 'inieswho', 'inieswhu',
            'inidsubc',  
            )
        }),
        (u'Identificación del estudio/ información', {
            'fields': ('inidnomb', 'inidlocf', 'inidudep', 'inidumun', 
            'iniduver', 'inidcare', 'inidcper', 'inidauth', 'inidanit', 
            'inidanor', 'inidanop',
            )
        }),
    )

#Socioeconómico - Actores Sociales
class DetaActSocAdmin(admin.StackedInline):
    model = inidseasdet 
    fields = (('isemetho', 'isemethd',), ('isedocum', 'isedocud', 'isedocas',),
        'iseactma', ('iseprior', 'isepride'), ('isedbact', 'isedbvar',),
    )

class ActSocAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']#['isocinfo', 'isocubic', 'isocauto']
    inlines = [DetaActSocAdmin]
    fieldsets = (
        (u'Cuenca y corporación', {
            'fields': ('iniescor', 'iniescue', 'inieswho', 'inieswhu',
            'inidsubc',  
            )
        }),
        (u'Información general', {
            'fields': ('inidnomb', 'inidlocf', 'inidauth', 'inidanit',
            'inidanor', 'inidanop', 'inidudep', 'inidumun', 'iniduver',
            )
        }),
    )

#Socioeconómico - Estrategia de Participación
class DetaEstrParAdmin(admin.StackedInline):
    model = inidseepdet 
class DetEstPaInsAdmin(admin.TabularInline):
    model = inidseepdin 
    extra = 2

class EstrParAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']#['isocinfo', 'isocubic', 'isocauto']
    inlines = [DetaEstrParAdmin]
    fieldsets = (
        (u'Cuenca y corporación', {
            'fields': ('iniescor', 'iniescue', 'inieswho', 'inieswhu',
            'inidsubc',  
            )
        }),
        (u'Información general', {
            'fields': ('inidnomb', 'inidlocf', 'inidauth', 'inidanit',
            'inidanor', 'inidanop', 'inidudep', 'inidumun', 'iniduver',
            )
        }),
    )
class EstPaDeAdmin(admin.ModelAdmin):
    inlines = [DetEstPaInsAdmin]
    fieldsets = (
        (u'Detalle de la información', {
            'fields': ('iseestra', 'isepestr', ('isepestg', 'isepestd'),
            ('iseppart', 'isepparm'), 'isepinst', ('isepcomu', 'isepcomd',),
            )
        }),
        (u'Información complementaria', {
            'fields': ('isepiamb', 'isepiamd', 'isepesta',
            )
        }),
    )

#Socioeconómico - Participación de comunidades étnicas 
class DetaComEtnAdmin(admin.StackedInline):
    model = inidsecedet 
    fields = (('isepccar', 'isepccaw',), 'isepccer', ('isepcdev', 'isepcded',),
    )
class CertComEtnAdmin(admin.TabularInline):
    model = inidsecedat
    extra = 2

class ComEtnAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']#['isocinfo', 'isocubic', 'isocauto']
    inlines = [DetaComEtnAdmin]
    fieldsets = (
        (u'Cuenca y corporación', {
            'fields': ('iniescor', 'iniescue', 'inieswho', 'inieswhu',
            'inidsubc',  
            )
        }),
        (u'Información general', {
            'fields': ('inidnomb', 'inidlocf', 'inidauth', 'inidanit',
            'inidanor', 'inidanop', 'inidudep', 'inidumun', 'iniduver',
            )
        }),
    )
class CoEtDeAdmin(admin.ModelAdmin):
    inlines = [CertComEtnAdmin]
    fields = ('iseparti',
        ('isepccar', 'isepccaw',), 'isepccer', ('isepcdev', 'isepcded',),
    )

#Socioeconómico - Diagnósticos Socioeconómicos
class DetaDiagSocAdmin(admin.StackedInline):
    model = inidsdsedet 
    fields = ('iseddina', ('iseddinv', 'iseddino'), 'isedserv', ('isedsere',
        'isedsero'), 'isedseal', ('isedseai', 'isedsede'), 'isedacti',
        ('isedactd', 'isedacto'), ('isedsitu', 'isedsitd'), ('isedproy', 
        'isedprod'), ('isedconf', 'isedcond'), ('isedpoli', 'isedpold',),
        ('isedpred', 'isedprec',), ('isedsegu', 'isedsegd',), 
    )

class DiagSocAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']#['isocinfo', 'isocubic', 'isocauto']
    inlines = [DetaDiagSocAdmin]
    fieldsets = (
        (u'Cuenca y corporación', {
            'fields': ('iniescor', 'iniescue', 'inieswho', 'inieswhu',
            'inidsubc',  
            )
        }),
        (u'Información general', {
            'fields': ('inidnomb', 'inidlocf', 'inidauth', 'inidanit',
            'inidambi', 'inidanor', 'inidanop', 'inidudep', 'inidumun', 
            'iniduver',
            )
        }),
    )

#Socioeconómico - Caracterización Cultural
class DetaCarCultAdmin(admin.StackedInline):
    model = inidseccdet 
    fields = ( 'isecccul', ('isecccuc', 'isecccuv'), ('iseccpat','iseccpad'),
        ('iseccdoc', 'iseccdcc',),
    )
class DetDCarCultAdmin(admin.StackedInline):
    model = inidseccdcc
    extra = 2

class CarCultAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']#['isocinfo', 'isocubic', 'isocauto']
    inlines = [DetaCarCultAdmin]
    fieldsets = (
        (u'Cuenca y corporación', {
            'fields': ('iniescor', 'iniescue', 'inieswho', 'inieswhu',
            'inidsubc',  
            )
        }),
        (u'Información general', {
            'fields': ('inidnomb', 'inidlocf', 'inidauth', 'inidanit',
            'inidanor', 'inidanop', 'inidudep', 'inidumun', 'iniduver',
            )
        }),
    )
class CaCUDetAdmin(admin.ModelAdmin):
    inlines = [DetDCarCultAdmin]
    fields = ('isecarac', 
        'isecccul', ('isecccuc', 'isecccuv'), ('iseccpat','iseccpad'),
        ('iseccdoc', 'iseccdcc',),
    )

#Socioeconómico - Valoración de Servicios Ecosistémicos
class DetaValorAdmin(admin.StackedInline):
    model = inidsevsdet 
    fields = ('isesemet', ('iseseser', 'iseseseo'), ('isesepil', 'isesepia'),
    )

class ValorAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']#['isocinfo', 'isocubic', 'isocauto']
    inlines = [DetaValorAdmin]
    fieldsets = (
        (u'Cuenca y corporación', {
            'fields': ('iniescor', 'iniescue', 'inieswho', 'inieswhu',
            'inidsubc',  
            )
        }),
        (u'Informacion general', {
            'fields': ('inidnomb', 'inidlocf', 'inidauth', 'inidanit',
            'inidanor', 'inidanop', 'inidudep', 'inidumun', 'iniduver',
            )
        }),
    )

#Socioeconómico - Relaciones funcionales urbano- regionales
class DetaRelacAdmin(admin.StackedInline):
    model = inidserfdet 
    fields = ('infucomp', 'infucone', ('infoconc', 'infocona'), 'infocapa',
        ('infocapo', 'infocapl',),
    )
class DeCompRelacAdmin(admin.StackedInline):
    model = inidserfure
    extra = 2

class RelacAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']#['isocinfo', 'isocubic', 'isocauto']
    inlines = [DetaRelacAdmin]
    fieldsets = (
        (u'Cuenca y corporación', {
            'fields': ('iniescor', 'iniescue', 'inieswho', 'inieswhu',
            'inidsubc',  
            )
        }),
        (u'Información general', {
            'fields': ('inidnomb', 'inidlocf', 'inidauth', 'inidanit',
            'inidambi', 'inidanor', 'inidanop', 'inidudep', 'inidumun', 
            'iniduver',
            )
        }),
    )
class RelacDetaAdmin(admin.ModelAdmin):
    inlines = [DeCompRelacAdmin]
    fields = ('infuurre',
        'infucomp', 'infucone', ('infoconc', 'infocona'), 'infocapa',
        ('infocapo', 'infocapl',),
    )

admin.site.register(inforcompon, InfoAdmin)
admin.site.register(inforconcep)
admin.site.register(inidcardatg, CartoAdmin)
admin.site.register(inidimagsat, ImageAdmin)
admin.site.register(inidfotogra, FotosAdmin)
admin.site.register(inidsuestud, SuelosAdmin)
admin.site.register(inidhlestud, HidrolAdmin)
admin.site.register(inidhlvarib)
admin.site.register(inidhlcauda)
admin.site.register(inidhlmetod, MethHidrAdmin)
admin.site.register(inidhgestud, HidrgAdmin)
admin.site.register(inidhgmetho, HdgMethAdmin)
admin.site.register(inidcaestud, CalAguaAdmin)
admin.site.register(inidcameth, CAMetoAdmin)
admin.site.register(inicainfoes, CAInfoeAdmin)
admin.site.register(inicainfoco, CAInfocAdmin)
admin.site.register(inidccestud, CargContAdmin)
admin.site.register(inidccminfe, CacoInfeAdmin)
admin.site.register(iniccicompl, CacoInfcAdmin)
admin.site.register(inidcoestud, CoberAdmin)
admin.site.register(inidffestud, FloraAdmin)
admin.site.register(inidpmestud, PMEcoAdmin)
admin.site.register(inidpmecofo, PMEFormAdmin)
admin.site.register(inriesamepr, AmenazAdmin)
admin.site.register(inidriestud, RiesgoAdmin)
admin.site.register(inidseasinf, ActSocAdmin)
admin.site.register(inidseepinf, EstrParAdmin)
admin.site.register(inidseepdet, EstPaDeAdmin)
admin.site.register(inidseceinf, ComEtnAdmin)
admin.site.register(inidsecedet, CoEtDeAdmin)
admin.site.register(inidsedsinf, DiagSocAdmin)
admin.site.register(inidseccinf, CarCultAdmin)
admin.site.register(inidseccdet, CaCUDetAdmin)
admin.site.register(inidsevsinf, ValorAdmin)
admin.site.register(inidserfinf, RelacAdmin)
admin.site.register(inidserfdet, RelacDetaAdmin)
