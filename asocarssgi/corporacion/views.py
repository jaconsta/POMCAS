# -*- coding: utf-8 -*-
from .models import *
from cuencas.models import cuencompart

def GetCuencasPorCoporac(sigla):
    corporac = corporaname.objects.get(corposig = sigla)
    cuencasoc = cuencompart.objects.filter(cuencomp = corporac)
    return cuencasoc
