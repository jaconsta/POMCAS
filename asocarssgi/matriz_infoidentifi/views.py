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
from corporacion.views import GetUserCorpo, GetUserCorpo

from matriz_infoidentifi.models import inforcompon, inforindice, inididestud
from matriz_infoidentifi.models import inidcardatg, inidimagsat, inidfotogra
from matriz_infoidentifi import forms
from matriz_infoidentifi.resume import GetResume, GetSubtopicResume, \
    GetCartoSubtopicFK, GetEstudFK

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
        'usr' : request.user, #'corpo': corpora, 'watersheed': watershed, 
        'title' : GetName(), 'compo' : GetCompo(),
        'shared_id' : shared_id,
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
            u'Hidrogeologia' : (u'Metodologia', u'DocumYCarto'),
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
        'forms': forms,
        'subfields': subfields,
        'subtree' : subtree[subcompo],
        'shared_id' : shared_id,
        'subcompo' : subcompo,
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
        form = formlist[subcompo] # getattr(forms, '%sForm(request.POST)' % subcompo.title())
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
            return HttpResponseRedirect(reverse('matriz_infoidentifi.views.resume', args=(shared_id, subcompo,)))#resume(request, shared_id, subcompo)
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
        form = formlist[subcompo] # getattr(forms, '%sForm()' % subcompo.title())
        return render(request, 'forms.html', {
            'form': form,
            'title' : GetName(), 
            'shared_id' : shared_id,
            'subcompo' : subcompo,
            #'compo' : GetCompo(),
        })
    ####
    #return getattr(forms, 'add_%s(request, usrattr)' % subcompo)

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
        form = formlist[subcompo] # getattr(forms, '%sForm(request.POST)' % subcompo.title())
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
            return HttpResponseRedirect(reverse('matriz_infoidentifi.views.resume', args=(shared_id, subcompo,)))#resume(request, shared_id, subcompo)
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
            #'compo' : GetCompo(),
        })

@login_required(login_url = ('%slogin/' %(default_names.SUB_SITE)))
def subte(request, shared_id, subcompo, pk, subtema):
    '''
    Subtemas de formatos
    '''
    usrattr = GetUserAttr(request, shared_id)
    content = None
    if request.method == 'POST':
        content = request.POST
    subtree = {
            u'Cartografia' : {
                u'SubCatastro': (u'Subtema catastro', 
                    forms.CartogSubCatastroForm(content)),
                u'SubTranspor': (u'Subtema transporte', 
                    forms.CartogSubTransporForm(content)),
                u'SubHidrolog': (u'Subtema Hidrología', 
                    forms.CartogSubHidrologForm(content)),
                u'SubeRelive': (u'Subtema Relieve', 
                    forms.CartogSubeReliveForm(content)),
                u'SubEntidade': (u'Subtema Entidades territoriales', 
                    forms.SubEntidadeForm(content)),
                },
            u'Imagenes' : (None,None),
            u'Fotografias' : (None,None),
            u'Suelos' : {
                u'MetodGeomor': (u'Metodología del estudio de geomorfología', 
                    forms.SuelosMetodGeomorForm(content)),
                u'MetodSuelos': (u'Metodología del estudio de suelos y \
                    capacidad de la tierra', 
                    forms.SuelosMetodSuelosForm(content)),
                u'DocumYCarto': (u'Documento técnico y Cartografía', 
                    forms.SuelosDocumYCartoForm(content)),
                },
            u'Hidrologia' : {
                u'Estaciones': (u'Estacones utilizadas durante el estudio',
                    forms.HidroloEstacionesForm(content)),
                u'Metodologia': (u'Metodología del estudio', 
                    forms.HidroloMetodologiaForm(content)),
                u'DocumYCarto': (u'Documento técnico y Cartografía', 
                    forms.HidroloDocumYCartoForm(content)),
                #u'Variabilida': (u'Estudios de variabilidad climática', 
                #    forms.HidroloVariabilidaForm(content)),
                #u'CalcuCaudal': (u'Cálculos de caudal ambiental', 
                #    forms.HidroloCalcuCaudalForm(content)),
                },
            u'Variabilida' : (None,None),
            u'CalcuCaudal' : (None,None),
            u'Hidrogeologia' : {
                u'Metodologia': (u'Metodología del estudio', 
                    forms.HidrogeoMetodologiaForm(content)),
                u'DocumYCarto': (u'Documento técnico y Cartografía', 
                    forms.HidrogeoDocumYCartoForm(content)),
                },
            u'CalidadDeAgua' : {
                u'Metodologia': (u'Metodología del estudio', 
                    forms.CaliAguaMetodologiaForm(content)),
                u'InfoEstudio': (u'Información del estudio', 
                    forms.CaliAguaInfoEstudioForm(content)),
                u'InfoComplem': (u'Información complementaria', 
                    forms.CaliAguaInfoComplemForm(content)),
                },
            u'CargasContaminantes' :{ 
                u'Metodologia': (u'Metodología del estudio', 
                    forms.CargContMetodologiaForm(content)),
                u'InfoEstudio': (u'Información del estudio', 
                    forms.CargContInfoEstudioForm(content)),
                u'InfoComplem': (u'Información complementaria', 
                    forms.CargContInfoComplemForm(content)),
                },
            u'Cobertura' : {
                u'Metodologia': (u'Metodología del estudio', 
                    forms.CobertuMetodologiaForm(content)),
                u'DocumYCarto': (u'Documento técnico y Cartografía', 
                    forms.CobertuDocumYCartoForm(content)),
                u'AnaliMultit': (u'Análisis multitemporal', 
                    forms.CobertuAnaliMultitForm(content)),
                },
            u'FloraYFauna' : {
                u'Metodologia': (u'Metodología del estudio', 
                    forms.FloFauMetodologiaForm(content)),
                u'DocumYCarto': (u'Documento técnico y Cartografía', 
                    forms.FloFauDocumYCartoForm(content)),
                },
            u'PMEcosistemas' : {
                u'Formulacion': (u'Formulación de planes y resultados', 
                    forms.PMEecosFormulacionForm(content)),
                u'InforPlanes': (u'Información de planes', 
                    forms.PMEecosInforPlanesForm(content)),
                },
            u'Amenazas' : {
                u'Actores': (u'Actores con influencia', 
                    forms.AmenazActoresForm(content)),
                },
            u'Riesgos' : {
                u'DocumYCarto': (u'Documento técnico y Cartografía', 
                    forms.RiesgoDocumYCartoForm(content)),
                },
            u'seActoresSoc' : {
                u'Detalle': (u'Detalle de la información', 
                    forms.seActoDetalleForm(content)),
                },
            u'seEstrParticip' : {
                u'Detalle': (u'Detalle de la información',
                    forms.sePartipDetalleForm(content)),
                },
            u'seParticComuEtnicas' : {
                u'Detalle': (u'Detalle de la información', 
                    forms.seComuEtnicDetalleForm(content)),
                },
            u'seDiagSocioEconom' : {
                u'Detalle': (u'Detalle de la información', 
                    forms.seDiagSociDetalleForm(content)),
                },
            u'seCaractCultural' : {
                u'Detalle': (u'Detalle de la información', 
                    forms.seCaraCultDetalleForm(content)),
                },
            u'seValorServicEcos' : {
                u'Detalle': (u'Detalle de la información', 
                    forms.seServEcosDetalleForm(content)),
                },
            u'seRelaFuncUrbaRegio' : {
                u'Detalle': (u'Detalle de la información', 
                    forms.seRFUrbRegDetalleForm(content)),
                },
    }
    if request.method == 'POST':
        form = subtree[subcompo][subtema][1]
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
            subtopic.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('matriz_infoidentifi.views.resume', args=(shared_id, subcompo,)))#resume(request, shared_id, subcompo)
        return render(request, 'forms_subcompo.html', {
            'form': form,
            'title' : GetName(), 
            'subtitle' : subtree[subcompo][subtema][0],
            'shared_id' : shared_id,
            'subcompo' : subcompo,
            'subtema' : subtema,
            'pk': pk,
            #'compo' : GetCompo(),
        })
    else:
        return render(request, 'forms_subcompo.html', {
            'form': subtree[subcompo][subtema][1],
            'title' : GetName(), 
            'subtitle' : subtree[subcompo][subtema][0],
            'shared_id' : shared_id,
            'subcompo' : subcompo,
            'subtema' : subtema,
            'pk': pk,
            #'compo' : GetCompo(),
        })
@login_required(login_url = ('%slogin/' %(default_names.SUB_SITE)))
def subte_edit(request, shared_id, subcompo, pk, subtema, subte_pk):
    '''
    Subtemas de formatos.
        Edición de subtemas diligenciados
    '''
    return HttpResponse(u'{% extends \'main.html\' %} \
        {% block naviside %}\
        <h2>Hello, on build</h2>\
        {% endblock %}')
