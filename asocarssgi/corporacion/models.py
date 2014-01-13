# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class corporaname(models.Model):
    corporac = models.CharField(u'Nombre Corporación', max_length = 100, unique = True)
    corpousr = models.ForeignKey(User, verbose_name = 'Usuario Asociado', null = True, blank = True)
    corposig = models.CharField(u'Sigla', max_length = 20, unique = True)
    corponit = models.IntegerField(u'NIT', unique = True)
    corpondv = models.SmallIntegerField(u'Dígito de verificación', null = True, blank = True)
    corpoadd = models.CharField(u'Dirección', max_length = 125, null = True, blank = True)
    cropodep = models.CharField(u'Departamento', max_length = 25, null = True, blank = True) #Should be a Foreign key
    corpocit = models.CharField(u'Ciudad', max_length = 25, null = True, blank = True)  #Should be a Foreign key
    corpodir = models.CharField(u'Nombre del director', max_length = 75, null = True, blank = True)

    def __unicode__(self):
        return u'%s, %s' % (self.corposig, self.corponit)
