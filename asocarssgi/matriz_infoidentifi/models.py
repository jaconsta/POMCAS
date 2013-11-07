#-*- coding: utf-8 -*-
from django.db import models

from corporacion.models import corporaname
from cuencas.models import cuencompart

import datetime

class inforcompon(models.Model):
    '''
    Componentes del formato
    '''
    infocomp = models.CharField(u'Componente', max_length = 75)
    
    def __unicode__(self):
        return self.infocomp
    
    class Meta:
        verbose_name = u'Componente del formato'
        verbose_name_plural = u'Componentes del formato'

class inforindice(models.Model):
    '''
    Índice de formatos de evaluación de información disponible.
    '''
    infocomp = models.ForeignKey('inforcompon' , verbose_name = u'Componente')
    infosubc = models.CharField(u'Subcomponente', max_length = 75)
    infotema = models.CharField(u'Tema a evaluar', max_length = 125)
    infourlc = models.URLField(u'Dirección capacitación')
    infoprio = models.PositiveSmallIntegerField(u'Prioridad')
    infonota = models.CharField(u'Notas aclaratorias', max_length = 1000)
    
    def __unicode__(self):
        return '%s, %s, %s, %s' % (self.infosubc, self.infotema, self.infourlc,
           self.infonota)
    class Meta:
        verbose_name = u'Formato de evaluación de información disponible.'
        verbose_name_plural = u'Índice de formatos de evaluación de información disponible.'

class incompoeval(models.Model):
    '''
    Formatos de evaluación de información
    Evaluación de la información
    '''
    incompon = models.ForeignKey('inforcompon', verbose_name = u'Componente')
    incoeval = models.CharField(u'Evaluación', max_length = 500)   
    incocome = models.CharField(u'Comentarios', max_length = 500)   
    
    def __unicode__(self):
        return '%s, %s' % (self.incoeval, self.incocome)

    class Meta:
        verbose_name = u'Evaluación de la información'
        verbose_name_plural = u'Evaluación de la información'

#Caracterización general, Identificación del estudio
#Hay
class inididestud(models.Model):
    '''
    Formato de evaluación de información, Caracterización general, 
    Identificación del estudio
    #
    It was considered to do this way because there are five forms which 
    requiere special fields then better to treat them all equal.
    #
    I'm using variables because the names to display are too long
    ''' 
    nombre = u'Nombre del estudio'
    loca= u'Localización física del estudio, Dependencia en la que reposa'
    funciona = u'Funcionario responsable de su custodia y/o manejo'
    geografi = u'Ubicación geográfica del estudio (municipios)'
    area = u'Área de cobertura del estudio sobre la cuenca'
    porcenta = u'Porcentaje de cobertura del estudio sobre la cuenca'
    autor = u'Autor del estudio'
    realizac = u'Año de realización del estudio'
    publicac = u'Año de publicación'
    
    YearChoose = []
    thisyear = datetime.datetime.now().year
    for i in range(1950, thisyear):
        YearChoose.append((i,i))

    #inidacti = models.ForeignKey('inforindice', verbose_name = 'Tema de evaluación')
    iniescor = models.ForeignKey(corporaname, verbose_name = u'Corporación')
    iniescue = models.ForeignKey(cuencompart, verbose_name = u'Cuenca')
    inidnomb = models.CharField(nombre , max_length = 500)
    inidlocf = models.CharField(loca , max_length = 250)
    inidfunc = models.CharField(funciona, max_length = 250)
    inidubig = models.CharField(geografi, max_length = 500)
    inidareh = models.FloatField(area)
    inidporc = models.FloatField(porcenta)
    inidauth = models.CharField(autor, max_length = 125)
    inidanor = models.PositiveSmallIntegerField(realizac, 
        choices = YearChoose, default = thisyear)
    inidanop = models.PositiveSmallIntegerField(publicac, 
        choices = YearChoose, default = thisyear)
    
    def __unicode__(self):
        return '%s, %s, %s, %s, %s' % (self.inidnomb, self.inidlocf, self.inidfunc, self.inidubig, self.inidauth)

    class Meta:
        abstract = True

#Suelos

class inidsuestud(inididestud):
    '''
    Suelos
    Identificación del estudio
    '''
    class Meta:
        verbose_name = u'Estudio de suelos'
        verbose_name_plural = u'Estudios de suelos'

class inidsumegeo(models.Model):
    '''
    Suelos
    Metodología utilizada para el estudio de Geomorfología
    '''
    metodo = u'Metodología utilizada para determinar las unidades \
        geomorfológicas, con qué criterios se definieron las unidades'
    clasif = u'¿La clasificación de las unidades geomorfológicas \
        expresan las características  y ambientes morfogenéticos o morfogénicos?'
    proces = u'¿En el análisis geomorfológico se identifican los \
        procesos morfodinámicos existentes en la cuenca?'
    amenaz = u'¿Se plantean relaciones de geomorfología con amenazas naturales?'
    
    BoolChoose = (
        (True, 'si'),
        (False, 'no'),
    )

    geoindic = models.OneToOneField('inidsuestud', verbose_name=u'Caracterización general')
    geometod = models.CharField(metodo, max_length = 500)
    geoclasi = models.BooleanField(clasif, choices = BoolChoose, default = False)
    geoproce = models.BooleanField(proces, choices = BoolChoose, default = False)
    geoamena = models.BooleanField(amenaz, choices = BoolChoose, default = False)
    
    def __unicode__(self):
        return '%s, %s, %s, %s' % (self.geometod, self.geoclasi, self.geoproce, self.geoamena)

    class Meta:
        verbose_name = 'Metodología utilizada para el estudio de Geomorfología'
        verbose_name_plural = 'Metodologías utilizadas para los estudios de Geomorfología'

class inidsumesue(models.Model):
    '''
    Suelos
    Metodología utilizada para el estudio de suelos y/o capacidad
        de uso de la tierra
    '''
    leyend = u'¿Existe leyenda de suelos compuesta por los siguientes temas \
        clima, geología, pendientes, geomorfología, suelos, capacidad de uso? '
    metodo = u'Metodología utilizada para determinar las unidades cartográficas \
        (unidades de suelos).'
    labres = u'¿Se cuenta los resultados del laboratorio de suelos?'
    georef = u'¿El documento tiene la ubicación georeferenciada de las \
        observaciones de suelos?'

    BoolChoose = (
        (True, 'si'),
        (False, 'no'),
    )

    tierindi = models.OneToOneField('inidsuestud', verbose_name=u'Caracterización general')
    inisutle = models.BooleanField(leyend, choices = BoolChoose, default = False) 
    inisutme = models.CharField(metodo, max_length = 500) 
    inisutla = models.BooleanField(labres, choices = BoolChoose, default = False) 
    inisutge = models.BooleanField(georef, choices = BoolChoose, default = False) 

    class Meta:
        verbose_name = u'Metodología utilizada para el estudio de suelos y/o \
            capacidad de uso de la tierra'
        verbose_name_plural = 'Metodologías utilizadas para el estudio de suelos y/o \
            capacidad de uso de la tierra'

class inidsuinfor(models.Model):
    '''
    Suelos
    Información general cartográfica y documentos técnicos
    '''

    escsal = u'Escala de salida de los mapas'
    esclev = u'Escala de trabajo del levantamiento de suelos y del análisis \
        geomorfológico'
    forma = u'Formato de los Mapas'
    mapext = u'Extensión de los Mapas, en caso que sean en formato Digital'
    metada = u'Existencia de metadatos'
    metaau = u'Metadatos: Autor'
    metafe = u'Metadatos: Año de toma de la información'
    cartdi = u'¿Que información está asociada a la cartografía digital?'
    leygeo = u'¿ Existe en el mapa leyenda geomorfológica que incluya \
        Ambiente morfogénetico o morfogénico, pendiente, forma de la \
        pendiente, procesos mordofinámicos actuales, etc.?'
    tecfor = u'Formato del Documento Técnico'
    tecext = u'Extensión del Documento Técnico, en caso que sean en formato \
        Digital'
    cartba = u'Fuente Cartografía Base del Estudio.'
    carcal = u'Calidad de la Cartografía temática (Topología y Simbología)'
    
    BoolChoose = (
        (True, 'si'),
        (False, 'no'),
    )
    FormatMapChoose = (
        ('ANA', u'análogo'),
        ('DIG', u'digital'),
    )
    FormatFileChoose = (
        ('doc', u'word'),
        ('xls', u'excel'),
        ('pdf', u'pdf'),
        ('otr', u'otro'),
    )
    MapChoose = (
        ('ECW', 'ECW'),
        ('Generate', 'Generate'),
        ('SHP', 'SHP'),
        ('e00', 'e00'),
        ('ArcInfo', 'ArcInfo'),
        ('ECW','ECW'),
        ('DWG', 'DWG'),
        ('DGN', 'DGN'),
        ('DXF', 'DXF'),
        ('PDF', 'PDF'),
        ('TIF', 'TIF'),
        ('JPG', 'JPG'),
        ('Otro', 'Otro'),      
    )
    thisyear = datetime.datetime.now().year
    YearChoose = []
    for i in range(1950, thisyear):
        YearChoose.append((i,i))

    suelindi = models.OneToOneField('inidsuestud', 
        verbose_name = u'Caracterización general')
    inisuess = models.CharField(escsal, max_length = 9, null = True, 
        blank = True)
    inisuesl = models.CharField(esclev, max_length = 9, null = True, 
        blank = True)
    inisufor = models.CharField(forma, max_length = 4, 
        choices = FormatMapChoose, null = True, blank = True)
    inisumex = models.CharField(mapext, max_length = 9, 
        choices = MapChoose, null = True, blank = True)
    inisumet = models.NullBooleanField(metada, choices = BoolChoose, 
        default = False)
    inisumea = models.NullBooleanField(metaau, choices = BoolChoose, 
        null = True, blank = True)
    inisumef = models.PositiveSmallIntegerField(metafe, null = True, 
        blank = True, choices = YearChoose, default = thisyear)
    inisucad = models.CharField(cartdi, max_length = 125, null = True, 
        blank = True)
    inisuley = models.NullBooleanField(leygeo, choices = BoolChoose, 
        default = False, null = True, blank = True)
    inisudoc = models.CharField(tecfor, max_length = 4, 
        choices = FormatMapChoose, null = True, blank = True)
    inisuexd = models.CharField(tecext, max_length = 6, null = True, 
        blank = True)
    inisufuc = models.CharField(cartba, max_length = 75, null = True, 
        blank = True)
    inisucac = models.CharField(carcal, max_length = 125, null = True, 
        blank = True)
     
    def __unicode__(self):
        return '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s' % (self.inisuess,
            self.inisuesl, self.inisufor, self.inisumex, self.inisucad,
            self.inisu)

    class Meta:
        verbose_name = 'Información general cartográfica y documento técnico'
        verbose_name_plural = 'Información general cartográfica y documentos técnicos'
    
#Hidrología

#Hidrogeología

#Calidad de Agua

#Cargas Contaminantes

#Cobertura

#Flora y Fauna

#Plan de manejo en ecosistemas

#Riesgos

#Socioeconómico


