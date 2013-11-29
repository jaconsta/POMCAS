#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from corporacion.models import corporaname
from cuencas.models import cuencompart

import datetime

#Each header form should have:
# Which corporation it belongs to
# Which watershed it belongs to
# Who filled the form (user)
# Who updated the form (user)
# First filling date
# Last Update
#
#SubForms should include
# Who updated the form (user)
# First filling date
# Last Update

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
    inieswho = models.ForeignKey(User, 
        verbose_name = u'Usuario que llena el formulario',
        related_name = '%(app_label)s_%(class)s_user_create')
    inieswhu = models.ForeignKey(User, 
        verbose_name = u'Último usuario actualiza el formulario',
        related_name = '%(app_label)s_%(class)s_user_edit')
    iniesdac = models.DateTimeField(u'Fecha de creación', auto_now_add = True)
    iniesdau = models.DateTimeField(u'Fecha de última actualización', 
        auto_now = True)
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
        return '%s, %s, %s, %s, %s' % (self.inidnomb, self.inidlocf, 
            self.inidfunc, self.inidubig, self.inidauth)

    class Meta:
        abstract = True

class inicartsubt(models.Model):
    '''
    Cartografía base
    Subtema cartográfico
    ####
    For filling purposes a table will be used for each component
    Later, a single table with an aditional field can represent all of them
    '''
    presen = u'Presencia de elementos que hacen parte del tema en el \
        catálogo de objetos'
    cuapre = u'Especifique cuáles'
    qualit = u'Calidad de datos'
    reltop = u'Relaciones topológicas'

    BoolChoose = (
        (True, 'si'),
        (False, 'no'),
    )

    icarsubt = models.OneToOneField('inidcardatg')
    icarspre = models.BooleanField(presen, choices = BoolChoose)
    icarsexi = models.CharField(cuapre, max_length = 500)
    icarsqua = models.BooleanField(qualit, choices = BoolChoose)
    icarsrel = models.BooleanField(reltop, choices = BoolChoose)

    class Meta:
        verbose_name = u'1.2 Subtema cartográfico'
        verbose_name_plural = u'1.2 Subtemas cartográficos'
        abstract = True

class inidgeorefe(models.Model):
    '''
    Tabla de georeferenciación
    '''
    origen = u'Orígen de coordenadas'
    coordx = u'X'
    coordy = u'Y'

    inigeoor = models.CharField(origen, max_length = 25)
    inigeocx = models.FloatField(coordx)
    inigeocy = models.FloatField(coordy)

    class Meta:
        abstract = True

class socioinfoge(models.Model):
    '''
    Socioeconómico y cultural
    Información General
    '''
    nombre = u'Nombre del documento'
    ubicac = u'Ubicación del documento'
    autore = u'Autor del estudio'
    elaano = u'Año de elaboración '
    docume = u'¿Documento elaborado para la cuenca o para el territorio \
        especifico de la jurisdicción de la CAR?'

    BoolChoose = (
        (True, 'si'),
        (False, 'no'),
    )

    iniescor = models.ForeignKey(corporaname, verbose_name = u'Corporación')
    iniescue = models.ForeignKey(cuencompart, verbose_name = u'Cuenca')
    inieswho = models.ForeignKey(User, 
        verbose_name = u'Usuario que llena el formulario',
        related_name = '%(app_label)s_%(class)s_user_create')
    inieswhu = models.ForeignKey(User, 
        verbose_name = u'Último usuario actualiza el formulario',
        related_name = '%(app_label)s_%(class)s_user_edit')
    isocinfo = models.CharField(nombre, max_length = 200)
    isocubic = models.CharField(ubicac, max_length = 200)
    isocauto = models.CharField(autore, max_length = 200)
    isocanoe = models.PositiveSmallIntegerField(elaano,
        null = True, blank = True)
    isocdocu = models.BooleanField(docume, choices = BoolChoose, default = True)

    class Meta:
        abstract = True
        verbose_name = u'Información General'
        verbose_name_plural = verbose_name

#Cartografía base

class inidcardatg(models.Model):
    '''
    Cartografía base.
    Datos generales
    '''
    escala = u'Escala de salida'
    numero = u'Identificación'
    respon = u'Responsable'
    cubrim = u'Cubrimiento geográfico de la cartografía'
    cubria = u'Área de cubrimiento con relación a la cuenca'
    cubrip = u'Porcentaje de cubrimiento con relación a la cuenca'
    formato = u'Formato de los archivos'
    forext = u'Extensión de los archivos'
    siscoo = u'Referencia espacial. Sistema de coordenadas'
    sisref = u'Referencia espacial. Sistema de referencia'
    sisori = u'Referencia espacial. Origen de coordenadas'
    sisdat = u'Referencia espacial. Dátum'
    esccap = u'Escala de captura'
    licenc = u'Licencia de uso'
    
    ScaleChoose = (
        (500000, u'1:500000'),
        (100000, u'1:100000'),
        (50000, u'1:50000'),
        (25000, u'1:25000'),
        (10000, u'1:10000'),
        (5000, u'1:5000'),
        (2000, u'1:2000'),
        (1000, u'1:1000'),
        (500, u'1:500'),
    )
    FormatMapChoose = (
        ('ANA', u'análogo'),
        ('DIG', u'digital'),
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
    SisCoordChoose = (
        ('PLA', u'Planas'),
        ('GEO', u'Geográficas'),
    )
    OriCoordChoose = (
        ('OO', u'Occidente Occidente'),
        ('O', u'Occidente'),
        ('C', u'Centro'),
        ('E', u'Oriente'),
        ('EE', u'Oriente Oriente'),
    )

    iniescor = models.ForeignKey(corporaname, verbose_name = u'Corporación')
    iniescue = models.ForeignKey(cuencompart, verbose_name = u'Cuenca')
    inieswho = models.ForeignKey(User, 
        verbose_name = u'Usuario que llena el formulario',
        related_name = '%(app_label)s_%(class)s_user_create')
    inieswhu = models.ForeignKey(User, 
        verbose_name = u'Último usuario actualiza el formulario',
        related_name = '%(app_label)s_%(class)s_user_edit')
    icartess = models.PositiveIntegerField(escala, choices = ScaleChoose,
        default = 25000)
    icartnum = models.CharField(numero, max_length = 8)
    icartres = models.CharField(respon, max_length = 125)
    icartcug = models.CharField(cubrim, max_length = 500)
    icartcua = models.FloatField(cubria)
    icartcup = models.FloatField(cubrip)
    icartfor = models.CharField(formato, max_length = 4, 
        choices = FormatMapChoose)
    icartfex = models.CharField(forext, max_length = 5,
        choices = MapChoose)
    icartrco = models.CharField(siscoo, max_length = 4,
        choices = SisCoordChoose)
    icartrre = models.CharField(sisref, max_length = 25)
    icartror = models.CharField(sisori, max_length = 3,
        choices = OriCoordChoose)
    icartrda = models.CharField(sisdat, max_length = 25)
    icartesc = models.PositiveIntegerField(esccap, choices = ScaleChoose,
        default = 25000, null = True, blank = True)
    icartlic = models.CharField(licenc, max_length = 25,
        null = True, blank = True)

    class Meta:
        verbose_name = u'01 Cartografía base'
        verbose_name_plural = verbose_name
   
class inicartdatf(models.Model):
    '''
    Cartografía base
    Datos generales - Fuentes y fecha'
    '''
    icarfuen = models.ForeignKey('inidcardatg')
    icarfnom = models.CharField(u'Nombre', max_length = 125) 
    icarfdes = models.CharField(u'Descripción', max_length = 500, null = True, 
        blank = True) 
    icarflin = models.CharField(u'Listado de información', max_length = 500,
        null = True, blank = True)
    icarfsen = models.CharField(u'Sensor', max_length = 125, null = True, 
        blank = True) 
    icarfano = models.PositiveSmallIntegerField(u'Año', null = True, 
        blank = True) 

    class Meta:
        verbose_name = '01.1 Fuente y Fecha'
        verbose_name_plural = '1.1 Fuentes y Fechas'

class inicartscat(inicartsubt):
    class Meta:
        verbose_name = u'01.2.1 Subtema. Catastro'
        verbose_name_plural = verbose_name

class inicartstra(inicartsubt):
    class Meta:
        verbose_name = u'01.2.2 Subtema. Transporte'
        verbose_name_plural = verbose_name

class inicartshdr(inicartsubt):
    class Meta:
        verbose_name = u'01.2.3 Subtema. Hidrografía'
        verbose_name_plural = verbose_name

class inicartsrlv(inicartsubt):
    class Meta:
        verbose_name = u'01.2.4 Subtema. Relieve'
        verbose_name_plural = verbose_name

class inicartsete(inicartsubt):
    class Meta:
        verbose_name = u'01.2.5 Subtema. Entidad Territorial'
        verbose_name_plural = verbose_name

#Imágenes

class inidimagsat(models.Model):
    '''
    Imágenes
    Imágenes de satélite
    '''
    nombre = u'Nombre de la imagen'
    sensor = u'Sensor / Satélite'
    seotro = u'Otro'
    fechai = u'Fecha y hora de la imagen'
    cubrim = u'Cubrimiento geográfico de la imagen'
    cubrid = u'Entidades territoriales y administrativas presentes \
        en el área de cubrimiento'
    cubria = u'Área de cubrimiento con relación a la cuenca'
    cubrip = u'Porcentaje de cobertura con relación a la cuenca'
    formai = u'Formato de la imágen'
    formae = u'Extensión de la imágen'
    reessc = u'Referencia espacial. Sistema de coordenadas'
    reessr = u'Referencia espacial. Sistema de referencia'
    reesoc = u'Referencia espacial. Orígen de coordenadas'
    reesda = u'Referencia espacial. Dátum'
    banpae = u'Banda pancromática'
    banpac = u'Especique cuales'
    banmul = u'Bandas multiespectrales'
    resolu = u'Resolución espacial'
    cosuix = u'Coordenadas esquina superior izquierda. X'
    cosuiy = u'Coordenadas esquina superior izquierda. Y'
    coindx = u'Coordenadas esquina inferior derecha. X'
    coindy = u'Coordenadas esquina inferior derecha. Y'
    pornub = u'Porcentaje de nubosidad'
    licenc = u'Licencia de uso'
    author = u'Autor'
    lugpub = u'Lugar de publicación'
    annopu = u'Año'
    tamano = u'Tamaño del archivo'

    BoolChoose = (
        (True, 'si'),
        (False, 'no'),
    )
    FormatMapChoose = (
        ('ANA', u'análogo'),
        ('DIG', u'digital'),
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
    SensChoose = (
        ('LandSat', u'LandSat'),
        ('SPOT', u'SPOT'),
        ('RapidEye', u'RapidEye'),
        ('IKONOS', u'IKONOS'),
        ('Otro', u'Otro'),
    )
    SisCoordChoose = (
        ('PLA', u'Planas'),
        ('GEO', u'Geográficas'),
    )
    OriCoordChoose = (
        ('OO', u'Occidente Occidente'),
        ('O', u'Occidente'),
        ('C', u'Centro'),
        ('E', u'Oriente'),
        ('EE', u'Oriente Oriente'),
    )

    iniescor = models.ForeignKey(corporaname, verbose_name = u'Corporación')
    iniescue = models.ForeignKey(cuencompart, verbose_name = u'Cuenca')
    inieswho = models.ForeignKey(User, 
        verbose_name = u'Usuario que llena el formulario',
        related_name = '%(app_label)s_%(class)s_user_create')
    inieswhu = models.ForeignKey(User, 
        verbose_name = u'Último usuario actualiza el formulario',
        related_name = '%(app_label)s_%(class)s_user_edit')
    iimanomb = models.CharField(nombre, max_length = 125)
    iimasens = models.CharField(sensor, max_length = 10, choices = SensChoose)
    iimaseno = models.CharField(seotro, max_length = 25, null = True,
        blank = True)
    iimadate = models.DateTimeField(fechai)
    iimacubr = models.FloatField(cubrim, null = True, blank = True)
    iimacubd = models.CharField(cubrid, max_length = 300, null = True,
        blank = True)
    iimacuba = models.FloatField(cubria)
    iimacubp = models.FloatField(cubrip)
    iimaform = models.CharField(formai, max_length = 4, choices = FormatMapChoose)
    iimafore = models.CharField(formae, max_length = 5, 
        choices = MapChoose)
    iimaresc = models.CharField(reessc, max_length = 4, choices = SisCoordChoose)
    iimaresr = models.CharField(reessr, max_length = 25)
    iimareoc = models.CharField(reesoc, max_length = 3, choices = OriCoordChoose)
    iimareda = models.CharField(reesda, max_length = 25)
    iimabanp = models.BooleanField(banpae, choices = BoolChoose, 
        default = False)
    iimabanc = models.CharField(banpac, max_length = 500, null = True, 
        blank = True)
    iimabanm = models.CharField(banmul, max_length = 300)
    iimarese = models.CharField(resolu, max_length = 50)
    iimacsix = models.FloatField(cosuix, null = True, blank = True)
    iimacsiy = models.FloatField(cosuiy, null = True, blank = True)
    iimacidx = models.FloatField(coindx, null = True, blank = True)
    iimacidy = models.FloatField(coindy, null = True, blank = True)
    iimanubp = models.FloatField(pornub)
    iimalice = models.CharField(licenc, max_length = 250, null = True,
        blank = True)
    iimafaut = models.CharField(author, max_length = 125)
    iimaflug = models.CharField(lugpub, max_length = 125)
    iimafano = models.PositiveSmallIntegerField(annopu)
    iimaftam = models.FloatField(tamano)

    class Meta:
        verbose_name = u'02 Imagen'
        verbose_name = u'02 Imágenes'

#Fotografías
class inidfotogra(models.Model):
    '''
    Fotografías
    Fotografías. Áreas
    '''
    nombre = u'Nombre de la fotografía'
    formaf = u'Formato de la fotografía'
    fotoex = u'Extensión de la fotografía'
    inivue = u'Fecha y hora de inicio del vuelo'
    finvue = u'Fecha y hora de finalización del vuelo'
    numsob = u'Número de sobre'
    escala = u'Escala de las fotografías aéreas'
    tipoca = u'Tipo de cámara'
    altvue = u'Altura del vuelo'
    numfot = u'Número de fotos por banda o pasada'
    punfot = u'Puntos de fotocontrol'
    pornub = u'Porcentaje de nubosidad'
    cubria = u'Área de cubrimiento con relación a la cuenca'
    cubrip = u'Porcentaje de cobertura con relación a la cuenca'
    reessc = u'Referencia espacial. Sistema de coordenadas'
    reessr = u'Referencia espacial. Sistema de referencia'
    reesoc = u'Referencia espacial. Orígen de coordenadas'
    reesda = u'Referencia espacial. Dátum'
    licenc = u'Licencia de uso'
    author = u'Autor'
    lugpub = u'Lugar de publicación'
    annopu = u'Año'
    tamano = u'Tamaño del archivo'

    BoolChoose = (
        (True, 'si'),
        (False, 'no'),
    )
    FormatMapChoose = (
        ('ANA', u'análogo'),
        ('DIG', u'digital'),
    )
    FotoFormChoose = (
        ('TIFF', u'TIFF'),
        ('ECW', u'ECW'),
        ('IMG', u'IMG'),
        ('Ana', u'Papel'),
        ('Otro', u'Otro'),
    )
    ScaleChoose = (
        (500000, u'1:500000'),
        (100000, u'1:100000'),
        (50000, u'1:50000'),
        (25000, u'1:25000'),
        (10000, u'1:10000'),
        (5000, u'1:5000'),
        (2000, u'1:2000'),
        (1000, u'1:1000'),
        (500, u'1:500'),
    )
    SisCoordChoose = (
        ('PLA', u'Planas'),
        ('GEO', u'Geográficas'),
    )
    OriCoordChoose = (
        ('OO', u'Occidente Occidente'),
        ('O', u'Occidente'),
        ('C', u'Centro'),
        ('E', u'Oriente'),
        ('EE', u'Oriente Oriente'),
    )

    iniescor = models.ForeignKey(corporaname, verbose_name = u'Corporación')
    iniescue = models.ForeignKey(cuencompart, verbose_name = u'Cuenca')
    inieswho = models.ForeignKey(User, 
        verbose_name = u'Usuario que llena el formulario',
        related_name = '%(app_label)s_%(class)s_user_create')
    inieswhu = models.ForeignKey(User, 
        verbose_name = u'Último usuario actualiza el formulario',
        related_name = '%(app_label)s_%(class)s_user_edit')
    ifonombr = models.CharField(nombre, max_length = 125)
    ifoformf = models.CharField(formaf, max_length = 4, 
        choices = FormatMapChoose)
    ifoforme = models.CharField(fotoex, max_length = 5, 
        choices = FotoFormChoose)
    ifoinivu = models.DateTimeField(inivue, null = True, blank = True)
    ifofinvu = models.DateTimeField(finvue, null = True, blank = True)
    ifonumes = models.CharField(numsob, max_length = 50)
    ifoescaf = models.PositiveIntegerField(escala, choices = ScaleChoose,
        default = 25000)
    ifotipoc = models.CharField(tipoca, max_length = 25, null = True,
        blank = True)
    ifoaltvu = models.FloatField(altvue, null = True, blank = True)
    ifonumfo = models.PositiveIntegerField(numfot)
    ifopunfo = models.BooleanField(punfot, choices = BoolChoose, 
        default = False)
    ifoanubp = models.FloatField(pornub)
    ifoacuba = models.FloatField(cubria)
    ifoacubp = models.FloatField(cubrip)
    ifoaresc = models.CharField(reessc, max_length = 4, choices = SisCoordChoose)
    ifoaresr = models.CharField(reessr, max_length = 25)
    ifoareoc = models.CharField(reesoc, max_length = 3, choices = OriCoordChoose)
    ifoareda = models.CharField(reesda, max_length = 25)
    ifoalice = models.CharField(licenc, max_length = 250, null = True,
        blank = True)
    ifoafaut = models.CharField(author, max_length = 125)
    ifoaflug = models.CharField(lugpub, max_length = 125)
    ifoafano = models.PositiveSmallIntegerField(annopu)
    ifoaftam = models.FloatField(tamano)

    class Meta:
        verbose_name = u'03 Fotografía'
        verbose_name_plural = u'03 Fotografías'

#Suelos

class inidsuestud(inididestud):
    '''
    Suelos
    Identificación del estudio
    '''
    class Meta:
        verbose_name = u'04 Estudio de suelos'
        verbose_name_plural = u'04 Estudios de suelos'

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
    amenaz = u'¿Relaciones de geomorfología con amenazas naturales?'
    
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
        return self.geometod
        #return '%s, %s, %s, %s' % (self.geometod, self.geoclasi, self.geoproce, self.geoamena)

    class Meta:
        verbose_name = u'04.1 Metodología Geomorfología'
        verbose_name_plural = verbose_name #u'Metodologías utilizadas para los estudios de Geomorfología'

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
        verbose_name = u'04.2 Metodología uso de tierra'
        verbose_name_plural = verbose_name
    #    verbose_name = u'Metodología utilizada para el estudio de suelos y/o \
    #        capacidad de uso de la tierra'
    #    verbose_name_plural = u'Metodologías utilizadas para el estudio de suelos y/o \
    #        capacidad de uso de la tierra'

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
        return u'%s, %s, %s, %s, %s, %s, %s, %s, %s, %s' % (self.inisuess,
            self.inisuesl, self.inisufor, self.inisumex, self.inisucad,
            self.inisu)

    class Meta:
        verbose_name = u'04.3 Información cartográfica'
        verbose_name_plural = verbose_name #u'Información general cartográfica y documentos técnicos'
    
#Hidrología

class inidhlestud(inididestud):
    '''
    Hidrología
    Identificación del estudio
    '''
    class Meta:
        verbose_name = u'05 Estudio hidrológico'
        verbose_name_plural = u'05 Estudios hidrológicos'

class inidhlmetod(models.Model):
    '''
    Hidrología
    Metodología utilizada para el estudio de Hidrología o Climatología
    '''
    estaci = u'Estaciones utilizadas dentro del estudio'
    perioi = u'Año inicio de las series'
    periof = u'Año fin de las series'
    tempor = u'Escala temporal'
    method = u'Metodologías utilizadas en el estudio'
    infoin = u'Cuenta con la información de entrada para los cálculos'
    indesc = u'Describa las entradas'
    calibr = u'¿En las modelaciones existentes, se realizaron las \
        calibraciones y validaciones necesarias?'
    #caafor = u'Número de aforo'
    
    EscTempChoose = (
        ('D', 'Diario'),
        ('M', 'Mensual'),
        ('A', 'Anual'),
    )
    BoolChoose = (
        (True, 'si'),
        (False, 'no'),
    )
    FormatFileChoose = (
        ('doc', u'word'),
        ('xls', u'excel'),
        ('pdf', u'pdf'),
        ('otr', u'otro'),
    )
    thisyear = datetime.datetime.now().year
    YearChoose = []
    for i in range(1950, thisyear):
        YearChoose.append((i,i))
 
    inihidme = models.OneToOneField('inidhlestud')
    inihlmes = models.CharField(estaci, max_length = 250) 
    inihlmpi = models.IntegerField(perioi, choices = YearChoose)
    iniglmpf = models.IntegerField(periof, choices = YearChoose)
    inihlmte = models.CharField(tempor, max_length = 2, choices = EscTempChoose)
    inihlmet = models.CharField(method, max_length = 500)
    inihlmin = models.BooleanField(infoin, choices = BoolChoose, 
        default = False)
    inihlmid = models.CharField(indesc, max_length = 300, null = True, 
        blank = True)
    inihlmmo = models.BooleanField(calibr, choices = BoolChoose, 
        default = False)
    #inihlmma = models.IntegerField(caafor, null = True, blank = True)
    
    class Meta:
        verbose_name = u'05.1 Metodología. hidrología/climatología'
        verbose_name_plural = verbose_name #u'Metodologías utilizadas para los estudio de hidrología o climatología'

class ihlmethafor(models.Model):
    '''
    Hidrología
    Metodología - Aforos
    Aforo: Medición del caudal
    '''
    caperi = u'Fecha de aforo'
    caudal = u'Valor del caudal'
    nivel = u'Valor del nivel de agua'
    caubic = u'Ubicación'

    thisyear = datetime.datetime.now().year
    YearChoose = []
    for i in range(1950, thisyear):
        YearChoose.append((i,i))
 
    inihlmma = models.ForeignKey('inidhlmetod')
    inihlmmp = models.IntegerField(caperi, null = True, blank = True)
    inihlmca = models.IntegerField(caudal, null = True, blank = True)
    inihlmni = models.IntegerField(nivel, null = True, blank = True)
    inihlmmu = models.CharField(caubic, max_length = 250)

    class Meta:
        verbose_name = u'05.1.1 Información de aforos'
        verbose_name_plural = verbose_name

class inidhlcarto(models.Model):
    '''
    Hidrología
    información general  cartográfica y documento técnico
    '''
    escalm = u'Escala de salida de los mapas'
    escale = u'Escala de realización del estudio'
    formma = u'Formato de los mapas'
    extmap = u'Extensión de los Mapas'
    metada = u'Existencia de metadatos'
    carinf = u'Que información está asociada a la cartografía digital'
    formdo = u'Formato del documento técnico'
    extedo = u'Extensión del Documento Técnico'
    
    BoolChoose = (
        (True, 'si'),
        (False, 'no'),
    )
    FormatMapChoose = (
        ('ANA', u'análogo'),
        ('DIG', u'digital'),
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
    FormatFileChoose = (
        ('doc', u'word'),
        ('xls', u'excel'),
        ('pdf', u'pdf'),
        ('otr', u'otro'),
    )
    InfoCartChoose = (
        ('TBL', 'Tabla asociada'),
        ('DBF', '.dbf'),
    )

    inihidca = models.OneToOneField('inidhlestud')
    inihlceo = models.IntegerField(escalm)
    inihlcer = models.IntegerField(escale)
    inihlcfo = models.CharField(formma, max_length = 4, 
        choices = FormatMapChoose)
    inihlcem = models.CharField(extmap, max_length = 9,
        choices = MapChoose, null = True, blank = True) 
    inihlcme = models.BooleanField(metada, choices = BoolChoose, 
        default = False)
    inihlccd = models.CharField(carinf, max_length = 4,
        choices = InfoCartChoose, null = True, blank = True)
    inihlcfd = models.CharField(formdo, max_length = 4,
        choices = FormatMapChoose) 
    inihlced = models.CharField(extedo, max_length = 4,
        choices = FormatFileChoose, null = True, blank = True)

    class Meta:
        verbose_name = u'05.2 Información general cartográfica'
        verbose_name_plural = verbose_name

class inidhlinfor(models.Model):
    '''
    Hidrología
    Información Complementaria
    '''
    estud = u'Relacione y describa los estudios de variabilidad climática (niño o niña)'
    calcu = u'¿Existen cálculos de caudal ambiental?'
    anno = u'Año'

    BoolChoose = (
        (True, 'si'),
        (False, 'no'),
    )
    thisyear = datetime.datetime.now().year
    YearChoose = []
    for i in range(1950, thisyear+1):
        YearChoose.append((i,i))

    inihidfo = models.OneToOneField('inidhlestud')
    inihliev = models.CharField(estud, max_length = 500)
    inihlica = models.BooleanField(calcu, choices = BoolChoose, default = False)
    inihlian = models.IntegerField(anno, choices = YearChoose, null = True, blank = True)

    class Meta: 
        verbose_name = u'05.3 Información Complementaria'
        verbose_name_plural = verbose_name

#Hidrogeología

class inidhgestud(inididestud):
    '''
    Hidrogeología
    Identificación del estudio
    '''
    class Meta:
        verbose_name = u'06 Estudio hidrogeológico'
        verbose_name_plural = u'06 Estudios hidrogeológicos'

class inidhgmetho(models.Model):
    '''
    Hidrogeología
    Metodología utilizada para el estudio
    '''
    ipafase = u'Inventario de puntos de agua'
    ipameth = u'Inventario de puntos de agua. Metodología'
    mggfase = u'Modelo geológico - geofísico'
    mggmeth = u'Modelo geológico - geofísico. Metodología'
    hqufase = u'Hidroquímica'
    hqumeth = u'Hidroquímica. Metodología'
    hdrfase = u'Hidráulica'
    hdrmeth = u'Hidráulica. Metodología'
    vulfase = u'Vulnerabilidad'
    vulmeth = u'Vulnerabilidad. Metodología'
    inventar = u'¿Existe base de datos de inventario de puntos de agua?'
    aquifer = u'Están identificados los acuíferos asociados a estos puntos de agua?'
    quality = u'¿Existen análisis de calidad?'
    parame = u'Parámetros evaluados en el análisis de calidad'
    balan = u'Se realizó balance de error de los análisis de calidad?'
    analis = u'El laboratorio que realizó los análisis está acreditado en \
        los parámetros analizados?'
    study = u'¿Se realizaron estudios geofísicos y geolectricos?'
    stumeth = u'Metodología utilizada'
    dimens = u'¿Tiene determinado las dimensiones del acuífero?'
    carach = u'Existen caracterizaciones hidráulicas de los acuíferos?'
    caracm = u'Metodología utilizada'
    vulnea = u'¿El estudio evaluó la vulnerabilidad de los acuíferos?'
    vulnem = u'Metodología utilizada'
    modehi = u'¿Existe un modelo hidrogeológico conceptual?'
    modedb = u'Base de datos relacionada?'
    modeca = u'Cartografía relacionada, escala.'
    modema = u'Existe un modelo matemático'

    BoolChoose = (
        (True, 'si'),
        (False, 'no'),
    )

    inihidge = models.OneToOneField('inidhgestud')
    inihgmif = models.BooleanField(ipafase,choices = BoolChoose, default = False)
    inihgmim = models.CharField(ipameth, max_length = 500, 
        null = True, blank = True)
    inihgmmf = models.BooleanField(mggfase,choices = BoolChoose, default = False)
    inihgmmm = models.CharField(mggmeth, max_length = 500,
        null = True, blank = True)
    inihgmqf = models.BooleanField(hqufase,choices = BoolChoose, default = False)
    inihgmqm = models.CharField(hqumeth, max_length = 500,
        null = True, blank = True)
    inihgmhf = models.BooleanField(hdrfase,choices = BoolChoose, default = False)
    inihgmhm = models.CharField(hdrmeth, max_length = 500,
        null = True, blank = True)
    inihgmvf = models.BooleanField(vulfase,choices = BoolChoose, default = False)
    inihgmvm = models.CharField(vulmeth, max_length = 500,
        null = True, blank = True)
    inighmia = models.BooleanField(inventar, choices = BoolChoose, 
        default = False)
    inighmaa = models.NullBooleanField(aquifer,choices = BoolChoose, 
        default = False, blank = True)
    inighmac = models.BooleanField(quality, choices = BoolChoose)
    inighmpc = models.CharField(parame, max_length = 500, null = True, 
        blank = True)
    inighmba = models.NullBooleanField(balan, blank = True)
    inighmla = models.NullBooleanField(analis, choices = BoolChoose, 
        blank = True)
    inighmge = models.BooleanField(study, choices = BoolChoose,
        default = False)
    inighmgm = models.CharField(stumeth, max_length = 500, null = True,
        blank = True)
    inighmda = models.NullBooleanField(dimens, choices = BoolChoose,
        default = False, blank = True)
    inighmch = models.BooleanField(carach, choices = BoolChoose,
        default = False)
    inighmcm = models.CharField(caracm, max_length = 500, null = True,
        blank = True)
    inighmva = models.BooleanField(vulnea, choices = BoolChoose,
        default = False)
    inighmvm = models.CharField(vulnem, max_length = 500, null = True,
        blank = True)
    inighmmh = models.BooleanField(modehi, choices = BoolChoose,
        default = True)
    inighmmb = models.NullBooleanField(modedb, choices = BoolChoose, 
        null = True, blank = True)
    inighmmc = models.IntegerField(modeca, null = True, blank = True)
    inighmma = models.BooleanField(modema, choices = BoolChoose, 
        default = True)

    class Meta:
        verbose_name = u'06.1 Metodología utilizada'
        verbose_name_plural = u'06.1 Metodologías utilizadas'
    
class inidhgcarto(models.Model):
    '''
    Hidrogeología
    Información general cartográfica y documento técnico
    '''
    outscal = u'Escala de salida de los mapas'
    stuscal = u'Escala de realización del estudio'
    forma = u'Formato de los Mapas'
    mapexte = u'Extensión de los Mapas'
    metadat = u'Existencia de metadatos'
    cartdig = u'Información asociada a la cartografía digital'
    docform = u'Formato del Documento Técnico'
    docexte = u'Extensión del Documento Técnico'

    BoolChoose = (
        (True, 'si'),
        (False, 'no'),
    )
    FormatMapChoose = (
        ('ANA', u'análogo'),
        ('DIG', u'digital'),
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
    FormatFileChoose = (
        ('doc', u'word'),
        ('xls', u'excel'),
        ('pdf', u'pdf'),
        ('otr', u'otro'),
    )
    InfoCartChoose = (
        ('TBL', 'Tabla asociada'),
        ('DBF', '.dbf'),
    )

    inihidge = models.OneToOneField('inidhgestud')
    inighcem = models.IntegerField(outscal)
    inighcee = models.IntegerField(stuscal)
    inighcmf = models.CharField(forma, max_length = 4, 
        choices = FormatMapChoose)
    inighcme = models.CharField(mapexte, max_length = 9, 
        choices = MapChoose, null = True, blank = True)
    inighcmd = models.BooleanField(metadat, choices = BoolChoose)
    inighcia = models.CharField(cartdig, max_length = 4, 
        choices = InfoCartChoose, null = True, blank = True)
    inighcdf = models.CharField(docform, max_length = 4, 
        choices = FormatMapChoose)
    inighcde = models.CharField(docexte, max_length = 4, 
        choices= FormatFileChoose, null = True, blank = True)

    class Meta:
        verbose_name = u'06.2 Información general cartográfica'
        verbose_name_plural = verbose_name

#Calidad de Agua

class inidcaestud(inididestud):
    '''
    Calidad de Agua
    Identificación del estudio
    '''
    class Meta:
        verbose_name = u'07 Estudio Calidad de agua'
        verbose_name_plural = u'07 Estudios Calidad de agua'

class inidcameth(models.Model):
    '''
    Calidad de Agua
    Metodología del estudio
    '''
    objeto = u'Objeto del estudio'
    metodo = u'Metodología utilizada para muestreos'
    estaci = u'Número de estaciones de la Red de monitoreo del recurso hídrico'
    #numeca = u'Numero de Campañas de muestreo /año y periodos'
    icaexi = u'¿Existe el Índice de Calidad de Agua - (ICA)?'
    icatra = u'ICA. Tramos o corrientes'
    icamap = u'ICA. Contiene mapas?'
    icames = u'ICA. Escala de salida de los mapas'
    icamfo = u'ICA. Formato de mapas'
    icamex = u'ICA. Extensión de los mapas'
    docfor = u'Formato del documento técnico'
    docext = u'Extensión del Documento Técnico'

    BoolChoose = (
        (True, 'si'),
        (False, 'no'),
    )
    FormatMapChoose = (
        ('ANA', u'análogo'),
        ('DIG', u'digital'),
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
    FormatFileChoose = (
        ('doc', u'word'),
        ('xls', u'excel'),
        ('pdf', u'pdf'),
        ('otr', u'otro'),
    )
    InfoCartChoose = (
        ('TBL', 'Tabla asociada'),
        ('DBF', '.dbf'),
    )

    inidcala = models.OneToOneField('inidcaestud')
    inicaobj = models.CharField(objeto, max_length = 500)
    inicamet = models.CharField(metodo, max_length = 500)
    inicaest = models.PositiveSmallIntegerField(estaci)
    inicaiex = models.BooleanField(icaexi, choices = BoolChoose, 
        default = False)
    inicaitr = models.CharField(icatra, max_length = 250,
        null = True, blank = True)
    inicaima = models.NullBooleanField(icamap, choices = BoolChoose, 
        default = False, null = True, blank = True)
    inicaime = models.PositiveIntegerField(icames, null = True,
        blank = True)
    inicaimf = models.CharField(icamfo, max_length = 4,
        choices = FormatMapChoose, blank = True, null = True)
    inicaimx = models.CharField(icamex, max_length = 9,
        choices = MapChoose, null = True, blank = True)
    inicadfo = models.CharField(docfor, max_length = 4,
        choices = FormatMapChoose, blank = True, null = True)
    inicadex = models.CharField(docext, max_length = 5,
        choices = FormatFileChoose, blank = True, null = True)

    class Meta:
        verbose_name = u'07.1 Metodología del estudio'
    
class inidcamecam(models.Model):
    '''
    Calidad de Agua
    Metodología - Número de campañas de muestreo
    '''

    YearChoose = []
    thisyear = datetime.datetime.now().year
    for i in range(1950, thisyear):
        YearChoose.append((i,i))

    icalamet = models.ForeignKey('inidcameth', verbose_name = u'Metodología')
    icamcano = models.IntegerField(u'Año', choices = YearChoose)
    icamcper = models.CharField(u'Periodo', max_length = 25)
    
    class Meta:
        verbose_name = u'07.1.1 Campaña de muestreo'
        verbose_name_plural = u'07.1.1 Campañas de muestreo'
    
class inicainfoes(models.Model):
    '''
    Calidad de Agua
    Información que debe contener el estudio
    '''
    inform = u'Informes y resultados de laboratorios acreditados para \
        los parámetros muestreados.'
    aforac = '¿Los aforos en la subcuenca están acreditados por el IDEAM?'
    aforos = 'Aforos de la subcuenca'
    observ = u'Observaciones del informe de laboratorio'
    parame = u'Parámetros Fisicoquímicos mínimos  muestreados en las \
        fuentes de agua superficial'

    BoolChoose = (
        (True, 'si'),
        (False, 'no'),
    )

    iicainfo = models.OneToOneField('inidcaestud', 
        verbose_name = u'estudio de Calidad de Agua')
    iicaiinf = models.CharField(inform, max_length = 500)
    iicaiafa = models.BooleanField(aforac, choices = BoolChoose, 
        default = False)
    iicaiobs = models.CharField(observ, max_length = 500)
    iicaipar = models.CharField(parame, max_length = 500)
    
    class Meta:
        verbose_name = '07.2 Información del estudio'
        verbose_name_plural = verbose_name

class inicainfgeo(inidgeorefe):
    '''
    Calidad de agua
    Información - Georreferenciación de estaciones de muestreo de la red de monitoreo
    '''
    iicaigeo = models.ForeignKey('inicainfoes')
    
    class Meta: 
        verbose_name = u'07.2.2 Estaciones de muestreo'

class inicainfoco(models.Model):
    '''
    Calidad de agua
    Información complementaria
    '''
    
    BoolChoose = (
        (True, 'si'),
        (False, 'no'),
    )

    iicainfc = models.OneToOneField('inidcaestud', 
        verbose_name = u'estudio de Calidad de Agua')
    iicaifoc = models.BooleanField(u'Existen objetivos de calidad de las corrientes',
        choices = BoolChoose, default = False)
    
    class Meta:
        verbose_name = '07.3 Información complementaria'
        verbose_name_plural = verbose_name

class inicaicca(models.Model):
    '''
    Calidad de agua
    Información complementaria- Estudios de capacidad de asimilación.
        o modelaciones
    '''
    capano = u'Año de estudio de capacidad de asimilación o modelación'

    YearChoose = []
    thisyear = datetime.datetime.now().year
    for i in range(1950, thisyear):
        YearChoose.append((i,i))
    
    iicaicom = models.ForeignKey(u'inicainfoco', 
        verbose_name = u'Información complementaria')
    iicaicap = models.PositiveSmallIntegerField(capano, choices = YearChoose)
    
    class Meta:
        verbose_name = u'07.3.1 Estudio de capac. de asimilación'   
        verbose_name = u'07.3.1 Estudios de capac de asimilación'   
    
#Cargas Contaminantes

class inidccestud(inididestud):
    '''
    Cargas Contaminantes
    Identificación del estudio
    '''
    aproba = u'¿Existe Acuerdo de aprobación de Línea base de carga \
        contaminante de DBO y SST y metas de reducción de carga contaminante?'
    
    BoolChoose = (
        (True, 'si'),
        (False, 'no'),
    )

    inidaalb = models.BooleanField(aproba, choices = BoolChoose)

    class Meta:
        verbose_name = u'08 Estudio Cargas contaminantes'
        verbose_name_plural = u'08 Estudios Cargas contaminantes'

class inidccmetho(models.Model):
    '''
    Cargas Contaminantes
    Metodologíadel estudio, levantamiento de datos y resultados
    '''
    objeto = u'Objeto del estudio'
    metodo = u'Metodología utilizada para la estimación de cargas \
        contaminantes de DBO y SST'
    lineab = u'¿La línea Base de carga contaminante de DBO y SST se \
        calculó para la zona rural y/o centros poblados?'
    muestr = u'¿Los muestreos de vertimientos que reposan en la CAR, \
        corresponden a  los últimos tres años?'
    concen = u'¿Se contemplan datos completos de concentraciones de \
        DBO (mg/l) y SST(mg/l) y Caudal(L/seg) en laboratorios \
        acreditados para éstos parámetros?'
    sumini = u'¿La fuente de muestreos de vertimientos de aguas \
        residuales, corresponden a los suministrados por los usuarios \
        de la Jurisdicción o han sido generados por la CAR?'
    usucor = u' ¿cuenta la Corporación con el inventario de usuarios objeto \
        de cobro de Tasa Retributiva o algún informe de usuarios por \
        sector productivo y cargas contaminantes de DBO y SST?'
    carsec = u'¿Se discriminan las cargas contaminantes por sectores productivos'
    forma = u'Formato del Documento Técnico'
    forext = u'Extensión del Documento Técnico'

    BoolChoose = (
        (True, 'si'),
        (False, 'no'),
    )
    SectChoose = (
        ('PRESU', u'presuntivamente'),
        ('CARAC', u'caracterización'),
        (False, u'no discrimina'),
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

    iiccmeth = models.OneToOneField('inidccestud')
    iiccmobj = models.CharField(objeto, max_length = 500)
    iiccmmet = models.CharField(metodo, max_length = 500)
    iiccmlin = models.BooleanField(lineab, choices = BoolChoose, default = False)
    iiccmmue = models.BooleanField(muestr, choices = BoolChoose, default = False)  
    iiccmdcc = models.BooleanField(concen, choices = BoolChoose, default = False)  
    iiccmsum = models.BooleanField(sumini, choices = BoolChoose, default = False)  
    iiccmusu = models.BooleanField(usucor, choices = BoolChoose, default = False)  
    iiccmcar = models.CharField(carsec, max_length = 6, choices = SectChoose, 
        default = False)  
    iiccmdoc = models.CharField(forma, max_length = 4, choices = FormatMapChoose)
    iiccmdoe = models.CharField(forext, max_length = 5, choices = FormatFileChoose,
        null = True, blank = True)

    class Meta:
        verbose_name = '08.1 Metodología del estudio'
        verbose_name_plural = verbose_name

class inidccminfe(models.Model):
    '''
    Cargas Contaminantes
    Información que debe contener el estudio
    '''
    inform = u'Informes y resultados de Laboratorios Acreditados por el IDEAM \
        para los parámetros muestreados'
    #georef = u'Georeferenciacion de estaciones de muestreo'
    observ = u'Observaciones del Informe de Laboratorio'
    percen = u'Porcentaje de remoción de carga contaminante de \
        DBO y SST de los Sistemas de Tratamiento de Aguas Residuales - \
        STAR disponibles para la cuenca'
    parame = u'Parámetros Fisicoquímicos mínimos muestreados en los \
        vertimientos de agua residual'
    
    iiccinfe = models.OneToOneField(u'inidccestud')
    iicciinf = models.CharField(inform, max_length = 500)
    iicciobs = models.CharField(observ, max_length = 500)
    iicciper = models.FloatField(percen)
    iiccipar = models.CharField(parame, max_length = 500)

    class Meta:
        verbose_name = u'08.2 Información del estudio'
        verbose_name_plural = verbose_name

class inidccmigeo(inidgeorefe):
    '''
    Cargas Contaminantes
    Información estudio - Georeferenciación de las estaciones de muestreo
    '''
    iiccmgeo = models.ForeignKey('inidccminfe')

    class Meta:
        verbose_name = u'08.2.1 Estación de muestreo'
        verbose_name_plural = u'08.2.1 Estaciones de muestreo'

class iniccicompl(models.Model):
    '''
    Cargas contaminantes
    Información complementaria
    '''
    muestre = u'¿La Corporación realiza contra muestreos de vertimientos de \
        aguas residuales domesticas e industriales?'
    percent = u'Porcentaje respecto al numero total de usuarios que vierten'
    imverti = u'¿la CAR cuenta con sistema de administración para la \
        información de monitoreos de vertimientos en relación con la \
        calidad del recurso hídrico?'
    eimpsmv = u'Estado de Implementación de Planes de saneamiento y \
        manejo de vertimientos - PSMV'
    porhexi = u'¿Existe Plan de Ordenamiento del Recurso Hídrico?'
    pueaaes = u'Estado de implementación de Planes de Uso Eficiente y \
        Ahorro del Agua existentes. ¿Estos suministran información sobre \
        consumos de agua - Dotaciones( L/Hab-dia)?'
    capdaex = u'Existe el Componente ambiental de los Planes \
        Departamentales de Agua'
    pmaaexi = u'¿Existen Planes Maestros de Acueducto y Alcantarillado?'
    
    BoolChoose = (
        (True, 'si'),
        (False, 'no'),
    )

    iiccicom = models.OneToOneField('inidccestud')
    iicccmue = models.BooleanField(muestre, choices = BoolChoose, 
        default = False)
    iicccper = models.FloatField(percent, null = True, blank = True)
    iicccprm = models.CharField(eimpsmv, max_length = 125,
        null = True, blank = True)
    iicccpor = models.NullBooleanField(porhexi, choices = BoolChoose,
        default = False)
    iicccpur = models.NullBooleanField(pueaaes, choices = BoolChoose,
        default = False)
    iiccccap = models.NullBooleanField(capdaex, choices = BoolChoose,
        default = False)
    iicccpma = models.NullBooleanField(pmaaexi, choices = BoolChoose,
        default = False)
    
    class Meta:
        verbose_name = u'08.3 Información complementaria'
        verbose_name_plural = verbose_name

#Cobertura

class inidcoestud(inididestud):
    '''
    Cobertura
    Identificación del estudio
    '''
    class Meta:
        verbose_name = u'09 Estudio de Cobertura'
        verbose_name_plural = u'09 Estudios de Cobertura'

class inidcometho(models.Model):
    '''
    Cobertura
    Metodología utilizada para levantamiento de coberturas'
    '''
    sensor = u'Tipo de sensores utilizados'
    fechai = u'Fecha de toma de la Imagen o fotografías utilizadas '
    methol = u'Metodología utilizada para el levantamiento'
    nivley = u'Nivel de aplicación de la Leyenda de la metodología utilizada' 
    interp = u'¿Qué método de interpretación se utilizó, visual y/o digital?'
    muestv = u'Muestreo de campo. Verificación de campo'
    mueste = u'Muestreo de campo. Época del año en que fue realizado'
    cartfu = u'Fuente de cartografía base'
    cartes = u'Fuente de cartografía base. Escala'
    cartan = u'Fuente de cartografía base. Año'

    MethChoose = (
        ('vis', 'visual'),
        ('dig', 'digital'),
    )
    thisyear = datetime.datetime.now().year
    YearChoose = []
    for i in range(1950, thisyear+1):
        YearChoose.append((i,i))

    iicometh = models.OneToOneField('inidcoestud')
    iicomsen = models.CharField(sensor, max_length = 125)
    iicomfec = models.DateField()
    iicommet = models.CharField(methol, max_length = 500)
    iicomniv = models.CharField(nivley, max_length = 125)
    iicommuv = models.CharField(muestv, max_length = 5, choices = MethChoose)
    iicommue = models.CharField(mueste, max_length = 125)
    iicomcfu = models.CharField(cartfu, max_length = 75)
    iicomces = models.IntegerField(cartes)
    iicomcan = models.IntegerField(cartan, choices = YearChoose, null = True,
        blank = True)

    class meta:
        verbose_name = u'09.1 Metodología de levantamiento'
        verbose_name_plural = verbose_name

class inidcoinfog(models.Model):
    '''
    Cobertura
    Información general cartográfica y documento técnico
    '''
    escas = u'Escala de salida de los mapas'
    escat = u'Escala de trabajo del levantamiento'
    mapfo = u'Formato de los Mapas'
    mapex = u'Extensión de los Mapas'
    metae = u'Existencia de metadatos'
    cadii = u'¿Qué información está asociada a la cartografía digital?'
    docfm = u'Formato del Documento Técnico'
    docex = u'Extensión del Documento Técnico'

    BoolChoose = (
        (True, 'si'),
        (False, 'no'),
    )
    FormatMapChoose = (
        ('ANA', u'análogo'),
        ('DIG', u'digital'),
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
    FormatFileChoose = (
        ('doc', u'word'),
        ('xls', u'excel'),
        ('pdf', u'pdf'),
        ('otr', u'otro'),
    )

    iicocart = models.OneToOneField('inidcoestud')
    iicoiesm = models.IntegerField(escas)
    iicoiesl = models.IntegerField(escat)
    iicoimfo = models.CharField(mapfo, max_length = 4, 
        choices = FormatMapChoose)
    iicoimex = models.CharField(mapex, max_length = 9,
        choices = MapChoose, null = True, blank = True)
    iicoimet = models.BooleanField(metae, choices = BoolChoose, default = False)
    iicoicdi = models.CharField(cadii, max_length = 500)
    iicoidof = models.CharField(docfm, max_length= 4,
        choices = FormatMapChoose)
    iicoidoe = models.CharField(docex, max_length = 5,
        choices = FormatFileChoose)

    class Meta:
        verbose_name = '09.2 Información cartográfica'
        verbose_name_plural = verbose_name

#Flora y Fauna

class inidffestud(inididestud):
    '''
    Flora y Fauna
    Identificación del estudio
    '''
    class Meta:
        verbose_name = u'10 Estudio de Flora y Fauna'
        verbose_name_plural = u'10 Estudios de Flora y Fauna'

class inidffmeth(models.Model):
    '''
    Flora y Fauna
    Metodología utilizada para levantamiento de información de flora,
    vegetación y fauna.
    '''
    metodo = u'Método utilizado para selección de sitios de muestreo'
    meinve = u'Metodología utilizada para inventario  de flora \
        y/o características de la vegetación'
    ticobe = u'Tipo de coberturas vegetales  naturales inventariadas.'
    vegete = u'¿Si en el área de estudio existe vegetación terrestre \
        y acuática los dos tipos possen inventarios?'
    ecoest = u'¿Si existieran ecosistemas acuáticos se han \
        realizado estudios  limnológicos?'
    numpar = u'Número de parcelas o transectos para inventarios \
        de vegetación o flora.'
    metfau = u'Metodología utilizada para inventario de fauna \
        por clase jerárquica'
    clafau = u'Clases jerárquicas  de fauna inventariada.'
    georef = u'¿Poseen georeferenciación los inventarios o están \
        relacionados a municipio o vereda?'
    carfue = u'¿La información de caracterización de flora y fauna se \
        realizó a partir de fuentes primarias o secundarias?'
    espame = u'¿Se han identificado especies de flora y/o fauna en \
        amenaza, peligro de extinción o endémicas?'
    geoame = u'¿Existe georeferenciación de las mismas?'
    
    BoolChoose = (
        (True, 'si'),
        (False, 'no'),
    )
    BoolNullChoose = (
        (True, 'si'),
        (False, 'no'),
        (None, 'No aplica'),
    )
    iffmeto = models.OneToOneField('inidffestud')
    iffmesm = models.CharField(metodo, max_length = 500)
    iffmein = models.CharField(meinve, max_length = 500)
    ifftico = models.CharField(ticobe, max_length = 500)
    iffvegi = models.NullBooleanField(vegete, blank = True,
        choices = BoolNullChoose)
    iffesli = models.NullBooleanField(ecoest, choices = BoolNullChoose)
    iffnupa = models.PositiveSmallIntegerField(numpar, 
        null = True, blank = True)
    iffmeif = models.CharField(metfau, max_length = 500,
        null = True, blank = True)
    iffclaj = models.CharField(clafau, max_length = 500, 
        null = True, blank = True)
    iffgeoi = models.NullBooleanField(georef, choices = BoolChoose,
        default = False)
    iffinfc = models.NullBooleanField(carfue, choices = BoolChoose,
        default = False)
    iffamen = models.NullBooleanField(espame, choices = BoolChoose,
        default = False)
    iffgeor = models.NullBooleanField(geoame, choices = BoolChoose,
        default = False)
    
    class Meta:
        verbose_name = u'10.1 Metodología de levantamiento'
        verbose_name_plural = verbose_name
    
class inidffcart(models.Model):
    '''
    Flora y Fauna
    Información general  del  documento técnico y cartografía
    '''
    docute = u'Documento técnico'
    planca = u'Planchas cartográficas asociadas a la información'
    metada = u'¿Existen metadatos?'
    metaau = u'Autor'
    infofl = u'¿Existe  información de flora y fauna  asociada a \
        la cartografía?'
    fuente = u'Fuente de cartografía base'
    escala = u'Escala'
    catano = u'Año'

    BoolChoose = (
        (True, 'si'),
        (False, 'no'),
    )
    FormatMapChoose = (
        ('ANA', u'análogo'),
        ('DIG', u'digital'),
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

    iffcart = models.OneToOneField('inidffestud')
    iffcocu = models.CharField(docute, max_length = 4, 
        choices = FormatMapChoose)
    iffcpla = models.CharField(planca, max_length = 9, choices = MapChoose)
    iffcmet = models.BooleanField(metada, choices = BoolChoose)
    iffclor = models.BooleanField(infofl, choices = BoolChoose)
    iffcfue = models.CharField(fuente, max_length = 120,
        null = True, blank = True)
    iffcesc = models.PositiveIntegerField(escala,  
        null = True, blank = True)
    iffcano = models.PositiveSmallIntegerField(catano,
        null = True, blank = True)

    class Meta:
        verbose_name = u'10.2 Información cartográfica'
        verbose_name_plural = verbose_name
    
#Plan de manejo en ecosistemas

class inidpmestud(inididestud):
    '''
    Plan de manejo en ecosistemas
    Identificación del estudio
    '''
    class Meta:
        verbose_name = u'11 Estudio PM ecosistemas'
        verbose_name_plural = u'11 Estudios PM ecosistemas'

class inidpmecofo(models.Model):
    '''
    Plan de manejo en ecosistemas
    Formulación del Plan y Resultados
    '''
    planma = u'Existen en la CAR planes de manejo de'
    planot = u'Si existiera otro tipo de plan de manejo que aplique al área \
        de interés, referéncielo'
    objeto = u'Objeto de estudio'
    planco = u'El Plan se encuentra adoptado por la Corporación'
    vigepl = u'Vigencia de los Planes existentes'
    planex = u'¿Los planes han sido ejecutados?'
    placua = u'¿Cuáles?'

    BoolChoose = (
        (True, 'si'),
        (False, 'no'),
    )

    ipmformu = models.OneToOneField('inidpmestud')
    ipmfplan = models.ManyToManyField('pmecoplanma', null = True, blank = True)
    ipmfobje = models.CharField(objeto, max_length = 500)
    ipmfadop = models.BooleanField(planco, choices = BoolChoose, 
        default = False)
    ipmfvige = models.CharField(vigepl, max_length = 125)
    ipmfplae = models.BooleanField(planex, choices = BoolChoose)
    ipmfplac = models.CharField(placua, max_length = 500, null = True,
        blank = True) 

    class Meta:
        verbose_name = u'11.1 Formulación del plan y resultados'
        verbose_name_plural = verbose_name

class pmecoplanma(models.Model):
    '''
    Plan Manejo en ecosistemas.
    Formulación del Plan y Resultados
    Planes de manejo
    '''
    pmecopla = models.ForeignKey('inidpmecofo')
    planmane = models.CharField(u'Plan de manejo', max_length = 200)

    class Meta:
        verbose_name = u'11.1.1 Plan de manejo'
        verbose_name_plural = u'11.1.1 Planes de manejo'

class inidpmecopm(models.Model):
    '''
    Plan Manejo en ecosistemas.
    Información sobre los planes de manejo
    '''
    formato = 'Formato del Documento Técnico'
    escatra = u'Escala de trabajo' 
    escapub = u'Escala de publicación' 
    escasal = u'Escala de salida de los mapas'
    mapfoem = u'Formato de los mapas'
    mapexte = u'Extensión de los mapas'

    FormatMapChoose = (
        ('ANA', u'análogo'),
        ('DIG', u'digital'),
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
    FormatFileChoose = (
        ('doc', u'word'),
        ('xls', u'excel'),
        ('pdf', u'pdf'),
        ('otr', u'otro'),
    )

    ipmanejo = models.OneToOneField('inidpmestud')
    ipminfdt = models.CharField(formato, max_length = 4,
        choices = FormatFileChoose) 
    ipminetr = models.PositiveIntegerField(escatra)
    ipminepu = models.PositiveIntegerField(escapub)
    ipminesa = models.PositiveIntegerField(escasal)
    ipminmfo = models.CharField(mapfoem, max_length = 4,
        choices = FormatMapChoose)
    ipminmex = models.CharField(mapexte, max_length = 9,
        choices = MapChoose)
    
    class Meta:
        verbose_name = u'11.2 Plan de manejo'
        verbose_name_plural = u'11.2 Planes de manejo'

#Riesgos

class inidriestud(inididestud):
    '''
    Plan de manejo en ecosistemas
    Identificación del estudio
    '''
    class Meta:
        verbose_name = u'12 Estudio Riesgos'
        verbose_name_plural = u'12 Estudios Riesgos'

#Socioeconómico

##
class inidseasinf(socioinfoge):
    '''
    Socioeconómico y Cultural
    Actores Sociales
    Información General
    '''
    class Meta:
        verbose_name = u'13.1 Actores sociales'
        verbose_name_plural = verbose_name

class inidseasdet(models.Model):
    '''
    Socioeconómico y Cultural
    Actores Sociales
    Detalle de la información
    '''
    metodo = u'Metodología del análisis de actores' 
    docume = u'Documentos, fichas'
    mapaac = u'Mapa de actores'
    matriz = u'Matriz de priorización'
    actore = u'Base de datos de actores, organizaciones sociales, \
        institucionales  y sectoriales'

    BoolChoose = (
        (True, 'si'),
        (False, 'no'),
    )

    isesocio = models.OneToOneField('inidseceinf')
    isesomet = models.CharField(metodo, max_length = 500)
    isesodoc = models.CharField(docume, max_length = 500)
    isesomap = models.BooleanField(mapaac, choices = BoolChoose,
        default = False)
    isesomat = models.BooleanField(matriz, choices = BoolChoose, 
        default = False)
    isesoact = models.BooleanField(actore, choices = BoolChoose,
        default = False)

    class Meta:
        verbose_name = u'13.1.2 Detalle de la información'
        verbose_name_plural = u'13.1.2 Detalles de la información'

##   
class inidseepinf(socioinfoge):
    '''
    Socioeconómico y Cultural
    Estrategias de participación
    Información General
    '''
    class Meta:
        verbose_name = u'13.2 Estrategia de participación'
        verbose_name_plural = u'13.2 Estrategias de participación'

class inidseepdet(models.Model):
    '''
    Socioeconómico y Cultural
    Estrategias de participación
    Detalle de la información
    '''
    estruc = u'Estructura de participación'
    incorp = u'Incorporación de la participación en los componentes \
        temáticos del plan'
    inform = u'Información de resultados de la aplicación de la estrategia'
    metodo = u'Metodología para el diagnóstico participativo'
    estado = u'Estado actual de la estructura de participación'
    estrat = u'Estrategia de comunicación'

    BoolChoose = (
        (True, 'si'),
        (False, 'no'),
    )

    iseestra = models.OneToOneField('inidseepinf')
    isepaest = models.CharField(estruc, max_length = 500)
    isepainc = models.BooleanField(incorp, choices = BoolChoose,
        default = True)
    isepainf = models.BooleanField(inform, choices = BoolChoose,
        default = True)
    isepamet = models.CharField(metodo, max_length = 500)
    isepasta = models.CharField(estado, max_length = 500)
    isepastr = models.CharField(estrat, max_length = 500)

    class Meta:
        verbose_name = u'13.2.1 Detalle de la información'
        verbose_name_plural = u'13.2.1 Detalles de la información'

##
class inidseceinf(socioinfoge):
    '''
    Socioeconómico y Cultural
    Participación de comunidades étnicas 
    Información General
    '''
    class Meta:
        verbose_name = u'13.3 Participación comunidad étnica'
        verbose_name_plural = u'13.3 Participación comunidades étnica'

class inidsecedet(models.Model):
    '''
    Socioeconómico y Cultural
    Participación de comunidades étnicas 
    Detalle de la información
    '''
    identif = u'Identificación y caracterización de grupos étnicos' 
    certifi = u'Certificados expedidos por el Ministerio de Interior sobre \
        la existencia de grupos étnicos presentes en la cuenca'
    consult = u'¿Cuáles consultas previas se están desarrollando actualmente \
        en el área de la cuenca?'
    resulta = u'Resultados de consultas previas  desarrolladas en el \
        área de la cuenca'
    sistema = u'Sistematización de experiencias participativas con \
        comunidades étnicas'
    existen = u'Existencia de estudios de participación con comunidades étnicas'

    BoolChoose = (
        (True, 'si'),
        (False, 'no'),
    )

    iseparti = models.OneToOneField('inidseceinf')
    iseceide = models.BooleanField(identif, choices = BoolChoose,
        default = False)
    isececer = models.CharField(certifi, max_length = 500)
    isececon = models.CharField(consult, max_length = 500)
    iseceres = models.CharField(resulta, max_length = 500)
    isecesis = models.BooleanField(sistema, choices = BoolChoose, 
        default = False)
    iseceexi = models.BooleanField(existen, choices = BoolChoose, 
        default = False)

    class Meta:
        verbose_name = u'13.3.1 Detalle de la información'
        verbose_name_plural = u'13.3.1 Detalles de la información'

##
class inidsedsinf(socioinfoge):
    '''
    Socioeconómico y Cultural
    Diagnósticos Socioeconómicos
    Información General
    '''
    class Meta:
        verbose_name = u'13.4 Diagnóstico socioeconómico'
        verbose_name_plural = u'13.4 Diagnósticos socioeconómicos'

class inidsdsedet(models.Model):
    '''
    Socioeconómico y Cultural
    Diagnósticos Socioeconómicos
    Detalle de la información
    '''
    inform = u'Información poblacional'
    descri = u'Descripción y caracterización servicios sociales existentes'
    segual = u'Análisis sobre Seguridad Alimentaria' 
    activi = u'Caracterización de las actividades económicas actuales y \
        dominantes'
    proyec = u'Análisis de proyectos regionales de impacto en la cuenca, \
        en desarrollo y futuros' 
    confli = u'Análisis de conflictos socioeconómicos' 
    politi = u'Descripción político administrativa e institucional de la \
        cuenca' 
    predia = u'Análisis predial o de tenencia de la tierra'
    seguri = u'Seguridad y convivencia' 

    BoolChoose = (
        (True, 'si'),
        (False, 'no'),
    )

    isediagn = models.OneToOneField('inidsedsinf')
    isedsinf = models.BooleanField(inform, choices = BoolChoose,
        default = True)
    isedsdes = models.CharField(descri, max_length = 500)
    isedsseg = models.BooleanField(segual, choices = BoolChoose,
        default = True)
    isedsact = models.BooleanField(activi, choices = BoolChoose,
        default = True)
    isedspro = models.BooleanField(proyec, choices = BoolChoose,
        default = True)
    isedscon = models.BooleanField(confli, choices = BoolChoose,
        default = True)
    isedspol = models.BooleanField(politi, choices = BoolChoose,
        default = True)
    isedspre = models.BooleanField(predia, choices = BoolChoose,
        default = True)
    isedscon = models.BooleanField(seguri, choices = BoolChoose,
        default = True)

    class Meta:
        verbose_name = u'13.4.1 Detalle de la información'
        verbose_name_plural = u'13.4.1 Detalles de la información'

##
class inidseccinf(socioinfoge):
    '''
    Socioeconómico y Cultural
    Caracterización Cultural
    Información General
    '''
    class Meta:
        verbose_name = u'13.5 Caracterización cultural'
        verbose_name_plural = verbose_name

class inidseccdet(models.Model):
    '''
    Socioeconómico y Cultural
    Caracterización Cultural
    Detalle de la información
    '''
    cultu = u'Caracterización cultural de la cuenca'
    patro = u'Caracterización de patrones de uso, ocupación y apropiación \
        del territorio'
    pract = u'Análisis de prácticas culturales, relacionadas con el \
        aprovechamiento y uso de la biodiversidad'

    BoolChoose = (
        (True, 'si'),
        (False, 'no'),
    )

    isecarac = models.OneToOneField('inidseccinf')
    isecucul = models.BooleanField(cultu, choices = BoolChoose,
        default = True)
    isecupat = models.BooleanField(patro, choices = BoolChoose,
        default = True)
    isesupra = models.CharField(pract, max_length = 500)

    class Meta:
        verbose_name = u'13.5.1 Detalle de la información'
        verbose_name_plural = u'13.5.1 Detalles de la información'

##
class inidsevsinf(socioinfoge):
    '''
    Socioeconómico y Cultural
    Valoración de Servicios Ecosistémicos
    Información General
    '''
    class Meta:
        verbose_name = u'13.6 Servicio ecosistémico'
        verbose_name_plural = u'13.6 Servicios ecosistémicos'

class inidsevsdet(models.Model):
    '''
    Socioeconómico y Cultural
    Valoración de Servicios Ecosistémicos
    Detalle de la información
    '''
    metodo = u'Metodología utilizada en el estudio'
    servic = u'Servicios ecosistémicos analizados'
    result = u'Resultados de la valoración económica de los servicios ecosistémicos'

    BoolChoose = (
        (True, 'si'),
        (False, 'no'),
    )
    
    isevalor = models.OneToOneField('inidsevsinf')
    isesemet = models.CharField(metodo, max_length = 500)
    iseseser = models.CharField(servic, max_length = 500)
    iseseres = models.CharField(result, max_length = 500)

    class Meta:
        verbose_name = u'13.6.1 Detalle de la información'
        verbose_name_plural = u'13.6.1 Detalles de la información'

##
class inidserfinf(socioinfoge):
    '''
    Socioeconómico y Cultural
    Relaciones funcionales urbano - regionales
    Información General
    '''
    class Meta:
        verbose_name = u'13.7 Relación urbano - regionales'
        verbose_name_plural = u'13.7 Relaciones urbano - regionales'

class inidserfdet(models.Model):
    '''
    Socioeconómico y Cultural
    Relaciones funcionales urbano - regionales
    Detalle de la información
    '''
    compet = u'Análisis de competitividad y producción'
    conect = u'Análisis de conectividad y movilidad'
    capaci = u'Análisis de capacidad de soporte ambiental de la región'

    BoolChoose = (
        (True, 'si'),
        (False, 'no'),
    )
    iserelaf = models.OneToOneField('inidserfinf')
    iserfcmp = models.BooleanField(compet, choices = BoolChoose, 
        default = False)
    iserfcon = models.BooleanField(conect, choices = BoolChoose, 
        default = False)
    iserfcap = models.BooleanField(capaci, choices = BoolChoose, 
        default = False)
    
    class Meta:
        verbose_name = u'13.7.1 Detalle de la información'
        verbose_name_plural = u'13.7.1 Detalles de la información'
