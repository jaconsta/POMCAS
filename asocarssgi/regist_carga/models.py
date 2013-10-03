#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from django.forms import ModelForm

class archivosb(models.Model):
    ESTADO_ARCHIVO = (
	('REC', 'Recibido'),
	('REV', 'Revisando'),
	('APR', 'Aprobado'),
	('INV', 'Invalido'),
	('REJ', 'Rechazado'),
    )
    archnomb = models.CharField(u'nombre del archivo', max_length = 25)
    archubic = models.FileField(u'Ubicación del archivo', upload_to= 'matrix/')
    archuser = models.ForeignKey(User, related_name = 'Usuario que carga')
    archdati = models.DateTimeField(auto_now_add = True)
    archorna = models.CharField(u'Nombre original del archivo', max_length = 100)
    #archmatr = models.(u'Matriz a la que pertenece', 
    #archmape = models.(u'Pestaña de la matriz',
    archesta = models.CharField(u'Estado del archivo', choices = ESTADO_ARCHIVO,
	                        default = 'REC', max_length = 4)

class archivostest(models.Model):
    archubic = models.FileField(u'Ubicación del archivo', upload_to= 'matrix/')
    archnomb = models.CharField(u'Nombre del archivo', max_length=75)

class CargaForm(ModelForm):
	class Meta:
		model = archivostest
