#-*- coding: utf-8 -*-
from django.contrib import admin
from matriz_infoidentifi.models import inforcompon, inforindice #General info
from matriz_infoidentifi.models import inidsuestud, inidsumegeo, inidsumesue, \
    inidsuinfor #Suelos

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
    
admin.site.register(inforcompon, InfoAdmin)
admin.site.register(inidsuestud, SuelosAdmin)
