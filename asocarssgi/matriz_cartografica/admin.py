#-*- coding: utf-8 -*-
from django.contrib import admin
from matriz_cartografica.models import cartoginven 
from matriz_cartografica.models import nargisyearc, nargisyearb

class InvenAdmin(admin.ModelAdmin):
    list_display = ['cartplan', 'cartuser', 'cartesca', 'cartfano', 'carteano']

admin.site.register(cartoginven, InvenAdmin)
admin.site.register(nargisyearb)
admin.site.register(nargisyearc)
