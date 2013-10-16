# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

from cuencas.models import cuencadescr
from corporacion.models import corporaname

class componentes(models.Model):
    componen = models.CharField(u'Componente', max_length = 500)
    comppadr = models.ForeignKey('componentes', null = True, blank = True)
    def __unicode__(self):
        return self.componen

class compoinform(models.Model):
    compinfo = models.ForeignKey('componentes')
    infouser = models.ForeignKey(corporaname, verbose_name = u'Corporación')
    infocuen = models.ForeignKey(cuencadescr, verbose_name = u'Cuenca')
    infoestu = models.CharField(u'Nombre del estudio', max_length = 250)
    infoubic = models.CharField(u'Ubicación', max_length = 250)
    infoform = models.CharField(u'Formato', max_length = 50)
    infoanno = models.SmallIntegerField(u'Año')
    def __unicode__(self):
        return u'%s, %s, %s'%(self.infoestu, self.infoubic, self.infoform)

class CompoInfoForm(ModelForm):
    class Meta:
        model = compoinform
