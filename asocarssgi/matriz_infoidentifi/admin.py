#-*- coding: utf-8 -*-
from django.contrib import admin
from matriz_infoidentifi.models import inforcompon, inforconcep, inforindice #General info
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
from matriz_infoidentifi.models import inidcoestud, inidcometho, inidcoinfog #Cobertura
from matriz_infoidentifi.models import inidffestud, inidffmeth, inidffcart #Flora y Fauna
from matriz_infoidentifi.models import inidpmestud, inidpmecofo, pmecoplanma, \
    inidpmecopm #PM Ecosistemas
from matriz_infoidentifi.models import inidriesame, inriesamepr,amenaidenti, \
    eventocurri, elemenexpue, inriesameac #Riesgos - Amenazas
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
class CarSTraAdmin(admin.StackedInline):
    model = inicartstra
    extra = 1
class CarSHdrAdmin(admin.StackedInline):
    model = inicartshdr
    extra = 1
class CarSRlvAdmin(admin.StackedInline):
    model = inicartsrlv
    extra = 1
class CarSEteAdmin(admin.StackedInline):
    model = inicartsete
    extra = 1

class CartoAdmin(admin.ModelAdmin):
    list_display = ['icartnum', 'icartess']
    inlines = [CarSCatAdmin, CarSTraAdmin, CarSHdrAdmin,
        CarSRlvAdmin, CarSEteAdmin]

#Imágenes                              
class ImageAdmin(admin.ModelAdmin):
    list_display = ['iimanomb', 'iimasens', 'iimadate', 'iimacubr']

#Fotogragías                           
class FotosAdmin(admin.ModelAdmin):
    list_display = ['ifonombr', 'ifoescaf']

# Suelos
class MetodGeoAdmin(admin.StackedInline):
    model = inidsumegeo
class MetodTieAdmin(admin.StackedInline):
    model = inidsumesue
class SueCartAdmin(admin.StackedInline):
    model = inidsuinfor

class SuelosAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']
    inlines = [MetodGeoAdmin, MetodTieAdmin, SueCartAdmin]
    
# Hidrología
class MethoHidroAdmin(admin.StackedInline):
    model = inidhlmetod
class MethoHEstaAdmin(admin.StackedInline):
    model = ihlmethaest
class CartHidroAdmin(admin.StackedInline):
    model = inidhlcarto
#class InfoCHidroAdmin(admin.StackedInline):
#    model = inidhlinfor
class AforMethAdmin(admin.TabularInline):
    model = ihlmethafor

class HidrolAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']
    inlines = [MethoHidroAdmin, MethoHEstaAdmin, CartHidroAdmin] 
        #InfoCHidroAdmin]

class MethHidrAdmin(admin.ModelAdmin):
    inlines = [AforMethAdmin]

# Hidrogeología
class MetHdgFaseAdmin(admin.StackedInline):
    model = inighgmetfa
class MetHdgModeAdmin(admin.StackedInline):
    model = inidhgmmoma
class MethoHidrgAdmin(admin.StackedInline):
    model = inidhgmetho
class CartHidrgAdmin(admin.StackedInline):
    model = inidhgcarto

class HidrgAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']
    inlines = [MethoHidrgAdmin, CartHidrgAdmin]
class HdgMethAdmin(admin.ModelAdmin):
    list_display = ['inhgdbpa', 'inhgquye', 'inhgceah',  
        'inghesgg', 'inghacui']
    inlines = [MetHdgFaseAdmin]

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
class CAMetoAdmin(admin.ModelAdmin):
    inlines = [CalACampaAdmin]
class CAInfoeAdmin(admin.ModelAdmin):
    inlines = [CalAGeoAdmin, CalALaborAdmin, CalAParFiAdmin]
class CAInfocAdmin(admin.ModelAdmin):
    inlines = [CalAcapaAdmin]

# Cargas Contaminantes
class CaCoMetoAdmin(admin.StackedInline):
    model = inidccmetho
class CaCoIestAdmin(admin.StackedInline):
    model = inidccminfe
class CaCoiIcomAdmin(admin.StackedInline):
    model = iniccicompl 
class CacoGeoAdmin(admin.TabularInline):
    model = inidccmigeo

class CargContAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']
    inlines = [CaCoMetoAdmin, CaCoIestAdmin, CaCoiIcomAdmin]
class CacoInfeAdmin(admin.ModelAdmin):
    inlines = [CacoGeoAdmin]

# Cobertura
class CobeMetoAdmin(admin.StackedInline):
    model = inidcometho
class CobeCartoAdmin(admin.StackedInline):
    model = inidcoinfog 

class CoberAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']
    inlines = [CobeMetoAdmin, CobeCartoAdmin]

# Flora y Fauna
class FloraMetoAdmin(admin.StackedInline):
    model = inidffmeth
class FloraCartAdmin(admin.StackedInline):
    model = inidffcart 

class FloraAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']
    inlines = [FloraMetoAdmin, FloraCartAdmin]

# PM Ecosistemas
class FormuPlanAdmin(admin.StackedInline):
    model = inidpmecofo
class PlanManeInfoAdmin(admin.StackedInline):
    model = inidpmecopm
class PlaManEjeAdmin(admin.TabularInline):
    model = pmecoplanma
    extra = 2

class PMEcoAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']
    inlines = [FormuPlanAdmin, PlanManeInfoAdmin]

class PMEFormAdmin(admin.ModelAdmin):
    inlines = [PlaManEjeAdmin]

# Riesgos - Amenazas
class AmenSitAdmin(admin.StackedInline):
    model = inriesamepr
class AmenActAdmin(admin.TabularInline):
    model = inriesameac

class AmenazAdmin(admin.ModelAdmin):
    inlines = [AmenSitAdmin]

# Riesgos - Estudios
class RiesCArtoAdmin(admin.StackedInline):
    model = inidriescar

class RiesgoAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']
    inlines = [RiesCArtoAdmin]

#Socioeconómico - Actores Sociales
class DetaActSocAdmin(admin.StackedInline):
    model = inidseasdet 

class ActSocAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']#['isocinfo', 'isocubic', 'isocauto']
    inlines = [DetaActSocAdmin]

#Socioeconómico - Estrategia de Participación
class DetaEstrParAdmin(admin.StackedInline):
    model = inidseepdet 
class DetEstPaInsAdmin(admin.TabularInline):
    model = inidseepdin 
    extra = 2

class EstrParAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']#['isocinfo', 'isocubic', 'isocauto']
    inlines = [DetaEstrParAdmin]
class EstPaDeAdmin(admin.ModelAdmin):
    inlines = [DetEstPaInsAdmin]

#Socioeconómico - Participación de comunidades étnicas 
class DetaComEtnAdmin(admin.StackedInline):
    model = inidsecedet 
class CertComEtnAdmin(admin.TabularInline):
    model = inidsecedat
    extra = 2

class ComEtnAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']#['isocinfo', 'isocubic', 'isocauto']
    inlines = [DetaComEtnAdmin]
class CoEtDeAdmin(admin.ModelAdmin):
    inlines = [CertComEtnAdmin]

#Socioeconómico - Diagnósticos Socioeconómicos
class DetaDiagSocAdmin(admin.StackedInline):
    model = inidsdsedet 

class DiagSocAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']#['isocinfo', 'isocubic', 'isocauto']
    inlines = [DetaDiagSocAdmin]

#Socioeconómico - Caracterización Cultural
class DetaCarCultAdmin(admin.StackedInline):
    model = inidseccdet 
class DetDCarCultAdmin(admin.StackedInline):
    model = inidseccdcc

class CarCultAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']#['isocinfo', 'isocubic', 'isocauto']
    inlines = [DetaCarCultAdmin]
class CaCUDetAdmin(admin.ModelAdmin):
    inlines = [DetDCarCultAdmin]

#Socioeconómico - Valoración de Servicios Ecosistémicos
class DetaValorAdmin(admin.StackedInline):
    model = inidsevsdet 
class DeAnValorAdmin(admin.StackedInline):
    model = inidseserec

class ValorAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']#['isocinfo', 'isocubic', 'isocauto']
    inlines = [DetaValorAdmin]
class ValorDetAdmin(admin.ModelAdmin):
    inlines = [DeAnValorAdmin]

#Socioeconómico - Relaciones funcionales urbano- regionales
class DetaRelacAdmin(admin.StackedInline):
    model = inidserfdet 
class DeCompRelacAdmin(admin.StackedInline):
    model = inidserfure

class RelacAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']#['isocinfo', 'isocubic', 'isocauto']
    inlines = [DetaRelacAdmin]
class RelacDetaAdmin(admin.ModelAdmin):
    inlines = [DeCompRelacAdmin]

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
admin.site.register(inidcoestud, CoberAdmin)
admin.site.register(inidffestud, FloraAdmin)
admin.site.register(inidpmestud, PMEcoAdmin)
admin.site.register(inidpmecofo, PMEFormAdmin)
admin.site.register(inidriesame, AmenazAdmin)
admin.site.register(inidriestud, RiesgoAdmin)
admin.site.register(inidseasinf, ActSocAdmin)
admin.site.register(inidseepinf, EstrParAdmin)
admin.site.register(inidseepdet, EstPaDeAdmin)
admin.site.register(inidseceinf, ComEtnAdmin)
admin.site.register(inidsecedet, CoEtDeAdmin)
admin.site.register(inidsedsinf, DiagSocAdmin)
admin.site.register(inidseccinf, CarCultAdmin)
admin.site.register(inidsevsinf, ValorAdmin)
admin.site.register(inidsevsdet, ValorDetAdmin)
admin.site.register(inidserfinf, RelacAdmin)
admin.site.register(inidserfdet, RelacDetaAdmin)
