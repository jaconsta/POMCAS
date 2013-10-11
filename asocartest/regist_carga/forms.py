#-*- coding: utf-8 -*-
from django import forms

class UploadFileForm(forms.Form):
    archivo = forms.FileField(label=u'Matriz Diagnóstico Institucional') #, upload_to= 'matrix/')
    soportes = forms.FileField(label=u'Soportes en archivo comprimido') #, upload_to= 'matrix/')

class UploadMCartogForm(forms.Form):
    archivo = forms.FileField(label=u'Matriz Cartográfica') #, upload_to= 'matrix/')
