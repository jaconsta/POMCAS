#-*- coding: utf-8 -*-
import datetime

from django.db import models
from django.contrib.auth.models import User

from corporacion.models import corporaname
from cuencas.models import cuencompart

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

class inforconcep(models.Model):
    '''
    Concepto General
    '''
    informat = models.ForeignKey(inforcompon, verbose_name = 'Formato')
    infcocor = models.ForeignKey(corporaname, verbose_name = 'Corporacion')
    infcocue = models.ForeignKey(cuencompart, verbose_name = 'Cuenca')
    infconce = models.CharField(u'Concepto', max_length = 500)
    infcowho = models.CharField(u'Nombre de quien firma', max_length = 250)
    
    
    def __unicode__(self):
        return self.infconce

    class Meta:
        verbose_name = u'Concepto de caracterizacion general'
        verbose_name_plural = verbose_name

class inforindice(models.Model):
    '''
    Índice de formatos de evaluación de información disponible.
    '''
    infocomp = models.ForeignKey('inforcompon' , verbose_name = u'Componente')
    infosubc = models.CharField(u'Subcomponente', max_length = 75)
    infotema = models.CharField(u'Tema a evaluar', max_length = 125)
    infonota = models.CharField(u'Preguntas orientadora', max_length = 1000)
    infoalca = models.CharField(u'Alcance', max_length = 1000)
    infourlc = models.URLField(u'Dirección capacitación', null = True,
        blank = True)
    infoprot = models.FileField(u'Archivo de Protocolo', upload_to = 'protocolos/',
        null = True)
    infoprio = models.PositiveSmallIntegerField(u'Prioridad')
    
    def __unicode__(self):
        return self.infotema
    class Meta:
        verbose_name = u'Formato de información disponible'
        verbose_name_plural = u'Índice de formatos de evaluación de información disponible'

#Select list.
class SelectList:
    '''
    All the choose list avaliable.
    In a class just to simplify code and unite them all
    call: lists = SelectList()
    use: lists.funcname()
    '''
    def StudiesChoose(self):
        StudiesChoose = (
            ('CART' , u'Cartografía'),
            ('FOTO' , u'Fotografías'),
            ('IMAG' , u'Imágenes'),
            ('SUEL' , u'Suelos'),
            ('HDRL' , u'Hidrología'),
            ('HDRG' , u'Hidrogeología'),
            ('QAGU' , u'Calidad de Agua'),
            ('CCON' , u'Cargas Contaminantes'),
            ('COBE' , u'Coberturas de la tierra'),
            ('FLFA' , u'Flora y Fauna'),
            ('PMEC' , u'Planes de manejo de ecosistemas'),
            ('AMEN' , u'Identificación de amenazas'),
            ('RIES' , u'Riesgos'),
            ('SACS' , u'Actores Sociales'),
            ('SPAR' , u'Participación'),
            ('SPCE' , u'Participación de comunidades étnicas'),
            ('SDIA' , u'Diagnósticos socioeconómicos'),
            ('SCCU' , u'Caracterización cultural'),
            ('SVSE' , u'Valoración de servicios ecosistémicos'),
            ('SFUR' , u'Relaciones Funcionales urbano - regionales'),
        )
        return StudiesChoose
    def BoolChoose(self):
        BoolChoose = (
            (True , u'si'),
            (False, u'no'),
        )
        return BoolChoose
    def BoolNullChoose(self):
        BoolNullChoose = (
            (True , u'si'),
            (False, u'no'),
            (None , u'no aplica'),
        )
        return BoolNullChoose 
    def YearList(self):
        thisyear = datetime.datetime.now().year
        YearChoose = []
        for i in range(1950, thisyear):
            YearChoose.append((i,i))
        return YearChoose
    def ThisYear(self):
        return datetime.datetime.now().year
    def FormatChoose(self):
        FormatMapChoose = (
            ('ANA', u'análogo'),
            ('DIG', u'digital'),
        )
        return FormatMapChoose
    def MapExtChoose (self):
        MapChoose = (
            ('ECW'     , 'ECW'),
            ('Generate', 'Generate'),
            ('SHP'     , 'SHP'),
            ('e00'     , 'e00'),
            ('ArcInfo' , 'ArcInfo'),
            ('ECW'     ,'ECW'),
            ('DWG'     , 'DWG'),
            ('DGN'     , 'DGN'),
            ('DXF'     , 'DXF'),
            ('PDF'     , 'PDF'),
            ('TIF'     , 'TIF'),
            ('JPG'     , 'JPG'),
            ('Otro'    , 'Otro'),      
        )
        return MapChoose 
    def FileExtChoose(self):
        FormatFileChoose = (
            ('doc', u'Word'),
            ('xls', u'Excel'),
            ('pdf', u'PDF'),
            ('Otr', u'Otro'),
        )
    def SensChoose (self):
        SensChoose = (
            ('LandSat' , u'LandSat'),
            ('SPOT'    , u'SPOT'),
            ('RapidEye', u'RapidEye'),
            ('IKONOS'  , u'IKONOS'),
            ('Otro'    , u'Otro'),
        )
        return SensChoose
    def SisCoordChoose (self):
        SisCoordChoose = (
            ('PLA', u'Planas'),
            ('GEO', u'Geográficas'),
        )
        return SisCoordChoose 
    def OriCoordChoose (self):
        OriCoordChoose = (
            ('OO', u'Occidente Occidente'),
            ('O' , u'Occidente'),
            ('C' , u'Centro'),
            ('E' , u'Oriente'),
            ('EE', u'Oriente Oriente'),
        )
        return OriCoordChoose 
    def ScaleChoose(self):
        ScaleChoose = (
            (25000, u'1:25.000'),
            (10000, u'1:10.000'),
            (5000 , u'1:5.000'),
            (2000 , u'1:2.000'),
            (1000 , u'1:1.000'),
            (500  , u'1:500'),
        )
        return ScaleChoose 
    def DefaultScale(self):
        return 25000
    def EscTempChoose(self):
        EscTempChoose = (
            ('D', 'Diario'),
            ('M', 'Mensual'),
            ('A', 'Anual'),
        )
        return EscTempChoose
    def MethChoose(self): 
        MethChoose = (
            ('vis', 'visual'),
            ('dig', 'digital'),
        )
        return MethChoose 
    def PeriAforChoose(self):
        PeriAforChoose = (
            ('SEQ', u'Sequía'), 
            ('INV', u'Invierno'),
        )
        return PeriAforChoose 
    def FotoFormChoose(self):
        FotoFormChoose = (
            ('TIFF', u'TIFF'),
            ('ECW' , u'ECW'),
            ('IMG' , u'IMG'),
            ('ANA' , u'Análogo (papel)'),
            ('Otr' , u'Otro'),
        )
        return FotoFormChoose 
    def InfoCartChoose(self):
        InfoCartChoose = (
            ('tas', u'tabla asociada'),
            ('dbf', u'dbf'),
        )
        return InfoCartChoose 
    def SectChoose(self):
        SectChoose = (
            ('pre', u'presuntivamente'),
            ('car', u'caracterización'),
            ('amb', u'Ambos'),
            (False, u'No Aplica'),
        )
        return SectChoose 
    def CartoSubteChoose(self):
        CartoSubteChoose = (
            ('CATAS', u'Catastro'),
            ('TRANS', u'Transporte'),
            ('HIDRO', u'Hidrografía'),
            ('RELIE', u'Relieve'),
            ('ENTID', u'Entidad Territorial'),
        )
    def HdrFaseChoose(self):
        HdrFaseChoose = (
            ('IPA', u'Inventario de puntos de agua'),
            ('MGG', u'Modelo geológico - geofísico'),
            ('HDQ', u'Hidroquímica'),
            ('HDL', u'Hidráulica'),
            ('VYR', u'Vulnerabilidad y riesgo'),
        )
        return HdrFaseChoose 
    def HdrAcuifChoose(self):
        HdrAcuifChoose = (
            ('lbr', u'Libre'),
            ('con', u'Confinado'),
            ('sco', u'Semiconfinado'),
        )
        return HdrAcuifChoose
    def HdrMatModChose(self):
        HdrMatModChose = (
            ('MFL', u'Modelo de flujo'),
            ('TRC', u'Transporte de contaminantes'),
            ('IAS', u'Interacción con aguas superficiales'),
        )
        return HdrMatModChose
    def CacaEstiChoose(self):
        CacaEstiChoose = (
            ('PRES', u'Forma presuntiva'),
            ('VERT', u'Caracterización de vertimento'),
            ('BOTH', u'Ambos'),
        )
        return CacaEstiChoose 
    def CacaParaChoose(self):
        CacaParaChoose = (
            ('ZORU', u'Zona rural'),
            ('CENT', u'Centro Poblado'),
            ('BOTH', u'Ambos'),
            (False, u'Ninguno'),
        )
        return CacaParaChoose 
    def CacaFuenChoose(self):
        CacaFuenChoose = (
            ('USU', u'Usuarios'),
            ('MUN', u'Municipios'),
            ('CAR', u'CAR'),
            ('MIX', u'Mixtos'),
        )
        return CacaFuenChoose 
    def CacaQuinChoose(self):
        CacaQuinChoose = (
            ('INV', u'Inventario de usuarios objeto de cobro de Tasa \
                Retributiva'),
            ('INF', u'Informe de usuarios por sector productivo'),
            ('CAC', u'Cargas contaminantes de DBO y SST'),
        )
        return CacaQuinChoose
    def CacaDiscChoose(self):
        CacaDiscChoose = (
            ('PRE', u'Presuntivamente'),
            ('CAR', u'Caracterización'),
            ('OTR', u'Otro'),
            (False, u'Ninguno'),
        )
        return CacaDiscChoose
    def CobeSensChoose(self):
        CobeSensChoose = (
            ('FOT', u'Fotografías'),
            ('IMG', u'Imágenes'),
            ('SAT', u'Satelitales'),
            ('RAD', u'Radar'),
            ('OTR', u'Otros'),
        )
        return CobeSensChoose 
    def CobeMetoChoose(self):
        CobeMetoChoose = (
            ('VIS', u'Visual'),
            ('DIG', u'Digital'),
        )
        return CobeMetoChoose
    def FlofInveChoose(self):
        FlofInveChoose = (
            ('TER', u'Terrestre'),
            ('ACU', u'Acuático'),
            ('AMB', u'Ambos'),
            (False, u'Ninguno'),
        )
        return FlofInveChoose 
    def FlofGeoChoose(self):
        FlofGeoChoose = (
            ('GEO', u'Georeferenciación'),
            ('REM', u'Relacionados a municipio'),
            ('REV', u'Relacionados a vereda'),
            ('OTR', u'Otros'),
            (False, u'No aplica'),
        )
        return FlofGeoChoose 
    def FlofPMEFuenChoose(self):
        FlofFuenChoose = (
            ('PRI', u'Primarias'),
            ('SEC', u'Secundarias'),
            ('MIX', u'Mixtas'),
        )
        return FlofFuenChoose 
    def FlofAmenChoose(self):
        FlofAmenChoose = (
            ('AME', u'Amenaza'),
            ('PEL', u'Peligro de extinción'),
            ('END', u'Endémica'),
            ('OTR', u'Otra'),
        )
        return FlofAmenChoose 
    def PMEInvChoose(self):
        PMEInvChoose = (
            ('TER', u'Terrestre'),
            ('AQU', u'Acuático'),
            ('AMB', u'Ambos'),
        )
        return PMEInvChoose 

#Caracterización general, Identificación del estudio
class inididinden(models.Model):
    '''
    User data of the filled formats.
    
    --------------
    I'm using variables because the names to display are too long
    '''
    lists = SelectList()

    iniescor = models.ForeignKey(corporaname, verbose_name = u'Corporación')
    iniescue = models.ForeignKey(cuencompart, verbose_name = u'Cuenca')
    inieswho = models.ForeignKey(User, 
        verbose_name = u'Usuario que llena el formulario',
        related_name = '%(app_label)s_%(class)s_user_create')
    inieswhu = models.ForeignKey(User, 
        verbose_name = u'Último usuario actualiza el formulario',
        related_name = '%(app_label)s_%(class)s_user_edit')
    iniesdac = models.DateTimeField(u'Fecha de creación', auto_now_add = True, 
        editable = False)
    iniesdau = models.DateTimeField(u'Fecha de última actualización', 
        auto_now = True, editable = False) 

    class Meta:
        abstract = True

class inididestud(inididinden):
    '''
    Formato de evaluación de información, Caracterización general, 
    Identificación del estudio
    ''' 
    subcom = u'Subcomponente de estudio'
    nombre = u'Nombre del estudio'
    docfor = u'Formato del documento técnico'
    docext = u'Extensión del documento técnico'
    doceot = u'Otro'
    locali = u'Localización física del estudio'
    respon = u'Funcionario responsable de su custodia y/o manejo'
    udepar = u'Ubicación geográfica del estudio. Departamento'
    udemun = u'Ubicación geográfica del estudio. Municipio'
    usubcu = u'Ubicación geográfica. Subcuenca'
    usecto = u'Ubicación geográfica. Sector'
    utramo = u'Ubicación geográfica. Tramo'
    uvered = u'Ubicación geográfica. Vereda'
    uchidg = u'Ubicación geográfica. Cuenca hidrogeológica'
    ubarea = u'Ubicación geográfica. Área'
    coarea = u'Área de cobertura del estudio sobre la cuenca'
    coperc = u'Porcentaje de cobertura del estudio sobre la cuenca'
    autor  = u'Autor del estudio'
    nit    = u'Número de Identificación'
    studin = u'Fecha de inicio del estudio'
    realiz = u'Año de realización del estudio'
    public = u'Año de publicación'
    acuerd = u'¿Existe acuerdo de aprobación de línea base de carga \
        contaminante de DBO y SST y metas de reducción de carga contaminante?'
    ambito = u'Ámbito de aplicación del diagnóstico'
    #HelpText
    docext_help = u'En caso que sea digital'
    locali_help = u'Dependencia en la que reposa'
    coarea_help = u'En hectáreas (ha)'
    coperc_help = u'Porcentaje (%)'
    nit_help    = u'NIT o Documento de identificación del autor. \
        Ej. 123456789-0'
    ambito_help = u'Planificación territorial, ordenación de la cuenca, otros'
    
    lists = SelectList()

    inidsubc = models.CharField(subcom, max_length = 20)
    inidnomb = models.CharField(nombre, max_length = 500)
    iniddocf = models.ForeignKey('documformat', verbose_name = docfor,
        null = True, blank = True)#CharField(docfor, max_length = 4, null = True,
        #blank = True, choices = lists.FormatChoose())
    iniddoce = models.ForeignKey('extdocuform', verbose_name = docext,#models.CharField(docext, max_length = 4, null = True,
        null = True, blank = True, #blank = True, choices = lists.FileExtChoose(),
        help_text = docext_help)
    iniddoco = models.CharField(doceot, max_length = 10, null = True,
        blank = True)
    inidlocf = models.CharField(locali, max_length = 250, null = True,
        blank =True, help_text = locali_help)
    inidresp = models.CharField(respon, max_length = 250, null = True,
        blank = True)
    inidudep = models.CharField(udepar, max_length = 150, null = True,
        blank = True)
    inidumun = models.CharField(udemun, max_length = 150, null = True,
        blank = True)
    inidusub = models.CharField(usubcu, max_length = 150, null = True,
        blank = True)
    inidusec = models.CharField(usecto, max_length = 150, null = True,
        blank = True)
    inidutra = models.CharField(utramo, max_length = 150, null = True,
        blank = True)
    iniduver = models.CharField(uvered, max_length = 150, null = True,
        blank = True)
    iniduchg = models.CharField(uchidg, max_length = 150, null = True,
        blank = True)
    iniduare = models.CharField(ubarea, max_length = 150, null = True,
        blank = True)
    inidcare = models.FloatField(coarea, null = True, blank = True, 
        help_text = coarea_help)
    inidcper = models.FloatField(coperc, null = True, blank = True,
        help_text = coperc_help)
    inidauth = models.CharField(autor, max_length = 125)
    inidanit = models.CharField(nit, max_length = 13, null = True, 
        blank = True, help_text = nit_help)
    inidsini = models.DateField(studin, blank = True, null = True)
    inidanor = models.PositiveSmallIntegerField(realiz, 
        null = True, blank = True,
        choices = lists.YearList(), default = lists.ThisYear())
    inidanop = models.PositiveSmallIntegerField(public, 
        choices = lists.YearList(), default = lists.ThisYear())
    inidacue = models.NullBooleanField(acuerd, choices = lists.BoolChoose(), 
        default = False)
    inidambi = models.CharField(ambito, max_length = 150, null = True,
        blank = True, help_text = ambito_help)
    
    def __unicode__(self):
        return '%s, %s, %s' % (self.inidnomb, self.inidauth, 
            self.inidlocf)

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

class inidcartog(models.Model):
    '''
    Informacion general cartográfica y documentos técnicos.
    '''
    escsal = u'Escala de salida de los mapas'
    esclev = u'Escala de trabajo del levantamiento'
    escpub = u'Escala de publicación'
    mapfor = u'Formato de los Mapas'
    mapext = u'Extensión de los Mapas'
    mapotr = u'Otro'
    metada = u'Existencia de metadatos'
    metind = u'Metadatos. Indíquelos'
    metinf = u'Metadatos. ¿A partir de qué información?'
    metaut = u'Metadatos. Autor'
    metnit = u'Metadatos. Número de identificación'
    metano = u'Metadatos. Año de toma de la información'
    infaso = u'Indique la información asociada a la cartografía digital'
    infflo = u'¿Existe  información de flora y fauna  asociada a la \
        cartografía ?'
    mapley = u'¿Existe en el mapa leyenda geomorfológica que incluya Ambiente \
        morfogénetico o morfogénico, pendiente, forma de la pendiente, \
        procesos mordofinámicos actuales, etc.?'
    fuente = u'Fuente Cartografía Base del Estudio'
    qualit = u'Calidad de la Cartografía temática'
    docfor = u'Formato del documento técnico'
    docext = u'Extensión del Documento Técnico'
    docotr = u'Otro'
    # Help_text
    mapext_help = u'En caso que sea digital'
    infaso_help = u'Ver la coherencia de la información asociada en la \
            tabla de atributos del mapa temático'
    qualit_help = u'Topología y simbología. Ver formato de cartografía base'
    docext_help = mapext

    lists = SelectList()

    cartestu = models.ForeignKey('inididestud',
        verbose_name = u'Caracterización general')
    carescs = models.CharField(escsal, max_length = 9, null = True, 
        blank = True)
    caruesle = models.CharField(esclev, max_length = 9, null = True, 
        blank = True)
    caruespu = models.CharField(escpub, max_length = 9, null = True, 
        blank = True)
    carmafor = models.ForeignKey('documformat', verbose_name = mapfor,#CharField(mapfor, max_length = 4, 
        null = True, blank = True,
        related_name = '%(app_label)s_%(class)s_mapfor')
        #choices = lists.FormatChoose(), null = True, blank = True)
    carmamex = models.ForeignKey('mapfileexte', verbose_name = mapext, #CharField(mapext, max_length = 9, 
        related_name = '%(app_label)s_%(class)s_mapext',
        null = True, blank = True, #choices = lists.MapExtChoose(), null = True, blank = True,
        help_text = mapext_help)
    carmamot = models.CharField(mapotr, max_length = 9, 
        null = True, blank = True)
    carmetad = models.NullBooleanField(metada, choices = lists.BoolChoose(), 
        default = False)
    carmeind = models.CharField(metind, max_length = 500, 
        null = True, blank = True)
    carmeinf = models.CharField(metinf, max_length = 500, 
        null = True, blank = True)
    carmeaut = models.CharField(metaut, max_length = 125, 
        null = True, blank = True)
    carmenit = models.NullBooleanField(metnit, max_length = 12, 
        null = True, blank = True)
    carmedat = models.PositiveSmallIntegerField(metano, null = True, 
        blank = True, choices = lists.YearList(), default = lists.ThisYear())
    carinaso = models.CharField(infaso, max_length = 125, null = True, 
        blank = True, help_text = infaso_help)
    carinflo = models.NullBooleanField(infflo, null = True, blank = True)
    carleyen = models.NullBooleanField(mapley, choices = lists.BoolChoose(), 
        default = False, null = True, blank = True)
    carfuent = models.CharField(fuente, max_length = 75, null = True, 
        blank = True)
    carqualy = models.CharField(qualit, max_length = 125, null = True, 
        blank = True, help_text = qualit_help)
    cardocfo = models.ForeignKey('documformat', verbose_name = docfor,#CharField(docfor, max_length = 4,
        related_name = '%(app_label)s_%(class)s_docfor', 
        null = True, blank = True)
        #choices = lists.FormatChoose()) 
    cardocex = models.ForeignKey('extdocuform', verbose_name = docext, #CharField(docext, max_length = 4,
        related_name = '%(app_label)s_%(class)s_docext',
        null = True, blank = True) #choices = lists.FileExtChoose(), null = True, blank = True)
    cardocot = models.CharField(docotr, max_length = 10, null = True, 
        blank = True)

# Subtema Cartografía.
class inicartogra(inididinden):
    '''
    Componente cartográfico. 
    Preguntas comunes
    '''
    subcom = u'Subcomponente de estudio'
    cubria = u'Área de cubrimiento con relación a la cuenca'
    cubrip = u'Porcentaje de cobertura con relación a la cuenca'
    formaf = u'Formato del archivo'
    archex = u'Extensión del archivo'
    archeo = u'Otro'
    reessc = u'Referencia espacial. Sistema de coordenadas'
    reessr = u'Referencia espacial. Sistema de referencia'
    reesoc = u'Referencia espacial. Orígen de coordenadas'
    reesda = u'Referencia espacial. Dátum'
    licenc = u'Licencia de uso'
    author = u'Autor'
    lugpub = u'Lugar de publicación'
    annopu = u'Año'
    tamano = u'Tamaño del archivo'
    # Help_text
    cubria_help = u'En hectáreas (ha)'
    cubrip_help = u'Porcentaje (%)'
    archex_help = u'En caso que sea digital'
    tamano_help = u'Expresado en MB'

    lists = SelectList()

    inidsubc = models.CharField(subcom, max_length = 20)
    incacuba = models.FloatField(cubria, help_text = cubria_help)
    incacubp = models.FloatField(cubrip, help_text = cubrip_help)
    incaforf = models.ForeignKey('documformat', verbose_name = formaf)#CharField(formaf, max_length = 4, 
        #choices = lists.FormatChoose())
    incafore = models.ForeignKey('extdocuform', verbose_name = archex,#CharField(archex, max_length = 5, null = True,
        null = True, blank = True)
    incaforo = models.CharField(archeo, max_length = 25, null = True,
        blank = True)
    incarsco = models.ForeignKey('cartcoorsys', verbose_name = reessc)#CharField(reessc, max_length = 4,
        #choices = lists.SisCoordChoose())
    incarsre = models.CharField(reessr, max_length = 25)
    incaroco = models.ForeignKey('cartcoorori', verbose_name = reesoc)#CharField(reesoc, max_length = 3, 
        #choices = lists.OriCoordChoose())
    incardat = models.CharField(reesda, max_length = 25)
    incarlic = models.CharField(licenc, max_length = 250)
    incaraut = models.CharField(author, max_length = 150)  
    incarlug = models.CharField(lugpub, max_length = 150)  
    incarano = models.PositiveSmallIntegerField(annopu, 
        choices = lists.YearList())
    incartam = models.FloatField(tamano, null = True, blank = True, 
        help_text = tamano_help)

    class Meta:
        abstract = True

class inicartsubt(models.Model):
    '''
    Cartografía base
    Subtemas cartográficos
    '''
    subtem = u'Subtema cartográfico'
    presen = u'Presencia de elementos que hacen parte del tema en el \
        catálogo de objetos'
    cuapre = u'Especifique cuáles'
    qualit = u'Calidad de datos'
    reltop = u'Relaciones topológicas'

    lists = SelectList()

    icarsubt = models.ForeignKey('inidcardatg')
    icarsnam = models.CharField(subtem, max_length = 20, editable = False)
    icarspre = models.BooleanField(presen, choices = lists.BoolChoose())
    icarsexi = models.CharField(cuapre, max_length = 500) 
    icarsqua = models.BooleanField(qualit, choices = lists.BoolChoose())
    icarsrel = models.BooleanField(reltop, choices = lists.BoolChoose())

    class Meta:
        verbose_name = u'1.2 Subtema cartográfico'
        verbose_name_plural = u'1.2 Subtemas cartográficos'

class documformat(models.Model):
    '''
    Componente cartográfico
    Extensión del documento
    '''
    value = models.CharField(u'Variable', max_length = 150)
    enable = models.BooleanField(u'Enabled', default = True)
    
    def __unicode__(self):
        return self.value

class matpfileexte(models.Model):
    '''
    Componente cartográfico
    Extensión del documento
    '''
    value = models.CharField(u'Variable', max_length = 150)
    enable = models.BooleanField(u'Enabled', default = True)
    
    def __unicode__(self):
        return self.value

class extdocuform(models.Model):
    '''
    Componente cartográfico
    Extensión del documento
    '''
    value = models.CharField(u'Variable', max_length = 150)
    enable = models.BooleanField(u'Enabled', default = True)
    
    def __unicode__(self):
        return self.value

class inimagsenso(models.Model):
    '''
    Componente cartográfico
    Sensor de las imágenes
    '''
    value = models.CharField(u'Variable', max_length = 150)
    enable = models.BooleanField(u'Enabled', default = True)
    
    def __unicode__(self):
        return self.value

class cartcoorsys(models.Model):
    '''
    Componente cartográfico
    Sistema de coordinadas
    '''
    value = models.CharField(u'Variable', max_length = 150)
    enable = models.BooleanField(u'Enabled', default = True)
    
    def __unicode__(self):
        return self.value

class cartcoorori(models.Model):
    '''
    Componente cartográfico
    Orígen de coordenadas
    '''
    value = models.CharField(u'Variable', max_length = 150)
    enable = models.BooleanField(u'Enabled', default = True)
    
    def __unicode__(self):
        return self.value

# Cartografía base

class inidcardatg(inicartogra):
    '''
    Cartografía base.
    Datos generales
    '''
    escala = u'Escala de salida'
    numero = u'Identificación'
    respon = u'Responsable de la cartografía'
    cubrim = u'Cubrimiento geográfico de la cartografía'
    esccap = u'Escala de captura'
    #help_text
    escala_help = u'Escala de presentación de la cartografía'
    numero_help = u'Número de las planchas IGAC. '
    respon_help = u'Entidad que desarrolló la cartografía: \
        IGAC, Invías, Corporación, Alcaldía, etc.'
    cubrim_help = u'Área de la catografía con la descripción de las \
        entidades territoriales y administrativas presentes como: \
        departamentos, municipios y veredas, entre otros.'
    
    lists = SelectList()

    icartess = models.ForeignKey('cartgridsca', verbose_name = escala, #PositiveIntegerField(escala, 
        related_name = '%(app_label)s_%(class)s_icartess',
        help_text = escala_help)
        #choices = lists.ScaleChoose(),
        #default = lists.DefaultScale(), help_text = escala_help)
    icartnum = models.CharField(numero, max_length = 8,
        help_text = numero_help)
    icartres = models.CharField(respon, max_length = 125,
        help_text = respon_help)
    icartcug = models.CharField(cubrim, max_length = 500,
        help_text = cubrim_help)
    icartesc = models.ForeignKey('cartgridsca', verbose_name =esccap, #PositiveIntegerField(esccap, 
        related_name = '%(app_label)s_%(class)s_icartesc',
        null = True, blank = True)
        #choices = lists.ScaleChoose(),
        #default = lists.DefaultScale(), null = True, blank = True)

    def __unicode__(self):
        return '%s, %s, %s' % (self.incaraut, self.incacuba, self.icartess) 

    class Meta:
        verbose_name = u'01 Cartografía base'
        verbose_name_plural = verbose_name
   
class inicartdatf(models.Model):
    '''
    Cartografía base
    Datos generales - Fuentes y fecha'
    Utilizado como fuente de información para la cartografía IGAC
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
        verbose_name_plural = '01.1 Fuentes y Fechas'

class inicartscat(inicartsubt):
    '''
    Cartografía base
    Subtema cartográfico
    Catastro
    '''
    ##presen_help = u'Presencia de elementos que hacen parte del tema\
    ##    Catastro del catálogo de objetos?'
    ##cuapre_help = u'Especifique cuales. Ej. <br />ÁREAS CATASTRALES: <br />\
    ##    Manzanas, predios. <br />EDIFICACIONES y OBRAS CIVILES: <br />\
    ##    construcciones, áreas deportivas, cercas, sitios de interés, \
    ##    canteras, etc'
    ##qualit_help = u'En la tabla de atributos. <br />\
    ##    Coherencia de la información con respecto a rasgos \
    ##    característicos de la zona demarcada. Es decir, se verifica que \
    ##    existan elementos del tema Catastro conocidos en el área de \
    ##    cubrimiento de la plancha.'

    class Meta:
        verbose_name = u'01.2.1 Subtema. Catastro'
        verbose_name_plural = verbose_name
        proxy = True

class inicartstra(inicartsubt):
    '''
    Cartografía base
    Subtema cartográfico
    Transporte
    '''
    ## Help_text
    ##presen_help = u'Presencia de elementos que hacen parte del tema \
    ##    Transporte del catálogo de objectos?'
    ##cuapre_help = u'Especifique cuales. Ej. <br />TRANSPORTE TERRESTRE: <br />\
    ##    vía principal, vía secundaria, vía terciaria, camino, carreteable, \
    ##    ferrocaril, etc.\
    ##    <br />INSTALACIONES y CONSTRUCCIONES:<br />\
    ##    puentes, líneas de alta tensión, poliducto, torres de alta tensión, \
    ##    etc.'
    ##qualit_help = u'En la tabla de atributos. <br />\
    ##    Coherencia de la información con respecto a rasgos \
    ##    característicos de la zona demarcada. Es decir, se verifica que \
    ##    existan elementos del tema Transporte conocidos en el área de \
    ##    cubrimiento de la plancha.'

    class Meta:
        verbose_name = u'01.2.2 Subtema. Transporte'
        verbose_name_plural = verbose_name
        proxy = True

class inicartshdr(inicartsubt):
    '''
    Cartografía base
    Subtema cartográfico
    Hidrografía
    '''
    class Meta:
        verbose_name = u'01.2.3 Subtema. Hidrografía'
        verbose_name_plural = verbose_name
        proxy = True

class inicartsrlv(inicartsubt):
    '''
    Cartografía base
    Subtema cartográfico
    Relieve
    '''
    class Meta:
        verbose_name = u'01.2.4 Subtema. Relieve'
        verbose_name_plural = verbose_name
        proxy = True

class inicartsete(inicartsubt):
    '''
    Cartografía base
    Subtema cartográfico
    Entidad Territorial'
    '''
    class Meta:
        verbose_name = u'01.2.5 Subtema. Entidad Territorial'
        verbose_name_plural = verbose_name
        proxy = True

#Imágenes

class inidimagsat(inicartogra):
    '''
    Imágenes
    Imágenes de satélite
    '''
    nombre = u'Nombre de la imagen'
    sensor = u'Sensor / Satélite'
    seotro = u'Cuál?'
    fechai = u'Fecha y hora de la imágen'
    cubrim = u'Cubrimiento geográfico de la imagen'
    banpae = u'¿Tiene banda pancromática?'
    banpac = u'Especique cuales'
    banmul = u'Bandas multiespectrales'
    resolu = u'Resolución espacial'
    cosuix = u'Coordenadas esquina superior izquierda. X'
    cosuiy = u'Coordenadas esquina superior izquierda. Y'
    coindx = u'Coordenadas esquina inferior derecha. X'
    coindy = u'Coordenadas esquina inferior derecha. Y'
    pornub = u'Porcentaje de nubosidad'
    # Help_text
    cubrim_help = u'Área de la imágen con la descripción de las entidades \
        territoriales y administrativas presentes como: departamentos, \
        municipio, veredas, entre otros'
    banmul_help = u'Identificar las bandas multiespectrales con que cuenta \
        la imágen. Ej: Azul, rojo, verde, infrarrojo, etc'
    resolu_help = u'El tamaño de los pixeles'
    cosuix_help = u'Límite superior en las coordenadas disponibles'
    coindx_help = u'Límite inferior en las coordenadas disponibles'
    pornub_help = u'Expresado en términos de hectáreas con respecto al \
        total de las imágenes'

    lists = SelectList()

    iimanomb = models.CharField(nombre, max_length = 125)
    iimasens = models.ForeignKey('inimagsenso', verbose_name = sensor) #CharField(sensor, max_length = 10, 
        #choices = lists.SensChoose())
    iimaseno = models.CharField(seotro, max_length = 25, null = True,
        blank = True)
    iimadate = models.DateTimeField(fechai)
    iimacubr = models.FloatField(cubrim, null = True, blank = True, 
        help_text = cubrim_help)
    iimabanp = models.BooleanField(banpae, choices = lists.BoolChoose(), 
        default = False)
    iimabanc = models.CharField(banpac, max_length = 500, null = True, 
        blank = True)
    iimabanm = models.CharField(banmul, max_length = 300, null = True,
        blank = True, help_text = banmul_help)
    iimarese = models.CharField(resolu, max_length = 50,
        help_text = resolu_help)
    iimacsix = models.FloatField(cosuix, null = True, blank = True,
        help_text = cosuix_help)
    iimacsiy = models.FloatField(cosuiy, null = True, blank = True)
    iimacidx = models.FloatField(coindx, null = True, blank = True,
        help_text = coindx_help)
    iimacidy = models.FloatField(coindy, null = True, blank = True)
    iimanubp = models.FloatField(pornub, null = True, blank = True,
        help_text = pornub_help)

    class Meta:
        verbose_name = u'02 Imagen'
        verbose_name = u'02 Imágenes'

#Fotografías
class inidfotogra(inicartogra):
    '''
    Fotografías
    Fotografías. Áreas
    '''
    nombre = u'Nombre de la fotografía'
    numsob = u'Número de sobre'
    escala = u'Escala de las fotografías aéreas'
    tipoca = u'Tipo de cámara'
    altvue = u'Altura del vuelo'
    punfot = u'Puntos de fotocontrol'
    pornub = u'Porcentaje de nubosidad'
    # Help_text
    pornub_help = u'Expresado en términos de hectáreas con respecto al \
        total de las imágenes'

    lists = SelectList()

    ifonombr = models.CharField(nombre, max_length = 125)
    ifonumes = models.CharField(numsob, max_length = 50)
    ifoescaf = models.ForeignKey('cartgridsca', verbose_name = escala) #PositiveIntegerField(escala, 
        #choices = lists.ScaleChoose(),
        #default = lists.DefaultScale())
    ifotipoc = models.CharField(tipoca, max_length = 25, null = True,
        blank = True)
    ifoaltvu = models.FloatField(altvue, null = True, blank = True)
    ifopunfo = models.BooleanField(punfot, choices = lists.BoolChoose(), 
        default = False)
    ifoanubp = models.FloatField(pornub, help_text = pornub_help)

    class Meta:
        verbose_name = u'03 Fotografía'
        verbose_name_plural = u'03 Fotografías'

class mapfileexte(models.Model):
    '''
    Componente cartográfico
    Extensión de los mapas
    '''
    value = models.CharField(u'Variable', max_length = 150)
    enable = models.BooleanField(u'Enabled', default = True)
    
    def __unicode__(self):
        return self.value

class extpictform(models.Model):
    '''
    Componente cartográfico
    Extensión de las fotografías
    '''
    value = models.CharField(u'Variable', max_length = 150)
    enable = models.BooleanField(u'Enabled', default = True)
    
    def __unicode__(self):
        return self.value

class cartgridsca(models.Model):
    '''
    Componente cartográfico
    Escala de las planchas
    '''
    value = models.CharField(u'Variable', max_length = 150)
    enable = models.BooleanField(u'Enabled', default = True)
    
    def __unicode__(self):
        return self.value

#Suelos

class inidsuestud(inididestud):
    '''
    Suelos
    Identificación del estudio
    '''
    class Meta:
        verbose_name = u'04 Estudio de suelos'
        verbose_name_plural = u'04 Estudios de suelos'
        proxy = True

class inidsumegeo(models.Model):
    '''
    Suelos
    Metodología utilizada para el estudio de Geomorfología
    '''
    metodo = u'Metodología utilizada para determinar las unidades \
        geomorfológicas'
    clasif = u'¿La clasificación de las unidades geomorfológicas \
        expresan las características y ambientes morfogenéticos o \
        morfogénicos?'
    observ = u'Obervaciones'
    proces = u'¿En el análisis geomorfológico se identifican los \
        procesos morfodinámicos existentes en la cuenca?'
    amenaz = u'¿Se plantean relaciones de geomorfología con amenazas \
        naturales?'
    amenti = u'¿Qué tipo de amenazas de asocian?'
    amenot = u'Otra'
    #Help Text
    metodo_help = u'Especificar la metogología utilizada para realizar \
        el levanteamiento de unidades geomorfológicas - Nivel de escala \
        utilizado para el levantamiento de suelos'
    proces_help = u'Aplica para estudios recientes'
    amenaz_help = u'Ej. Movimientos en masa, inundaciones, flujos \
        torrenciales, otros'
    
    lists = SelectList()

    geoindic = models.OneToOneField('inidsuestud', 
        verbose_name=u'Caracterización general')
    geometod = models.CharField(metodo, max_length = 500,
        help_text = metodo_help)
    geoclasi = models.BooleanField(clasif, choices = lists.BoolChoose(), 
        default = False)
    geoclaso = models.CharField(observ, max_length = 500, 
        null = True, blank = True)
    geoproce = models.BooleanField(proces, choices = lists.BoolChoose(), 
        default = False, help_text = proces_help)
    geoproco = models.CharField(observ, max_length = 500, 
        null = True, blank = True)
    geoamena = models.BooleanField(amenaz, choices = lists.BoolChoose(), 
        default = False, help_text = amenaz_help)
    geoament = models.ManyToManyField('inidsumegea', verbose_name = amenti, 
        null = True, blank = True)
    geoameno = models.CharField(amenot, max_length = 500, 
        null = True, blank = True)
    
    def __unicode__(self):
        return self.geometod

    class Meta:
        verbose_name = u'04.1 Metodología Geomorfología'
        verbose_name_plural = verbose_name 

class inidsumegea(models.Model):
    '''
    Suelos
    Metodología utilizada para el estudio de Geomorfología
    Lista de selección múltiple para la pregunta geoament
    '''
    tipoamen = models.CharField(u'Tipo amenaza', max_length = 75)

    def __unicode__(self):
        return self.tipoamen

    class meta:
        verbose_name = u'Tipo de amenaza'
        verbose_name_plural = verbose_name

class inidsumesue(models.Model):
    '''
    Suelos
    Metodología utilizada para el estudio de suelos y/o capacidad
        de uso de la tierra
    '''
    leyend = u'¿Existe leyenda de suelos?' 
    observ = u'Obervaciones'
    metodo = u'Metodología utilizada para determinar las unidades cartográficas'
    labres = u'¿Se cuenta los resultados del laboratorio de suelos?'
    labora = u'Laboratorio'
    labori = u'Número de identificación'
    georef = u'¿El documento tiene la ubicación georeferenciada de las \
        observaciones de suelos?'
    # Help Text
    leyend_help = u'Compuesta por los siguientes temas: \
        clima, geología, pendientes, geomorfología, suelos, capacidad de uso.'
    metodo_help = u'Unidades de suelos. \r\n Aclarar si el estudio tuvo \
        trabajo de campo y detalle taxonómico a nivel de familia'
    labori_help = u'Ej. 123456789-0'

    lists = SelectList()

    tierindi = models.OneToOneField('inidsuestud', 
        verbose_name=u'Caracterización general')
    inisutle = models.BooleanField(leyend, choices = lists.BoolChoose(), 
        default = False, help_text = leyend_help) 
    inisutlo = models.CharField(observ, max_length = 500, 
        null = True, blank = True)
    inisutme = models.CharField(metodo, max_length = 500, 
        help_text = metodo_help) 
    inisutla = models.BooleanField(labres, choices = lists.BoolChoose(), 
        default = False) 
    inisutln = models.CharField(labora, max_length = 150, 
        null = True, blank = True)
    inisutli = models.CharField(labori, max_length = 15, 
        null = True, blank = True, help_text = labori_help)
    inisutge = models.BooleanField(georef, choices = lists.BoolChoose(), 
        default = False) 

    class Meta:
        verbose_name = u'04.2 Metodología uso de tierra'
        verbose_name_plural = verbose_name

class inidsuinfor(inidcartog):
    '''
    Suelos
    Información general cartográfica y documentos técnicos
    '''

    class Meta:
        verbose_name = u'04.3 Información cartográfica'
        verbose_name_plural = verbose_name 
        proxy = True
    
#Hidrología

class inidhlestud(inididestud):
    '''
    Hidrología
    Identificación del estudio
    '''
    class Meta:
        verbose_name = u'05 Estudio hidrológico'
        verbose_name_plural = u'05 Estudios hidrológicos'
        proxy = True

class inidhlmetod(models.Model):
    '''
    Hidrología
    Metodología utilizada para el estudio de Hidrología o Climatología
    '''
    promet = u'Procedimiento utilizado para la evaluación de los \
        parámetros meteorológicos y el cálculo de índices ERA'
    prohdr = u'Procedimiento utilizado para la evaluación de los \
        parámetros hidrológicos y cálculo de oferta, demanda e \
        indicadores ERA'
    infcal = u'¿Cuenta con información de entrada para los cálculos?'
    infcad = u'Describa la información de entrada para los cálculos'
    calibr = u'¿En las modelaciones existentes se realizaron las \
        calibraciones y validaciones necesarias?'
    procal = u'Describa brevemente el procedimiento utilizado para la \
        calibración'
    # Help text 
    infcad = u'Datos de origen para las metodologías'
    
    lists = SelectList()
 
    inihidme = models.OneToOneField('inidhlestud')
    inihlppa = models.CharField(promet, max_length = 500)
    inihlphd = models.CharField(prohdr, max_length = 500)
    inihlmin = models.BooleanField(infcal, choices = lists.BoolChoose(), 
        default = False)
    inihlpid = models.CharField(infcad, max_length = 500, null = True, 
        blank = True)
    inihlcal = models.BooleanField(calibr, choices = lists.BoolChoose(), 
        default = False)
    inihlcad = models.CharField(procal, max_length = 500, null = True, 
        blank = True)
    
    class Meta:
        verbose_name = u'05.1 Metodología hidro/climatología'
        verbose_name_plural = verbose_name 

class ihlmethaest(models.Model):
    '''
    Hidrología
    Metodología - Estaciones
    Estaciones utilizadas dentro del estudio
    '''
    nombre = u'Nombre de la estación'
    codigo = u'Código de la estación'
    perioi = u'Año de inicio del periodo de las series históricas'
    periof = u'Año de fin del periodo de las series históricas'
    escate = u'Escala temporal'
    # Help text
    nombre_help = u'Según el catálogo del IDEAM'
    codigo_help = nombre_help
    perioi_help = u'De las variables hidrológicas y meteorológicas'
    
    lists = SelectList()

    ihlmetod = models.ForeignKey(inidhlmetod, verbose_name = u'Metodología')
    ihlmeesn = models.CharField(nombre, max_length = 25, 
        help_text = nombre_help)
    ihlmeesc = models.CharField(codigo, max_length = 10,
        help_text = codigo_help)
    ihlmeesi = models.PositiveSmallIntegerField(perioi, 
        choices = lists.YearList(), default = lists.ThisYear())
    ihlmeesf = models.PositiveSmallIntegerField(periof, 
        choices = lists.YearList(), default = lists.ThisYear())
    ihlmeese = models.ForeignKey('hlmetimesca', verbose_name = escate) #CharField(escate, max_length = 2, 
        #choices = lists.EscTempChoose())

    class Meta:
        verbose_name = u'05.1.1 Estación dentro del estudio'
        verbose_name_plural = u'Estaciones dentro del estudio'
    
class ihlmethafor(models.Model):
    '''
    Hidrología
    Metodología - Aforos
    Aforo: Medición del caudal
    '''
    period = u'Periodo de la medición' 
    caperi = u'Fecha de aforo'
    caudal = u'Valor del caudal'
    nivel  = u'Valor del nivel de agua'
    subcue = u'Subcuenca'
    sector = u'Sector'

    lists = SelectList()
 
    inihlmma = models.ForeignKey('inidhlmetod')
    inihlmpe = models.ForeignKey('hdlaforperi', verbose_name = period) #CharField(period, max_length = 4, 
        #choices = lists.PeriAforChoose())
    inihlmmp = models.FloatField(caperi, null = True, blank = True)
    inihlmca = models.FloatField(caudal, null = True, blank = True)
    inihlmni = models.FloatField(nivel, null = True, blank = True)
    inihlmsc = models.CharField(subcue, max_length = 250)
    inihlmse = models.CharField(sector, max_length = 250, 
        null = True, blank = True)

    class Meta:
        verbose_name = u'05.1.2 Información de aforos'
        verbose_name_plural = verbose_name

class hlmetimesca(models.Model):
    '''
    Hidrología
    Escala temporal
    '''
    value = models.CharField(u'Variable', max_length = 150)
    enable = models.BooleanField(u'Enabled', default = True)
    
    def __unicode__(self):
        return self.value

class hdlaforperi(models.Model):
    '''
    Hidrología
    Periodo de la medición del aforo
    '''
    value = models.CharField(u'Variable', max_length = 150)
    enable = models.BooleanField(u'Enabled', default = True)
    
    def __unicode__(self):
        return self.value

class inidhlcarto(inidcartog):
    '''
    Hidrología
    información general  cartográfica y documento técnico
    '''

    class Meta:
        verbose_name = u'05.2 Información gener cartográfica'
        verbose_name_plural = verbose_name
        proxy = True

class inidhlvarib(inididestud):
    '''
    Hidrología.
    Información complementaria.
    Estudios de variabilidad climática (niño o niña) para la cuenca en estudio    
    '''
    class Meta:
        verbose_name = u'05.3.1 Estudio variab. climática'
        verbose_name_plural = verbose_name
        proxy = True

class inidhlcauda(inididestud):
    '''
    Hidrología.
    Información complementaria.
    Calculos de caudal ambiental
    '''
    class Meta:
        verbose_name = u'05.3.2 Cálculo de caudal ambiental'
        verbose_name_plural = verbose_name
        proxy = True

#Hidrogeología

class inidhgestud(inididestud):
    '''
    Hidrogeología
    Identificación del estudio
    '''
    class Meta:
        verbose_name = u'06 Estudio hidrogeológico'
        verbose_name_plural = u'06 Estudios hidrogeológicos'
        proxy = True

class inighgmetfa(models.Model):
    '''
    Hidrogeología
    Metodología utilizada para el estudio
    Fases que contempló el estudio
    '''

    lists = SelectList()

    esthidrg = models.ForeignKey('inidhgestud', 
        verbose_name = u'Estudio de hidrogeología')
    fasesest = models.ForeignKey('inhdrefases', 
        verbose_name = u'Fase que contempló el estudio') #CharField(u'Fase que contempló el estudio', 
        #max_length = 5, choices = lists.HdrFaseChoose())  
    metodolo = models.CharField(u'Metodología usada en la fase', 
        max_length = 500, null = True, blank = True)
    class Meta:
        verbose_name = u'Fase del estudio'
        verbose_name_plural = u'Fases del estudio'
        
class inhdrefases(models.Model):
    '''
    Hidrogeología
    Fases que contempló el estudio
    '''
    value = models.CharField(u'Variable', max_length = 150)
    enable = models.BooleanField(u'Enabled', default = True)
    
    def __unicode__(self):
        return self.value

class inidhgmetho(models.Model):
    '''
    Hidrogeología
    Metodología utilizada para el estudio
    '''
    dbpunag = u'¿Existe base de datos de inventario de puntos de agua?'
    dbpaubi = u'Ubicación de la base de datos'
    dbpaatr = u'Atributos de la base de datos'
    dbpaaci = u'¿Están identificados los acuíferos asociados a estos\
        puntos de agua?'
    dbpaacp = u'Porcentaje de puntos asociados al acuífero'
    quality = u'¿Existen análisis de calidad?'
    qualiye = u'Año de inicio del monitorieo de calidad'
    qualinc = u'Número de campañas de muestreo al año'
    qualipa = u'Parámetros evaluados en el análisis de calidad'
    balehgq = u'Se realizó balance de error de los análisis hidrogeoquímicos?'
    balehqp = u'Indicar el porcentaje de error obtenido al realizar el balance'
    laboacr = u'El laboratorio que realizó los análisis está acreditado en \
        los parámetros analizados?'
    labonom = u'Nombre del laboratorio'
    labonit = u'Número de identificación'
    geoestu = u'¿Se realizaron estudios geofísicos y geolectricos?'
    geosond = u'Número de sondeos'
    geometo = u'Metodología utilizada'
    acuigeo = u'¿Tiene determinado la geometría del acuífero?'
    acuiesp = u'Espesor'
    acuirec = u'Recursos'
    acuires = u'Rerservas'
    carhidr = u'Existen caracterizaciones hidráulicas de los acuífeos'
    cahimet = u'Explique la metodología utilizada en la caracterización \
        hidráulica de los acuíferos'
    cahipar = u'Indique los parámetros obtenidos en las pruebas de bombeo'
    riescon = u'¿El estudio evaluó el riesgo a la contaminación?'
    cargcon = u'¿Se evaluó la carga contaminante asociada al acuífero?'
    vulneaq = u'¿El estudio evaluó la vulnerabilidad de los acuíferos?'
    vulneme = u'Explique la metodología'
    vulnepr = u'Método y procedimiento de evaluación'
    modhdrc = u'¿Existe un modelo hidrogeológico conceptual?'
    modhdin = u'Información relevante sobre el modelo'
    acuiana = u'Tipo de acuífero analizado en el estudio'
    aguasub = u'¿Está identificada la cantidad de puntos de agua subterránea?'
    agsubnp = u'Número de puntos'
    agsucon = u'¿Están identificadas las concesiones de agua subterránea?'
    agsucnu = u'Número de concesiones' 
    modmate = u'Existe un modelos matemático?'
    modmato = u'Otro'
    # Help text
    labonit_help = u'Ej. 123456789-0' 

    lists = SelectList()

    inihidge = models.OneToOneField('inidhgestud')
    inhgdbpa = models.BooleanField(dbpunag,choices = lists.BoolChoose(), 
        default = False)
    inhgdbpu = models.CharField(dbpaubi, max_length = 150, 
        null = True, blank = True)
    inhgdbat = models.CharField(dbpaatr, max_length = 150, 
        null = True, blank = True)
    inhgdbac = models.NullBooleanField(dbpaaci, choices = lists.BoolChoose(), 
        default = False, null = True, blank = True)
    inhgdbpa = models.FloatField(dbpaacp, null = True, blank = True)
    inhgqual = models.BooleanField(dbpunag, choices = lists.BoolChoose(), 
        default = False)
    inhgquye = models.PositiveSmallIntegerField(qualiye, 
        choices = lists.YearList(), default = lists.ThisYear(),
        null = True, blank = True)
    inhgqunc = models.PositiveSmallIntegerField(qualinc, 
        null = True, blank = True)
    inhgqupa = models.CharField(qualipa, max_length = 500, 
        null = True, blank = True)
    inhgceah = models.BooleanField(balehgq, choices = lists.BoolChoose(), 
        default = False)
    inhgahpo = models.FloatField(balehqp, null = True, blank = True)
    inhglaba = models.BooleanField(laboacr, choices = lists.BoolChoose(), 
        default = False)
    inhglabn = models.CharField(labonom, max_length =150,
        null = True, blank = True)
    inhglabi = models.CharField(labonit, max_length = 15, 
        null = True, blank = True, help_text = labonit_help)
    inghesgg = models.BooleanField(geoestu, choices = lists.BoolChoose(), 
        default = False)
    inhgeggn = models.PositiveSmallIntegerField(geosond, 
        null = True, blank = True)
    inghegme = models.CharField(geometo, max_length = 500, 
        null = True, blank = True)
    inghacui = models.BooleanField(acuigeo, choices = lists.BoolChoose(), 
        default = False)
    inghaces = models.FloatField(acuiesp, null = True, blank = True)
    inghacre = models.FloatField(acuirec, null = True, blank = True)
    inghacrs = models.FloatField(acuires, null = True, blank = True)
    inghchdr = models.BooleanField(carhidr , choices = lists.BoolChoose(), 
        default = False)
    inghchme = models.CharField(cahimet, max_length = 500,   
        null = True, blank = True)
    inghchpo = models.CharField(cahipar, max_length = 500,
        null = True, blank = True)
    inghries = models.BooleanField(riescon, choices = lists.BoolChoose(), 
        default = False)
    inghcaco = models.BooleanField(cargcon, choices = lists.BoolChoose(), 
        default = False)
    inghvuln = models.BooleanField(vulneaq, choices = lists.BoolChoose(), 
        default = False)
    inghvume = models.CharField(vulneme, max_length = 500,   
        null = True, blank = True)
    inghcupr = models.CharField(vulnepr, max_length = 500,   
        null = True, blank = True)
    inghmhco = models.BooleanField(modhdrc, choices = lists.BoolChoose(), 
        default = False)
    inghmhci = models.CharField(modhdin, max_length = 500,   
        null = True, blank = True)
    inghtacu = models.ForeignKey('inhdrmeacui', verbose_name = acuiana, #CharField(acuiana, max_length = 5, 
        null = True, blank = True)
        #choices = lists.HdrAcuifChoose(), null = True, blank = True)
    inghagsu = models.BooleanField(aguasub, choices = lists.BoolChoose(), 
        default = False)
    inghasnp = models.PositiveSmallIntegerField(agsubnp, 
        null = True, blank = True)
    inghasco = models.NullBooleanField(agsucon, choices = lists.BoolChoose(), 
        default = False, null = True, blank = True)
    inghmoma = models.ManyToManyField('inidhgmmoma', verbose_name = modmate, 
        null = True, blank = True)
    inghmomo = models.CharField(modmato, max_length = 25, 
        null = True, blank = True)

    class Meta:
        verbose_name = u'06.1 Metodología utilizada'
        verbose_name_plural = u'06.1 Metodologías utilizadas'

class inhdrmeacui(models.Model):
    '''
    Hidrogeología
    Tipo de acuifero analizado
    '''
    value = models.CharField(u'Variable', max_length = 150)
    enable = models.BooleanField(u'Enabled', default = True)
    
    def __unicode__(self):
        return self.value

class inidhgmmoma(models.Model):
    '''
    Hidrogeología
    Metodología.
    Modelos matemáticos
    '''
    modelo = models.CharField('Nombre del modelo matemático', max_length = 50)

    def __unicode__(self):
        return self.modelo

    class Meta:
        verbose_name = u'Modelo matemático'
        verbose_name_plural = verbose_name
    
class inidhgcarto(inidcartog):
    '''
    Hidrogeología
    Información general cartográfica y documento técnico
    '''

    class Meta:
        verbose_name = u'06.2 Información gen cartográfica'
        verbose_name_plural = verbose_name
        proxy = True

#Calidad de Agua

class inidcaestud(inididestud):
    '''
    Calidad de Agua
    Identificación del estudio
    '''
    class Meta:
        verbose_name = u'07 Estudio Calidad de agua'
        verbose_name_plural = u'07 Estudios Calidad de agua'
        proxy = True

class inidcameth(models.Model):
    '''
    Calidad de Agua
    Metodología del estudio
    '''
    objeto = u'Objeto del estudio'
    metodo = u'Metodología utilizada para muestreos'
    estaci = u'Número de estaciones de la Red de monitoreo del recurso hídrico'
    numeca = u'Numero de Campañas de muestreo'
    camani = u'Año desde que se realizan las campañas de muestreo'
    icaexi = u'¿Se han realizado cálculos para el Índice de Calidad de Agua \
        - (ICA)?'
    icatra = u'ICA. Tramos o corrientes a los cuales se ha realizado cálculos'
    icamap = u'ICA. Existen mapas de ICA?'
    icames = u'ICA. Escala de salida de los mapas'
    icamfo = u'ICA. Formato de mapas'
    icamex = u'ICA. Extensión de los mapas'
    icameo = u'ICA. Otra'
    #Help Text
    metodo_help = u'Aclarar si los muestreos fueron compuestos o simples'

    lists = SelectList()

    inidcala = models.OneToOneField('inidcaestud')
    inicaobj = models.CharField(objeto, max_length = 500)
    inicamet = models.CharField(metodo, max_length = 500, 
        help_text = metodo_help)
    inicaest = models.PositiveSmallIntegerField(estaci, null = True, 
        blank = True)
    inicacan = models.PositiveSmallIntegerField(numeca, null = True, 
        blank = True)
    inicacaa = models.PositiveSmallIntegerField(camani, 
        choices = lists.YearList(), null = True, blank = True)
    inicaiex = models.BooleanField(icaexi, choices = lists.BoolChoose(), 
        default = False)
    inicaitr = models.CharField(icatra, max_length = 250,
        null = True, blank = True)
    inicaima = models.NullBooleanField(icamap, choices = lists.BoolChoose(), 
        default = False, null = True, blank = True)
    inicaime = models.PositiveIntegerField(icames, null = True,
        blank = True)
    inicaimf = models.ForeignKey('documformat', verbose_name = icamfo, #CharField(icamfo, max_length = 4,
        null = True, blank = True)
        #choices = lists.FormatChoose(), blank = True, null = True)
    inicaimx = models.ForeignKey('mapfileexte', verbose_name = icamex, #CharField(icamex, max_length = 9,
        null = True, blank = True)
        #choices = lists.MapExtChoose(), null = True, blank = True)
    inicaixo = models.CharField(icameo, max_length = 25,
        null = True, blank = True)

    class Meta:
        verbose_name = u'07.1 Metodología del estudio'
        verbose_name_plural = verbose_name
    
class inidcamecam(models.Model):
    '''
    Calidad de Agua
    Metodología - Número de campañas de muestreo
    '''

    lists = SelectList()

    icalamet = models.ForeignKey('inidcameth', verbose_name = u'Metodología')
    icamcano = models.IntegerField(u'Año', choices = lists.YearList())
    icamcper = models.CharField(u'Periodo', max_length = 25)
    
    class Meta:
        verbose_name = u'07.1.1 Campaña de muestreo'
        verbose_name_plural = u'07.1.1 Campañas de muestreo'
    
class inicainfoes(models.Model):
    '''
    Calidad de Agua
    Información que debe contener el estudio
    '''
    inform = u'Informes y resultados de laboratorios acreditados por el IDEAM \
        para los parámetros muestreados.'
    aforac = '¿Los aforos en la subcuenca, tramos y/o corrientes principales \
        fueron realizados según protocolos acreditados por el IDEAM?'
    estaci = u'¿Se encuentran georeferenciadas las estaciones de muestreo en \
        la red de monitoreo?'
    observ = u'Observaciones generales del informe de laboratorio'
    parame = u'Parámetros Fisicoquímicos mínimos muestreados en las \
        fuentes de agua superficial'
    paraot = u'Otros parámetros'

    lists = SelectList()

    iicainfo = models.OneToOneField('inidcaestud', 
        verbose_name = u'Estudio de Calidad de Agua')
    iicaiinf = models.CharField(inform, max_length = 500)
    iicaiafa = models.BooleanField(aforac, choices = lists.BoolChoose(), 
        default = False)
    iicaiest = models.NullBooleanField(estaci, choices = lists.BoolChoose(), 
        default = False, null = True, blank = True)
    iicaiobs = models.CharField(observ, max_length = 500, null = True, 
        blank = True)
    iicaipar = models.ManyToManyField('incainfpara', verbose_name = parame,
        null = True, blank = True)
    iicaipao = models.CharField(paraot, max_length = 70, null = True,
        blank = True)
    
    class Meta:
        verbose_name = '07.2 Información del estudio'
        verbose_name_plural = verbose_name

class inicainflab(models.Model):
    '''
    Calidad de Agua.
    Información del estudio
    Laboratorios acreditados por el IDEAM
    '''
    estudi = models.ForeignKey('inicainfoes', verbose_name = u'Estudio')
    labora = models.CharField(u'Nombre del laboratorio acreditado por \
        el IDEAM', max_length = 150)
    identi = models.CharField(u'NIT', max_length = 25,
        help_text = 'Ej. 123456789-0')

    class Meta:
        verbose_name = u'Laboratorio acreditado'
        verbose_name_plural = u'Laboratorios acreditados' 
    
class inicainfgeo(inidgeorefe):
    '''
    Calidad de agua
    Información - Georreferenciación de estaciones de muestreo de la red de 
    monitoreo
    '''
    iicaigeo = models.ForeignKey('inicainfoes')
    
    class Meta: 
        verbose_name = u'07.2.2 Estación de muestreo'
        verbose_name_plural = verbose_name

class incainfpara(models.Model):
    '''
    Calidad de Agua.
    Información del estudio
    Parámetros Fisicoquímicos 
    '''
    variab = models.CharField('Parámetro', max_length = 50)
    expres = models.CharField('Expresión', max_length = 20)
    
    def __unicode__(self):
        return '%s---%s' %(self.variab, self.expres)
    class Meta:
        verbose_name = u'Parámetro Fisicoquímicos'
        verbose_name_plural = verbose_name

class inicainfoco(models.Model):
    '''
    Calidad de agua
    Información complementaria
    '''
    estudio = u'Estudio de Calidad de Agua'
    qualobj = u'¿Existen objetivos de calidad de las corrientes?'
    capasim = u'¿Existen estudios de capacidad de asimilación o modelaciones?'
    capayea = u'Año de los estudios de capacidad de asimilación o modelaciones'
    # Help text
    capayea_help = u'Ingrese los valores sin puntos y separados por comas \n \
        Ej. 1999, 2009, 2013'

    lists = SelectList()

    iicainfc = models.OneToOneField('inidcaestud', verbose_name = estudio)
    iicaifoc = models.BooleanField(qualobj,
        choices = lists.BoolChoose(), default = False)
    iicaifca = models.BooleanField(capasim,
        choices = lists.BoolChoose(), default = False)
    #iicaincy = models.CharField(capayea, max_length = 150, 
    #    help_text = capayea_help, null = True, blank = True)
    
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

    lists = SelectList()
    
    iicaicom = models.ForeignKey(u'inicainfoco', 
        verbose_name = u'Información complementaria')
    iicaicap = models.PositiveSmallIntegerField(capano, choices = lists.YearList())
    
    class Meta:
        verbose_name = u'07.3.1 Estudio de capac. de asimilación'   
        verbose_name = u'07.3.1 Estudios de capac de asimilación'   
    
#Cargas Contaminantes

class inidccestud(inididestud):
    '''
    Cargas Contaminantes
    Identificación del estudio
    '''

    class Meta:
        verbose_name = u'08 Estudio Cargas contaminantes'
        verbose_name_plural = u'08 Estudios Cargas contaminantes'
        proxy = True

class inidccmetho(models.Model):
    '''
    Cargas Contaminantes
    Metodologíadel estudio, levantamiento de datos y resultados
    '''
    objeto = u'Objeto del estudio'
    metodo = u'Metodología utilizada para la estimación de cargas \
        contaminantes de DBO y SST'
    estima = u'La estimación de cargas contaminantes se realizó:'
    lineab = u'¿La línea Base de carga contaminante de DBO y SST se \
        calculó para la zona rural y/o centros poblados?'
    concen = u'¿Se contemplan datos completos de concentraciones de \
        DBO (mg/l) y SST(mg/l) y Caudal(L/seg) en laboratorios \
        acreditados para éstos parámetros?'
    sumini = u'¿La fuente de muestreos de vertimientos de aguas \
        residuales, corresponden a los suministrados por los usuarios \
        de la Jurisdicción o han sido generados por la CAR?'
    invent = 'Si no existiera línea base de carga contaminante de DBO y SST \
        del último quinquenio, la corporación cuenta con:'
    carsec = u'¿Se discriminan las cargas contaminantes por sectores productivos?'
    # Help Text
    metodo_help = u'Aclarar si el cálculo de cargas contaminantes se realizó \
        de forma presuntiva o por caracterización de vertimientos'

    lists = SelectList()

    iiccmeth = models.OneToOneField('inidccestud')
    iiccmobj = models.CharField(objeto, max_length = 500)
    iiccmmet = models.CharField(metodo, max_length = 500, help_text = metodo_help)
    iiccmest = models.ForeignKey('incameestim', verbose_name = estima, #CharField(estima, max_length = 5, 
        null = True, blank = True) #, choices = lists.CacaEstiChoose())
    iiccmlin = models.ForeignKey('incamelineb', verbose_name = lineab) #CharField(lineab, max_length = 5,
        #choices = lists.CacaParaChoose(), default = False)
    iiccmdcc = models.BooleanField(concen, choices = lists.BoolChoose(), 
        default = False)  
    iiccmsum = models.ForeignKey('incamesourc', verbose_name = sumini, #CharField(sumini, max_length = 5,
        null = True, blank = True)  
        #choices = lists.CacaFuenChoose(), default = False,
    iiccminv = models.ForeignKey('incamequinq', verbose_name = invent, #CharField(invent, max_length = 4, 
        null = True, blank = True)  
        #choices = lists.CacaQuinChoose(), null = True, blank = True)
    iiccmsec = models.ForeignKey('incamediscr', verbose_name = carsec) #CharField(carsec, max_length = 4, 
        #choices = lists.CacaDiscChoose(), default = False)

    class Meta:
        verbose_name = '08.1 Metodología del estudio'
        verbose_name_plural = verbose_name

class incameestim(models.Model):
    '''
    Cargas Contaminantes
    Estimación de cargas contaminantes
    '''
    value = models.CharField(u'Variable', max_length = 150)
    enable = models.BooleanField(u'Enabled', default = True)
    
    def __unicode__(self):
        return self.value

class incamelineb(models.Model):
    '''
    Cargas Contaminantes
    Cálculo de La línea Base de carga contaminante de DBO y SST
    '''
    value = models.CharField(u'Variable', max_length = 150)
    enable = models.BooleanField(u'Enabled', default = True)
    
    def __unicode__(self):
        return self.value


class incamesourc(models.Model):
    '''
    Cargas Contaminantes
    La fuente de muestreos de vertimientos de aguas 
        residuales
    '''
    value = models.CharField(u'Variable', max_length = 150)
    enable = models.BooleanField(u'Enabled', default = True)
    
    def __unicode__(self):
        return self.value

class incamequinq(models.Model):
    '''
    Cargas Contaminantes
    La corporación cuenta con. En caso de disponer información
        del último quinquenio
    '''
    value = models.CharField(u'Variable', max_length = 150)
    enable = models.BooleanField(u'Enabled', default = True)
    
    def __unicode__(self):
        return self.value

class incamediscr(models.Model):
    '''
    Cargas Contaminantes
    Cargas contaminantes discriminadas por sectores productivos
    '''
    value = models.CharField(u'Variable', max_length = 150)
    enable = models.BooleanField(u'Enabled', default = True)
    
    def __unicode__(self):
        return self.value

class inidccminfe(models.Model):
    '''
    Cargas Contaminantes
    Información que debe contener el estudio
    '''
    inform = u'Informes y resultados de Laboratorios Acreditados por el IDEAM \
        para los parámetros muestreados'
    georef = u'¿Se encuentran georeferenciadas las estaciones de muestreo?'
    observ = u'Observaciones generales del Informe de Laboratorio'
    percen = u'Porcentaje (%) de remoción de carga contaminante de \
        DBO y SST de los Sistemas de Tratamiento de Aguas Residuales - \
        STAR disponibles para la cuenca'
    parame = u'Parámetros Fisicoquímicos mínimos muestreados en los \
        vertimientos de agua residual'
    paraot = u'Otros parámetros'

    lists = SelectList()
    
    iiccinfe = models.OneToOneField(u'inidccestud')
    iicciinf = models.BooleanField(inform, choices = lists.BoolChoose(),
        default = False)
    iiccigeo = models.NullBooleanField(georef, choices = lists.BoolChoose(),
        default = False, null = True, blank = True)
    iicciobs = models.CharField(observ, max_length = 500, blank = True,
        null = True)
    iicciper = models.FloatField(percen, null = True, blank = True)
    iiccipar = models.ManyToManyField('incainfpara', verbose_name = parame,
        null = True, blank = True)
    iiccipao = models.CharField(paraot, max_length = 70, blank = True,
        null = True)

    class Meta:
        verbose_name = u'08.2 Información del estudio'
        verbose_name_plural = verbose_name

class iniccinflab(models.Model):
    '''
    Cargas Contaminantes
    Información que debe contener el estudio
    Laboratorios acreditados por el IDEAM
    '''
    estudi = models.ForeignKey('inidccminfe', verbose_name = u'Estudio')
    labora = models.CharField(u'Nombre del laboratorio acreditado por \
        el IDEAM', max_length = 150)
    identi = models.CharField(u'NIT', max_length = 25,
        help_text = 'Ej. 123456789-0')

    class Meta:
        verbose_name = u'Laboratorio acreditado'
        verbose_name_plural = u'Laboratorios acreditados' 

    #Local field clashes with field of similar name from base class
    #estudi = models.ForeignKey('inidccminfe', verbose_name = u'Estudio')

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
    inverti = u'¿La CAR cuenta con sistema de administración para la \
        información de monitoreos de vertimientos en relación con la \
        calidad del recurso hídrico?'
    porhexi = u'¿Existe Plan de Ordenamiento del Recurso Hídrico?'
    secporh = u'Sector donde fue realizado el Plan de Ordenamiento de \
        Recurdo Hídrico'
    pueaaes = u'Estado de implementación de los Planes de Uso Eficiente y \
        Ahorro del Agua existentes a nivel de municipio o sector'
    pmaaexi = u'¿Existen Planes Maestros de Acueducto y Alcantarillado?'
    
    lists = SelectList()


    iiccicom = models.OneToOneField('inidccestud')
    iicccmue = models.BooleanField(muestre, choices = lists.BoolChoose(), 
        default = False)
    iicccper = models.FloatField(percent, null = True, blank = True)
    iicccprm = models.NullBooleanField(inverti, choices = lists.BoolChoose(),
        default = False)
    iicccpor = models.NullBooleanField(porhexi, choices = lists.BoolChoose(),
        default = False)
    iicccpse = models.CharField(secporh, max_length = 500, blank = True,
        null = True) 
    iicccpur = models.NullBooleanField(pueaaes, choices = lists.BoolChoose(),
        default = False)
    iicccpma = models.NullBooleanField(pmaaexi, choices = lists.BoolChoose(),
        default = False)
    
    class Meta:
        verbose_name = u'08.3 Información complementaria'
        verbose_name_plural = verbose_name

class iniccicomps(models.Model):
    '''
    Cargas contaminantes
    Información complementaria
    Municipios con PSMV
    '''
    munici = u'Municipio sobre la cuenca con PSMV'
    estado = u'Estado de implementación de los PSMV'

    estudio = models.ForeignKey('iniccicompl', 
        verbose_name = u'Información complementaria')
    munipio = models.CharField(munici, max_length = 30)
    estadoi = models.CharField(estado, max_length = 150)

    class Meta:
        verbose_name = u'Municipio con PSMV'
        verbose_name_plural = u'Municipios con PSMV'

class iniccicompu(models.Model):
    '''
    Cargas contaminantes
    Información complementaria
    Municipios con Planes de Uso Eficiente y Ahorro de Agua 
    '''
    munici = u'Municipio o sector productivo'
    estado = u'Estado de implementación de los Planes\
        de Uso Eficiente y Ahorro de Agua'

    estudio = models.ForeignKey('iniccicompl', 
        verbose_name = u'Información complementaria')
    munipio = models.CharField(munici, max_length = 30)
    estadoi = models.CharField(estado, max_length = 150)

    class Meta:
        verbose_name = u'Municipio con PUEyAA'
        verbose_name_plural = u'Municipios con PUEyAA'
    
#Cobertura de la tierra

class inidcoestud(inididestud):
    '''
    Cobertura de la tierra 
    Identificación del estudio
    '''
    class Meta:
        verbose_name = u'09 Cobertura de la tierra'
        verbose_name_plural = u'09 Coberturas de la tierra'
        proxy = True

class inidcometho(models.Model):
    '''
    Cobertura de la tierra 
    Metodología utilizada para levantamiento de coberturas'
    '''
    sensor = u'Tipo de sensores utilizados'
    sensoo = u'Otro'
    fotfor = u'Formato de las fotos'
    fotfoo = u'Otro'
    imgfor = u'Formato de las imágenes satelitales'
    imgfoo = fotfoo 
    fechai = u'Fecha de toma de la Imagen o fotografías utilizadas '
    nivley = u'Nivel de aplicación de la Leyenda' 
    interp = u'Método de interpretación utilizado'
    verifi = u'Verificación de campo'
    cartfu = u'Fuente de cartografía base'
    cartes = u'Escala de cartografía base'
    cartan = u'Año de cartografía base'
    # Help text
    interp_help = u'Supervisado'
    verifi_help = u'Época del año en que fue realizado'

    lists = SelectList()

    iicometh = models.OneToOneField('inidcoestud')
    iicomsen = models.ManyToManyField('inidcosenso', verbose_name = sensor) 
    iicomseo = models.CharField(sensoo, max_length = 25, null  = True,
        blank = True)
    iicomfot = models.ForeignKey('mapfileexte',verbose_name = fotfor, #CharField(fotfor, max_length = 9, 
        null= True, blank = True)
        #choices = lists.MapExtChoose(), null= True, blank = True)
    iicomfoo = models.CharField(fotfoo, max_length = 25, null  = True,
        blank = True)
    iicomimg = models.ForeignKey('inimagsenso', verbose_name = imgfor, #CharField(imgfor, max_length = 9,
        null= True, blank = True)
        #choices = lists.SensChoose(), null = True, blank = True)
    iicomimo = models.CharField(imgfoo, max_length = 25, null  = True,
        blank = True)
    iicomdat = models.PositiveSmallIntegerField(fechai, 
        choices = lists.YearList(), null = True, blank = True)
    iicomniv = models.CharField(nivley, max_length = 250, null = True, 
        blank = True)
    iicomint = models.ForeignKey('incomeinter', verbose_name = interp, #CharField(interp, max_length = 4, 
        null= True, blank = True,
        help_text = interp_help)
        #choices = lists.CobeMetoChoose(), null = True, blank = True,
    iicomver = models.CharField(verifi, max_length = 200, 
        null = True, blank = True, help_text = verifi_help)
    iicomcfu = models.CharField(cartfu, max_length = 75)
    iicomces = models.IntegerField(cartes)
    iicomcan = models.IntegerField(cartan, choices = lists.YearList(), 
        null = True, blank = True)

    class Meta:
        verbose_name = u'09.1 Metodología de levantamiento'
        verbose_name_plural = verbose_name

class incomeinter(models.Model):
    '''
    Coberturas de la tierra
    Método de interpretación utilizado
    '''
    value = models.CharField(u'Variable', max_length = 150)
    enable = models.BooleanField(u'Enabled', default = True)
    
    def __unicode__(self):
        return self.value

class inidcoinfog(inidcartog):
    '''
    Cobertura de la tierra 
    Información general cartográfica y documento técnico
    '''

    class Meta:
        verbose_name = '09.2 Información cartográfica'
        verbose_name_plural = verbose_name
        proxy = True

class inidcoanmul(models.Model):
    '''
    Cobertura de la tierra
    Análisis multitemporales'
    '''
    analis = u'¿El estudio es un análisis multitemporal?'
    period = u'Periodo del estudio'
    metodo = u'Metodología utilizada'
    escala = u'Escala'

    lists = SelectList()

    cobertur = models.OneToOneField('inidcoestud')
    mulanali = models.BooleanField(analis, choices = lists.BoolChoose(),
        default = False)
    mulperio = models.CharField(period, max_length = 150)
    mulmetod = models.CharField(metodo, max_length = 500)
    mulescal = models.ForeignKey('inidcoanmue', verbose_name = escala)

    class Meta:
        verbose_name = u'Análisis multitemporal'
        verbose_name_plural = u'Análisis multitemporales'

class inidcosenso(models.Model):
    '''
    Cobertura de la tierra 
    Metodología utilizada para levantamiento de coberturas'
    Sensores utilizados
    '''
    sensor = models.CharField(u'Sensor Utilizado', max_length = 150)
    enable = models.BooleanField(u'Enabled', default = True)
    
    def __unicode__(self):
        return self.sensor

class inidcoanmue(models.Model):
    '''
    Cobertura de la tierra
    Análisis multitemporales'
    Escala
    '''
    escala = models.CharField(u'Valor de escala', max_length = 50)
    
    def __unicode__(self):
        return self.escala

#Flora y Fauna

class inidffestud(inididestud):
    '''
    Flora y Fauna
    Identificación del estudio
    '''
    class Meta:
        verbose_name = u'10 Estudio de Flora y Fauna'
        verbose_name_plural = u'10 Estudios de Flora y Fauna'
        proxy = True

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
    vegete = u'Tipo de vegetación en el área de estudio con inventario'
    ecoest = u'¿Si existieran ecosistemas acuáticos se han \
        realizado estudios  limnológicos?'
    numpar = u'Número de parcelas o transectos para inventarios \
        de vegetación o flora'
    metfau = u'Metodología utilizada para inventario de fauna \
        por clase jerárquica'
    clafau = u'Clases jerárquicas  de fauna inventariada'
    georef = u'¿Poseen georeferenciación los inventarios o están \
        relacionados a municipio o vereda?'
    carfue = u'La información de caracterización de flora y fauna se \
        realizó a partir de fuentes:'
    espame = u'¿Se han identificado especies de flora y/o fauna en \
        amenaza, peligro de extinción o endémicas?'
    espacu = u'¿Cuál o cuáles especies?'
    geoame = u'¿Existe georeferenciación de las mismas?'
    #Help text
    meinve_help = u'Incluye época del año de realización del estudio'
    metfau_help = meinve_help
    clafau_help = u'Mamíferos, aves, peces, reptiles, etc.'
    
    lists = SelectList()

    iffmeto = models.OneToOneField('inidffestud')
    iffmesm = models.CharField(metodo, max_length = 500)
    iffmein = models.CharField(meinve, max_length = 500, 
        help_text = meinve_help)
    ifftico = models.CharField(ticobe, max_length = 500)
    iffvegi = models.ForeignKey('inffmeveget', verbose_name = vegete, #CharField(vegete, max_length = 4,
        null = True, blank = True)
        #choices = lists.FlofInveChoose(), blank = True)
    iffesli = models.NullBooleanField(ecoest, choices = lists.BoolNullChoose())
    iffnupa = models.PositiveSmallIntegerField(numpar, 
        null = True, blank = True)
    iffmeif = models.CharField(metfau, max_length = 500,
        null = True, blank = True, help_text = metfau_help)
    iffclaj = models.CharField(clafau, max_length = 500, 
        null = True, blank = True, help_text = clafau_help)
    iffgeoi = models.ForeignKey('inffmegeore', verbose_name = georef, #CharField(georef, max_length = 4, 
        null = True, blank = True)
        #choices = lists.FlofGeoChoose(), null = True, blank = True)
    iffinfc = models.ForeignKey('inffmesouri', verbose_name = carfue) #CharField(carfue, max_length = 4,
        #choices = lists.FlofPMEFuenChoose())
    iffamen = models.ForeignKey('inffmeamena', verbose_name = espame) #CharField(espame, max_length = 4,
        #choices = lists.FlofAmenChoose())
    iffamec = models.CharField(espacu, max_length = 150, null = True, 
        blank = True)
    iffgeor = models.NullBooleanField(geoame, choices = lists.BoolChoose(),
        default = False)
    
    class Meta:
        verbose_name = u'10.1 Metodología de levantamiento'
        verbose_name_plural = verbose_name

class inffmeveget(models.Model):
    '''
    Flora y Fauna
    Tipo de vegetación en el área de estudio con inventario
    '''
    value = models.CharField(u'Variable', max_length = 150)
    enable = models.BooleanField(u'Enabled', default = True)
    
    def __unicode__(self):
        return self.value

class inffmegeore(models.Model):
    '''
    Flora y Fauna
    Georeferenciación de inventarios relacionados a municipio
    o vereda
    '''
    value = models.CharField(u'Variable', max_length = 150)
    enable = models.BooleanField(u'Enabled', default = True)
    
    def __unicode__(self):
        return self.value

class inffmesouri(models.Model):
    '''
    Flora y Fauna
    Fuentes de caracterización de flora y fauna
    '''
    value = models.CharField(u'Variable', max_length = 150)
    enable = models.BooleanField(u'Enabled', default = True)
    
    def __unicode__(self):
        return self.value

class inffmeamena(models.Model):
    '''
    Flora y fauna
    Especies de flora y/o fauna en 
        amenaza, peligro de extinción o endémicas.
    '''
    value = models.CharField(u'Variable', max_length = 150)
    enable = models.BooleanField(u'Enabled', default = True)
    
    def __unicode__(self):
        return self.value
    
class inidffcart(inidcartog):
    '''
    Flora y Fauna
    Información general  del  documento técnico y cartografía
    '''

    class Meta:
        verbose_name = u'10.2 Información cartográfica'
        verbose_name_plural = verbose_name
        proxy = True
    
#Plan de manejo en ecosistemas

class inidpmestud(inididestud):
    '''
    Plan de manejo en ecosistemas
    Identificación del estudio
    '''
    class Meta:
        verbose_name = u'11 Estudio PM ecosistemas'
        verbose_name_plural = u'11 Estudios PM ecosistemas'
        proxy = True

class inidpmecofo(models.Model):
    '''
    Plan de manejo en ecosistemas
    Formulación del Plan y Resultados
    '''
    planma = u'Existen en la CAR planes de manejo de:'
    planot = u'Si existiera otro tipo de plan de manejo que aplique al área \
        de interés, referéncielo'
    objeto = u'Objeto de estudio'
    planco = u'¿El Plan se encuentra adoptado por la Corporación?'
    vigepl = u'Vigencia del Planes'
    planex = u'¿El plan ha sido ejecutado?'
    #Help text

    lists = SelectList()

    ipmformu = models.OneToOneField('inidpmestud')
    ipmfplan = models.ManyToManyField('pmecoplanma', verbose_name = planma,
        null = True, blank = True)
    ipmfplao = models.CharField(planot, max_length = 500, 
        null = True, blank = True)
    ipmfobje = models.CharField(objeto, max_length = 500)
    ipmfadop = models.BooleanField(planco, choices = lists.BoolChoose(), 
        default = False)
    ipmfvige = models.PositiveSmallIntegerField(vigepl, 
        choices = lists.YearList(), default = lists.ThisYear())
    ipmfplae = models.BooleanField(planex, choices = lists.BoolChoose())

    class Meta:
        verbose_name = u'11.1 Formulación del plan y resultados'
        verbose_name_plural = verbose_name

class pmecoplanma(models.Model):
    '''
    Plan Manejo en ecosistemas.
    Formulación del Plan y Resultados
    Planes de manejo
    '''
    #pmecopla = models.ForeignKey('inidpmecofo')
    planmane = models.CharField(u'Plan de manejo', max_length = 200)

    def __unicode__(self):
        return self.planmane 

    class Meta:
        verbose_name = u'11.1.1 Plan de manejo'
        verbose_name_plural = u'11.1.1 Planes de manejo'

class inidpmecopm(inidcartog):
    '''
    Plan Manejo en ecosistemas.
    Información sobre los planes de manejo
    '''
    
    class Meta:
        verbose_name = u'11.2 Plan de manejo'
        verbose_name_plural = u'11.2 Planes de manejo'
        proxy = True

#Riesgos

## Identificación de Amenazas
# Caracterización de estudios
#class inidriesame(inididestud):
#    '''
#    Riesgos
#    Identificación de amenazas
#    Información general
#    '''
#
#    class Meta:
#        verbose_name = u'12.1 Identificación de amanaza'
#        verbose_name_plural = u'12.1 Identificación de amanazas'

class inriesamepr(inididinden):
    '''
    Riesgos
    Identificación de amenazas
    Identificación preliminar de los sitios con condiciones de 
        amenazas y eventos
    '''
    amenaz = u'Amenzas que se identifican en la cuenca'
    amenao = u'Otras amenazas'
    ubidep = u'Ubicación geográfica. Departamento'
    ubimun = u'Ubicación geográfica. Municipio'
    ubiver = u'Ubicación geográfica. Vereda'
    evento = u'Eventos que han ocurrido en la cuenca'
    eveotr = u'Otros eventos'
    recurr = u'Recurrencia'
    causas = u'Posibles causas para que se presenten los eventos'
    elemen = u'Elementos expuestos que se vieron afectados'
    elemot = u'Otros elementos'
    actsoc = u'¿Las actividades sociales, culturales o económicas \
        contribuyeron al incremento de las amenzas o la frecuencia \
        de los eventos' 
    activi = u'Actividades que contribuyeron al incremento de las \
        amenazas o la frecuencia'
    mapaam = u'Mapa de amenazas y/o eventos'
    georef = u'Georeferenciación de amenazas y/o eventos'
   
    lists = SelectList()

#    amenazas = models.ForeignKey('inidriesame', verbose_name = u'Amenazas en la cuenca')
    ameniden = models.ForeignKey('amenaidenti', verbose_name = amenaz)
    amenotra = models.CharField(amenao, max_length = 100, null = True,
        blank = True)
    ubidepar = models.CharField(ubidep, max_length = 250, null = True, 
        blank = True)
    ubimunic = models.CharField(ubimun, max_length = 250, null = True, 
        blank = True)
    ubivered = models.CharField(ubiver, max_length = 250, null = True, 
        blank = True)
    eventocu = models.ManyToManyField('eventocurri', verbose_name = evento, 
        null = True, blank = True)
    eventoot = models.CharField(eveotr, max_length = 250, null = True, 
        blank = True)
    eventrec = models.CharField(recurr, max_length = 125, null = True,
        blank = True)
    evencaus = models.CharField(causas, max_length = 250, null = True, 
        blank = True)
    elemento = models.ManyToManyField('elemenexpue', verbose_name = elemen, 
        null = True, blank = True)
    elemotro = models.CharField(elemot, max_length = 250, null = True, 
        blank = True)
    actosoci = models.BooleanField(actsoc, choices = lists.BoolChoose(),
        default = False)
    activida = models.CharField(activi, max_length = 250, null = True, 
        blank = True)
    amenmapa = models.FileField(mapaam, upload_to = 'amen_map/',
        null = True, blank = True)
    amengeor = models.CharField(georef, max_length = 250, null = True, 
        blank = True) 

    class Meta:
        verbose_name = u'12.1 Riesgos - Amenazas'
        verbose_name_plural = verbose_name

class amenaidenti(models.Model):
    '''
    Riesgos
    Amenazas identificadas en la cuenca
    '''
    amenaz = models.CharField(u'Amenaza identificada', max_length = 150)
    enable = models.BooleanField(u'Enabled', default = True)
    
    def __unicode__(self):
        return self.amenaz
    
class eventocurri(models.Model):
    '''
    Riesgos
    Eventos que han ocurrido en la cuenca
    '''
    evento = models.CharField(u'Evento ocurrido', max_length = 150)
    enable = models.BooleanField(u'Enabled', default = True)

    def __unicode__(self):  
        return self.evento

class elemenexpue(models.Model):
    '''
    Riesgos
    Elementos expuestos que se vieron afectados
    '''
    elemen = models.CharField(u'Elemento ocurrido', max_length = 150)
    enable = models.BooleanField(u'Enabled', default = True)

    def __unicode__(self):
        return self.elemen

class inriesameac(models.Model):
    '''
    Riesgos
    Identificación de amenazas
    Identificación preliminar de los sitios con condiciones de 
        amenazas y eventos
    Actores que tienen registros e información
    '''
    lists = SelectList()
    
    amenaz = models.ForeignKey('inriesamepr', 
        verbose_name = u'Amenaza identificada')
    iactor = models.CharField(u'Actor', max_length = 100)
    idyear = models.PositiveSmallIntegerField(u'Año',
        choices = lists.YearList(), default = lists.ThisYear())

    class Meta:
        verbose_name = u'Actor con registros'
        verbose_name_plural = u'Actores con registros'

## Estudios y cartografía
class inidriestud(inididestud):
    '''
    Riesgos
    Identificación del estudio
    '''
    class Meta:
        verbose_name = u'12.2.1 Estudio de Riesgos'
        verbose_name_plural = u'12.2.1 Estudios de Riesgos'
        proxy = True

class inidriescar(inidcartog):
    '''
    Riesgos
    Información general cartográfica.
    '''
    class Meta:
        verbose_name = u'12.2.2 Información cartográfica'
        verbose_name_plural = verbose_name
        proxy = True

#Socioeconómico

## Actores Sociales 
class inidseasinf(inididestud):
    '''
    Socioeconómico y Cultural
    Actores Sociales
    Información General
    '''
    class Meta:
        verbose_name = u'13.1 Actores sociales'
        verbose_name_plural = verbose_name
        proxy = True

class inidseasdet(models.Model):
    '''
    Socioeconómico y Cultural
    Actores Sociales
    Detalle de la información
    '''
    method = u'¿Existe metodología del análisis de actores?' 
    methde = u'Describa la metodología del análisis de actores'
    docume = u'¿Existen documentos, fichas, herramientas u otros que \
        consoliden la  caracterización de actores?'
    docesp = u'¿Cuáles son los documentos que consolidan la caracterización \
        de actores?'
    docasp = u'Aspectos abordados en la caracterización'
    actmap = u'¿Existen Mapa de actores?'
    priori = u'¿Existen matrices de priorización de actores?'
    priode = u'¿Qué actores están priorizados?'
    dbacto = u'¿Existen Base de datos de actores, organizaciones sociales, \
        institucionales  y sectoriales?'
    dbvari = u'¿Cuáles son las variables de la base de datos?'

    lists = SelectList()

    isesocio = models.OneToOneField('inidseasinf')
    isemetho = models.BooleanField(method, choices = lists.BoolChoose(),
        default = False)
    isemethd = models.CharField(methde, max_length = 500, 
        null = True, blank = True)
    isedocum = models.BooleanField(docume, choices = lists.BoolChoose(),
        default = False)
    isedocud = models.CharField(docesp, max_length = 500, 
        null = True, blank = True)
    isedocas = models.CharField(docasp, max_length = 500, 
        null = True, blank = True)
    iseactma = models.BooleanField(actmap, choices = lists.BoolChoose(),
        default = False)
    iseprior = models.BooleanField(priori, choices = lists.BoolChoose(),
        default = False)
    isepride = models.CharField(priode, max_length = 500, 
        null = True, blank = True)
    isedbact = models.BooleanField(dbacto, choices = lists.BoolChoose(),
        default = False)
    isedbvar = models.CharField(dbvari, max_length = 500, 
        null = True, blank = True)

    class Meta:
        verbose_name = u'13.1.2 Detalle de la información'
        verbose_name_plural = u'13.1.2 Detalles de la información'

## Participación 
class inidseepinf(inididestud):
    '''
    Socioeconómico y Cultural
    Estrategias de participación
    Información General
    '''
    class Meta:
        verbose_name = u'13.2 Participación'
        verbose_name_plural = u'13.2 Participación'
        proxy = True

class inidseepdet(models.Model):
    '''
    Socioeconómico y Cultural
    Estrategias de participación
    Detalle de la información
    '''
    estrat = u'¿Se han desarrollado estrategias de participación en  las \
        fases del POMCA?' 
    estrwh = u'Realizar una descripción de las estrategias desarrolladas \
        en la fase del POMCA'
    estter = u'Especificar los territorios en que se ha desarrollado'
    partic = u'¿Se incorporó la participación de los actores sociales en \
        la construcción del diagnóstico?'
    parmet = u'Describir el método de participación que se implementó \
        en la construcción del diagnóstico'
    instan = u'¿Se conformaron instancias (estructura) de participación \
        en el proceso POMCA?'
    comunic = u'¿Se han desarrollado estrategias de comunicación en el \
        proceso POMCA?'
    comudes = u'Realizar una breve descripción de los medios de \
        comunicación que implementó la corporación en el POMCA'
    iambien = u'¿Existen instancias participativas ambientales que hagan \
        parte del territorio de la cuenca?'
    iamdes = u'Especificar las instancias participativas ambientales que \
        hacen parte del territorio'
    estado = u'Estado de funcionamiento de las instancias participativas'
    # Help Text
    partic_help = u'Físico- biótico y socioeconómico'
    instan_help = u'Mesas regionales, mesas de trabajo municipales, \
        consejo de cuenca, entre otros'
    iambien_help = u'Mesas ambientales municipales, entre otros'

    lists = SelectList()

    iseestra = models.OneToOneField('inidseepinf')
    isepestr = models.BooleanField(estrat, choices = lists.BoolChoose(),
        default = False)
    isepestg = models.CharField(estrwh, max_length = 500, 
        null = True, blank = True)
    isepestd = models.CharField(estter, max_length = 500, 
        null = True, blank = True)
    iseppart = models.BooleanField(partic, choices = lists.BoolChoose(),
        default = False, help_text = partic_help)
    isepparm = models.CharField(parmet, max_length = 500, 
        null = True, blank = True)
    isepinst = models.BooleanField(instan, choices = lists.BoolChoose(),
        default = False, help_text = instan_help)
    isepcomu = models.BooleanField(comunic, choices = lists.BoolChoose(),
        default = False)
    isepcomd = models.CharField(comudes, max_length = 500, 
        null = True, blank = True)
    isepiamb = models.BooleanField(iambien, choices = lists.BoolChoose(),
        default = False, help_text = iambien_help)
    isepiamd = models.CharField(iamdes, max_length = 500, 
        null = True, blank = True)
    isepesta = models.CharField(estado, max_length = 500, 
        null = True, blank = True)

    class Meta:
        verbose_name = u'13.2.1 Detalle de la información'
        verbose_name_plural = u'13.2.1 Detalles de la información'

class inidseepdin(models.Model):
    '''
    Socioeconómico y Cultural
    Estrategias de participación
    Instancias de participación conformadas
    '''
    descri = u'Describir las instancias de participación'
    acstat = u'¿Cuál es el estado actual de la estructura de participación?'

    instanci = models.ForeignKey('inidseepdet', 
        verbose_name = u'Estrategias de participación')
    descripc = models.CharField(descri, max_length = 500)
    estadoac = models.CharField(acstat, max_length = 500)

    class Meta:
        verbose_name = u'Instancia de participación'
        verbose_name_plural = verbose_name

## Participación de comunidades étnicas 
class inidseceinf(inididestud):
    '''
    Socioeconómico y Cultural
    Participación de comunidades étnicas 
    Información General
    '''
    class Meta:
        verbose_name = u'13.3 Participación comunidad étnica'
        verbose_name_plural = u'13.3 Participación comunidades étnica'
        proxy = True

class inidsecedet(models.Model):
    '''
    Socioeconómico y Cultural
    Participación de comunidades étnicas 
    Detalle de la información
    '''
    caract = u'¿Existe Identificación y caracterización de grupos étnicos \
         asentados en la cuenca?' 
    carwho = u'¿Cuáles son los grupos étnicos asentados en la cuenca?'
    certif = u'¿Existen Certificados expedidos por el Ministerio de \
        Interior sobre la existencia de grupos étnicos presentes en la cuenca?'
    develp = u'¿La corporación ha desarrollado estrategias de participación \
        con comunidades étnicas en la cuenca?'
    devede = u'Realice una breve descripción de las estrategias de \
        participación con comunidades étnicas en la cuenca'

    lists = SelectList()

    iseparti = models.OneToOneField('inidseceinf')
    isepccar = models.BooleanField(caract, choices = lists.BoolChoose(),
        default = False)
    isepccaw = models.CharField(carwho, max_length = 500, 
        null = True, blank = True)
    isepccer = models.BooleanField(certif, choices = lists.BoolChoose(),
        default = False)
    isepcdev = models.BooleanField(develp, choices = lists.BoolChoose(),
        default = False)
    isepcded = models.CharField(devede, max_length = 500, 
        null = True, blank = True)

    class Meta:
        verbose_name = u'13.3.1 Detalle de la información'
        verbose_name_plural = u'13.3.1 Detalles de la información'

class inidsecedat(models.Model):
    '''
    Socioeconómico y Cultural
    Participación de comunidades étnicas 
    Datos de certificados expedidos por el Ministerio de Interior
        sobre la existencia de grupos étnicos presentes en la cuenca?'
    '''
    comuni = u'Comunidad'
    exdate = u'Fecha de expedición'
    resolu = u'Resolución'

    particip = models.ForeignKey('inidsecedet')
    comunida = models.CharField(comuni, max_length = 150)
    expediti = models.DateField(exdate)
    resoluti = models.CharField(resolu, max_length = 50)

    class Meta:
        verbose_name = u'Datos de certificado'
        verbose_name_plural = u'Datos de certificados'

## Diagnósticos Socioeconómicos 
class inidsedsinf(inididestud):
    '''
    Socioeconómico y Cultural
    Diagnósticos Socioeconómicos
    Información General
    '''
    class Meta:
        verbose_name = u'13.4 Diagnóstico socioeconómico'
        verbose_name_plural = u'13.4 Diagnósticos socioeconómicos'
        proxy = True

class inidsdsedet(models.Model):
    '''
    Socioeconómico y Cultural
    Diagnósticos Socioeconómicos
    Detalle de la información
    '''
    dinami = u'¿Existen análisis de la dinámica poblacional?' 
    dinava = u'Identificar las variables analizadas'
    dinavo = u'Otros'
    servso = u'¿Existe descripción y caracterización servicios sociales \
        existentes?'
    servca = u'Especifique los servicios sociales caracterizados'
    servco = u'Otros'
    segali = u'¿Existen documentos sobre Seguridad Alimentaria?'
    segcob = u'Indicar la cobertura de del estudio de seguridad alimentaria '
    segdes = u'Una descripción breve del alcance del estudio de seguridad \
        alimentaria'
    activi = u'¿Existe caracterización de las actividades económicas actuales \
        y dominantes en la cuenca?'
    actide = u'Especificar las actividades económicas en la cuenca están \
        caracterizadas'
    actido = u'Otros'
    situac = u'¿Existe análisis o descripción de la situación de pobreza \
        y desigualdad de los territorios de  la cuenca?'
    situde = u'Realizar una breve descripción de los indicadores analizados'
    proyec = u'¿Existe análisis de proyectos regionales de impacto en la \
        cuenca, en desarrollo y futuros?'
    proyde = u'Realizar una breve descripción de los proyectos regionales \
        de impacto en la cuenca en desarrollo y futuros'
    confli = u'¿Existen análisis de conflictos socioeconómicos?'
    confde = u'Describir los principales conflictos que se presentan en \
        la cuenca'
    politi = u'¿Existe documentos con la descripción político \
        administrativa e institucional de la cuenca?'
    polide = u'Describir la jurisdicción político administrativa \
        institucional de la cuenca'
    predia = u'¿Existe un documento con análisis predial o de tenencia de \
        la tierra?'
    predco = u'Indicar la cobertura del documento con el análisis \
        predial o de tenencia de la tierra'
    seguri = u'¿Existe documento con análisis sobre Seguridad y convivencia?'
    seguco = u'Indicar la cobertura del documento con análisis sobre \
        seguridad y convivencia'
    # Help text
    segali_help = u'Regional, municipal, otros'
    seguco_help = segali_help 

    lists = SelectList()

    isediagn = models.OneToOneField('inidsedsinf')
    iseddina = models.BooleanField(dinami, choices = lists.BoolChoose(),
        default = False)
    iseddinv = models.ManyToManyField('inidsedsvar', 
        verbose_name = dinava, null = True, blank = True)
    iseddino = models.CharField(dinavo, max_length = 250, null = True, 
        blank = True)
    isedserv = models.BooleanField(servso, choices = lists.BoolChoose(),
        default = False)
    isedsere = models.ManyToManyField('inidsedsser', 
        verbose_name = servca, null = True, blank = True)
    isedsero = models.CharField(servco, max_length = 250, null = True, 
        blank = True)
    isedseal = models.BooleanField(segali, choices = lists.BoolChoose(),
        default = False, help_text = segali_help)
    isedseai = models.CharField(segcob, max_length = 500, null = True, 
        blank = True)
    isedsede = models.CharField(segdes, max_length = 500, null = True, 
        blank = True)
    isedacti = models.BooleanField(activi, choices = lists.BoolChoose(),
        default = False)
    isedactd = models.ManyToManyField('inidsedsact', 
        verbose_name = actide, null = True, blank = True)
    isedacto = models.CharField(actido, max_length = 100, null = True, 
        blank = True)
    isedsitu = models.BooleanField(situac, choices = lists.BoolChoose(),
        default = False)
    isedsitd = models.CharField(situde, max_length = 500, null = True, 
        blank = True)
    isedproy = models.BooleanField(proyec, choices = lists.BoolChoose(),
        default = False)
    isedprod = models.CharField(proyde, max_length = 500, null = True, 
        blank = True)
    isedconf = models.BooleanField(confli, choices = lists.BoolChoose(),
        default = False)
    isedcond = models.CharField(confde, max_length = 500, null = True, 
        blank = True)
    isedpoli = models.BooleanField(politi, choices = lists.BoolChoose(),
        default = False)
    isedpold = models.CharField(polide, max_length = 500, null = True, 
        blank = True)
    isedpred = models.BooleanField(predia, choices = lists.BoolChoose(),
        default = False)
    isedprec = models.CharField(predco, max_length = 500, null = True, 
        blank = True)
    isedsegu = models.BooleanField(seguri, choices = lists.BoolChoose(),
        default = False)
    isedsegd = models.CharField(seguco, max_length = 500, null = True, 
        blank = True, help_text = seguco_help)

    class Meta:
        verbose_name = u'13.4.1 Detalle de la información'
        verbose_name_plural = u'13.4.1 Detalles de la información'

class inidsedsvar(models.Model):
    '''
    Socioeconómico y Cultural
    Diagnósticos Socioeconómicos
    Variables analizadas
    '''
    variab = models.CharField(u'Variables analizadas', max_length = 50)
    enable = models.BooleanField(u'Enabled', default = True)
    
    def __unicode__(self):
        return self.variab

    class Meta:
        verbose_name = u'Variable Analizada'
        verbose_name_plural = u'Variables Analizadas'

class inidsedsser(models.Model):
    '''
    Socioeconómico y Cultural
    Diagnósticos Socioeconómicos
    Servicios sociales
    '''
    sevici = models.CharField(u'Servicios sociales', max_length = 50)
    enable = models.BooleanField(u'Enabled', default = True)
    
    def __unicode__(self):
        return self.sevici

    class Meta:
        verbose_name = u'Servicio social'
        verbose_name_plural = u'Servicios sociales'

class inidsedsact(models.Model):
    '''
    Socioeconómico y Cultural
    Diagnósticos Socioeconómicos
    Actividades económicas en la cuenca caracterizadas.
    '''
    activi = models.CharField(u'Actividades económicas', max_length = 50)
    enable = models.BooleanField(u'Enabled', default = True)
    
    def __unicode__(self):
        return self.activi

    class Meta:
        verbose_name = u'Actividad económica'
        verbose_name_plural = u'Actividades económicas'

## Caracterización Cultural 
class inidseccinf(inididestud):
    '''
    Socioeconómico y Cultural
    Caracterización Cultural
    Información General
    '''
    class Meta:
        verbose_name = u'13.5 Caracterización cultural'
        verbose_name_plural = verbose_name
        proxy = True

class inidseccdet(models.Model):
    '''
    Socioeconómico y Cultural
    Caracterización Cultural
    Detalle de la información
    '''
    cultur = u'¿Existen documentos de caracterización cultural?'
    cultco = u'Indicar la cobertura del estudio de caracterización \
        cultural'
    cultva = u'Variables caracterizadas'
    patron = u'¿Existen documentos con la caracterización de patrones \
        de uso,  ocupación y apropiación del territorio?' 
    cobert = u'Indicar la cobertura del estudio'
    docume = u'¿Existen documentos que caractericen las prácticas culturales,\
        relacionadas con el aprovechamiento y uso de la biodiversidad?' 
    docuco = u'Indicar la cobertura del estudio'
    # Help text
    cultco_help = u'Regional, municipal, otros'
    cobert_help = cultco_help 
    docuco_help = cultco_help 

    lists = SelectList()

    isecarac = models.OneToOneField('inidseccinf')
    isecccul = models.BooleanField(cultur, choices = lists.BoolChoose(),
        default = False)
    isecccuc = models.CharField(cultco, max_length = 500, null = True, 
        blank = True, help_text = cultco_help)
    isecccuv = models.CharField(cultva, max_length = 500, null = True, 
        blank = True)
    iseccpat = models.BooleanField(patron, choices = lists.BoolChoose(),
        default = False)
    iseccpad = models.CharField(cobert, max_length = 500, null = True, 
        blank = True, help_text = cobert_help)
    iseccdoc = models.BooleanField(docume, choices = lists.BoolChoose(),
        default = False)
    iseccdcc = models.CharField(docuco, max_length = 500, null = True, 
        blank = True, help_text = docuco_help)

    class Meta:
        verbose_name = u'13.5.1 Detalle de la información'
        verbose_name_plural = u'13.5.1 Detalles de la información'

class inidseccdcc(models.Model):
    '''
    Socioeconómico y Cultural
    Caracterización Cultural
    Cobertura del documento de caracterización cultural
    '''
    cobert = u'Cobertura del documento de caracterización cultural'
    variab = u'Variables culturales caracterizadas'
    #Help text
    cobert_help = u'Regional, municipal, otros'

    caracter = models.ForeignKey('inidseccdet', 
        verbose_name = u'Caracterización cultural')
    cobertur = models.CharField(cobert, max_length = 250,
        help_text = cobert_help)
    variable = models.CharField(variab, max_length = 300)

    class Meta:
        verbose_name = u'13.5.1.1 Cobertura del documento'
        verbose_name_plural = u'13.5.1.1 Cobertura del documento'

## Valoración de Servicios Ecosistémicos
class inidsevsinf(inididestud):
    '''
    Socioeconómico y Cultural
    Valoración de Servicios Ecosistémicos
    Información General
    '''
    class Meta:
        verbose_name = u'13.6 Servicio ecosistémico'
        verbose_name_plural = u'13.6 Servicios ecosistémicos'
        proxy = True

class inidsevsdet(models.Model):
    '''
    Socioeconómico y Cultural
    Valoración de Servicios Ecosistémicos
    Detalle de la información
    '''
    metodo = u'Describir la metodología utilizada en el estudio'
    servic = u'¿Cuales son los servicios ecosistémicos analizados?'
    sercio = u'Otros'
    piloto = u'¿Hay estudios piloto de valoración de servicios \
        ecosistemicos en curso?'
    piloal = u'Describir el alcance del estudio piloto de valoración \
        económica de bienes y servicios ambientales como herramienta \
        estratégica para la conservación y uso sostenible de la cuenca'

    lists = SelectList()

    isevalor = models.OneToOneField('inidsevsinf')
    isesemet = models.CharField(metodo, max_length = 500)
    iseseser = models.ManyToManyField('inidseserec', 
        verbose_name = servic, null = True, blank = True)
    iseseseo = models.CharField(sercio, max_length = 500,
        null = True, blank = True)
    isesepil = models.BooleanField(piloto, choices = lists.BoolChoose(),
        default = False)
    isesepia = models.CharField(piloal, max_length = 500,
        null = True, blank = True)

    class Meta:
        verbose_name = u'13.6.1 Detalle de la información'
        verbose_name_plural = u'13.6.1 Detalles de la información'

class inidseserec(models.Model):
    '''
    Socioeconómico y Cultural
    Valoración de Servicios Ecosistémicos
    Servicios ecosistémicos analizados
    '''
    servic = models.CharField(u'Servicio ecosistémico analizado', 
        max_length = 50)
    enable = models.BooleanField(u'Enabled', default = True)
    
    def __unicode__(self):
        return self.servic

## Relaciones Funcionales Urbano- Regionales 
class inidserfinf(inididestud):
    '''
    Socioeconómico y Cultural
    Relaciones funcionales urbano - regionales
    Información General
    '''
    class Meta:
        verbose_name = u'13.7 Relación urbano - regionales'
        verbose_name_plural = u'13.7 Relaciones urbano - regionales'
        proxy = True

class inidserfdet(models.Model):
    '''
    Socioeconómico y Cultural
    Relaciones funcionales urbano - regionales
    Detalle de la información
    '''
    compet = u'¿Existen análisis de competitividad y producción?' 
    conect = u'¿Existe análisis de conectividad?'
    coneco = u'Indicar la cobertura del estudio'
    coneal = u'Describir el alcance tienen de estudios de competitividad'
    capaci = u'¿Existe análisis de capacidad de soporte ambiental de la región?'
    capaco = u'Indicar la cobertura del estudio'
    capaal = u'Describir el alcance que tienen los estudios'

    lists = SelectList()

    infuurre = models.OneToOneField('inidserfinf', 
        verbose_name = u'Relac. Func. Urb.-Reg.')
    infucomp = models.BooleanField(compet, choices = lists.BoolChoose(),
        default = False)
    infucone = models.BooleanField(conect, choices = lists.BoolChoose(),
        default = False)
    infoconc = models.CharField(coneco, max_length = 500,
        null = True, blank = True)
    infocona = models.CharField(coneal, max_length = 500,
        null = True, blank = True)
    infocapa = models.BooleanField(capaci, choices = lists.BoolChoose(),
        default = False)
    infocapo = models.CharField(capaco, max_length = 500,
        null = True, blank = True)
    infocapl = models.CharField(capaal, max_length = 500,
        null = True, blank = True)
    
    class Meta:
        verbose_name = u'13.7.1 Detalle de la información'
        verbose_name_plural = u'13.7.1 Detalles de la información'

class inidserfure(models.Model):
    '''
    Socioeconómico y Cultural
    Relaciones funcionales urbano - regionales
    Análisis de competitividad y producción
    '''
    lists = SelectList()

    cober = u'Cobertura del estudio'
    alcan = u'Alcance del estudio de competitividad y producción'
    # Help text
    cober_help = u'Regional, municipal, otros'

    inserela = models.ForeignKey('inidserfdet', 
        verbose_name = u'Estudio')
    inseurco = models.CharField(cober, max_length = 500, null = True,
        blank = True, help_text = cober_help)
    inseural = models.CharField(alcan, max_length = 500, null = True,
        blank = True)

    class Meta:
        verbose_name = u'Competitividad y producción'
        verbose_name_plural = verbose_name
