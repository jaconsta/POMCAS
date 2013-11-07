#-*- coding: utf-8 -*-
from django.contrib import admin

from matriz_institucional.models import minstportada #Portada
from matriz_institucional.models import minstdatgene #Datos generales
from matriz_institucional.models import minstestdire, minstedcorpa, minstedcondi #Est Directiva
from matriz_institucional.models import minstorganiz, minesorasesd#Organizacion
from matriz_institucional.models import minesorsudico, minesorsubdir #Organizacion
from matriz_institucional.models import minstdescentr, midesceoficte #Descentralización
from matriz_institucional.models import minstplanific, minstplanpgar #Planeacion
from matriz_institucional.models import minsplanpaime, minstplanpdai #Planeacion
from matriz_institucional.models import minspresupues, minspresactad, minsprespomca #presupuesto
from matriz_institucional.models import minssopotecni, minssotesigpc, minssoptechrs #Sop Tec 
from matriz_institucional.models import minsrecurhuma, minsrhvinpomc #POMCAS

#Portada 
class PortadaAdmin(admin.ModelAdmin):
    list_display = ['getnit', 'mipofede', 'mipofeha', 'mipoprof'] 
    
    def getnit(self, obj):
        return '%s'%(obj.mipodatg.midginit)
    getnit.short_description = u'Corporación'

#Datos generales
class DatGeneAdmin(admin.ModelAdmin):
    list_display =['midgrazs', 'midgenit', 'midgcity', 'midgphon']

#Est Directiva
class AsamblyAdmin(admin.TabularInline):
    model = minstedcorpa
    extra = 1
class CounsilAdmin(admin.TabularInline):
    model = minstedcondi 
    extra = 1

class EstDirectAdmin(admin.ModelAdmin):
#    list_display =['miedcorp', 'miediceo', 'getnit']
    list_display =['getnit', 'miediceo'] 
    inlines = [AsamblyAdmin, CounsilAdmin]
    
    def getnit(self, obj):
        return '%s'%(obj.miedcorp.midginit)
    getnit.short_description = u'Corporación'

#Organizacion
class AsesoDirecAdmin(admin.TabularInline):
    model = minesorasesd
    extra = 1
class SubdirecCorpAdmin(admin.TabularInline):
    model = minesorsubdir
    extra = 1
class CoordSubdirAdmin(admin.TabularInline):
    model = minesorsudico
    extra = 1

class OrganizAdmin(admin.ModelAdmin):
    list_display= ['getnit', 'mieoaata', 'mieoaano', 'mieofnrp', 
        'mieofnrn', 'mieofnfc'
    ]
    inlines = [AsesoDirecAdmin, SubdirecCorpAdmin]

    def getnit(self, obj):
        return '%s'%(obj.mieocorp.midginit)
    getnit.short_description = u'Corporación'

class SubdirecAdmin(admin.ModelAdmin):
    list_display = ['getnit', 'nuacto', 'mieosuof', 'mieosuno']
    inlines = [CoordSubdirAdmin]
    
    def getnit(self, obj):
        return '%s'%(obj.miesorsu.mieocorp.midginit)
    getnit.short_description = u'Corporación'
    
    def nuacto(self, obj):
        return '%s'%(obj.miesorsu.mieoaano)
    nuacto.short_description = u'Número de acto'

#Descentralización
class OficTerrAdmin(admin.StackedInline):
    model = midesceoficte
    extra = 1

class RegionalAdmin(admin.ModelAdmin):
    list_display = ['getnit',  'midesofi']
    inlines = [OficTerrAdmin]

    def getnit(self, obj):
        return '%s'%(obj.midesnco.midginit)
    getnit.short_description = u'Corporación'

#Planeacion
class CompPGARAdmin(admin.TabularInline):
    model = minstplanpgar
    extra = 1
class PlanPAIAdmin(admin.TabularInline):
    model = minstplanpdai
    max_num = 1
class MetaPOMCAdmin(admin.TabularInline):
    model = minsplanpaime
    extra = 1

class PGARAdmin(admin.ModelAdmin):
    list_display = ['getnit', 'mipltipg']
    inlines = [CompPGARAdmin, PlanPAIAdmin, MetaPOMCAdmin]

    def getnit(self, obj):
        return '%s'%(obj.miplanif.midginit)
    getnit.short_description = u'Corporación'

#class PAIAdmin(admin.ModelAdmin):
#    list_display = ['getnit', 'miplapai', 'miplaait']
#    inlines = [MetaPOMCAdmin]
#
#    def getpai(self, obj):
#        return '%s'%(obj.miplapai.miplaait)
#    getpai.short_description = u'PAI'
#    
#    def getnit(self, obj):
#        return '%s'%(obj.miplapa.imiplanif.midginit)
#    getnit.short_description = u'Corporación'

#Presupuesto
class PresupXIIIAdmin(admin.TabularInline):
    model = minspresactad
    extra = 1
class PresupPOMCAdmin(admin.TabularInline):
    model = minsprespomca
    extra = 1

class PresupuesAdmin(admin.ModelAdmin):
    list_display = ['getnit', 'miplprgp', 'miplgrge', 'miplgrip', 'miplgrie', 
        'miplgrsp', 'miplgrse'
    ]
    inlines = [PresupXIIIAdmin,PresupPOMCAdmin]

    def getnit(self, obj):
        return '%s'%(obj.miplanpr.midginit)
    getnit.short_description = u'Corporación'

#Soporte Técnico
class SIGpcAdmin(admin.TabularInline):
    model = minssotesigpc
    extra = 1
class SopPeopAdmin(admin.TabularInline):
    model = minssoptechrs
    extra = 1

class SopTecAdmin(admin.ModelAdmin):
    list_display = ['getnit', 'misoptec', 'missigex', 'missrhex', 'mislaexi', 'misrmaex', 
        'misrmcex', 'misrmhex'] 
    inlines = [SIGpcAdmin, SopPeopAdmin]

    def getnit(self, obj):
        return '%s'%(obj.misoptec.midginit)
    getnit.short_description = u'Corporación'

#POMCAS
class POMCAPeopAdmin(admin.TabularInline):
    model = minsrhvinpomc
    extra = 1

class POMCAAdmin(admin.ModelAdmin):
    list_display = ['getnit', 'mipomcex', 'mipomcde', 'mipomcdm']
    inlines = [POMCAPeopAdmin]

    def getnit(self, obj):
        return '%s'%(obj.mipocasc.midginit)
    getnit.short_description = u'Corporación'

admin.site.register(minstportada, PortadaAdmin)
admin.site.register(minstdatgene, DatGeneAdmin)
admin.site.register(minstestdire, EstDirectAdmin)
admin.site.register(minstorganiz, OrganizAdmin)
admin.site.register(minesorsubdir, SubdirecAdmin)
admin.site.register(minstdescentr, RegionalAdmin)
admin.site.register(minstplanific, PGARAdmin)
#admin.site.register(minstplanpdai, PAIAdmin)
admin.site.register(minspresupues, PresupuesAdmin)
admin.site.register(minssopotecni, SopTecAdmin)
admin.site.register(minsrecurhuma, POMCAAdmin)
