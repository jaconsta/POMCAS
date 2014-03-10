#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# Copyright 2013-2014 ASOCARS
#
'''
'''

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from matriz_presupuestos import forms

def GetForm(request):
    if request.method == 'POST':
        print request.POST
        form = forms.presup_recieve(request.POST)
        if form.is_valid():
            form.save()
        #for i in form:
        #    if i.errors:
        #        print (i.label, i.errors)
        return HttpResponse(u'Hello World')
    else:
        form = forms.presup_recieve()
    return render(request, 'recie.xml', {
        'form': form,
    })
       # HttpResponse(u'Nothing recieved')
