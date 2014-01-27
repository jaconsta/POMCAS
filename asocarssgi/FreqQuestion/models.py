#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Topic (models.Model):
    tema = models.CharField(u'Tema', max_length = 200)

    def __unicode__(self):
        return self.tema
    class Meta:
        verbose_name = u'1. Contexto'

class Questions(models.Model):
    qutopic = models.ForeignKey('Topic', verbose_name = u'Tema', null = True, blank = True)
    questio = models.CharField(u'Pregunta', max_length = 250)
    pubdate = models.DateField(u'Fecha de publicación', auto_now_add = True)
    whopost = models.CharField(u'Quién pregunta', max_length = 150)

    def __unicode__(self):
        return self.questio
    class Meta:
        verbose_name = u'2. Pregunta'

class Answer(models.Model):
    questio = models.ForeignKey('Questions', verbose_name = u'Pregunta')
    answers = models.CharField(u'Respuesta', max_length = 500)
    whoansr = models.ForeignKey(User, verbose_name = u'Usuario que responde')
    sources = models.CharField(u'Fuente', max_length = 250)
    avaliab = models.BooleanField(u'Mostrar', default = True)

    def __unicode__(self):
        return self.answers
    class Meta:
        verbose_name = u'3. Respuesta'
