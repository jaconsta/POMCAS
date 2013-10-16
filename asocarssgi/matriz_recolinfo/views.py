# -*- coding: utf-8 -*-
from matriz_recolinfo.models import *
import xlrd

from asocarssgi import default_names

def SetComponentesFile(text_addr):
    source = file.open(text_addr, 'r+')
    return False

def SetComponentesExcel(excel_addr):
    '''
    Must be on the first sheet
    '''
    def SetComponentes(compo, padr):
        component = componentes(
            componen = compo,
            comppadr = padr,
        )
        component.save()
        return component

    firstval = componentes.objects.get(pk=1)
    componen = 0
    subcompo = 0

    excel_file = xlrd.open_workbook(excel_addr)
    excel_sheet = excel_file.sheet_by_index(0)
    
    for rowini in range(excel_sheet):
        #Componente
        colcompo = excel_sheet.cell_value(colx = 0, rowx = rowini)
        if not colcompo:
            coponen = SetComponentes(colcompo, firstval)
        #SubComponente
        colsubco = excel_sheet.cell_value(colx = 1, rowx = rowini)
        if not colsubco;
            subcompo = SetComponentes(colsubco, componen)
        #Actividad
        coltipoi = excel_sheet.cell_value(colx = 2, rowx = rowini)
        SetComponentes(coltipoi, subcompo) 

@login_required(login_url = ('%slogin/' %(default_names.SUB_SITE)))
def recolinfo_form(request):
    if request.method == 'POST':
        form = CompoInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('formulario_completo.html')
    else:
        form = CompoInfoForm()

        return render(request, 'recoleccion_info.html', {
            'form':form,
        })
