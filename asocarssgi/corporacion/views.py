# -*- coding: utf-8 -*-
from .models import *
from cuencas.models import cuencompart

def GetCuencasPorCoporac(sigla):
    corporac = corporaname.objects.get(corposig = sigla)
    cuencasoc = cuencompart.objects.filter(cuencomp = corporac)
    return cuencasoc

def GetUserCorpo(user_id):
    '''
    Get all corporations which belongs to an user
    '''
    return corporaname.objects.filter(corpousr = user_id.id)
