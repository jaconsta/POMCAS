#-*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
#from django.contrib.auth.models import User

from asocarssgi import default_names
from cuencas.views import GetCorpoCuencas, GetUserWatersheed
from corporacion.views import GetUserCorpo, GetUserCorpo

from matriz_infoidentifi.models import inforcompon, inforindice
from matriz_infoidentifi import forms

def GetName():
    title = u'Formatos de evaluación de información disponible para la \
        Formulación y/o Ajuste de los POMCAS'
    return title

class GetUserAttr():
    def __init__(self, request, shared_id):
        self.user = request.user
        self.corpora = GetUserCorpo(request.user)
        self.watersheed = GetUserWatersheed(self.corpora, shared_id)

@login_required(login_url = ('%slogin/' %(default_names.SUB_SITE)))
def CuencasDeCorpo(request):
    '''
    List all watersheds avaliable for a given corporation
    '''
    try:
        corpora = GetUserCorpo(request.user)
        watershed = GetCorpoCuencas(corpora)
    except ObjectDoesNotExist:
       return render(request, 'recoleccion_error.html', {
           'error':u'El Usuario no tiene una corporación asociada Exp',
       })

    if not len(corpora):
       return render(request, 'recoleccion_error.html', {
           'error':u'El Usuario no tiene una corporación asociada',
       })
    if not len(watershed):
       return render(request, 'recoleccion_error.html', {
           'error':u'La corporación no tiene cuencas asociadas',
       })

    return render(request, 'list_cuenca.html', {
        'usr' : request.user, 'corpo': corpora, 'watersheed': watershed, 
        'title' : GetName(),
    }) 

def list(request, shared_id):
    '''
    This should do something about showing a resume of all objects.
    - List all forms filled  
    - The evaluation concept
    - Link to the different forms for this module
    
    Now it'll do nothing
    '''
    templink ='<a href="add">Click Aqui</a>'
    return HttpResponse(templink)   
    
@login_required(login_url = ('%slogin/' %(default_names.SUB_SITE)))
def addi(request, shared_id):
    '''
    Provides a link for all the forms avaliable. 
    As the Index page in the Excel file.
    '''
    def GetCompo():
        comp = inforcompon.objects.all()
        compolist = []
        for i in comp:
            subcom = inforindice.objects.filter(infocomp = i)
            compolist.append([i, subcom])
        return compolist
    return render(request, 'formlist.html', {
        'usr' : request.user, #'corpo': corpora, 'watersheed': watershed, 
        'title' : GetName(), 'compo' : GetCompo(),
    }) 

@login_required(login_url = ('%slogin/' %(default_names.SUB_SITE)))
def add(request, shared_id, subcompo):
    '''
    Selects which subcomponent will be added, 
        for that uses the subcompo variable
    '''
    usrattr = GetUserAttr(request, shared_id)
    ####
    if request.method == 'POST':
        formlist = {u'Cartografia' : forms.CartografiaForm(request.POST),
            u'Imagenes' : forms.ImagenesForm(request.POST),
            u'Fotografias' : forms.FotografiasForm(request.POST),
            u'Suelos' : forms.SuelosForm(request.POST),
            u'Hidrologia' : forms.HidrologiaForm(request.POST),
            u'Hidrogeologia' : forms.HidrogeologiaForm(request.POST),
            u'CalidadDeAgua' : forms.CalidadDeAguaForm(request.POST),
            u'CargasContaminantes' : forms.CargasContaminantesForm(request.POST),
            u'Cobertura' : forms.CoberturaForm(request.POST),
            u'FloraYFauna' : forms.FloraYFaunaForm(request.POST),
            u'PMEcosistemas' : forms.PMEcosistemasForm(request.POST),
            u'Amenazas' : forms.AmenazasForm(request.POST),
            u'Riesgos' : forms.RiesgosForm(request.POST),
            u'seActoresSoc' : forms.seActoresSocForm(request.POST),
            u'seEstrParticip' : forms.seEstrParticipForm(request.POST),
            u'seParticComuEtnicas' : forms.seParticComuEtnicasForm(request.POST),
            u'seDiagSocioEconom' : forms.seDiagSocioEconomForm(request.POST),
            u'seCaractCultural' : forms.seCaractCulturalForm(request.POST),
            u'seValorServicEcos' : forms.seValorServicEcosForm(request.POST),
            u'seRelaFuncUrbaRegio' : forms.seRelaFuncUrbaRegioForm(request.POST),
        }
        form = formlist[subcompo] # getattr(forms, '%sForm(request.POST)' % subcompo.title())
        if form.is_valid():
            form.iniescor = usrattr.corpora
            form.iniescue = usrattr.watersheed
            form.inieswho = usrattr.user
            form.inieswhu = usrattr.user
            return 
    else:
        formlist = {u'Cartografia' : forms.CartografiaForm(),
            u'Imagenes' : forms.ImagenesForm(),
            u'Fotografias' : forms.FotografiasForm(),
            u'Suelos' : forms.SuelosForm(),
            u'Hidrologia' : forms.HidrologiaForm(),
            u'Hidrogeologia' : forms.HidrogeologiaForm(),
            u'CalidadDeAgua' : forms.CalidadDeAguaForm(),
            u'CargasContaminantes' : forms.CargasContaminantesForm(),
            u'Cobertura' : forms.CoberturaForm(),
            u'FloraYFauna' : forms.FloraYFaunaForm(),
            u'PMEcosistemas' : forms.PMEcosistemasForm(),
            u'Amenazas' : forms.AmenazasForm(),
            u'Riesgos' : forms.RiesgosForm(),
            u'seActoresSoc' : forms.seActoresSocForm(),
            u'seEstrParticip' : forms.seEstrParticipForm(),
            u'seParticComuEtnicas' : forms.seParticComuEtnicasForm(),
            u'seDiagSocioEconom' : forms.seDiagSocioEconomForm(),
            u'seCaractCultural' : forms.seCaractCulturalForm(),
            u'seValorServicEcos' : forms.seValorServicEcosForm(),
            u'seRelaFuncUrbaRegio' : forms.seRelaFuncUrbaRegioForm(),
        }
        form = formlist[subcompo] # getattr(forms, '%sForm()' % subcompo.title())
        return render(request, 'forms.html', {
            'form': form,
            'title' : GetName(), 
            #'compo' : GetCompo(),
        })
    ####
    return getattr(forms, 'add_%s(request, usrattr)' % subcompo)

#    #Fist, validate if subcompo is in the list of matrices avaliable
#    #Kinda a security validation, because using 'eval'
#    
#    #Execute the add function to render or process the form
##    eval('add_'+subcompo+'()')
##    if subcompo == 'cartografia':
##        return add_(request, shared_id)
##    elif subcompo == 'imagenes':
##        return add_(request, shared_id)
##    elif subcompo == 'fotografias':
##        return add_(request, shared_id)
##    elif subcompo == 'suelos':
##        return add_(request, shared_id)
##    elif subcompo == 'hidrologia':
##        return add_(request, shared_id)
##    elif subcompo == 'hidrogeologia':
##        return add_(request, shared_id)
##    elif subcompo == 'calidaddeagua':
##        return add_(request, shared_id)
##    elif subcompo == 'cargascontaminantes':
##        return add_(request, shared_id)
##    elif subcompo == 'cobertura':
##        return add_(request, shared_id)
##    elif subcompo == 'florayfauna':
##        return add_(request, shared_id)
##    elif subcompo == 'pmecosistemas':
##        return add_(request, shared_id)
##    elif subcompo == 'riesgos':
##        return add_(request, shared_id)
##    elif subcompo == 'seactoressoc':
##        return add_(request, shared_id)
##    elif subcompo == 'seestrparticip':
##        return add_(request, shared_id)
##    elif subcompo == 'separticcomuetnicas':
##        return add_(request, shared_id)
##    elif subcompo == 'sediagsocioeconom':
##        return add_(request, shared_id)
##    elif subcompo == 'secaractcultural':
##        return add_(request, shared_id)
##    elif subcompo == 'sevalorservicecos':
##        return add_(request, shared_id)
##    elif subcompo == 'serelafuncurbaregio':
##        return add_(request, shared_id)
##    else:
##        return HttpResponse('La matriz no existe')   
