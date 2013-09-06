# -*- coding: utf-8 -*-
from django.db import models

class minstportada(models.Model):
    '''
    Cover
    Characterization:
        - Form: Matriz Institucional
        - Tab: Portada
        - Title: Datos generales sobre el diligenciamiento de la matriz
    '''	
    mipofede = models.DateField()
    mipofeha = models.DateField()
    mipoprof = models.CharField(max_length = 250)
    mipodesc = models.TextField()

class minstdatgene(models.Model):    
    '''
    Corporation general data.
    Characterization:
        - Form : Matriz Institucional
        - Tab: Datos Generales
        - Title: Datos Generales de la Corporación
    '''
    #Naming each day
    MONDAY = 'Mon'
    TUESDAY = 'Tue'
    WEDNESDAY = 'Wed'
    THURSDAY = 'Thu'
    FRIDAY = 'Fri'
    SATURDAY = 'Sat'
    SUNDAY = 'Sun'
    #Weedays in Spanish
    WEEKDAYS_ES = (
        (MONDAY , 'Lunes'),
        (TUESDAY , 'Martes'),
        (WEDNESDAY , 'Miercoles'),
        (THURSDAY , 'Jueves'),
        (FRIDAY , 'Viernes'),
        (SATURDAY , 'Sabado'),
        (SUNDAY , 'Domingo'),
    )   
    midglogo = models.ImageField(u'Logo', upload_to = 'img/business/', 
                            height_field = None, width_field = None, null = True, blank = True) #Corporation logo
    midgrazs = models.CharField(u'Nombre de la corporación', max_length = 50)    #Corporation Name
    midgenit = models.IntegerField(u'NIT')                #NIT
    midgnitd = models.IntegerField(u'NIT DV')                #Headquarters Address
    midginit = models.CharField(u'Sigla', max_length = 20)    #Initials
    midgaddr = models.CharField(u'dirección de sede principal', max_length = 50)    #Headquarters address
    midgcity = models.CharField(u'Ciudad', max_length = 20)    #City
    midgssop = models.TimeField(u'Horario de atención. De')                   #Service schedule, openning
    midgsscl = models.TimeField(u'A')                   #Service schedule, close
    midgapdf = models.CharField(u'Días de atención al público', max_length = 3,
                                choices = WEEKDAYS_ES,
                                default = MONDAY)   #Public Attention days, from
    midgapdt = models.CharField(u'A', max_length = 3,
                                choices = WEEKDAYS_ES,
                                default = FRIDAY)   #Public Attention days, to
    midgphon = models.IntegerField(u'Teléfono (PBX)')                #Phone (PBX)
    midgwebp = models.URLField(u'Página Web')                    #Webpage
    midgmail = models.EmailField(u'Correo electrónico de contacto')                  #email contact.
    midgarju = models.CharField(u'área de Jurisdicción', max_length = 50)    #Area of jurisdiction
    midgnumj = models.IntegerField(u'Número de municipios de la jurisdicción')                #Number of municipalities in the area of jurisdiction
    midgscda = models.DateField(auto_now_add = True)    #Creation date on our system
    
    class Meta:
        verbose_name = 'Datos generales de la coporación'
        verbose_name_plural = 'Datos generales de las corporaciones'

    def __unicode__(self):
        return u'%s, %s, %s, %s, %s, %s, %s, %s, %s' %(self.midgrazs, self.midginit, 
            self.midgaddr, self.midgcity, self.midgapdf, self.midgapdt, 
            self.midgwebp, self.midgmail ,self.midgarju)

class minstestdire(models.Model):    
    '''
    Corporation Directive Structure
    Characterization:
        - Form: Matriz Institucional
        - Tab: Est Directiva
        - Title: Estructura directiva de la corporación
    '''
    miedcorp = models.ForeignKey('minstdatgene', verbose_name = 'empresa')     #Corporation
    miediceo = models.CharField(u'nombre del director general de la corporación',
                                max_length = 50)    #CEO name
    mieddatp = models.DateField(u'Fecha de posesión del actual director')                   #CEO Posession Date
    miedceip = models.BooleanField(u'Director general está activo?', 
                                default = True)                #CEO currently posessed? 
    
    class Meta: 
        verbose_name = 'estructura directiva de la corporación'
        verbose_name_plural = 'estructura directiva de las corporaciones'
    def __unicode__(self):
        return self.miediceo

class minstedcorpa(models.Model):     
    '''
    Conformation of the Directive assembly
    Characterization:
        - Form: Matriz Institucional
        - Tab: Est Directiva
        - Title: Estructura directiva de la corporación
        - SubTitle: Conformación de la asamblea corportativa
    '''
    miestdir = models.ForeignKey('minstestdire')      #Corpation Directive Structure
    miesddep = models.CharField(u'Departamento', max_length = 25)    #Department
    miesdmay = models.IntegerField(u'Número de alcaldes')            #Number of mayors

    class Meta: 
        verbose_name = 'Conformación de la asamblea directiva'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.miesddep

class minstedcondi(models.Model):
    '''
    Conformation of the board of directors 
    Characterization:
        - Form: Matriz Institucional
        - Tab: Est Directiva
        - Title: Estructura directiva de la corporación
        - SubTitle: Conformación de la asamblea corportativa
    '''
    miesddir = models.ForeignKey('minstestdire')      #Corpation Directive Structure
    miesdsec = models.CharField(u'Sector representado', max_length = 20)    #Represented sector
    miesdcna = models.CharField(u'Nombre de consejo', max_length = 32)    #Council Name
    miesdent = models.CharField(u'Entidad / Empresa / Gremio', max_length = 50)    #Entity, Business, guild

    class Meta:
        verbose_name = 'Conformación del consejo directivo'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s, %s, %s' %(self.miesdsec, self.miesdcna, self.miesdent)

class minstorganiz(models.Model):
    '''
    Organizational structure
    Characterization:
        - Form: Matriz Institucional
        - Tab: Organización
        - Title: Estructura organizativa de la Corporación
    '''
    mieocorp = models.ForeignKey('minstdatgene', verbose_name = 'empresa')     #Corporation
    mieoorga = models.ImageField(upload_to = 'img/business/', 
                            height_field = None, width_field = None, null = True, blank = True)    #Organization chart
    mieoaata = models.CharField(max_length = 125)     #Type of act
    mieoaano = models.IntegerField()                  #Act number
    mieoaada = models.DateField()                     #Act Date
    mieofnrp = models.PositiveIntegerField()
    mieofnrn = models.PositiveIntegerField()
    mieofnfc = models.PositiveIntegerField()

class minesorasesd(models.Model):
    '''
    
    Characterization:
        - Form: Matriz Institucional
        - Tab: Organización
        - Title: Estructura organizativa de la Corporación
        - SubTitle: Asesores de dirección
    '''
    miesoras = models.ForeignKey('minstorganiz')
    mieoadno = models.CharField(max_length = 125) 
    mieoadro = models.CharField(max_length = 125) 
    mieoadex = models.PositiveSmallIntegerField()
    mieoadco = models.EmailField()

class minesorsubdir(models.Model):
    '''
    
    Characterization:
        - Form: Matriz Institucional
        - Tab: Organización
        - Title: Estructura organizativa de la Corporación
        - SubTitle: Subdirecciones y oficinas de la corporación.
    '''
    miesorsu = models.ForeignKey('minstorganiz')
    mieosuof = models.CharField(max_length = 125) 
    mieosuex = models.PositiveSmallIntegerField()
    mieosuno = models.CharField(max_length = 125) 
    mieosutv = models.CharField(max_length = 125) 
    mieosuub = models.CharField(max_length = 125) 

class minesorsudico(models.Model):
    '''
    
    Characterization:
        - Form: Matriz Institucional
        - Tab: Organización
        - Title: Estructura organizativa de la Corporación
        - SubTitle: Subdirecciones y oficinas de la corporación.
        - Complement: Coordinaciones que conforman la subdirección u oficina.
    '''
    mieosubd = models.ForeignKey('minesorsubdir')
    mieosoco = models.CharField(max_length = 125) 
    mieosoln = models.PositiveSmallIntegerField()
    mieosoca = models.PositiveSmallIntegerField()
    mieosopr = models.PositiveSmallIntegerField()
    mieosocn = models.PositiveSmallIntegerField()

class minstdescentr(models.Model):
    '''
    
    Characterization:
        - Form: Matriz Institucional
        - Tab: Descentralización
        - Title: Estructura organizativa de las coporaciones (Should be changed?)
    '''
    midesnco = models.ForeignKey('minstdatgene', verbose_name = 'empresa')     #Corporation
    midesofi = models.BooleanField()
    midesmap = models.ImageField(upload_to = 'img/business/', 
                            height_field = None, width_field = None, null = True, blank = True)

class midesceoficte(models.Model):
    '''
    
    Characterization:
        - Form: Matriz Institucional
        - Tab: Descentralización
        - Title: Estructura organizativa de las coporaciones (Should be changed?)
        - Subtitle: Oficinas territoriales - Regionales
    '''
    midodesc = models.ForeignKey('minstdescentr')
    midocrit = models.CharField(max_length = 250)
    midofunc = models.CharField(max_length = 500)
    midonomb = models.CharField(max_length = 125)
    midodire = models.CharField(max_length = 200)
    midocity = models.CharField(max_length = 75)
    midotcou = models.PositiveSmallIntegerField(default = 75)
    midotind = models.PositiveSmallIntegerField()
    mitotelf = models.PositiveIntegerField()
    midotext = models.PositiveSmallIntegerField(null = True, blank = True)
    midomail = models.EmailField()
    midojuri = models.PositiveIntegerField()
    midojuri = models.PositiveSmallIntegerField()
    midonore = models.CharField(max_length = 200)
    midotivi = models.CharField(max_length = 75)
    midocarg = models.CharField(max_length = 125)
    midopvln = models.PositiveSmallIntegerField()
    midopvca = models.PositiveSmallIntegerField()
    midopvpr = models.PositiveSmallIntegerField()
    midopvco = models.PositiveSmallIntegerField()

class minstplanific(models.Model):
    '''
    
    Characterization:
        - Form: Matriz Institucional
        - Tab: Planeación
        - Title: Instrumentos de planificación de la corporación
    '''
    miplanif = models.ForeignKey('minstdatgene', verbose_name = u'empresa')     #Corporation
    miplpgar = models.FileField(u'Plan de gestión ambiental regional PGAR', 
                               upload_to = 'doc/business/', null = True, blank = True)
    mipltipg = models.CharField(u'Título de PGAR',max_length = 200)
    miprpgpe = models.CharField(u'Periodo del PGAR', max_length = 75)
    miplpgaa = models.CharField(u'Adopción PGAR. Tipo de acto administrativo',
                               max_length = 75)
    miplpgno = models.PositiveIntegerField(u'Adopción PGAR. Número')
    miplpgda = models.DateField(u'Adopción PGAR. Fecha')
    miplpamj = models.CharField(u'Prospectiva ambiental de la jurisdicción',
                               max_length = 200)
    mipldiag = models.CharField(u'Diagnóstico ambiental', max_length = 200)
    miplaaiv = models.FileField(u'Plan de acción institucional', 
                               upload_to = 'doc/business/')
    miplaait = models.CharField(u'Título del plan de acción',max_length = 200)
    miplaaip = models.CharField(u'Periodo del plán de acción',
                               max_length = 75)
    miplaiaa = models.CharField(u'Adopción plan de acción. Acto administrativo',
                                max_length = 75)
    miplaino = models.PositiveIntegerField('Adopción plan de acción. Número')
    miplaida = models.DateField(u'Adopción plan de acción. Fecha')

class minstplanpgar(models.Model):
    '''
    
    Characterization:
        - Form: Matriz Institucional
        - Tab: Planeación
        - Title: Instrumentos de planificación de la corporación
        - Subtitle: Plan de Gestión Ambiental Regional - PGAR
            Relacionar los componentes del PGAR correspondientes a procesos de POMCAS
    '''
    miplanpg = models.ForeignKey('minstplanific', verbose_name=u'Planificación institucional')
    miplpges = models.CharField(u'Estrategias', max_length = 200)
    miplpgse = models.CharField(u'Mecanismos de seguimiento y evaluación',
                               max_length = 200)

class minsplanplaci(models.Model):
    '''
    
    Characterization:
        - Form: Matriz Institucional
        - Tab: Planeación
        - Title: Instrumentos de planificación de la corporación
        - Subtitle: Plan de acción institucional
            Relacional las metas correspondientes a procesos de POMCAS
    '''
    miplanai = models.ForeignKey('minstplanific', verbose_name=u'Planificación institucional')
    miplaipr = models.CharField(u'Programas', max_length = 200)
    miplaipj = models.CharField(u'Proyectos', max_length = 200)
    miplaimt = models.CharField(u'Metas', max_length = 200)

class minspresupues(models.Model):
    '''
    
    Characterization:
        - Form: Matriz Institucional
        - Tab: Presupuesto
        - Title: Presupuesto
            Ejecución presupuestal 2012
    '''
    miplanpr = models.ForeignKey('minstdatgene', verbose_name = u'empresa')     #Corporation
    miplprgp = models.PositiveIntegerField(u'Gastos de funcionamiento. Proyectado')
    miplgrge = models.PositiveIntegerField(u'Gastos de funcionamiento. Ejecutado')
    miplgrip = models.PositiveIntegerField(u'Inversión. Proyectado')
    miplgrie = models.PositiveIntegerField(u'Inversión. Ejecutado')
    miplgrsp = models.PositiveIntegerField(u'Servicio a la Deuda. Proyectado')
    miplgrse = models.PositiveIntegerField(u'Servicio a la Deuda. Ejecutado')
    miplgfrp = models.PositiveIntegerField(u'Fondo de compensación. Recibido. Proyectado')
    miplgfre = models.PositiveIntegerField(u'Fondo de compensación. Recibido. Ejecutado')
    miplgfap = models.PositiveIntegerField(u'Fondo de compensación. Aportado. Proyectado')
    miplgfae = models.PositiveIntegerField(u'Fondo de compensación. Aportado. Ejecutado')

class minspresactad(models.Model):
    '''
    
    Characterization:
        - Form: Matriz Institucional
        - Tab: Presupuesto
        - Title: Presupuesto
        - Subtitle: Actos administrativos por los cuales se adopta o modifica el presupuesto 2013'
    '''
    mipraaco = models.ForeignKey('minspresupues', verbose_name = u'Prespuesto')
    mipraati = models.CharField(u'Tipo acto administrativo', max_length = 75)
    mipraano = models.CharField(u'Número', max_length = 75)
    mipraada = models.DateField(u'Fecha')
    mipraaac = models.CharField(u'Acción', max_length = 200)

class minsprespomca(models.Model):
    '''
    
    Characterization:
        - Form: Matriz Institucional
        - Tab: Presupuesto
        - Title: Presupuesto
        - Subtitle: Presupuesto de proyectos asociados a POMCAS - Uso interno
    '''
    miprprco = models.ForeignKey('minspresupues', verbose_name = u'Presupuesto')
    miprprpr = models.CharField(u'Proyecto', max_length = 200)
    miprprpr = models.CharField(u'Fuente de Financiación', max_length = 200)
    miprprva = models.PositiveIntegerField(u'Valor')
    miprprcu = models.PositiveIntegerField(u'Cuencas')
    miprpras = models.BooleanField(u'ASOCARS',)

class minssopotecni(models.Model):
    '''
    
    Characterization:
        - Form: Matriz Institucional
        - Tab: Sop Tec 
        - Title: Soporte Técnico
        - Subtitle : Sistema de Información Geográfica (SIG).
            Sistema de Información del Recurso Hídrico (SIRH)
            Laboratorio de Aguas (LA)
            Red de Monitoreo Amibental (RMA)
            Red de Monitoreo Climatológica (RMC)
            Red de Monitorio Hidrolófica (RMH)

    '''
    misoptec = models.ForeignKey('minstdatgene', verbose_name = u'empresa')     #Corporation
    missigex = models.CharField(u'Existe en la Corporación un SIG', max_length = 50)
    missigre = models.CharField(u'Nombre del Responsable SIG', max_length = 150)
    missiget = models.PositiveSmallIntegerField(u'Responsable SIG, Extensión')
    missrhex = models.BooleanField(u'Existe en la Corporación SIRH?')
    missrhns = models.CharField(u'Nombre del Sistema SIRH', max_length = 150)
    missrhde = models.CharField(u'Breve descripción del sistema SIRH', max_length = 500)
    missrhwe = models.BooleanField(u'Disponible para consulta vía Web el SIRH?')
    missrhur = models.URLField(u'Dirección electrónica del SIRH', null = True, blank = True)
    mislaexi = models.BooleanField(u'Existe en la Corporación un LA?')
    mislacon = models.NullBooleanField(u'Si no tiene LA, Tiene convenios con entidades para el uso de LA?')
    mislacoc = models.CharField('Especifique el convenio de LA', max_length = 150, null = True, blank = True)
    mislaacr = models.NullBooleanField(u'Si tiene LA, Se encuentra acreditado el LA?')
    mislaaea = models.CharField(u'Entidad acreditadora del LA', max_length = 150, null = True, blank = True)
    mislares = models.CharField(u'Número de resolución del LA', max_length = 50, null = True, blank = True)
    misladat = models.DateField(u'Fecha de Acreditación del LA', null = True, blank = True)
    mislapar = models.CharField(u'Parámetros acreditados del LA', max_length = 200, null = True, blank = True)
    mislapro = models.CharField(u'Procesos acreditados del LA', max_length = 200, null = True, blank = True)
    misrmaex = models.BooleanField(u'La Corporación dispone de RMA?')
    misrmaco = models.NullBooleanField(u'Si no tiene RMA. Tiene convenios con entindades para RMA?')
    misrmacc = models.CharField('Especifique el convenio de RMA', max_length = 150, null = True, blank = True)
    misrmana = models.NullBooleanField(u'Está asociada a una RMA nacional?')
    misrmano = models.CharField(u'Nombre de RMA nacional', max_length = 150, null = True, blank = True)
    misrmaed = models.CharField(u'Estaciones definidas de RMA', max_length = 150, null = True, blank = True) 
    misrmapm = models.CharField(u'Parámetros monitoreo de RMA', max_length = 150, null = True, blank = True) 
    misrmcex = models.BooleanField(u'La Corporación dispone de RMC?')
    misrmcco = models.NullBooleanField(u'Si no tiene RMC. Tiene convenios con entindades para RMC?')
    misrmccc = models.CharField('Especifique el convenio de RMC', max_length = 150, null = True, blank = True)
    misrmced = models.CharField(u'Estaciones definidas de RMC', max_length = 150, null = True, blank = True) 
    misrmcpm = models.CharField(u'Parámetros monitoreo de RMC', max_length = 150, null = True, blank = True) 
    misrmhex = models.BooleanField(u'La Corporación dispone de RMH?')
    misrmhco = models.NullBooleanField(u'Si no tiene RMC. Tiene convenios con entindades para RMC?')
    misrmhcc = models.CharField('Especifique el convenio de RMH', max_length = 150, null = True, blank = True)
    misrmhed = models.CharField(u'Estaciones definidas de RMH', max_length = 150, null = True, blank = True) 
    misrmhpm = models.CharField(u'Parámetros monitoreo de RMH', max_length = 150, null = True, blank = True) 

class minssotesigpc(models.Model):
    '''
    
    Characterization:
        - Form: Matriz Institucional
        - Tab: Sop Tec 
        - Title: Soporte Técnico
        - Subtitle : SIG. Equipos de cómputo para el proceso SIG disponibles en la corporación.
    '''
    misotepc = models.ForeignKey('minssopotecni', verbose_name = u'Soporte técnico')
    mistpcpr = models.CharField(u'Procesador', max_length = 150)
    mistpcra = models.CharField(u'RAM', max_length = 150)
    mistpcdd = models.CharField(u'Disco Duro', max_length = 150)
    mistpcgc = models.CharField(u'Tarjeta de Video', max_length = 150)
    mistpcos = models.CharField(u'Sistema Operativo', max_length = 150)
    mistpcps = models.CharField(u'Procesamiento', max_length = 150)
    mistpcim = models.CharField(u'Interpretación de imágenes', max_length = 150)

class minssoptechrs(models.Model):
    '''
    
    Characterization:
        - Form: Matriz Institucional
        - Tab: Sop Tec 
        - Title: Soporte Técnico
        - Subtitle : Personal involucrado con la operación de los diversos sistemas de información y plantas técnicas.
    '''
    INFO_SYSTEMS = (
        ('SIG', 'SIG'),
        ('SIRH', 'SIRH'),
        ('LA', 'LA'),
        ('RMA', 'RMA'),
        ('RMC', 'RMC'),
        ('RMH', 'RMH'),
    )
    misotehr = models.ForeignKey('minssopotecni', verbose_name = u'Soporte técnico')
    misthrcl = models.CharField(u'Operación del:', max_length = 5)
    misthrno = models.CharField(u'Nombre', max_length = 150)
    misthrpr = models.CharField(u'Profesión', max_length = 150)
    misthrpg = models.CharField(u'Posgrado', max_length = 150, null = True)
    misthrca = models.CharField(u'Cargo', max_length = 150)
    misthrtv = models.CharField(u'Tipo de Vinculación', max_length = 150)
    misthrtd = models.PositiveIntegerField(u'Tiempo de dedicación')
    misthrfr = models.CharField(u'Otras funciones no relacionadas', max_length = 150)

class minsrecurhuma(models.Model):
    '''
    
    Characterization:
        - Form: Matriz Institucional
        - Tab: POMCAS
        - Title: Recursos Humanos 
        - Subtitle: Comisión de ordenamiento territorial - POMCAS.
    '''
    mipocasc = models.ForeignKey('minstdatgene', related_name = u'Corporation')
    mipomcex = models.BooleanField(u'Existe en la Corporación equipo de trabajo o comité de ordenamiento territorial con funión de POMCA?')
    mipomcac = models.CharField(u'Tipo de acto adminstración para la adopción',
                                max_length = 25, null = True, blank = True)
    mipomcno = models.CharField(u'Número de acto admin', max_length = 50, 
                                null = True, blank = True)
    mipomcda = models.DateField(u'Fecha de acto admin', null = True, blank = True)
    mipomcde = models.CharField(u'Nombre del delegado de la Corporación a la Comisión departamental de Ordenamiento territorial', 
                                max_length = 120, null = True, blank = True)
    mipomcdc = models.CharField(u'Cargo del delegado', max_length = 120,
                                null = True, blank = True)
    mipomcdm = models.EmailField(u'Correo del delegado', null = True, 
                                blank = True) 

class minsrhvinpomc(models.Model):
    '''
    
    Characterization:
        - Form: Matriz Institucional
        - Tab: POMCAS
        - Title: Recursos Humanos.
        - Subtitle: Personal vinculado con el proceso de POMCAS.
            Funcionarios Responsables del proceso de gestión de POMCAS. 
            Funcionarios Involucrados en el proceso de gestión de POMCAS.
            Funcionarios Responsables del proceso de gestión del Riesgo.
            Funcionarios Involucrados en el proceso de gestión del Riesgo.
            Funcionarios Responsables del proceso de Participación.
            Funcionarios Involucrados en el proceso de Participación.
            Funcionarios Involucrados en Otras temáticas.
    '''
    FUNCIONARIOS=(
        ('RESPOMC', 'Responsable POMCA'),
        ('INVPOMC', 'Involucrado POMCA'),
        ('RESRIES', 'Responsable Riesgo'),
        ('INVRIES', 'Involucrado Riesgo'),
        ('RESPART', 'Responsable Participación'),
        ('INVPART', 'Involucrado Participación'), 
        ('INVOTEM', 'Involucrado Otras temáticas'),
    )
    mirhpomc = models.ForeignKey('minsrecurhuma', verbose_name = u'Recursos Humanos POMCA')
    mirhpopc = models.CharField(u'Proceso', max_length = 6)
    mirhpono = models.CharField(u'Nombre', max_length = 120)
    mirhpopr = models.CharField(u'Profesión', max_length = 120) 
    mirhpoec = models.CharField(u'Estudios complementarios',max_length = 120, 
                         null = True, blank = True) 
    mirhpoca = models.CharField(u'Cargo', max_length = 120) 
    mirhpotv = models.CharField(u'Tipo de vinculación', max_length = 50) 
    mirhpoof = models.CharField(u'Subdirección u oficina', max_length = 120) 
    mirhpodi = models.CharField(u'Dirección y/o coordinación de área',
                         max_length = 120) 
    mirhpotd = models.PositiveSmallIntegerField(u'Tiempo de dedicación', 
                         null = True, blank = True)
    mirhporo = models.CharField(u'Rol / Función en el preaprestamiento', 
                         max_length = 120, null = True, blank = True) 
    mirhpoot = models.CharField(u'Otras Funciones relacionadas con el POMCA ', 
                         max_length = 120, null = True, blank = True) 
    mirhpote = models.CharField(u'Temática a la que se encuentra adscrito', 
                         max_length = 120, null = True, blank = True) 
 
