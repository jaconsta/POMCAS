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

class compoactivi(models.Model):
    compoact = models.ForeignKey('componentes', verbose_name = u'Componente')
    coacdesc = models.CharField(u'Tipo de información', max_length = 500)
    coacpreg = models.CharField(u'Pregunta validación', max_length = 500, null = True, blank = True)
    #coacmins = models.ForeignKey('formatminst', verbose_name = 'Formulario Ministerio')
    def __unicode__(self):
        return u'%s, %s' % (self.coacdesc, self.coacpreg)

class compoinform(models.Model):
    compinfo = models.ForeignKey('compoactivi', verbose_name = u'Actividad')
    infouser = models.ForeignKey(corporaname, verbose_name = u'Corporación')
    infocuen = models.ForeignKey(cuencadescr, verbose_name = u'Cuenca')
    infoestu = models.CharField(u'Nombre del estudio', max_length = 250)
    infoubic = models.CharField(u'Ubicación geográfica del estudio', max_length = 250)
    infocubr = models.FloatField(u'#Cubrimiento espacial de la cuenca en hectáreas')
    infocupr = models.FloatField(u'#Cubrimiento espacial de la cuenca en porcentaje')
    infocuti = models.CharField(u'Tipo de cobertura', max_length = 10)
    infocude = models.CharField(u'Detalle de cobertura', max_length = 50)
    infoform = models.CharField(u'Formato', max_length = 50)
    infoanoe = models.SmallIntegerField(u'#Año de realización')
    infolode = models.CharField(u'#Localización dependencia', max_length = 250)
    infofure = models.CharField(u'#Funcionario Responsable', max_length = 250)
    infoauth = models.CharField(u'#Autor del estudio', max_length = 250, null = True, 
        blank = True, editable = False)
    infoanop = models.SmallIntegerField(u'Año de publicación', null = True,
        blank = True, editable = False)
    def __unicode__(self):
        return u'%s, %s, %s, %s, %s, %s, %s'%(self.infoestu, self.infoubic, self.infocuti,
            self.infocude, self.infoform, self.infolode, self.infoauth)

###Adición formato ministerio

class formatminst(models.Model):
    fominomb = models.CharField(u'Nombre del formato', max_length = 125)
    fomitema = models.CharField(u'Tema a evaluar', max_length = 125)
    def __unicode__(self):
        return u'%s, %s' % (self.fominomb, self.fomitema)

class fomicarcomp(models.Model):
    forminst = models.ForeignKey('formatminst', verbose_name = u'Formato del ministerio')
    fomicomp = models.CharField(u'Componente', max_length = 125)
    def __unicode__(self):
        return self.fomicomp

class fomicaracte(models.Model):
    fomicomp = models.ForeignKey('formatminst', verbose_name = u'Componente')
    fomcarac = models.CharField(u'Característica', max_length = 250)
    fomcisnu = models.BooleanField(u'Campo numérico?', default = False)
    fomcisfl = models.BooleanField(u'Campo flotante?', default = False)
    foecisbo = models.BooleanField(u'Campo Boolean?', default = False)
    def __unicode__(self):
        return self.fomcarac

class fomidescrip(models.Model):
    fomicara = models.ForeignKey('fomicaracte', verbose_name = u'Característica del componente')
    fomiapli = models.NullBooleanField(u'Aplica?')
    fomidesc = models.CharField(u'Descripción', max_length = 500)
    fomideda = models.DateTimeField(u'Última modificación', auto_now = True)
    def __unicode__(self):
        return self.fomidesc

class relaminlist(models.Model):
    remilimi = models.ForeignKey('fomicarcomp')
    remilili = models.ForeignKey('compoactivi')

### Forms
class CompoInfoForm(ModelForm):
    class Meta:
        model = compoinform
