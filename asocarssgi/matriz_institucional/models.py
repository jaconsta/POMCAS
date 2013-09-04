# -*- coding: utf-8 -*-
from django.db import models

class busigendata(models.Model):    
    '''
    Corporation general data.
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
    gbuslogo = models.ImageField(u'Logo', upload_to = 'img/business/', 
                            height_field = None, width_field = None) #Corporation logo
    gbusrazs = models.CharField(u'Nombre de la corporaciÃ³n', max_length = 50)    #Corporation Name
    gbusnnit = models.IntegerField(u'NIT')                #NIT
    gbusnitd = models.IntegerField(u'NIT DV')                #Headquarters Address
    gbusinit = models.CharField(u'Sigla', max_length = 20)    #Initials
    gbusaddr = models.CharField(u'direcciÃ³n de sede principal', max_length = 50)    #Headquarters address
    gbuscity = models.CharField(u'Ciudad', max_length = 20)    #City
    gbusssop = models.TimeField(u'Horario de atenciÃ³n. De')                   #Service schedule, openning
    gbussscl = models.TimeField(u'A')                   #Service schedule, close
    gbusapdf = models.CharField(u'DÃ­as de atenciÃ³n al pÃºblico', max_length = 3,
                                choices = WEEKDAYS_ES,
                                default = MONDAY)   #Public Attention days, from
    gbusapdt = models.CharField(u'A', max_length = 3,
                                choices = WEEKDAYS_ES,
                                default = FRIDAY)   #Public Attention days, to
    gbusphon = models.IntegerField(u'TelÃ©fono (PBX)')                #Phone (PBX)
    gbuswebp = models.URLField(u'PÃ¡gina Web')                    #Webpage
    gbusmail = models.EmailField(u'Correo electrÃ³nico de contacto')                  #email contact.
    gbusarju = models.CharField(u'Ãrea de JurisdicciÃ³n', max_length = 50)    #Area of jurisdiction
    gbusnumj = models.IntegerField(u'NÃºmero de municipios de la jurisdicciÃ³n')                #Number of municipalities in the area of jurisdiction
    gbusscda = models.DateField(auto_now_add = True)    #Creation date on our system
    
    class Meta:
        verbose_name = 'Datos generales de la coporaciÃ³n'
        verbose_name_plural = 'Datos generales de las corporaciones'

    def __unicode__(self):
        return u'%s, %s, %s, %s, %s, %s, %s, %s, %s' %(self.gbusrazs, self.gbusinit, 
            self.gbusaddr, self.gbuscity, self.gbusapdf, self.gbusapdt, 
            self.gbuswebp, self.gbusmail ,self.gbusarju)

class busdirstru(models.Model):     
    '''
    Corporation Directive Structure
    '''
    bdscorpp = models.ForeignKey('busigendata', verbose_name = 'empresa')     #Corporation
    bdsceona = models.CharField(u'nombre del director general de la corporaciÃ³n',
                                max_length = 50)    #CEO name
    bdscdatp = models.DateField(u'Fecha de posesiÃ³n del actual director')                   #CEO Posession Date
    bdsceoip = models.BooleanField(u'Director general estÃ¡ activo?', 
                                default = True)                #CEO currently posessed? 
    
    class Meta: 
        verbose_name = 'estructura directiva de la corporaciÃ³n'
        verbose_name_plural = 'estructura directiva de las corporaciones'
    def __unicode__(self):
        return self.bdsceona

class bdscopassm(models.Model):     
    '''
    Conformation of the Directive assembly
    '''
    bdscadis = models.ForeignKey('busdirstru')      #Corpation Directive Structure
    bdscadep = models.CharField(u'Departamento', max_length = 25)    #Department
    bdsmayon = models.IntegerField(u'NÃºmero de alcaldes')            #Number of mayors

    class Meta: 
        verbose_name = 'ConformaciÃ³n de la asamblea directiva'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.bdscadep

class bdscadirco(models.Model):
    '''
    Conformation of the board of directors 
    '''
    bdscadis = models.ForeignKey('busdirstru')      #Corpation Directive Structure
    bdscasec = models.CharField(u'Sector representado', max_length = 20)    #Represented sector
    bdscacna = models.CharField(u'Nombre de consejo', max_length = 32)    #Council Name
    bdscaent = models.CharField(u'Entidad / Empresa / Gremio', max_length = 50)    #Entity, Business, guild

    class Meta:
        verbose_name = 'ConformaciÃ³n del consejo directivo'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s, %s, %s' %(self.bdscasec, self.bdscacna, self.bdscaent)

class busifinanc(models.Model):
    '''
    Business financial records
    '''
    YEAR_CHOICES=(
        (2009 , '2009'),
        (2010 , '2010'),
        (2011 , '2011'),
        (2012 , '2012'),
        (2013 , '2013'),
    )
    bufibusi = models.ForeignKey('busigendata', verbose_name = 'empresa')
    bufiyear = models.IntegerField(u'aÃ±o', choices = YEAR_CHOICES,
                                    default = 2013)
    bufiacti = models.FloatField(u'total activos del aÃ±o')

    class Meta:
        verbose_name = 'Activos financieros'
        verbose_name_plural = verbose_name

