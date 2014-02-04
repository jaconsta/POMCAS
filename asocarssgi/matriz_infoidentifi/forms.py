#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# Copyright 2013-2014 ASOCARS
#
'''
'''

from django.forms import ModelForm
from django import forms

from corporacion.views import GetUserCorpo
from matriz_infoidentifi.models import SelectList
from matriz_infoidentifi.models import inforcompon, inforconcep, inforindice #General info
from matriz_infoidentifi.models import inididestud, inidcartog #Source of all proxies
from matriz_infoidentifi.models import inidcardatg, inicartdatf, \
    inicartscat, inicartstra, inicartshdr, inicartsrlv, inicartsete #Cartografía base
from matriz_infoidentifi.models import inidimagsat #Imágenes
from matriz_infoidentifi.models import inidfotogra #Fotogragías
from matriz_infoidentifi.models import inidsuestud, inidsumegeo, inidsumegea, \
    inidsumesue, inidsuinfor #Suelos
from matriz_infoidentifi.models import inidhlestud, inidhlmetod,  ihlmethaest, \
    ihlmethafor, inidhlcarto, inidhlvarib, inidhlcauda #Hidrología
from matriz_infoidentifi.models import inidhgestud, inighgmetfa, inidhgmetho, \
    inidhgmmoma, inidhgcarto #Hidrogeología
from matriz_infoidentifi.models import inidcaestud, inidcameth, inidcamecam, \
    inicainfoes, inicainflab, inicainfgeo, incainfpara, inicainfoco, inicaicca #Calidad de Agua
from matriz_infoidentifi.models import inidccestud, inidccmetho, inidccminfe, \
    iniccinflab, inidccmigeo, iniccicompl, iniccicomps #Cargas Contaminantes
from matriz_infoidentifi.models import inidcoestud, inidcometho, inidcoinfog, \
    inidcoanmul #Cobertura
from matriz_infoidentifi.models import inidffestud, inidffmeth, inidffcart #Flora y Fauna
from matriz_infoidentifi.models import inidpmestud, inidpmecofo, pmecoplanma, \
    inidpmecopm #PM Ecosistemas
from matriz_infoidentifi.models import inriesamepr,amenaidenti, \
    eventocurri, elemenexpue, inriesameac #Riesgos - Amenazas inidriesame, 
from matriz_infoidentifi.models import inidriestud, inidriescar #Riesgos - Estudios
from matriz_infoidentifi.models import inidseasinf, inidseasdet #Socioeconómico - Actores Sociales
from matriz_infoidentifi.models import inidseepinf, inidseepdet, inidseepdin #Socioeconómico - Estrategia de Participación
from matriz_infoidentifi.models import inidseceinf, inidsecedet, inidsecedat #Socioeconómico - Participación de comunidades étnicas 
from matriz_infoidentifi.models import inidsedsinf, inidsdsedet, inidsedsvar, \
    inidsedsser, inidsedsact #Socioeconómico - Diagnósticos Socioeconómicos
from matriz_infoidentifi.models import inidseccinf, inidseccdet, inidseccdcc #Socioeconómico - Caracterización Cultural
from matriz_infoidentifi.models import inidsevsinf, inidsevsdet, inidseserec #Socioeconómico - Valoración de Servicios Ecosistémicos
from matriz_infoidentifi.models import inidserfinf, inidserfdet, inidserfure #Socioeconómico - Relaciones funcionales urbano- regionales

### Cartografía base ###

class CartografiaForm(ModelForm):
    '''
    Cartografía base
    Datos generales
    '''
    class Meta:
        model = inidcardatg
        fields = ['icartess', 'icartnum', 'icartres', 'icartcug', 
            'incacuba', 'incacubp', 'incaforf', 'incafore', 'incaforo',
            'incarsco', 'incarsre', 'incaroco', 'incardat',
            'icartesc', 'incarlic', 'icartfue',
        ]
        widgets = {
            'icartnum': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'icartcug': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'incarlic': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'icartfue': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
        }
    def names(self):
        return u'Cartografía base'
    def subtopic(self):
        return u'Datos generales'

class CartogSubCatastroForm(ModelForm):
    '''
    Cartografía base
    Subtema Cartográfico
    Catastro
    '''
    lists = SelectList()

    icarspre = forms.ChoiceField(label = u'Presencia de elementos que hacen \
        parte del tema Catastro del catálogo de objetos?', 
        choices = lists.BoolChoose(),
        )
    icarsexi = forms.CharField(label = u'Especifique cuales. Ej. \
        ÁREAS CATASTRALES: \
        Manzanas, predios. EDIFICACIONES y OBRAS CIVILES: \
        Construcciones, áreas deportivas, cercas, sitios de interés, \
        canteras, etc', 
        max_length = 500, widget = forms.Textarea(attrs ={'rows':3, 'cols':40}),
        required = False)
    icarsqua = forms.ChoiceField(label = u'En la tabla de atributos. \
        Coherencia de la información con respecto a rasgos \
        característicos de la zona demarcada. Es decir, se verifica que \
        existan elementos del tema Catastro conocidos en el área de \
        cubrimiento de la plancha', 
        choices = lists.BoolChoose(),
        )

    class Meta:
        model = inicartscat
        fields = ['icarspre', 'icarsexi', 'icarsqua', 'icarsrel',
        ]
    def names(self):
        return u'Cartografía base'
    def subtopic(self):
        return u'Subtema cartográfico: Catastro'
class CartogSubTransporForm(ModelForm):
    '''
    Cartografía base
    Subtema Cartográfico
    Transporte
    '''
    lists = SelectList()

    icarspre = forms.ChoiceField(label = u'Presencia de elementos que hacen\
        parte del tema Transporte del catálogo de objetos', 
        choices = lists.BoolChoose(),
        )
    icarsexi = forms.CharField(label = u'Especifique cuales.',
        help_text = u' Ej. TRANSPORTE TERRESTRE: \
            Vía principal, vía secundaria, vía terciaria, camino, carreteable, \
            ferrocarril. \
            INSTALACIONES Y CONSTRUCCIONES: \
            Puente, líneas de alta tensión, poliducto, torres de alta tensión', 
        max_length = 500, widget = forms.Textarea(attrs ={'rows':3, 'cols':40}),
        required = False)
    icarsqua = forms.ChoiceField(label = u'Coherencia de la información con \
        respecto a rasgos característicos de la zona demarcada.', 
        help_text = u'Se verifica que existan elementos del tema Transporte \
        conocidos en el área de cubrimiento de la plancha. En la tabla de \
        atributos.',
        choices = lists.BoolChoose(),
        )

    class Meta:
        model = inicartstra
        fields = ['icarspre', 'icarsexi', 'icarsqua', 'icarsrel',
        ]
    def names(self):
        return u'Cartografía base'
    def subtopic(self):
        return u'Subtema cartográfico: Transporte'
class CartogSubHidrologForm(ModelForm):
    '''
    Cartografía base
    Subtema Cartográfico
    Hidrografía
    '''
    lists = SelectList()

    icarspre = forms.ChoiceField(label = u'Presencia de elementos que hacen\
            parte del tema Hidrografía del catálogo de objetos', 
        choices = lists.BoolChoose(),
        )
    icarsexi = forms.CharField(label = u'Especifique cuales.',
        help_text = u'SUPERFICIES DE AGUA: Drenaje doble, canal, lago, \
            pantano, humedal, drenaje sencillo o quebrada', 
        max_length = 500, widget = forms.Textarea(attrs ={'rows':3, 'cols':40}),
        required = False)
    icarsqua = forms.ChoiceField(label = u'Coherencia de la información con \
            respecto a rasgos característicos de la zona demarcada.', 
        help_text = u'Se verifica que existan elementos del tema Hidrografía \
            conocidos en el área de cubrimiento de la plancha. En la tabla \
            de atributos',
        choices = lists.BoolChoose(),
        )

    class Meta:
        model = inicartshdr
        fields = ['icarspre', 'icarsexi', 'icarsqua', 'icarsrel',
        ]
    def names(self):
        return u'Cartografía base'
    def subtopic(self):
        return u'Subtema cartográfico: Hidrografía'
class CartogSubeReliveForm(ModelForm):
    '''
    Cartografía base
    Subtema Cartográfico
    Relieve
    '''
    lists = SelectList()

    icarspre = forms.ChoiceField(label = u'Presencia de elementos que hacen\
            parte del tema relieve del catálogo de objetos', 
        choices = lists.BoolChoose(),
        )
    icarsexi = forms.CharField(label = u'Especifique cuales.',
        help_text = u'CURVAS DE NIVEL: Índice e intermedia', 
        max_length = 500, widget = forms.Textarea(attrs ={'rows':3, 'cols':40}),
        required = False)
    icarsqua = forms.ChoiceField(label = u'Coherencia de la información con \
            respecto a rasgos característicos de la zona demarcada.', 
        help_text = u'Identificación de las zonas planas, altas, declives, \
            entre otros. En la tabla de atributos.',
        choices = lists.BoolChoose(),
        )

    class Meta:
        model = inicartsrlv
        fields = ['icarspre', 'icarsexi', 'icarsqua', 'icarsrel',
        ]
    def names(self):
        return u'Cartografía base'
    def subtopic(self):
        return u'Subtema cartográfico: Relieve'
class SubEntidadeForm(ModelForm):
    '''
    Cartografía base
    Subtema Cartográfico
    Entidad territorial y unidad administrativa
    '''
    lists = SelectList()

    icarspre = forms.ChoiceField(label = u'Presencia de elementos que hacen\
        parte del tema Entidad Territorial y Unidad Administrativa \
        del catálogo de objetos', 
        choices = lists.BoolChoose(),
        )
    icarsexi = forms.CharField(label = u'Especifique cuales.',
        help_text = u'ENTIDAD TERRITORIAL: República, departamento, \
            municipio, entidad territorial indígena. \
            UNIDAD ADMINISTRATIVA: Región, área rural, área urbana, provincia, \
            comuna o localidad, corregimiento, vereda, barrio, área \
            metropolitana, resguardo indígena, comunidad negra, cabildo \
            indígena, área protegida, área de reserva o área de manejo especial', 
        max_length = 500, widget = forms.Textarea(attrs ={'rows':3, 'cols':40}),
        required = False)
    icarsqua = forms.ChoiceField(label = u'Coherencia de la información con \
        respecto a rasgos característicos de la zona demarcada.', 
        help_text = u'Se verifica que existan elementos del tema \
            Entidad Territorial y Unidad Administrativa \
            conocidos en el área de cubrimiento de la plancha. En la tabla \
            de atributos',
        choices = lists.BoolChoose(),
        )

    class Meta:
        model = inicartsete
        fields = ['icarspre', 'icarsexi', 'icarsqua', 'icarsrel',
        ]
    def names(self):
        return u'Cartografía base'
    def subtopic(self):
        return u'Subtema cartográfico: Entidad territorial y unidad administrativa'

### Imágenes ###

class ImagenesForm(ModelForm):
    '''
    Imágenes
    Imágenes de satélite
    '''
    class Meta:
        model = inidimagsat
        fields = ['iimanomb', 'iimasens', 'iimaseno', 'iimadate',
            'iimacubr', 'incacuba', 'incacubp', 'incaforf',
            'incafore', 'incaforo',
            'incarsco', 'incarsre', 'incaroco', 'incardat',
            'iimabanp', 'iimabanc',
            'iimabanm', 'iimarese',
            'iimacsix', 'iimacsiy',
            'iimacidx', 'iimacidy',
            'iimanubp', 'incarlic',
            'incaraut', 'incarlug', 'incarano',
        ]
    def names(self):
        return u'Imágenes de satélite'
    def subtopic(self):
        return u'Caracterización de las Imágenes de satélite.'

### Fotogragías ###                           

class FotografiasForm(ModelForm):
    '''
    Fotografías
    Fotografías aereas
    '''
    class Meta:
        model = inidfotogra
        fields = [
            'ifonombr', 'incaforf', 'incafore', 'incaforo',
            'ifonumes', 'ifoescaf', 'ifotipoc', 'ifoaltvu',
            'ifopunfo', 'incacuba', 'incacubp', 'ifoanubp',
            'incarsco', 'incarsre', 'incaroco', 'incardat',
            'incarlic',
            'incaraut', 'incarlug', 'incarano'
        ]
    def names(self):
        return u'Fotografías aéreas'
    def subtopic(self):
        return u'Caracterización de las fotografías aéreas.'

### Suelos ###
class SuelosForm(ModelForm):
    '''
    Suelos
    Identificación del estudio de suelos y/o capacidad
    de uso de la tierra
    '''
    class Meta:
        model = inidsuestud
        fields = [
            'inidnomb', 'iniddocf', 'iniddoce', 'iniddoco', 'inidlocf',
            'inidresp', 'inidumun', 'inidcare', 'inidcper',
            'inidauth', 'inidanit', 'inidanor', 'inidanop',
        ]
    def names(self):
        return u'Suelos'
    def subtopic(self):
        return u'Identificación del estudio de suelos y/o capacidad \
            de uso de la tierra'

class SuelosMetodGeomorForm(ModelForm):
    '''
    Suelos
    Metodología utilizada para el estudio de Geomorfología
    '''
    class Meta:
        model = inidsumegeo
        fields = [
            'geometod', 'geoclasi', 'geoclaso',
            'geoproce', 'geoproco', 'geoamena', 'geoament', 'geoameno',
        ]
        widgets = {
            'geometod': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'geoclaso': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'geoproco': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
        }
    def names(self):
        return u'Suelos'
    def subtopic(self):
        return u'Metodología utilizada para el estudio de Geomorfología'
class SuelosMetodSuelosForm(ModelForm):
    '''
    Suelos
    Metodoogía utilizada para el estudio de 
    suelos y/o coberturas de la tierra
    '''
    class Meta:
        model = inidsumesue
        fields = [
            'inisutle', 'inisutlo', 'inisutla', 'inisutln', 'inisutli',
            'inisutge',
        ]
        widgets = {
            'inisutlo': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
        }
    def names(self):
        return u'Suelos'
    def subtopic(self):
        return u'Metodoogía utilizada para el estudio de \
            suelos y/o coberturas de la tierra'
class SuelosDocumYCartoForm(ModelForm):
    '''
    Suelos
    Información general cartográfica y documentos técnicos
    '''
    class Meta:
        model = inidsuinfor
        fields = [
            'carescs', 'caruesle', 'carmafor', 'carmamex', 'carmamot',
            'carmetad', 'carmeaut', 'carmedat', 'carinaso', 
            'carleyen', 'carfuent', 'carqualy',
        ]
    def names(self):
        return u'Suelos'
    def subtopic(self):
        return u'Información general cartográfica y documentos técnicos'

### Hidrología ###
class HidrologiaForm(ModelForm):
    '''
    Hidrología
    Identificación del estudio de hidrología y climatología
    '''
    class Meta:
        model = inidhlestud
        fields = ['inidnomb', 'iniddocf', 'iniddoce', 'iniddoco', 'inidlocf',
            'inidresp', 'inidusub', 'inidusec', 'inidutra', 'inidumun', 
            'inidcare', 'inidcper', 'inidauth', 'inidanit', 
            'inidanor', 'inidanop',
        ]
    def names(self):
        return u'Hidrología'
    def subtopic(self):
        return u'Identificación del estudio de hidrología y climatología'

class HidroloEstacionesForm(ModelForm):
    '''
    Hidrología
    Estaciones utilizadas dentro del estudio
    '''
    class Meta:
        model = ihlmethaest
        fields = [
            'ihlmeesn', 'ihlmeesc', 'ihlmeesi', 'ihlmeesf',
            'ihlmeese',
        ]
    def names(self):
        return u'Hidrología'
    def subtopic(self):
        return u'Estaciones utilizadas dentro del estudio'
class HidroloMetodologiaForm(ModelForm):
    '''
    Hidrología
    Metología utilizada para el estudio de hidrología o climatología
    '''
    class Meta:
        model = inidhlmetod
        fields = [
            'inihlppa', 'inihlphd', 'inihlmin', 'inihlpid',
            'inihlcal' ,'inihlcad',
        ]
        widgets = {
            'inihlppa': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'inihlphd': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'inihlpid': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'inihlcad': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
        }
    def names(self):
        return u'Hidrología'
    def subtopic(self):
        return u'Metología utilizada para el estudio de hidrología o climatología'
class HidroloDocumYCartoForm(ModelForm):
    '''
    Hidrología
    Información general cartográfica y documento técnico
    '''
    class Meta:
        model = inidhlcarto
        fields = [
            'carescs', 'caruesle', 'carmafor', 'carmamex', 'carmamot',
            'carmetad', 'carinaso',
        ]
    def names(self):
        return u'Hidrología'
    def subtopic(self):
        return u'Información general cartográfica y documento técnico'
class HidroloVariabilidaForm(ModelForm):
    '''
    Hidrología
    Estudios de variabilidad climática (niño o niña) para la cuenca en estudio    
    '''
    class Meta:
        model = inidhlvarib
        fields = ['inidnomb', 'iniddocf', 'iniddoce', 'iniddoco', 'inidlocf',
            'inidresp', 'inidusub', 'inidusec', 'inidutra', 'inidumun', 
            'inidcare', 'inidcper', 'inidauth', 'inidanit', 'inidsini', 
            'inidanor', 'inidanop',
        ]
    def names(self):
        return u'Hidrología'
    def subtopic(self):
        return u'Estudios de variabilidad climática (niño o niña) para la cuenca en estudio'
class HidroloCalcuCaudalForm(ModelForm):
    '''
    Hidrología
    Calculos de caudal ambiental
    '''
    class Meta:
        model = inidhlcauda
        fields = ['inidnomb', 'iniddocf', 'iniddoce', 'iniddoco', 'inidlocf',
            'inidresp', 'inidusub', 'inidusec', 'inidutra', 'inidumun', 
            'inidcare', 'inidcper', 'inidauth', 'inidanit', 'inidsini', 
            'inidanor', 'inidanop',
        ]
    def names(self):
        return u'Hidrología'
    def subtopic(self):
        return u'Calculos de caudal ambiental'

### Hidrogeología ###
class HidrogeologiaForm(ModelForm):
    '''
    Hidrogeología
    Identificación del estudio de hidrogeología
    '''
    class Meta:
        model = inidhgestud
        fields = ['inidnomb', 'iniddocf', 'iniddoce', 'iniddoco', 'inidlocf',
            'inidresp', 'inidumun', 'inidcare', 'inidcper', 
            'inidauth', 'inidanit', 'inidanor', 'inidanop',
        ]
    def names(self):
        return u'Hidrogeología'
    def subtopic(self):
        return u'Identificación del estudio de hidrogeología'

class HidrogeoMetodologiaForm(ModelForm):
    '''
    Hidrogeología
    Metodología utilizada para el estudio de hidrogeología
    '''
    class Meta:
        model = inidhgmetho
        fields = [
            'inhgdbpa', 'inhgdbpu', 'inhgdbat', 'inhgdbac', 'inhgdbpa',
            'inhgquye', 'inhgqunc', 'inhgqupa', 'inhgceah', 'inhgahpo',
            'inhglaba', 'inhglabn', 'inhglabi', 'inghesgg', 'inhgeggn', 
            'inghegme', 'inghacui', 'inghaces', 'inghacre', 'inghacrs', 
            'inghchdr', 'inghchme', 'inghchpo', 'inghries', 'inghcaco',
            'inghvuln', 'inghvume', 'inghcupr', 'inghmhco', 'inghmhci',
            'inghtacu','inghagsu','inghasnp', 'inghasco', 
            'inghmoma', 'inghmomo',
        ]
        widgets = {
            'inhgdbat': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'inhgqupa': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'inghegme': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'inghchme': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'inghchpo': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'inghvume': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'inghcupr': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'inghmhci': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
        }
    def names(self):
        return u'Hidrogeología'
    def subtopic(self):
        return u'Metodología utilizada para el estudio de hidrogeología'
class HidrogeoDocumYCartoForm(ModelForm):
    '''
    Hidrogeología
    Información general cartográfica y documento técnico
    '''
    class Meta:
        model = inidhgcarto
        fields = [
            'carescs', 'caruesle', 'carmafor', 'carmamex', 'carmamot',
            'carmetad', 'carinaso',
        ]
    def names(self):
        return u'Hidrogeología'
    def subtopic(self):
        return u'Información general cartográfica y documento técnico'

### Calidad de Agua ###
class CalidadDeAguaForm(ModelForm):
    '''
    Calidad de Agua
    Identificación del estudio de calidad y recurso hídrico
    '''
    class Meta:
        model = inidcaestud
        fields = ['inidnomb', 'iniddocf', 'iniddoce', 'iniddoco',
            'inidlocf', 'inidresp', 'inidudep', 'inidumun', 'inidcare',
            'inidcper', 'inidauth', 'inidanit', 'inidanor', 'inidanop',
        ]
    def names(self):
        return u'Calidad de Agua'
    def subtopic(self):
        return u'Identificación del estudio de calidad y recurso hídrico'

class CaliAguaMetodologiaForm(ModelForm):
    '''
    Calidad de Agua
    Metología del estudio, levantamiento de datos y resultados
    '''
    class Meta:
        model = inidcameth
        fields = [
            'inicaobj', 'inicamet', 'inicaest',
            'inicacan', 'inicacaa', 'inicaiex',
            'inicaitr', 'inicaima', 'inicaime', 'inicaimf',
            'inicaimx', 'inicaixo',
        ]
        widgets = {
            'inicaobj': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'inicamet': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'inicaitr': forms.TextInput(attrs={'size': 40}),
        }
    def names(self):
        return u'Calidad de Agua'
    def subtopic(self):
        return u'Metología del estudio, levantamiento de datos y resultados'
class CaliAguaInfoEstudioForm(ModelForm):
    '''
    Calidad de Agua
    Información que debe contener el estudio
    '''
    class Meta:
        model = inicainfoes
        fields = [
            'iicaiinf', 'iicaiafa', 'iicaiest', 'iicaiobs',
            'iicaipar', 'iicaipao', 
        ]
        widgets = {
            'iicaiinf': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'iicaiobs': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
        }
    def names(self):
        return u'Calidad de Agua'
    def subtopic(self):
        return u'Información que debe contener el estudio'
class CaliAguaInfoComplemForm(ModelForm):
    '''
    Calidad de Agua
    Información Complementaria
    '''
    class Meta:
        model = inicainfoco
        fields = [
            'iicaifoc', 'iicaifca',
        ]
    def names(self):
        return u'Calidad de Agua'
    def subtopic(self):
        return u'Información Complementaria'

### Cargas Contaminantes ###
class CargasContaminantesForm(ModelForm):
    '''
    Cargas Contaminantes
    Estudio de cargas contaminantes de DBO y SST vertidas 
    en la subcuenca, tramos y/o corrientes principales
    en la cuenca objeto de ordenación 
    '''
    class Meta:
        model = inidccestud
        fields = ['inidnomb', 'iniddocf', 'iniddoce', 'iniddoco',
            'inidlocf', 'inidresp', 'inidudep', 'inidumun', 'inidcare',
            'inidcper', 'inidauth', 'inidanit', 'inidanor', 'inidanop',
            'inidacue',
        ]
    def names(self):
        return u'Cargas Contaminantes'
    def subtopic(self):
        return u'Estudio de cargas contaminantes de DBO y SST vertidas \
            en la subcuenca, tramos y/o corrientes principales \
            en la cuenca objeto de ordenación' 

class CargContMetodologiaForm(ModelForm):
    '''
    Cargas Contaminantes
    Metodología del estudio, levantamiento de datos y resultados
    '''
    class Meta:
        model = inidccmetho
        fields = [
            'iiccmobj', 'iiccmmet', 'iiccmest', 'iiccmlin',
            'iiccmdcc', 'iiccmsum', 'iiccminv', 'iiccmsec',
        ]
        widgets = {
            'iiccmobj': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'iiccmmet': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
        }
    def names(self):
        return u'Cargas Contaminantes'
    def subtopic(self):
        return u'Metodología del estudio, levantamiento de datos y resultados'
class CargContInfoEstudioForm(ModelForm):
    '''
    Cargas Contaminantes
    Información que debe contener el estudio
    '''
    class Meta:
        model = inidccminfe
        fields = [
            'iicciinf', 'iiccigeo', 'iicciobs', 'iicciper',
            'iiccipar', 'iiccipao',
        ]
        widgets = {
            'iicciobs': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
        }
    def names(self):
        return u'Cargas Contaminantes'
    def subtopic(self):
        return u'Información que debe contener el estudio'
class CargContInfoComplemForm(ModelForm):
    '''
    Cargas Contaminantes
    Información complementaria
    '''
    class Meta:
        model = iniccicompl 
        fields = [
            'iicccmue', 'iicccper', 'iicccprm',
            'iicccpor', 'iicccpse', 'iicccpur', 'iicccpma',
        ]
        widgets = {
            'iicccpse': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
        }
    def names(self):
        return u'Cargas Contaminantes'
    def subtopic(self):
        return u'Información complementaria'

### Cobertura de la tierra ###
class CoberturaForm(ModelForm):
    '''
    Cobertura de la tierra
    Identificación del estudio / información
    '''
    class Meta:
        model = inidcoestud
        fields = ['inidnomb', 'iniddocf', 'iniddoce', 'iniddoco',
            'inidlocf', 'inidresp', 'inidudep', 'inidumun', 'inidcare',
            'inidcper', 'inidauth', 'inidanit', 'inidanor', 'inidanop',
        ]
    def names(self):
        return u'Cobertura de la tierra'
    def subtopic(self):
        return u'Identificación del estudio / información'

class CobertuMetodologiaForm(ModelForm):
    '''
    Cobertura de la tierra
    Metodología utilizada para levantamiento de coberturas
    '''
    class Meta:
        model = inidcometho
        fields =[
            'iicomsen', 'iicomseo', 'iicomfot', 'iicomfoo',
            'iicomimg', 'iicomimo', 'iicomdat', 'iicomniv', 'iicomint',
            'iicomver', 'iicomcfu', 'iicomces', 'iicomcan',
        ]
    def names(self):
        return u'Cobertura de la tierra'
    def subtopic(self):
        return u'Metodología utilizada para levantamiento de coberturas'
class CobertuDocumYCartoForm(ModelForm):
    '''
    Cobertura de la tierra
    Información general cartográfica y documento técnico
    '''
    class Meta:
        model = inidcoinfog 
        fields = [
            'carescs', 'caruesle', 'carmafor', 'carmamex', 'carmamot',
            'carmetad', 'carinaso',
        ]
    def names(self):
        return u'Cobertura de la tierra'
    def subtopic(self):
        return u'Información general cartográfica y documento técnico'
class CobertuAnaliMultitForm(ModelForm):
    '''
    Cobertura de la tierra
    Análisis multitemporales
    '''
    class Meta:
        model = inidcoanmul
        fields = [
            'mulanali', 'mulperio', 'mulmetod', 'mulescal',
        ]
        widgets = {
            'mulmetod': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
        }
    def names(self):
        return u'Cobertura de la tierra'
    def subtopic(self):
        return u'Análisis multitemporales'

### Flora y Fauna ###
class FloraYFaunaForm(ModelForm):
    '''
    Flora y Fauna
    Identificación del estudio / información
    '''
    class Meta:
        model = inidffestud
        fields = ['inidnomb', 'iniddocf', 'iniddoce', 'iniddoco',
            'inidlocf', 'inidresp', 'inidudep', 'inidumun', 'inidcare',
            'inidcper', 'inidauth', 'inidanit', 'inidanor', 'inidanop',
        ]
    def names(self):
        return u'Flora y Fauna'
    def subtopic(self):
        return u'Identificación del estudio / información'

class FloFauMetodologiaForm(ModelForm):
    '''
    Flora y Fauna
    Metología utilizada para levantamiento de información
    de flora, vegetación y fauna
    '''
    class Meta:
        model = inidffmeth
        fields = [
            'iffmesm', 'iffmein', 'ifftico', 'iffvegi', 'iffesli',
            'iffnupa', 'iffmeif', 'iffclaj', 'iffgeoi',
            'iffinfc', 'iffamen', 'iffamec', 'iffgeor',
        ]
        widgets = {
            'iffmesm': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'iffmein': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'ifftico': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'iffmeif': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'iffclaj': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'iffamec': forms.TextInput(attrs={'size': 40}),
        }
    def names(self):
        return u'Flora y Fauna'
    def subtopic(self):
        return u'Metología utilizada para levantamiento de información \
            de flora, vegetación y fauna'
class FloFauDocumYCartoForm(ModelForm):
    '''
    Flora y Fauna
    Información general del documento técnico y cartografía
    '''
    class Meta:
        model = inidffcart 
        fields = [
            'carmafor', 'carmamex', 'carmamot', 'carmetad', 'carmeaut',
            'carinflo', 'carfuent',
        ]
    def names(self):
        return u'Flora y Fauna'
    def subtopic(self):
        return u'Información general del documento técnico y cartografía'

### PM Ecosistemas ###
class PMEcosistemasForm(ModelForm):
    '''
    Planes de manejo de ecosistemas
    Identificación de los planes de manejo existentes
    '''
    inidcare = forms.FloatField(label = u'Área de cobertura del estudio sobre la cuenca',
        required = False, help_text = u'En hectáreas (ha) o usuarios')

    class Meta:
        model = inidpmestud
        fields = ['inidnomb', 'iniddocf', 'iniddoce', 'iniddoco',
            'inidlocf', 'inidresp', 'inidudep', 'inidumun', 'inidcare',
            'inidcper', 'inidauth', 'inidanit', 'inidanor', 'inidanop',
        ]
    def names(self):
        return u'Planes de manejo de ecosistemas'
    def subtopic(self):
        return u'Identificación de los planes de manejo existentes'

class PMEecosFormulacionForm(ModelForm):
    '''
    Planes de manejo de ecosistemas
    Formulación del plan y resultados
    '''
    class Meta:
        model = inidpmecofo
        fields = [
            'ipmfplan', 'ipmfplao', 'ipmfobje', 'ipmfadop',
            'ipmfvige', 'ipmfplae',
        ]
        widgets = {
            'ipmfplao': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'ipmfobje': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
        }
    def names(self):
        return u'Planes de manejo de ecosistemas'
    def subtopic(self):
        return u'Formulación del plan y resultados'
class PMEecosInforPlanesForm(ModelForm):
    '''
    Planes de manejo de ecosistemas
    Información sobre los planes de manejo
    '''
    class Meta:
        model = inidpmecopm
        fields = [
            'caruesle', 'caruespu', 'carescs', 'carmafor',
            'carmamex', 'carmamot',
        ]
    def names(self):
        return u'Planes de manejo de ecosistemas'
    def subtopic(self):
        return u'Información sobre los planes de manejo'

### Riesgos - Amenazas ###
class AmenazasForm(ModelForm):
    '''
    Identificación de amenazas en la cuenca
    Identificación preeliminar de los sitios con condiciones
    de amenazas y eventos
    '''
    class Meta:
        model = inriesamepr
        fields = ['ameniden', 'amenotra', 'ubidepar',
            'ubimunic', 'ubivered',
            'eventocu', 'eventoot', 'eventrec', 'evencaus',
            'elemento', 'elemotro', 'actosoci', 'activida',
            'amenmapa', 'amengeor',
        ]
    def names(self):
        return u'Identificación de amenazas en la cuenca'
    def subtopic(self):
        return u'Identificación preeliminar de los sitios con condiciones \
            de amenazas y eventos'

class AmenazActoresForm(ModelForm):
    '''
    Identificación de amenazas en la cuenca
    Actores que tienen registros e información
    '''
    class Meta:
        model = inriesameac
        fields = [
            'iactor', 'idyear',
        ]
    def names(self):
        return u'Identificación de amenazas en la cuenca'
    def subtopic(self):
        return u'Actores que tienen registros e información'

### Riesgos - Estudios ###
class RiesgosForm(ModelForm):
    '''
    Estudios de riesgos
    Identificación del estudio o informes técnicos por cada 
    tipo de amenaza o evento identificados
    '''
    class Meta:
        model = inidriestud
        fields = ['inidnomb', 'inidlocf', 'inidudep', 'inidumun', 
            'iniduver', 'inidcare', 'inidcper', 'inidauth', 'inidanit', 
            'inidanor', 'inidanop',
        ]
    def names(self):
        return u'Estudios de riesgos'
    def subtopic(self):
        return u'Identificación del estudio o informes técnicos por cada \
        tipo de amenaza o evento identificados'

class RiesgoDocumYCartoForm(ModelForm):
    '''
    Estudios de riesgos
    Información general cartográfica y documentos técnicos
    relacionados por cada tipo de amenaza en la cuenca
    '''
    class Meta:
        model = inidriescar
        fields = [
            'carescs', 'caruesle', 'carmafor', 'carmamex', 'carmamot',
            'carmetad', 'carmeaut', 'carmenit', 'carmeinf', 'carmedat', 
            'carinaso', 'cardocfo', 'cardocex', 'cardocot',
        ]
    def names(self):
        return u'Estudios de riesgos'
    def subtopic(self):
        return u' Información general cartográfica y documentos técnicos \
        relacionados por cada tipo de amenaza en la cuenca'

### Socioeconómico - Actores Sociales ###
class seActoresSocForm(ModelForm):
    '''
    Socioeconómico
    Actores Sociales 
    Información general
    '''
    lists = SelectList()

    inidnomb = forms.CharField(label = u'Nombre del documento', 
        max_length = 500)
    inidlocf = forms.CharField(label = u'Ubicación del documento',
        max_length = 250, required = False)
    inidanor  = forms.ChoiceField(label = u'Año de elaboración',
        required = False, choices = lists.YearList())

    class Meta:
        model = inidseasinf
        fields = ['inidnomb', 'inidlocf', 'inidauth', 'inidanit',
            'inidanor', 'inidanop', 'inidudep', 'inidumun', 'iniduver',
        ]
    def names(self):
        return u'Socioeconómico. Actores Sociales'
    def subtopic(self):
        return u'Información general'

class seActoDetalleForm(ModelForm):
    '''
    Socioeconómico
    Actores Sociales 
    Detalle de la información
    '''
    class Meta:
        model = inidseasdet 
        fields = [
            'isemetho', 'isemethd', 'isedocum', 'isedocud', 'isedocas',
            'iseactma', 'iseprior', 'isepride', 'isedbact', 'isedbvar',
        ]
        widgets = {
            'isemethd': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'isedocud': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'isedocas': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'isepride': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'isedbvar': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
        }
    def names(self):
        return u'Socioeconómico. Actores Sociales'
    def subtopic(self):
        return u'Detalle de la información'

### Socioeconómico - Estrategia de Participación ###
class seEstrParticipForm(ModelForm):
    '''
    Socioeconómico
    Estrategia de Participación 
    Información general
    '''
    lists = SelectList()

    inidnomb = forms.CharField(label = u'Nombre del documento', 
        max_length = 500)
    inidlocf = forms.CharField(label = u'Ubicación del documento',
        max_length = 250, required = False)
    inidanor  = forms.ChoiceField(label = u'Año de elaboración',
        required = False, choices = lists.YearList())

    class Meta:
        model = inidseepinf
        fields = ['inidnomb', 'inidlocf', 'inidauth', 'inidanit',
            'inidanor', 'inidanop', 'inidudep', 'inidumun', 'iniduver',
        ]
    def names(self):
        return u'Socioeconómico. Estrategia de Participación'
    def subtopic(self):
        return u'Información general'

class sePartipDetalleForm(ModelForm):
    '''
    Socioeconómico
    Estrategia de Participación 
    Detalle de la información
    '''
    class Meta:
        model = inidseepdet 
        fields = [
            'isepestr', 'isepestg', 'isepestd',
            'iseppart', 'isepparm', 'isepinst', 'isepcomu', 'isepcomd',
            'isepiamb', 'isepiamd', 'isepesta',
        ]
        widgets = {
            'isepestg': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'isepestd': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'isepparm': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'isepcomd': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'isepiamd': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'isepesta': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
        }
    def names(self):
        return u'Socioeconómico. Estrategia de Participación'
    def subtopic(self):
        return u'Detalle de la información'

### Socioeconómico - Participación de comunidades étnicas  ###
class seParticComuEtnicasForm(ModelForm):
    '''
    Socioeconómico
    Participación de comunidades étnicas 
    Información general
    '''
    lists = SelectList()

    inidnomb = forms.CharField(label = u'Nombre del documento', 
        max_length = 500)
    inidlocf = forms.CharField(label = u'Ubicación del documento',
        max_length = 250, required = False)
    inidanor  = forms.ChoiceField(label = u'Año de elaboración',
        required = False, choices = lists.YearList())

    class Meta:
        model = inidseceinf
        fields = ['inidnomb', 'inidlocf', 'inidauth', 'inidanit',
            'inidanor', 'inidanop', 'inidudep', 'inidumun', 'iniduver',
        ]
    def names(self):
        return u'Socioeconómico. Participación de comunidades étnicas'
    def subtopic(self):
        return u'Información general'

class seComuEtnicDetalleForm(ModelForm):
    '''
    Socioeconómico
    Participación de comunidades étnicas 
    Detalle de la información
    '''
    class Meta:
        model = inidsecedet 
        fields = [
            'isepccar', 'isepccaw', 'isepccer', 'isepcdev', 'isepcded',
        ]
        widgets = {
            'isepccaw': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'isepcded': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
        }
    def names(self):
        return u'Socioeconómico. Participación de comunidades étnicas'
    def subtopic(self):
        return u'Detalle de la información'

### Socioeconómico - Diagnósticos Socioeconómicos ###
class seDiagSocioEconomForm(ModelForm):
    '''
    Socioeconómico
    Diagnósticos Socioeconómicos 
    Información general
    '''
    lists = SelectList()

    inidnomb = forms.CharField(label = u'Nombre del documento', 
        max_length = 500)
    inidlocf = forms.CharField(label = u'Ubicación del documento',
        max_length = 250, required = False)
    inidanor  = forms.ChoiceField(label = u'Año de elaboración',
        required = False, choices = lists.YearList())

    class Meta:
        model = inidsedsinf
        fields = ['inidnomb', 'inidlocf', 'inidauth', 'inidanit',
            'inidambi', 'inidanor', 'inidanop', 'inidudep', 'inidumun', 
            'iniduver',
        ]
    def names(self):
        return u'Socioeconómico. Diagnósticos Socioeconómicos'
    def subtopic(self):
        return u'Información general'

class seDiagSociDetalleForm(ModelForm):
    '''
    Socioeconómico
    Diagnósticos Socioeconómicos 
    Detalle de la información
    '''
    class Meta:
        model = inidsdsedet 
        fields = [
            'iseddina', 'iseddinv', 'iseddino', 'isedserv', 'isedsere',
            'isedsero', 'isedseal', 'isedseai', 'isedsede', 'isedacti',
            'isedactd', 'isedacto', 'isedsitu', 'isedsitd', 'isedproy', 
            'isedprod', 'isedconf', 'isedcond', 'isedpoli', 'isedpold',
            'isedpred', 'isedprec', 'isedsegu', 'isedsegd',
        ]
        widgets = {
            'iseddino': forms.TextInput(attrs={'size': 40}),
            'isedsero': forms.TextInput(attrs={'size': 40}),
            'isedseai': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'isedsede': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'isedsitd': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'isedprod': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'isedcond': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'isedpold': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'isedprec': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'isedsegd': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
        }
    def names(self):
        return u'Socioeconómico. Diagnósticos Socioeconómicos'
    def subtopic(self):
        return u'Detalle de la información'

### Socioeconómico - Caracterización Cultural ###
class seCaractCulturalForm(ModelForm):
    '''
    Socioeconómico
    Caracterización Cultural
    Información general
    '''
    lists = SelectList()

    inidnomb = forms.CharField(label = u'Nombre del documento', 
        max_length = 500)
    inidlocf = forms.CharField(label = u'Ubicación del documento',
        max_length = 250, required = False)
    inidanor  = forms.ChoiceField(label = u'Año de elaboración',
        required = False, choices = lists.YearList())

    class Meta:
        model = inidseccinf
        fields = ['inidnomb', 'inidlocf', 'inidauth', 'inidanit',
            'inidanor', 'inidanop', 'inidudep', 'inidumun', 'iniduver',
        ]
    def names(self):
        return u'Socioeconómico. Caracterización Cultural'
    def subtopic(self):
        return u'Información general'

class seCaraCultDetalleForm(ModelForm):
    '''
    Socioeconómico
    Caracterización Cultural
    Detalle de la información
    '''
    class Meta:
        model = inidseccdet 
        fields = [
            'isecccul', 'isecccuc', 'isecccuv', 'iseccpat','iseccpad',
            'iseccdoc', 'iseccdcc',
        ]
        widgets = {
            'isecccuc': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'isecccuv': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'iseccpad': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'iseccdcc': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
        }
    def names(self):
        return u'Socioeconómico. Caracterización Cultural'
    def subtopic(self):
        return u'Detalle de la información'

### Socioeconómico - Valoración de Servicios Ecosistémicos ###
class seValorServicEcosForm(ModelForm):
    '''
    Socioeconómico
    Valoración de Servicios Ecosistémicos
    Información general
    '''
    lists = SelectList()

    inidnomb = forms.CharField(label = u'Nombre del documento', 
        max_length = 500)
    inidlocf = forms.CharField(label = u'Ubicación del documento',
        max_length = 250, required = False)
    inidanor  = forms.ChoiceField(label = u'Año de elaboración',
        required = False, choices = lists.YearList())

    class Meta:
        model = inidsevsinf
        fields = ['inidnomb', 'inidlocf', 'inidauth', 'inidanit',
            'inidanor', 'inidanop', 'inidudep', 'inidumun', 'iniduver',
        ]
    def names(self):
        return u'Socioeconómico. Valoración de Servicios Ecosistémicos'
    def subtopic(self):
        return u'Información general'

class seServEcosDetalleForm(ModelForm):
    '''
    Socioeconómico
    Valoración de Servicios Ecosistémicos
    Detalle de la información
    '''
    class Meta:
        model = inidsevsdet 
        fields = [
            'isesemet', 'iseseser', 'iseseseo', 'isesepil', 'isesepia',
        ]
        widgets = {
            'isesemet': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'isesepia': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
        }
    def names(self):
        return u'Socioeconómico. Valoración de Servicios Ecosistémicos'
    def subtopic(self):
        return u'Detalle de la información'

### Socioeconómico - Relaciones funcionales urbano- regionales ###
class seRelaFuncUrbaRegioForm(ModelForm):
    '''
    Socioeconómico
    Relaciones funcionales urbano- regionales
    Información general
    '''
    lists = SelectList()

    inidnomb = forms.CharField(label = u'Nombre del documento', 
        max_length = 500)
    inidlocf = forms.CharField(label = u'Ubicación del documento',
        max_length = 250, required = False)
    inidanor  = forms.ChoiceField(label = u'Año de elaboración',
        required = False, choices = lists.YearList())

    class Meta:
        model = inidserfinf
        fields = ['inidnomb', 'inidlocf', 'inidauth', 'inidanit',
            'inidambi', 'inidanor', 'inidanop', 'inidudep', 'inidumun', 
            'iniduver',
        ]
    def names(self):
        return u'Socioeconómico. Relaciones funcionales urbano- regionales'
    def subtopic(self):
        return u'Información general'

class seRFUrbRegDetalleForm(ModelForm):
    '''
    Socioeconómico
    Relaciones funcionales urbano- regionales
    Detalle de la información
    '''
    class Meta:
        model = inidserfdet 
        fields = [
            'infucomp', 'infucone', 'infoconc', 'infocona', 'infocapa',
            'infocapo', 'infocapl',
        ]
        widgets = {
            'infoconc': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'infocona': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'infocapo': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
            'infocapl': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
        }
    def names(self):
        return u'Socioeconómico. Relaciones funcionales urbano- regionales'
    def subtopic(self):
        return u'Detalle de la información'

##class GetUserAttr(request, shared_id):
##    def __init__(self):
##        self.user = request.User
##        self.corpora = GetUserCorpo(request.user)
##        self.watersheed = GetUserWatersheed(corpora, shared_id)
#
##Calling the forms
#def add_cartografia(request):
#    if request.method == 'POST':
#        form = CartografiaForm(request.POST)
#        if form.is_valid():
#            return 
#    else:
#        form = CartografiaForm()
#        return render(request, 'form.html', {
#            'form': form,
#        })
