# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

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

class cartoginven(models.Model):
    cartuser = models.ForeignKey(User)
    cartplan = models.CharField(u'Numeración de la plancha', max_length = 50)
    cartform = models.CharField(u'Formato', max_length = 10)
    cartesca = models.IntegerField(u'Escala')
    cartfano = models.SmallIntegerField(u'Año. Fuente')
    carteano = models.SmallIntegerField(u'Año. Elaboración')
    
    class Meta:
        verbose_name = u'Inventario de cartografía'
        verbose_name_plural = verbose_name

class cartogrlist(models.Model):
    listplan = models.CharField(u'Nombre de plancha', max_length = 25)
    listuser = models.ForeignKey(User, verbose_name=u'Usuario')
    listfano = models.SmallIntegerField(u'Año. Fuente')
    listeano = models.SmallIntegerField(u'Año. Elaboración')

class cartonargis(models.Model):
    planchav = models.CharField(max_length = 15, null = True, blank = True)
    objectid = models.IntegerField(null = True, blank = True)
    estedosc = models.CharField(max_length = 15, null = True, blank = True)
    shapelen = models.FloatField(null = True, blank = True)
    shapeare = models.FloatField(null = True, blank = True)
    repetida = models.IntegerField(null = True, blank = True)
    disponib = models.CharField(max_length = 3, null = True, blank = True)

class nargisyearc(models.Model):
    archgrid = models.ForeignKey('cartonargis', verbose_name=u'Plancha ArcGIS', unique = True)
    yeafeigh = models.NullBooleanField(u'Años Fuente Menores al año 1990')
    yeafnine = models.NullBooleanField(u'Años Fuente entre 1990 y 2000')
    yeaftwen = models.NullBooleanField(u'Años Fuente entre 2000 y 2010')
    yeaftwte = models.NullBooleanField(u'Años Fuente mayores al 2010')
    yeaeeigh = models.NullBooleanField(u'Años Elaboracion Menores al año 1990')
    yeaenine = models.NullBooleanField(u'Años Elaboracion entre 1990 y 2000')
    yeaetwen = models.NullBooleanField(u'Años Elaboracion entre 2000 y 2010')
    yeaetwte = models.NullBooleanField(u'Años Elaboracion mayores al 2010')

    class Meta:
        verbose_name = u'Clasificación cartografía [2010, 2000, 1990]'
        verbose_name_plural = verbose_name

class nargisyearb(models.Model):
    archgrid = models.ForeignKey('cartonargis', verbose_name=u'Plancha ArcGIS', unique = True)
    yeafzero = models.NullBooleanField(u'Fuente: Últimos cinco años - Corte 2013', default = False) 
    yeaffive = models.NullBooleanField(u'Fuente: Entre cinco y quince años', default = False)
    yeaffift = models.NullBooleanField(u'Fuente: Entre quince y veinticinco años', default = False)  
    yeaftwnt = models.NullBooleanField(u'Fuente: Mayor a veinticinco años', default = False)  
    yeafnone = models.NullBooleanField(u'Fuente: No reporta año', default = False)
    yeaezero = models.NullBooleanField(u'Elaboración: Últimos cinco años - Corte 2013', default = False) 
    yeaefive = models.NullBooleanField(u'Elaboración: Entre cinco y quince años', default = False)
    yeaefift = models.NullBooleanField(u'Elaboración: Entre quince y veinticinco años', default = False)  
    yeaetwnt = models.NullBooleanField(u'Elaboración: Mayor a veinticinco años', default = False)  
    yeaenone = models.NullBooleanField(u'Elaboración: No reporta año', default = False)
    class Meta:
        verbose_name = u'Clasificación cartografía [5, 10, 15, 25] años'
        verbose_name_plural = verbose_name
    
class areaspomcab(models.Model):
    arpopomc = models.CharField(max_length = 50)
    arponcar = models.CharField(max_length = 50)
    arpoarea = models.IntegerField()
    arpopora = models.FloatField()
