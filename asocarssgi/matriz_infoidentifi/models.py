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
        verbose_name = u'Metodología Geomorfología'
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
        verbose_name = u'Metodología uso de tierra'
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
        verbose_name = u'Información cartográfica'
        verbose_name_plural = verbose_name #u'Información general cartográfica y documentos técnicos'
    
#Hidrología

class inidhlestud(inididestud):
    '''
    Hidrología
    Identificación del estudio
    '''
    class Meta:
        verbose_name = u'Estudio hidrológico'
        verbose_name_plural = u'Estudios hidrológicos'

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
        verbose_name = u'Metodología. hidrología/climatología'
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
        verbose_name = u'Información de aforos'
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
        verbose_name = u'Información general cartográfica'
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
        verbose_name = u'Información Complementaria'
        verbose_name_plural = verbose_name

#Hidrogeología

class inidhgestud(inididestud):
    '''
    Hidrogeología
    Identificación del estudio
    '''
    class Meta:
        verbose_name = u'Estudio hidrogeológico'
        verbose_name_plural = u'Estudios hidrogeológicos'

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
        verbose_name = u'Metodología utilizada'
        verbose_name_plural = u'Metodologías utilizadas'
    
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
        verbose_name = u'Información general cartográfica'
        verbose_name_plural = verbose_name

#Calidad de Agua

class inidcaestud(inididestud):
    '''
    Calidad de Agua
    Identificación del estudio
    '''
    class Meta:
        verbose_name = u'Estudio Calidad de agua'
        verbose_name_plural = u'Estudios Calidad de agua'

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
        verbose_name = u'Campaña de muestreo'
        verbose_name_plural = u'Campañas de muestreo'
    
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
        verbose_name = 'Información que debe contener'
        verbose_name_plural = verbose_name

class inicainfgeo(inidgeorefe):
    '''
    Calidad de agua
    Información - Georreferenciación deestaciones de muestreo de la red de monitoreo
    '''
    iicaigeo = models.ForeignKey('inicainfoes')

class inicainfoco(models.Model):
    iicainfc = models.OneToOneField('inidcaestud', 
        verbose_name = u'estudio de Calidad de Agua')
    
    BoolChoose = (
        (True, 'si'),
        (False, 'no'),
    )

    iicaifoc = models.BooleanField(u'Existen objetivos de calidad de las corrientes',
        choices = BoolChoose, default = False)
    
    class Meta:
        verbose_name = 'Información complementaria'
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
        verbose_name = u'Estudio de capacidad de asimilación'   
        verbose_name = u'Estudios de capacidad de asimilación'   
    
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
        verbose_name = u'Estudio Cargas contaminantes'
        verbose_name_plural = u'Estudios Cargas contaminantes'

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
        verbose_name = 'Metodología del estudio'
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

class inidccmigeo(inidgeorefe):
    '''
    Cargas Contaminantes
    Información estudio - Georeferenciación de las estaciones de muestreo
    '''
    iiccmgeo = models.ForeignKey('inidccminfe')

class iniccicompl(models.Model):
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

    iiccicom = models.ForeignKey('inidccestud')
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

#Cobertura

class inidcoestud(inididestud):
    '''
    Cobertura
    Identificación del estudio
    '''
    class Meta:
        verbose_name = u'Estudio Cobertura'
        verbose_name_plural = u'Estudios Cobertura'

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

    iicometh = models.OneToOneField(inidcoestud)
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
        verbose_name = u'Metodología levantamiento coberturas'
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
        verbose_name = 'Información cartográfica'
        verbose_name_plural = verbose_name

#Flora y Fauna

class inidffestud(inididestud):
    '''
    Flora y Fauna
    Identificación del estudio
    '''
    class Meta:
        verbose_name = u'Estudio Flora y Fauna'
        verbose_name_plural = u'Estudios Flora y Fauna'

#Plan de manejo en ecosistemas

class inidpmestud(inididestud):
    '''
    Plan de manejo en ecosistemas
    Identificación del estudio
    '''
    class Meta:
        verbose_name = u'Estudio PM ecosistemas'
        verbose_name_plural = u'Estudios PM ecosistemas'

#Riesgos

class inidriestud(inididestud):
    '''
    Plan de manejo en ecosistemas
    Identificación del estudio
    '''
    class Meta:
        verbose_name = u'Estudio Riesgos'
        verbose_name_plural = u'Estudios Riesgos'

#Socioeconómico


