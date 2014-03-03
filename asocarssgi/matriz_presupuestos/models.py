from django.db import models

# Create your models here.

class presupuest_recieve(models.Model):
    watersheed = models.CharField(max_length = 500, null = True, blank = True)
    aprest_transpor_unitario = models.FloatField(null = True, blank = True)
    aprest_transpor_cantidad = models.IntegerField(null = True, blank = True)
    diag_estudio_coberturas = models.FloatField(null = True, blank = True)
    diag_estudio_multitemporal = models.FloatField(null = True, blank = True)
    diag_estudio_plana = models.FloatField(null = True, blank = True)
    diag_estudio_ladera = models.FloatField(null = True, blank = True)
    diag_estudio_geologica = models.FloatField(null = True, blank = True)
    diag_estudio_electricos = models.FloatField(null = True, blank = True)
    diag_estudio_caliagua = models.FloatField(null = True, blank = True)
    diag_estudio_ecologica = models.FloatField(null = True, blank = True)
    diag_transpor_unitario = models.FloatField(null = True, blank = True)
    diag_transpor_cantidad = models.FloatField(null = True, blank = True)
    zoni_transpor_unitario = models.FloatField(null = True, blank = True)
    zoni_transpor_cantidad = models.IntegerField(null = True, blank = True)
    formula_transpor_unitario = models.FloatField(null = True, blank = True)
    formula_transpor_cantidad = models.IntegerField(null = True, blank = True)
