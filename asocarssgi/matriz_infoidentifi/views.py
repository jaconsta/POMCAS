#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# Copyright 2013-2014 ASOCARS
#
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
#from django.contrib.auth.models import User

from asocarssgi import default_names
from cuencas.views import GetCorpoCuencas, GetUserWatersheed
from corporacion.views import GetUserCorpo

from matriz_infoidentifi.models import inforcompon, inforindice, inididestud
from matriz_infoidentifi.models import inidcardatg, inidimagsat, inidfotogra
from matriz_infoidentifi import forms
from matriz_infoidentifi.resume import GetResume, GetSubtopicResume, \
    GetCartoSubtopicFK, GetEstudFK, GetSubcompoName

from matriz_infoidentifi.reports import FormsFilled, LoadCartoProgress #General Load process
from matriz_infoidentifi.reports import WatersheedCartografiaResume, CorporationsWhoCartografia,\
    CorporationsCartografiaFilled, CorporationsScaleCartografia,\
    WatersheedWhoCartografia, WatersheedCartografiaFilled, \
    WatersheedCartoGridsClassif, WatersheedCartoGridsOfficialClassif,\
    WatersheedCartoCoveredArea # Cartografía

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

@login_required(login_url = ('%slogin/' %(default_names.SUB_SITE)))
def index(request, shared_id):
    '''
    Provides a link for all the forms avaliable. 
    As the Index page in the Excel file.
    '''
    def GetCompo():
        comp = inforcompon.objects.all()
        compolist = []
        for i in comp:
            subcom = inforindice.objects.filter(infocomp = i).order_by('infoprio')
            compolist.append([i, subcom])
        return compolist
    return render(request, 'formlist.html', {
        'usr' : request.user, 
        'title' : GetName(), 'compo' : GetCompo(),
        'shared_id' : shared_id,
        'watersheed': GetUserWatersheed(GetUserCorpo(request.user), shared_id),
    }) 

def resume(request, shared_id, subcompo):
    '''
    This should do something about showing a resume of all objects.
    - List all forms filled  
    - The evaluation concept
    - Link to the different forms for this module
    '''
    #Get quantity of forms filled by the corporation for the subcompo. 
    corpora = GetUserCorpo(request.user)
    forms = GetResume(request.user, shared_id, subcompo)
    subtree = {
            u'Cartografia' : (u'SubCatastro', u'SubTranspor', 
                u'SubHidrolog', u'SubeRelive', u'SubEntidade'),
            u'Imagenes' : (None),
            u'Fotografias' : (None),
            u'Suelos' : (u'MetodGeomor', u'MetodSuelos', u'DocumYCarto'),
            u'Hidrologia' : (u'Metodologia', u'DocumYCarto'),
            u'Variabilida': (None),
            u'CalcuCaudal': (None),
            u'Hidrogeologia' : (u'MetodoFases', u'Metodologia', u'DocumYCarto'),
            u'CalidadDeAgua' : (u'Metodologia', u'InfoEstudio', u'InfoComplem'),
            u'CargasContaminantes' :(u'Metodologia', u'InfoEstudio', 
                u'InfoComplem'),
            u'Cobertura' : (u'Metodologia', u'DocumYCarto', u'AnaliMultit'),
            u'FloraYFauna' : (u'Metodologia', u'DocumYCarto'),
            u'PMEcosistemas' : (u'Formulacion', u'InforPlanes'),
            u'Amenazas' : (u'Actores'),
            u'Riesgos' : (u'DocumYCarto'),
            u'seActoresSoc' : (u'Detalle'),
            u'seEstrParticip' : (u'Detalle'),
            u'seParticComuEtnicas' : (u'Detalle'),
            u'seDiagSocioEconom' : (u'Detalle'),
            u'seCaractCultural' : (u'Detalle'),
            u'seValorServicEcos' : (u'Detalle'),
            u'seRelaFuncUrbaRegio' : (u'Detalle'),
    }
    subfields = []
    for study in forms:
        subtopic = GetSubtopicResume(subcompo, study)
        subfields.append({'study': study, 'subtopic': subtopic
        })
    return render(request, 'forms_resume.html', {
        'usr': request.user,
        'title': GetName(),
        'subtitle': GetSubcompoName(subcompo),
        'forms': forms,
        'subfields': subfields,
        'subtree' : subtree[subcompo],
        'shared_id' : shared_id,
        'subcompo' : subcompo,
        'watersheed': GetUserWatersheed(GetUserCorpo(request.user), shared_id),
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
        formlist = {
            u'Cartografia' : forms.CartografiaForm(request.POST),
            u'Imagenes' : forms.ImagenesForm(request.POST),
            u'Fotografias' : forms.FotografiasForm(request.POST),
            u'Suelos' : forms.SuelosForm(request.POST),
            u'Hidrologia' : forms.HidrologiaForm(request.POST),
            u'Variabilida': forms.HidroloVariabilidaForm(request.POST),
            u'CalcuCaudal': forms.HidroloCalcuCaudalForm(request.POST),
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
        form = formlist[subcompo] 
        if form.is_valid():
            informacion = form.save(commit = False)
            informacion.iniescor = usrattr.corpora[0]
            informacion.iniescue = usrattr.watersheed
            informacion.inieswho = usrattr.user
            informacion.inieswhu = usrattr.user
            if subcompo != 'Amenazas':
                informacion.inidsubc = subcompo
            informacion.save()
            if subcompo == 'Amenazas':
                #Amenazas is he only one which uses it many2many
                form.save_m2m()
            return HttpResponseRedirect(reverse('matriz_infoidentifi.views.resume', args=(shared_id, subcompo,)))
        return render(request, 'forms.html', {
            'form': form,
            'title' : GetName(), 
            'shared_id' : shared_id,
            'subcompo' : subcompo,
            #'compo' : GetCompo(),
        })

    else:
        formlist = {
            u'Cartografia' : forms.CartografiaForm(),
            u'Imagenes' : forms.ImagenesForm(),
            u'Fotografias' : forms.FotografiasForm(),
            u'Suelos' : forms.SuelosForm(),
            u'Hidrologia' : forms.HidrologiaForm(),
            u'Variabilida': forms.HidroloVariabilidaForm(),
            u'CalcuCaudal': forms.HidroloCalcuCaudalForm(),
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
        form = formlist[subcompo] 
        return render(request, 'forms.html', {
            'form': form,
            'title' : GetName(), 
            'shared_id' : shared_id,
            'subcompo' : subcompo,
            'watersheed': GetUserWatersheed(GetUserCorpo(request.user), shared_id),
            #'compo' : GetCompo(),
        })
    ####

@login_required(login_url = ('%slogin/' %(default_names.SUB_SITE)))
def edit(request, shared_id, subcompo, pk):
    '''
    Selects which subcomponent will be added, 
        for that uses the subcompo variable
    '''
    usrattr = GetUserAttr(request, shared_id)
    if subcompo == 'Cartografia':
        instance = get_object_or_404(inidcardatg, id = pk)
    elif subcompo == 'Imagenes':
        instance = get_object_or_404(inidimagsat, id = pk)
    elif subcompo == 'Fotografias':
        instance = get_object_or_404(inidfotogra, id = pk)
    else:
        instance = get_object_or_404(inididestud, id = pk)
    ####
    if request.method == 'POST':
        formlist = {
            u'Cartografia' : forms.CartografiaForm(request.POST, instance = instance),
            u'Imagenes' : forms.ImagenesForm(request.POST, instance = instance),
            u'Fotografias' : forms.FotografiasForm(request.POST, instance = instance),
            u'Suelos' : forms.SuelosForm(request.POST, instance = instance),
            u'Hidrologia' : forms.HidrologiaForm(request.POST, instance = instance),
            u'Variabilida': forms.HidroloVariabilidaForm(request.POST, instance = instance),
            u'CalcuCaudal': forms.HidroloCalcuCaudalForm(request.POST, instance = instance),
            u'Hidrogeologia' : forms.HidrogeologiaForm(request.POST, instance = instance),
            u'CalidadDeAgua' : forms.CalidadDeAguaForm(request.POST, instance = instance),
            u'CargasContaminantes' : forms.CargasContaminantesForm(request.POST, instance = instance),
            u'Cobertura' : forms.CoberturaForm(request.POST, instance = instance),
            u'FloraYFauna' : forms.FloraYFaunaForm(request.POST, instance = instance),
            u'PMEcosistemas' : forms.PMEcosistemasForm(request.POST, instance = instance),
            u'Amenazas' : forms.AmenazasForm(request.POST, instance = instance),
            u'Riesgos' : forms.RiesgosForm(request.POST, instance = instance),
            u'seActoresSoc' : forms.seActoresSocForm(request.POST, instance = instance),
            u'seEstrParticip' : forms.seEstrParticipForm(request.POST, instance = instance),
            u'seParticComuEtnicas' : forms.seParticComuEtnicasForm(request.POST, instance = instance),
            u'seDiagSocioEconom' : forms.seDiagSocioEconomForm(request.POST, instance = instance),
            u'seCaractCultural' : forms.seCaractCulturalForm(request.POST, instance = instance),
            u'seValorServicEcos' : forms.seValorServicEcosForm(request.POST, instance = instance),
            u'seRelaFuncUrbaRegio' : forms.seRelaFuncUrbaRegioForm(request.POST, instance = instance),
        }
        form = formlist[subcompo] 
        if form.is_valid():
            #f = AuthorForm(request.POST)
            #new_Author = f.save(commit=False)
            #new_Author.some_field = 'some_value'
            #new_Author.save()
            #f.save_m2m()
            informacion = form.save(commit = False)
            informacion.inieswhu = usrattr.user #Updates the user who updates
            #I should validate that the form belongs to the user and watersheed
            # that is connected.
            informacion.save(force_update = True)
            return HttpResponseRedirect(reverse('matriz_infoidentifi.views.resume', args=(shared_id, subcompo,)))
        return render(request, 'forms.html', {
            'form': form,
            'title' : GetName(), 
            'shared_id' : shared_id,
            'subcompo' : subcompo,
            'pk' : pk,
            'watersheed': GetUserWatersheed(GetUserCorpo(request.user), shared_id),
            #'compo' : GetCompo(),
        })
    else:
        formlist = {
            u'Cartografia' : forms.CartografiaForm(request.POST or None, instance = instance),
            u'Imagenes' : forms.ImagenesForm(request.POST or None, instance = instance),
            u'Fotografias' : forms.FotografiasForm(request.POST or None, instance = instance),
            u'Suelos' : forms.SuelosForm(request.POST or None, instance = instance),
            u'Hidrologia' : forms.HidrologiaForm(request.POST or None, instance = instance),
            u'Hidrogeologia' : forms.HidrogeologiaForm(request.POST or None, instance = instance),
            u'Variabilida': forms.HidroloVariabilidaForm(request.POST or None, instance = instance),
            u'CalcuCaudal': forms.HidroloCalcuCaudalForm(request.POST or None, instance = instance),
            u'CalidadDeAgua' : forms.CalidadDeAguaForm(request.POST or None, instance = instance),
            u'CargasContaminantes' : forms.CargasContaminantesForm(request.POST or None, instance = instance),
            u'Cobertura' : forms.CoberturaForm(request.POST or None, instance = instance),
            u'FloraYFauna' : forms.FloraYFaunaForm(request.POST or None, instance = instance),
            u'PMEcosistemas' : forms.PMEcosistemasForm(request.POST or None, instance = instance),
            u'Amenazas' : forms.AmenazasForm(request.POST or None, instance = instance),
            u'Riesgos' : forms.RiesgosForm(request.POST or None, instance = instance),
            u'seActoresSoc' : forms.seActoresSocForm(request.POST or None, instance = instance),
            u'seEstrParticip' : forms.seEstrParticipForm(request.POST or None, instance = instance),
            u'seParticComuEtnicas' : forms.seParticComuEtnicasForm(request.POST or None, instance = instance),
            u'seDiagSocioEconom' : forms.seDiagSocioEconomForm(request.POST or None, instance = instance),
            u'seCaractCultural' : forms.seCaractCulturalForm(request.POST or None, instance = instance),
            u'seValorServicEcos' : forms.seValorServicEcosForm(request.POST or None, instance = instance),
            u'seRelaFuncUrbaRegio' : forms.seRelaFuncUrbaRegioForm(request.POST or None, instance = instance),
        }
        form = formlist[subcompo] 
        return render(request, 'forms.html', {
            'form': form,
            'title' : GetName(), 
            'shared_id' : shared_id,
            'subcompo' : subcompo,
            'pk' : pk,
            'watersheed': GetUserWatersheed(GetUserCorpo(request.user), shared_id),
            #'compo' : GetCompo(),
        })

def subte_forms(request, subcompo, subtema, instance = None):
    subtree = {
            u'Cartografia' : {
                u'SubCatastro': 
                    forms.CartogSubCatastroForm(request.POST or None, instance = instance),
                u'SubTranspor': 
                    forms.CartogSubTransporForm(request.POST or None, instance = instance),
                u'SubHidrolog': 
                    forms.CartogSubHidrologForm(request.POST or None, instance = instance),
                u'SubeRelive': 
                    forms.CartogSubeReliveForm(request.POST or None, instance = instance),
                u'SubEntidade': 
                    forms.SubEntidadeForm(request.POST or None, instance = instance),
                },
            u'Imagenes' : (None,None),
            u'Fotografias' : (None,None),
            u'Suelos' : {
                u'MetodGeomor': 
                    forms.SuelosMetodGeomorForm(request.POST or None, instance = instance),
                u'MetodSuelos': 
                    forms.SuelosMetodSuelosForm(request.POST or None, instance = instance),
                u'DocumYCarto': 
                    forms.SuelosDocumYCartoForm(request.POST or None, instance = instance),
                },
            u'Hidrologia' : {
                u'Estaciones': 
                    forms.HidroloEstacionesForm(request.POST or None, instance = instance),
                u'Metodologia': 
                    forms.HidroloMetodologiaForm(request.POST or None, instance = instance),
                u'AforosCaud':
                    forms.HidroloAforosCaudForm(request.POST or None, instance = instance),
                u'DocumYCarto': 
                    forms.HidroloDocumYCartoForm(request.POST or None, instance = instance),
                #u'Variabilida': 
                #    forms.HidroloVariabilidaForm(request.POST or None, instance = instance),
                #u'CalcuCaudal': 
                #    forms.HidroloCalcuCaudalForm(request.POST or None, instance = instance),
                },
            u'Variabilida' : (None,None),
            u'CalcuCaudal' : (None,None),
            u'Hidrogeologia' : {
                u'MetodoFases':
                    forms.HidrogeoMetodoFasesForm(request.POST or None, instance = instance),
                u'Metodologia': 
                    forms.HidrogeoMetodologiaForm(request.POST or None, instance = instance),
                u'DocumYCarto': 
                    forms.HidrogeoDocumYCartoForm(request.POST or None, instance = instance),
                },
            u'CalidadDeAgua' : {
                u'Metodologia': 
                    forms.CaliAguaMetodologiaForm(request.POST or None, instance = instance),
                u'InfoEstudio': 
                    forms.CaliAguaInfoEstudioForm(request.POST or None, instance = instance),
                u'InfoComplem': 
                    forms.CaliAguaInfoComplemForm(request.POST or None, instance = instance),
                },
            u'CargasContaminantes' :{ 
                u'Metodologia': 
                    forms.CargContMetodologiaForm(request.POST or None, instance = instance),
                u'InfoEstudio': 
                    forms.CargContInfoEstudioForm(request.POST or None, instance = instance),
                u'InfoComplem': 
                    forms.CargContInfoComplemForm(request.POST or None, instance = instance),
                },
            u'Cobertura' : {
                u'Metodologia': 
                    forms.CobertuMetodologiaForm(request.POST or None, instance = instance),
                u'DocumYCarto': 
                    forms.CobertuDocumYCartoForm(request.POST or None, instance = instance),
                u'AnaliMultit': 
                    forms.CobertuAnaliMultitForm(request.POST or None, instance = instance),
                },
            u'FloraYFauna' : {
                u'Metodologia': 
                    forms.FloFauMetodologiaForm(request.POST or None, instance = instance),
                u'DocumYCarto': 
                    forms.FloFauDocumYCartoForm(request.POST or None, instance = instance),
                },
            u'PMEcosistemas' : {
                u'Formulacion': 
                    forms.PMEecosFormulacionForm(request.POST or None, instance = instance),
                u'InforPlanes': 
                    forms.PMEecosInforPlanesForm(request.POST or None, instance = instance),
                },
            u'Amenazas' : {
                u'Actores': 
                    forms.AmenazActoresForm(request.POST or None, instance = instance),
                },
            u'Riesgos' : {
                u'DocumYCarto': 
                    forms.RiesgoDocumYCartoForm(request.POST or None, instance = instance),
                },
            u'seActoresSoc' : {
                u'Detalle': 
                    forms.seActoDetalleForm(request.POST or None, instance = instance),
                },
            u'seEstrParticip' : {
                u'Detalle': 
                    forms.sePartipDetalleForm(request.POST or None, instance = instance),
                },
            u'seParticComuEtnicas' : {
                u'Detalle': 
                    forms.seComuEtnicDetalleForm(request.POST or None, instance = instance),
                },
            u'seDiagSocioEconom' : {
                u'Detalle': 
                    forms.seDiagSociDetalleForm(request.POST or None, instance = instance),
                },
            u'seCaractCultural' : {
                u'Detalle': 
                    forms.seCaraCultDetalleForm(request.POST or None, instance = instance),
                },
            u'seValorServicEcos' : {
                u'Detalle': 
                    forms.seServEcosDetalleForm(request.POST or None, instance = instance),
                },
            u'seRelaFuncUrbaRegio' : {
                u'Detalle':  
                    forms.seRFUrbRegDetalleForm(request.POST or None, instance = instance),
                },
    }

    return subtree[subcompo][subtema]

@login_required(login_url = ('%slogin/' %(default_names.SUB_SITE)))
def subte(request, shared_id, subcompo, pk, subtema, subte_pk = None):
    '''
    Subtemas de formatos
    '''
    usrattr = GetUserAttr(request, shared_id)
    instance = None
    if subte_pk:
        instance = get_object_or_404(subte_forms(request, subcompo, subtema, instance).Meta.model, id = subte_pk)

    #CobertuMetodologiaForm.Meta.model.objects.all()
    if request.method == 'POST':
        form = subte_forms(request, subcompo, subtema, instance)
        if form.is_valid():
            #im having a id null constraint because I should assign'
            # 'the correct main topic in all the forms'
            #Maybe i'll be easier to change all fk names in models
            subtopic = form.save(commit = False)
            if subcompo == 'Cartografia':
                subtopic.icarsnam = subtema
                subtopic.icarsubt = GetCartoSubtopicFK(pk)
            else:
                #foreignfield = GetEstudFModel(pk, subtopic)
                #subtopic._meta.get_field(foreignfield) = GetEstudFK(pk)
                subtopic = GetEstudFK(subcompo, pk, subtopic)
            if subte_pk:
                subtopic.save(force_update = True)
            else:
                subtopic.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('matriz_infoidentifi.views.resume', args=(shared_id, subcompo,)))
        return render(request, 'forms_subcompo.html', {
            'form': form,
            'title' : GetName(), 
            'shared_id' : shared_id,
            'subcompo' : subcompo,
            'subtema' : subtema,
            'pk': pk,
            'subte_pk': subte_pk,
            'watersheed': GetUserWatersheed(GetUserCorpo(request.user), shared_id),
            #'compo' : GetCompo(),
        })
    else:
        return render(request, 'forms_subcompo.html', {
            'form': subte_forms(request, subcompo, subtema, instance), 
            'title' : GetName(), 
            'shared_id' : shared_id,
            'subcompo' : subcompo,
            'subtema' : subtema,
            'pk': pk,
            'subte_pk': subte_pk,
            'watersheed': GetUserWatersheed(GetUserCorpo(request.user), shared_id),
            #'compo' : GetCompo(),
        })

###----------------------------------------------###
### Reports

### Reports - Load Progress
def LoadTrack():
    '''
    Question: The total ammount of forms uploaded
    '''
    question = FormsFilled()

## Reports - Load Progress - Cartography
def LoadCartoTrack():
    '''
    Question 1: Corporations who have filled Cartografía
    Question 2: The daily load progress by corporations of Cartography 
    '''
#    questions = []
#    questions.append((u'Corporaciones que han cargado los formatos de \
#        Cartografía',
#        CorporationsWhoCartografia())
#    questions.append((u'Avance diario del cargue de formatos por corporación',
#        LoadCartoProgress())
#
    pass
##def ():
##    '''
##    Question: The daily load progress by corporations of Cartography 
##    '''
##    question = LoadCartoProgress()
#
### Reports - Cartografía
def ReportCartog(request):
    '''
    Question 1: ¿Cuántas cuencas tienen cartografía base?
    Question 2: ¿Cuáles son las Cuencas con cartografía base?
    Question 3: ¿Cuáles son oficiales? (Autor: IGAC)
    Question 4: Las oficiales ¿En qué escala están?
    Question 5: ¿Cuáles son las planchas por escala?
    Question 6: La escala en la cuenca ¿Qué área cubre con respecto a la cuenca?
    Question 7: El año de las planchas
    '''
    # Process 
    # 1st. Get all the waterwheeds (Q: 1,2)
    # 2nd. On each ask if it has official gridsgrids  (Q: 3)
    # 3rd. On them get the avaliable scales and values (Q: 4,5)
    # 4rd. Calculate the covered percentage of all distinct grids 
    #   against the watersheed total area(Q: 6)
    # 5th. Q:7 Sure!... Why not? wait maybe... later 
    
    # 1st
    watersheeds = WatersheedCartografiaResume() # WatersheedWhoCartografia()
    # 2nd
    watersheeds_total = len(watersheeds)
    return render(request, 'reports_carto.html', {
        'watersheeds' : watersheeds,
        'watersheeds_total' : watersheeds_total,  
        })

    #questions = []
    #questions.append(u'Cantidad de cuencas con cartografía base',
    #    WatersheedCartografiaFilled())
    #questions.append(u'Cuencas con cartografía base reportada',
    #    WatersheedWhoCartografia())
    #questions.append(u'Cuencas con cartografía oficial',
    #    WatersheedCartoGridsOfficialClassif())

##def ():
##    '''
##    Question: ¿Cuáles son las Cuencas con cartografía base?
##    '''
##
##def ():
##    '''
##    Question: ¿Cuáles son oficiales? (Autor: IGAC)
##    '''
##
##def ():
##    '''
##    Question: Las oficiales ¿En qué escala están?
##    '''
##
##def ():
##    '''
##    Question: ¿Cuáles son las planchas por escala?
##    '''
##
##def ():
##    '''
##    Question: La escala en la cuenca ¿Qué área cubre con respecto a la cuenca?
##    '''
##
