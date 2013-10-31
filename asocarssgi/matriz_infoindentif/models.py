from django.db import models

class infocompon(models.Model):
    infocomp = models.CharField(u'Componente', max_length = 75)

class infoindice(models.Model):
    infocomp = models.ForeignKey('infocompon' , verbose_name = u'Componente')
    infosubc = models.CharField(u'Subcomponente', max_length = 75)
    infourlc = models.URLField(u'Dirección capacitación')
    infoprio = models.PositiveSmallIntegerField(u'Prioridad')
    infonota = models.CharField(u'Notas aclaratorias', max_length = 1000)

    

