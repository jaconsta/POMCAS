#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
import settings

# Enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'usuarios.views.infouser', name='cargando'),
    url(r'^matrix/$', 'usuarios.views.matrixlist', name = 'Matrix_list'),
    #Matriz Upload
    url(r'^matrix/(?P<matrix>\w+)/capture', 
        'regist_carga.views.Recolection', 
        name='matrix_upload'),
#    #Matriz Institucional
#    url(r'^matrix/institucional/capture', 
#        'regist_carga.views.RecolInstitucional', 
#        name='matrix_institucional_upload'),
#    #Matriz Cartográfica
#    url(r'^matrix/cartografica/capture', 'regist_carga.views.RecolCartografic', 
#        name='matrix_cartografica_upload'),
    url(r'^matrix/cartografica/reports/coporacion/$', 
        'matriz_cartografica.views.Consolidado', 
        name='matrix_cartografica_consolidado'),
    url(r'^matrix/cartografica/reports/planchas/$', 
        'matriz_cartografica.views.Planchas', 
        name='matrix_cartografica_planchas'),
#    #Matriz Información a identificar
#    url(r'^matrix/recoleccion_informacion/$', 
#            'matriz_recolinfo.views.CuencasDeCorpo', 
#            name ='matrix_recolinfo_cuencas'),
#    url(r'^matrix/recoleccion_informacion/(?P<shared_id>\d+)/upload/$', 
#            'matriz_recolinfo.views.recolinfo_form', 
#            name = 'matriz_recolinfo_upload'),
#    #Matriz Formatos de caracterización
    url(r'^matrix/caracterizacion/$',
        'matriz_infoidentifi.views.CuencasDeCorpo', 
        name = 'matrix_infoident_cuencas'),
    url(r'^matrix/caracterizacion/(?P<shared_id>\d+)/$',
        'matriz_infoidentifi.views.index', 
        name='matrix_infoident_index'),
    url(r'^matrix/caracterizacion/(?P<shared_id>\d+)/(?P<subcompo>\w+)/$',
        'matriz_infoidentifi.views.resume', 
        name='matrix_infoident_resume'),
    url(r'^matrix/caracterizacion/(?P<shared_id>\d+)/(?P<subcompo>\w+)/add/$',
        'matriz_infoidentifi.views.add', 
        name='matrix_infoident_add'),
    url(r'^matrix/caracterizacion/(?P<shared_id>\d+)/(?P<subcompo>\w+)/(?P<pk>\d+)/$',
        'matriz_infoidentifi.views.edit', 
        name='matrix_infoident_edit'),
    url(r'^matrix/caracterizacion/(?P<shared_id>\d+)/(?P<subcompo>\w+)/(?P<pk>\d+)/(?P<subtema>\w+)/$',
        'matriz_infoidentifi.views.subte', 
        name='matrix_infoident_subte'),
    url(r'^matrix/caracterizacion/(?P<shared_id>\d+)/(?P<subcompo>\w+)/(?P<pk>\d+)/(?P<subtema>\w+)/(?P<subte_pk>\d+)/$',
        'matriz_infoidentifi.views.subte', 
        name='matrix_infoident_subte_edit'),
    # Reports
    url(r'^reports/caracterizacion/Carto/$',
        'matriz_infoidentifi.views.ReportCartog',
        name = 'reports_infoident_cartog'),
    # Budget
    url(r'^matrix/budget/recieve', 'matriz_presupuestos.views.GetForm',
        name = 'matriz_presupu_recieve'),
    # Users management
    url(r'^login/', 'usuarios.views.loginuser', name='start_session'),
    url(r'^logout/', 'usuarios.views.logoutuser', name='close_session'),
    url(r'^adduser/', 'usuarios.views.newuser', name = 'create_user'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Admin:
    url(r'^admin/', include(admin.site.urls)),
    #(r'^%s/' % settings.SUB_SITE, include('asocarssgi.urls_subsite')),
)
