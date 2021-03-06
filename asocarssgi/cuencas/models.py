#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2013-2014 ASOCARS
#
from django.db import models
from django.contrib.auth.models import User

from corporacion.models import corporaname
    
class macrocuenca(models.Model):
    macrcuen = models.CharField(u'Nombre de la macrocuenca', max_length = 50)

    def __unicode__(self):
        return self.macrcuen

class cuencadescr(models.Model):
    macrocue = models.ForeignKey('macrocuenca', verbose_name=u'Macrocuenca')
    cuencano = models.CharField(u'Nombre de la cuenca', max_length = 250)
    cuencodi = models.IntegerField(u'Código')
    cuensubc = models.SmallIntegerField(u'Sub-Código', null = True, blank = True)
    cuenprio = models.SmallIntegerField(u'Prioridad', null = True, blank = True)
    cuennive = models.CharField(u'Nivel', max_length = 10)
    cuenarea = models.FloatField(u'Área')
    cuencomp = models.NullBooleanField(u'Compartida', default = False, null = True, blank = True)
    cuenobse = models.CharField(u'Observaciones', max_length = 500, null = True, blank = True)
    cuenmuni = models.IntegerField(u'Cantidad de municipios', null = True, blank = True)

    def __unicode__(self):
        if self.cuensubc == None:
            return '%s, %s' % (self.cuencodi, self.cuencano)
        return u'%s - %s, %s' % (self.cuencodi, self.cuensubc, self.cuencano)

class cuencompart(models.Model):
    cuencano = models.ForeignKey('cuencadescr', verbose_name = u'Nombre de la cuenca')
    cuencomp = models.ForeignKey(corporaname, verbose_name = u'Nombre de la corporación')
    comparea = models.FloatField(u'Área compartida de la corporación', null = True, blank = True)
    compporc = models.FloatField(u'Porcentaje área compartida', null = True, blank = True)

    def __unicode__(self):
        if self.cuencano.cuensubc == None:
            return '%s, %s' % (self.cuencano.cuencodi, self.cuencano.cuencano)
        return '%s - %s, %s' % (self.cuencano.cuencodi, self.cuencano.cuensubc, self.cuencano.cuencano)
