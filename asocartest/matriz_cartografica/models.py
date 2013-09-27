# -*- coding: utf-8 -*-
from django.db import models

class matrcartogb(models.Model):
    cartcorp = models.CharField(u'Corporacion SIGLA', max_length = 10)
    cartnupl = models.CharField(u'Numeracion de plancha', max_length = 20, null = True, blank = True)
    cartform = models.CharField(u'Formato', max_length = 100, null = True, blank = True)
    cartfeel = models.PositiveSmallIntegerField(u'Fecha elaboracion', max_length = 20, null = True, blank = True)
    cartliex = models.BooleanField(u'Licencia, tiene')
    cartliti = models.CharField(u'Licencia, tipo', max_length = 5, null = True, blank = True)
    cartlinu = models.CharField(u'Licencia, numero', max_length = 20, null = True, blank = True)
    cartubde = models.CharField(u'Ubicacion de la cartografia, descripcion', max_length = 100, null = True, blank = True)
    cartubre = models.CharField(u'Ubicacion de la cartografia, descripcion', max_length = 25, null = True, blank = True)
    cartcuco = models.CharField(u'Cuenca para la que fue adquirida, codigo', max_length = 20, null = True, blank = True)
    cartcuno = models.CharField(u'Cuenca para la que fue adquirida, Nombre', max_length = 100, null = True, blank = True)
    cartvali = models.BooleanField(u'La matriz es valida', default = False)

class areaspomcab(models.Model):
    arpopomc = models.CharField(max_length = 50)
    arponcar = models.CharField(max_length = 50)
    arpoarea = models.IntegerField()
    arpopora = models.FloatField()
