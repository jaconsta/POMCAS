#-*- coding: utf-8 -*-
from django.contrib import admin
from matriz_cartografica.models import cartoginven 
from matriz_cartografica.models import nargisyearc, nargisyearb

class InvenAdmin(admin.ModelAdmin):
    list_display = ['cartplan', 'cartuser', 'cartesca', 'cartfano', 'carteano']
    list_filter = ['cartuser']

class yearCAdmin(admin.ModelAdmin):
    list_display = ['archgrid', 'yeafeigh', 'yeafnine', 'yeaftwen', 'yeaftwte', 'yeaeeigh', 'yeaenine', 'yeaetwen', 'yeaetwte']
    list_filter = ['archgrid__planchav']

admin.site.register(cartoginven, InvenAdmin)
admin.site.register(nargisyearb)
admin.site.register(nargisyearc, yearCAdmin)
