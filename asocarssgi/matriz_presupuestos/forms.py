#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# Copyright 2013-2014 ASOCARS
#
'''
'''

from django.forms import ModelForm
from django import forms

from matriz_presupuestos.models import presupuest_recieve

class presup_recieve(ModelForm):
    class Meta:
        model = presupuest_recieve
