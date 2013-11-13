#-*- coding: utf-8 -*-
from django.contrib import admin
from matriz_infoidentifi.models import inforcompon, inforindice #General info
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

#General Information

class InfoIndice(admin.TabularInline):
    model = inforindice
    extra = 2

class InfoAdmin(admin.ModelAdmin):
    list_display = ['infocomp']
    inlines = [InfoIndice]

#Cartografía base
class CartFuenAdmin(admin.TabularInline):
    model = inicartdatf 
    extra = 2
class CarSCatAdmin(admin.StackedInline):
    model = inicartscat
class CarSTraAdmin(admin.StackedInline):
    model = inicartstra
class CarSHdrAdmin(admin.StackedInline):
    model = inicartshdr
class CarSRlvAdmin(admin.StackedInline):
    model = inicartsrlv
class CarSEteAdmin(admin.StackedInline):
    model = inicartsete

class CartoAdmin(admin.ModelAdmin):
    list_display = ['icartnum', 'icartess', 'icartcua']
    inlines = [CartFuenAdmin, CarSCatAdmin, CarSTraAdmin, CarSHdrAdmin,
        CarSRlvAdmin, CarSEteAdmin]

#Imágenes                              
class ImageAdmin(admin.ModelAdmin):
    list_display = ['iimanomb', 'iimasens', 'iimadate', 'iimacubr']

#Fotogragías                           
class FotosAdmin(admin.ModelAdmin):
    list_display = ['ifonombr', 'ifoinivu', 'ifoescaf', 'ifoacuba']

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
    
#Hidrología
class MethoHidroAdmin(admin.StackedInline):
    model = inidhlmetod
class CartHidroAdmin(admin.StackedInline):
    model = inidhlcarto
class InfoCHidroAdmin(admin.StackedInline):
    model = inidhlinfor
class AforMethAdmin(admin.TabularInline):
    model = ihlmethafor

class HidrolAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']
    inlines = [MethoHidroAdmin, CartHidroAdmin, InfoCHidroAdmin]

class MethHidrAdmin(admin.ModelAdmin):
    inlines = [AforMethAdmin]

#Hidrogeología
class MethoHidrgAdmin(admin.StackedInline):
    model = inidhgmetho
class CartHidrgAdmin(admin.StackedInline):
    model = inidhgcarto

class HidrgAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']
    inlines = [MethoHidrgAdmin, CartHidrgAdmin]

#Calidad de Agua
class CalAMethAdmin(admin.StackedInline):
    model = inidcameth
class CalAIestAdmin(admin.StackedInline):
    model = inicainfoes
class CalAIcomAdmin(admin.StackedInline):
    model = inicainfoco
class CalACampaAdmin(admin.TabularInline):
    model = inidcamecam
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
    inlines = [CalAGeoAdmin]
class CAInfocAdmin(admin.ModelAdmin):
    inlines = [CalAcapaAdmin]

#Cargas Contaminantes
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

#Cobertura
class CobeMetoAdmin(admin.StackedInline):
    model = inidcometho
class CobeCartoAdmin(admin.StackedInline):
    model = inidcoinfog 

class CoberAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']
    inlines = [CobeMetoAdmin, CobeCartoAdmin]

#Flora y Fauna
class FloraMetoAdmin(admin.StackedInline):
    model = inidffmeth
class FloraCartAdmin(admin.StackedInline):
    model = inidffcart 

class FloraAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']
    inlines = [FloraMetoAdmin, FloraCartAdmin]

#PM Ecosistemas
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

#Riesgos
class RiesgoAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']
    #inlines = [Admin]

#Socioeconómico - Actores Sociales
class DetaActSocAdmin(admin.StackedInline):
    model = inidseasdet 

class ActSocAdmin(admin.ModelAdmin):
    list_display = ['isocinfo', 'isocubic', 'isocauto']
    inlines = [DetaActSocAdmin]

#Socioeconómico - Estrategia de Participación
class DetaEstrParAdmin(admin.StackedInline):
    model = inidseepdet 

class EstrParAdmin(admin.ModelAdmin):
    list_display = ['isocinfo', 'isocubic', 'isocauto']
    inlines = [DetaEstrParAdmin]

#Socioeconómico - Participación de comunidades étnicas 
class DetaComEtnAdmin(admin.StackedInline):
    model = inidsecedet 

class ComEtnAdmin(admin.ModelAdmin):
    list_display = ['isocinfo', 'isocubic', 'isocauto']
    inlines = [DetaComEtnAdmin]

#Socioeconómico - Diagnósticos Socioeconómicos
class DetaDiagSocAdmin(admin.StackedInline):
    model = inidsdsedet 

class DiagSocAdmin(admin.ModelAdmin):
    list_display = ['isocinfo', 'isocubic', 'isocauto']
    inlines = [DetaDiagSocAdmin]

#Socioeconómico - Caracterización Cultural
class DetaCarCultAdmin(admin.StackedInline):
    model = inidseccdet 

class CarCultAdmin(admin.ModelAdmin):
    list_display = ['isocinfo', 'isocubic', 'isocauto']
    inlines = [DetaCarCultAdmin]

#Socioeconómico - Valoración de Servicios Ecosistémicos
class DetaValorAdmin(admin.StackedInline):
    model = inidsevsdet 

class ValorAdmin(admin.ModelAdmin):
    list_display = ['isocinfo', 'isocubic', 'isocauto']
    inlines = [DetaValorAdmin]

#Socioeconómico - Relaciones funcionales urbano- regionales
class DetaRelacAdmin(admin.StackedInline):
    model = inidserfdet 

class RelacAdmin(admin.ModelAdmin):
    list_display = ['isocinfo', 'isocubic', 'isocauto']
    inlines = [DetaRelacAdmin]

admin.site.register(inforcompon, InfoAdmin)
admin.site.register(inidcardatg, CartoAdmin)
admin.site.register(inidimagsat, ImageAdmin)
admin.site.register(inidfotogra, FotosAdmin)
admin.site.register(inidsuestud, SuelosAdmin)
admin.site.register(inidhlestud, HidrolAdmin)
admin.site.register(inidhlmetod, MethHidrAdmin)
admin.site.register(inidhgestud, HidrgAdmin)
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
admin.site.register(inidriestud, RiesgoAdmin)
admin.site.register(inidseasinf, ActSocAdmin)
admin.site.register(inidseepinf, EstrParAdmin)
admin.site.register(inidseceinf, ComEtnAdmin)
admin.site.register(inidsedsinf, DiagSocAdmin)
admin.site.register(inidseccinf, CarCultAdmin)
admin.site.register(inidsevsinf, ValorAdmin)
admin.site.register(inidserfinf, RelacAdmin)
