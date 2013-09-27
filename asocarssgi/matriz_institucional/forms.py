#-*- coding: utf-8 -*-
from django import forms

class UploadFileForm(forms.Form):
    archivo = forms.FileField(u'Matriz Diagnóstico Institucional')
    soportes = forms.FileField(u'Soportes en archivo comprimido')
