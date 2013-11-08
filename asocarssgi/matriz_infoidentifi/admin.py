#-*- coding: utf-8 -*-
from django.contrib import admin
from matriz_infoidentifi.models import inforcompon, inforindice #General info
from matriz_infoidentifi.models import inidsuestud, inidsumegeo, inidsumesue, \
    inidsuinfor #Suelos
from matriz_infoidentifi.models import inidhlestud, inidhlmetod, inidhlcarto, \
    ihlmethafor #Hidrología
from matriz_infoidentifi.models import inidhgestud, inidhgmetho, inidhgcarto #Hidrogeología

#General Information

class InfoIndice(admin.TabularInline):
    model = inforindice
    extra = 2

class InfoAdmin(admin.ModelAdmin):
    list_display = ['infocomp']
    inlines = [InfoIndice]

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
class AforMethAdmin(admin.TabularInline):
    model = ihlmethafor

class HidrolAdmin(admin.ModelAdmin):
    list_display = ['iniescor', 'iniescue', 'inidnomb']
    inlines = [MethoHidroAdmin, CartHidroAdmin]

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

admin.site.register(inforcompon, InfoAdmin)
admin.site.register(inidsuestud, SuelosAdmin)
admin.site.register(inidhlestud, HidrolAdmin)
admin.site.register(inidhlmetod, MethHidrAdmin)
admin.site.register(inidhgestud, HidrgAdmin)
