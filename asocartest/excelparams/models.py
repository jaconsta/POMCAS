from django.db import models

class matriznombr(models.Model):
	matrinombr = models.CharField(max_length = 250)
	matriobjet = models.CharField(max_length = 500)
	matrifeche = models.DateField()
	matrifechc = models.DateTimeField()
	matriautoa = models.CharField(max_length = 125)
	matriautob = models.CharField(max_length = 125, null = True, blank = True)
	matriaturb = models.CharField(max_length = 125, null = True, blank = True)
	matrinomin = models.CharField(max_length = 250, null = True, blank = True)

class matrizpesta(models.Model):
	pestamatri = models.ForeignKey('matriznombr')
	pestanombr = models.CharField(max_length = 250)
	pestaindic = models.PositiveIntegerField()

class matrizparam(models.Model):
	paramatriz = models.ForeignKey('matriznombr')
	parapestan = models.ForeignKey('matrizpesta')
	paranombre = models.CharField(max_length = 250)
	paramtexto = models.CharField(max_length = 250, null = True, blank = True)
	paranocolu = models.PositiveSmallIntegerField()
	paranofila = models.PositiveSmallIntegerField()
	paramvalor = models.CharField(max_length = 250, null = True, blank = True)
	paravacolu = models.PositiveSmallIntegerField()
	paravafila = models.PositiveSmallIntegerField()
	paraobliga = models.BooleanField(default = True)
