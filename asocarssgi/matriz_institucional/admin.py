#-*- coding: utf-8 -*-
#from django.utils.functional import curry
from  django.forms.models import BaseInlineFormSet
from django.contrib import admin

from matriz_institucional.models import minstportada #Portada
from matriz_institucional.models import minstdatgene #Datos generales
from matriz_institucional.models import minstestdire, minstedcorpa, minstedcondi #Est Directiva
from matriz_institucional.models import minstorganiz, minesorasesd#Organizacion
from matriz_institucional.models import minesorsudico, minesorsubdir #Organizacion
from matriz_institucional.models import minstdescentr, midesceoficte #Descentralización
from matriz_institucional.models import minstplanific, minstplanpgar #Planeacion
from matriz_institucional.models import minsplanpaime, minstplanpdai #Planeacion
from matriz_institucional.models import minspresupues, minspresactad, minsprespomca #presupuesto
from matriz_institucional.models import minssopotecni, minssotesigpc, minssoptechrs #Sop Tec 
from matriz_institucional.models import minsrecurhuma, minsrhvinpomc #POMCAS

#Portada 
class PortadaAdmin(admin.ModelAdmin):
    list_display = ['getnit', 'mipofede', 'mipofeha', 'mipoprof'] 
    
    def getnit(self, obj):
        return '%s'%(obj.mipodatg.midginit)
    getnit.short_description = u'Corporación'

#Datos generales
class DatGeneAdmin(admin.ModelAdmin):
    list_display =['midgrazs', 'midgenit', 'midgcity', 'midgphon']
    fieldsets = (
        ('Logo', {
            'fields': (('midglogo', 'midgmanl'),)
        }),
        (None, {
            'fields': ('midgrazs', ('midgenit', 'midgnitd'), 'midginit', 
                'midgaddr', 'midgcity', ('midgssop', 'midgsscl', ), 
                ('midgapdf', 'midgapdt',),('midgphin', 'midgphon',), 'midgwebp',
                'midgmail', 'midgarju', 'midgnumj' )
        }),
    )

#Est Directiva
class AsamblyAdmin(admin.TabularInline):
    model = minstedcorpa
    extra = 1
class CounsilAdmin(admin.TabularInline):
    model = minstedcondi 
    extra = 1

class EstDirectAdmin(admin.ModelAdmin):
#    list_display =['miedcorp', 'miediceo', 'getnit']
    list_display =['getnit', 'miediceo'] 
    inlines = [AsamblyAdmin, CounsilAdmin]
    
    def getnit(self, obj):
        return '%s'%(obj.miedcorp.midginit)
    getnit.short_description = u'Corporación'

#Organizacion
class AsesoDirecAdmin(admin.TabularInline):
    model = minesorasesd
    extra = 1
class SubdirecCorpAdmin(admin.TabularInline):
    model = minesorsubdir
    extra = 1
class CoordSubdirAdmin(admin.TabularInline):
    model = minesorsudico
    extra = 1

class OrganizAdmin(admin.ModelAdmin):
    list_display= ['getnit', 'mieoaata', 'mieoaano', 'mieofnrp', 
        'mieofnrn', 'mieofnfc'
    ]
    inlines = [AsesoDirecAdmin, SubdirecCorpAdmin]
    fieldsets = (
        (None, {
            'fields': ('mieoorga', )
        }),
        (u'ACTO ADMINISTRATIVO MEDIANTE EL CUAL SE CREA LA PLANTA VIGENTE', {
            'fields': (('mieoaata', 'mieoaano', 'mieoaada'), )
        }),
        (u'FINANCIACIÓN DEL COSTO ANUAL DE LA NÓMINA', {
            'fields': (('mieofnrp', 'mieofnrn', 'mieofnfc'), )
        }),
    )

    def getnit(self, obj):
        return '%s'%(obj.mieocorp.midginit)
    getnit.short_description = u'Corporación'

class SubdirecAdmin(admin.ModelAdmin):
    list_display = ['getnit', 'nuacto', 'mieosuof', 'mieosuno']
    inlines = [CoordSubdirAdmin]
    
    def getnit(self, obj):
        return '%s'%(obj.miesorsu.mieocorp.midginit)
    getnit.short_description = u'Corporación'
    
    def nuacto(self, obj):
        return '%s'%(obj.miesorsu.mieoaano)
    nuacto.short_description = u'Número de acto'

#Descentralización
class OficTerrAdmin(admin.StackedInline):
    model = midesceoficte
    extra = 1

class RegionalAdmin(admin.ModelAdmin):
    list_display = ['getnit',  'midesofi']
    inlines = [OficTerrAdmin]

    def getnit(self, obj):
        return '%s'%(obj.midesnco.midginit)
    getnit.short_description = u'Corporación'

#Planeacion
class CompPGARAdmin(admin.TabularInline):
    model = minstplanpgar
    extra = 1
class PlanPAIAdmin(admin.TabularInline):
    model = minstplanpdai
    max_num = 1
class MetaPOMCAdmin(admin.TabularInline):
    model = minsplanpaime
    extra = 1

class PGARAdmin(admin.ModelAdmin):
    list_display = ['getnit', 'mipltipg']
    inlines = [CompPGARAdmin, PlanPAIAdmin, MetaPOMCAdmin]
    fieldsets = (
        (u'Plan de Gestion Ambiental Regional', {
            'fields': ('miplpgar', ('mipltipg', 'miplpgpe', ), 
                ('miplpgaa', 'miplpgno', 'miplpgda',),
                'miplpamj', 'mipldiag',) 
        }),
    )

    def getnit(self, obj):
        return '%s'%(obj.miplanif.midginit)
    getnit.short_description = u'Corporación'

#class PAIAdmin(admin.ModelAdmin):
#    list_display = ['getnit', 'miplapai', 'miplaait']
#    inlines = [MetaPOMCAdmin]
#
#    def getpai(self, obj):
#        return '%s'%(obj.miplapai.miplaait)
#    getpai.short_description = u'PAI'
#    
#    def getnit(self, obj):
#        return '%s'%(obj.miplapa.imiplanif.midginit)
#    getnit.short_description = u'Corporación'

#Presupuesto
class PresupXIIIAdmin(admin.TabularInline):
    model = minspresactad
    extra = 1
class PresupPOMCAdmin(admin.TabularInline):
    model = minsprespomca
    extra = 1

class PresupuesAdmin(admin.ModelAdmin):
    list_display = ['getnit', 'miplprgp', 'miplgrge', 'miplgrip', 'miplgrie', 
        'miplgrsp', 'miplgrse'
    ]
    inlines = [PresupXIIIAdmin,PresupPOMCAdmin]
    fieldsets = (
        (u'Ejecución presupuestal 2012',{
            'fields':(('miplprgp', 'miplgrge', ),
                ('miplgrip', 'miplgrie', ), ('miplgrsp', 'miplgrse', ),
                ('miplgfrp', 'miplgfre', ), ('miplgfap', 'miplgfae', ),
            )
        }),
    )

    def getnit(self, obj):
        return '%s'%(obj.miplanpr.midginit)
    getnit.short_description = u'Corporación'

#Soporte Técnico
class SIGpcAdmin(admin.TabularInline):
    model = minssotesigpc
    extra = 1
class SopPeopAdmin(admin.TabularInline):
    model = minssoptechrs
    extra = 1
class SopPeopSIGFormset(BaseInlineFormSet):
    def clean(self):
        super(SopPeopSIGFormset, self).clean()
        for form in self.forms:
            form.cleaned_data['misthrcl'] = 'SIG'
            form.instance.misthrcl = form.cleaned_data['misthrcl']
    def save_new(self, form, commit=True):
        return super(SopPeopSIGFormset, self).save_new(form, commit=commit)
    def save_existing(self, form, instance, commit=True):
        return form.save(commit=commit)
class SopPeopSIGAdmin(admin.TabularInline):
    '''
    Personal invulucrado con la operación del Sistema de Información Geográfico
    '''
    model = minssoptechrs
    extra = 1
    formset = SopPeopSIGFormset
    exclude = ('misthrcl', )
    verbose_name = "7.2.1 Personal involucrado con la operación del Sistema de Información Geográfico"
    verbose_name_plural = verbose_name
    def queryset(self, request):
        return super(SopPeopSIGAdmin, self).queryset(request).filter(misthrcl = 'SIG')
class SopPeopLAFormset(BaseInlineFormSet):
    def clean(self):
        super(SopPeopLAFormset, self).clean()
        for form in self.forms:
            form.cleaned_data['misthrcl'] = 'LA'
            form.instance.misthrcl = form.cleaned_data['misthrcl']

    def save_new(self, form, commit=True):
        return super(SopPeopLAFormset, self).save_new(form, commit=commit)
    def save_existing(self, form, instance, commit=True):
        return form.save(commit=commit)
class SopPeopLAAdmin(admin.TabularInline):
    '''
    Personal involucrado con la operacion del Laboratorio de Aguas
    '''
    model = minssoptechrs
    extra = 1
    formset = SopPeopLAFormset
    exclude = ('misthrcl', )
    verbose_name = "7.2.2 Personal involucrado con la operación del Laboratorio de Aguas"
    verbose_name_plural = verbose_name
    def queryset(self, request):
        return super(SopPeopLAAdmin, self).queryset(request).filter(misthrcl = 'LA')
class SopPeopRMAFormset(BaseInlineFormSet):
    def clean(self):
        super(SopPeopRMAFormset, self).clean()
        for form in self.forms:
            form.cleaned_data['misthrcl'] = 'RMA'
            form.instance.misthrcl = form.cleaned_data['misthrcl']

    def save_new(self, form, commit=True):
        return super(SopPeopRMAFormset, self).save_new(form, commit=commit)
    def save_existing(self, form, instance, commit=True):
        return form.save(commit=commit)
class SopPeopRMAAdmin(admin.TabularInline):
    '''
    Personal involucrado con la operación dela Red de Monitoreo Ambiental
    '''
    model = minssoptechrs
    extra = 1
    formset = SopPeopRMAFormset
    exclude = ('misthrcl', )
    verbose_name = "7.2.3 Personal involucrado con la operación del Red de Monitoreo Ambiental"
    verbose_name_plural = verbose_name
    def queryset(self, request):
        return super(SopPeopRMAAdmin, self).queryset(request).filter(misthrcl = 'RMA')
class SopPeopRMCFormset(BaseInlineFormSet):
    def clean(self):
        super(SopPeopRMCFormset, self).clean()
        for form in self.forms:
            form.cleaned_data['misthrcl'] = 'RMC'
            form.instance.misthrcl = form.cleaned_data['misthrcl']

    def save_new(self, form, commit=True):
        return super(SopPeopRMCFormset, self).save_new(form, commit=commit)
    def save_existing(self, form, instance, commit=True):
        return form.save(commit=commit)
class SopPeopRMCAdmin(admin.TabularInline):
    '''
    Personal involucrado con la operación de la Red de Monitoreo Climatológica
    '''
    model = minssoptechrs
    extra = 1
    formset = SopPeopRMCFormset
    exclude = ('misthrcl', )
    verbose_name = "7.2.4 Personal involucrado con la operación del Red de Monitoreo Climatológica"
    verbose_name_plural = verbose_name
    def queryset(self, request):
        return super(SopPeopRMCAdmin, self).queryset(request).filter(misthrcl = 'RMC')
class SopPeopRMHFormset(BaseInlineFormSet):
    def clean(self):
        super(SopPeopRMHFormset, self).clean()
        for form in self.forms:
            form.cleaned_data['misthrcl'] = 'RMH'
            form.instance.misthrcl = form.cleaned_data['misthrcl']

    def save_new(self, form, commit=True):
        return super(SopPeopRMHFormset, self).save_new(form, commit=commit)
    def save_existing(self, form, instance, commit=True):
        return form.save(commit=commit)
class SopPeopRMHAdmin(admin.TabularInline):
    '''
    Personal involucrado con la operación de la Red de Monitoreo Hidrológica
    '''
    model = minssoptechrs
    extra = 1
    formset = SopPeopRMHFormset
    exclude = ('misthrcl', )
    verbose_name = "7.2.5 Personal involucrado con la operación del Red de Monitoreo Hidrológica"
    verbose_name_plural = verbose_name
    def queryset(self, request):
        return super(SopPeopRMHAdmin, self).queryset(request).filter(misthrcl = 'RMH')


class SopTecAdmin(admin.ModelAdmin):
    list_display = ['getnit', 'misoptec', 'missigex', 'missrhex', 'mislaexi', 'misrmaex', 
        'misrmcex', 'misrmhex'] 
    inlines = [SIGpcAdmin, SopPeopSIGAdmin, SopPeopLAAdmin, SopPeopRMAAdmin, 
        SopPeopRMCAdmin, SopPeopRMHAdmin]
    fieldsets = (
        (u'Datos básicos', {
            'fields': ('misoptec', 
            )
        }),
        (u'SISTEMA DE INFORMACIÓN GEOGRÁFICA', {
            'fields': ('missigex', 'missigre', 'missiget',
            )
        }),
        (u'SISTEMA DE INFORMACIÓN DEL RECURSO HÍDRICO', {
            'fields': (('missrhex', 'missrhns'), 'missrhde', 
                ('missrhwe', 'missrhur'), 
            )
        }),
        (u'LABORATORIO DE AGUAS', {
            'fields': ('mislaexi', ('mislacon', 'mislacoc'), 'mislaacr',
                ('mislaaea', 'mislares', 'misladat'), ('mislapar', 'mislapro'),
            )
        }),
        (u'RED DE MONITOREO AMBIENTAL', {
            'fields': ('misrmaex', ('misrmaco', 'misrmacc'), 
                ('misrmana', 'misrmano'), ('misrmaed', 'misrmapm'),
            )
        }),
        (u'RED DE MONITOREO CLIMATOLÓGICA', {
            'fields': ('misrmcex', ('misrmcco', 'misrmccc', ), 
                ('misrmced', 'misrmcpm',),
            )
        }),
        (u'RED DE MONITOREO HIDROLÓGICA', {
            'fields': ('misrmhex', ('misrmhco', 'misrmhcc', ),
                ('misrmhed', 'misrmhpm', ),
            )
        }),
    )

    def getnit(self, obj):
        return '%s'%(obj.misoptec.midginit)
    getnit.short_description = u'Corporación'

#POMCAS
class POMCAPeopRPFormset(BaseInlineFormSet):
    def clean(self):
        super(POMCAPeopRPFormset, self).clean()
        for form in self.forms:
            form.cleaned_data['mirhpopc'] = 'RESPOMC'
            form.instance.mirhpopc = form.cleaned_data['mirhpopc']
            
    def save_new(self, form, commit=True):
        return super(POMCAPeopRPFormset, self).save_new(form, commit=commit)

    def save_existing(self, form, instance, commit=True):
        return form.save(commit=commit)

class POMCAPeopRPAdmin(admin.TabularInline):
    model = minsrhvinpomc
    extra = 1
    formset = POMCAPeopRPFormset
    exclude = ('mirhpopc', )
    verbose_name = "8.1 FUNCIONARIOS RESPONSABLES DEL PROCESO DE GESTIÓN DE POMCAS"
    verbose_name_plural = verbose_name

    def queryset(self, request):
        return super(POMCAPeopRPAdmin, self).queryset(request).filter(mirhpopc = 'RESPOMC')

class POMCAPeopIPFormset(BaseInlineFormSet):
    def clean(self):
        super(POMCAPeopIPFormset, self).clean()
        for form in self.forms:
            form.cleaned_data['mirhpopc'] = 'INVPOMC'
            form.instance.mirhpopc = form.cleaned_data['mirhpopc']
            
    def save_new(self, form, commit=True):
        return super(POMCAPeopIPFormset, self).save_new(form, commit=commit)

    def save_existing(self, form, instance, commit=True):
        return form.save(commit=commit)

class POMCAPeopIPAdmin(admin.TabularInline):
    model = minsrhvinpomc
    extra = 1
    formset = POMCAPeopIPFormset
    exclude = ('mirhpopc', )
    verbose_name = "8.2 FUNCIONARIOS INVOLUCRADOS  EN EL PROCESO DE GESTIÓN DE POMCAS"
    verbose_name_plural = verbose_name

    def queryset(self, request):
        return super(POMCAPeopIPAdmin, self).queryset(request).filter(mirhpopc = 'INVPOMC')

class POMCAPeopRRFormset(BaseInlineFormSet):
    def clean(self):
        super(POMCAPeopRRFormset, self).clean()
        for form in self.forms:
            form.cleaned_data['mirhpopc'] = 'RESRIES'
            form.instance.mirhpopc = form.cleaned_data['mirhpopc']
            
    def save_new(self, form, commit=True):
        return super(POMCAPeopRRFormset, self).save_new(form, commit=commit)

    def save_existing(self, form, instance, commit=True):
        return form.save(commit=commit)

class POMCAPeopRRAdmin(admin.TabularInline):
    model = minsrhvinpomc
    extra = 1
    formset = POMCAPeopRRFormset
    exclude = ('mirhpopc', )
    verbose_name = "8.3 FUNCIONARIOS RESPONSABLES DEL PROCESO DE GESTIÓN DEL RIESGO"
    verbose_name_plural = verbose_name

    def queryset(self, request):
        return super(POMCAPeopRRAdmin, self).queryset(request).filter(mirhpopc = 'RESRIES')

class POMCAPeopIRFormset(BaseInlineFormSet):
    def clean(self):
        super(POMCAPeopIRFormset, self).clean()
        for form in self.forms:
            form.cleaned_data['mirhpopc'] = 'INVRIES'
            form.instance.mirhpopc = form.cleaned_data['mirhpopc']
            
    def save_new(self, form, commit=True):
        return super(POMCAPeopIRFormset, self).save_new(form, commit=commit)

    def save_existing(self, form, instance, commit=True):
        return form.save(commit=commit)

class POMCAPeopIRAdmin(admin.TabularInline):
    model = minsrhvinpomc
    extra = 1
    formset = POMCAPeopIRFormset
    exclude = ('mirhpopc', )
    verbose_name = "8.4 FUNCIONARIOS INVOLUCRADOS EN EL PROCESO DE GESTIÓN DEL RIESGO"
    verbose_name_plural = verbose_name

    def queryset(self, request):
        return super(POMCAPeopIRAdmin, self).queryset(request).filter(mirhpopc = 'INVRIES')

class POMCAPeopRPaFormset(BaseInlineFormSet):
    def clean(self):
        super(POMCAPeopRPaFormset, self).clean()
        for form in self.forms:
            form.cleaned_data['mirhpopc'] = 'RESPART'
            form.instance.mirhpopc = form.cleaned_data['mirhpopc']
            
    def save_new(self, form, commit=True):
        return super(POMCAPeopRPaFormset, self).save_new(form, commit=commit)

    def save_existing(self, form, instance, commit=True):
        return form.save(commit=commit)

class POMCAPeopRPaAdmin(admin.TabularInline):
    model = minsrhvinpomc
    extra = 1
    formset = POMCAPeopRPaFormset
    exclude = ('mirhpopc', )
    verbose_name = "8.5 FUNCIONARIOS RESPONSABLES DEL PROCESO DE PARTICIPACIÓN"
    verbose_name_plural = verbose_name

    def queryset(self, request):
        return super(POMCAPeopRPaAdmin, self).queryset(request).filter(mirhpopc = 'RESPART')

class POMCAPeopIPaFormset(BaseInlineFormSet):
    def clean(self):
        super(POMCAPeopIPaFormset, self).clean()
        for form in self.forms:
            form.cleaned_data['mirhpopc'] = 'INVPART'
            form.instance.mirhpopc = form.cleaned_data['mirhpopc']
            
    def save_new(self, form, commit=True):
        return super(POMCAPeopIPaFormset, self).save_new(form, commit=commit)

    def save_existing(self, form, instance, commit=True):
        return form.save(commit=commit)

class POMCAPeopIPaAdmin(admin.TabularInline):
    model = minsrhvinpomc
    extra = 1
    formset = POMCAPeopIPaFormset
    exclude = ('mirhpopc', )
    verbose_name = "8.6 FUNCIONARIOS INVOLUCRADOS EN EL PROCESO DE PARTICIPACIÓN"
    verbose_name_plural = verbose_name

    def queryset(self, request):
        return super(POMCAPeopIPaAdmin, self).queryset(request).filter(mirhpopc = 'INVPART')

class POMCAPeopITFormset(BaseInlineFormSet):
    def clean(self):
        super(POMCAPeopITFormset, self).clean()
        for form in self.forms:
            form.cleaned_data['mirhpopc'] = 'INVOTEM'
            form.instance.mirhpopc = form.cleaned_data['mirhpopc']
            
    def save_new(self, form, commit=True):
        return super(POMCAPeopITFormset, self).save_new(form, commit=commit)

    def save_existing(self, form, instance, commit=True):
        return form.save(commit=commit)

class POMCAPeopITAdmin(admin.TabularInline):
    model = minsrhvinpomc
    extra = 1
    formset = POMCAPeopITFormset
    exclude = ('mirhpopc', )
    verbose_name = "8.7 FUNCIONARIOS INVOLUCRADOS EN OTRAS TEMÁTICAS"
    verbose_name_plural = verbose_name

    def queryset(self, request):
        return super(POMCAPeopITAdmin, self).queryset(request).filter(mirhpopc = 'INVOTEM')

class POMCAAdmin(admin.ModelAdmin):
    list_display = ['getnit', 'mipomcex', 'mipomcde', 'mipomcdm']
    inlines = [POMCAPeopRPAdmin, POMCAPeopIPAdmin, POMCAPeopRRAdmin, POMCAPeopIRAdmin, POMCAPeopRPaAdmin, POMCAPeopIPaAdmin, POMCAPeopITAdmin]

    def getnit(self, obj):
        return '%s'%(obj.mipocasc.midginit)
    getnit.short_description = u'Corporación'

admin.site.register(minstportada, PortadaAdmin)
admin.site.register(minstdatgene, DatGeneAdmin)
admin.site.register(minstestdire, EstDirectAdmin)
admin.site.register(minstorganiz, OrganizAdmin)
admin.site.register(minesorsubdir, SubdirecAdmin)
admin.site.register(minstdescentr, RegionalAdmin)
admin.site.register(minstplanific, PGARAdmin)
#admin.site.register(minstplanpdai, PAIAdmin)
admin.site.register(minspresupues, PresupuesAdmin)
admin.site.register(minssopotecni, SopTecAdmin)
admin.site.register(minsrecurhuma, POMCAAdmin)
