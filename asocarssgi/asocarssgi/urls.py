#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
import settings

# Enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'usuarios.views.infouser', name='cargando'),
    url(r'^matrix/$', 'usuarios.views.matrixlist', name = 'Matrix_list'),
    #Matriz Institucional
    url(r'^matrix/institucional/capture', 
            'regist_carga.views.RecolInstitucional', 
            name='matrix_institucional_upload'),
    #Matriz Cartográfica
    url(r'^matrix/cartografica/capture', 'regist_carga.views.RecolCartografic', 
            name='matrix_institucional_upload'),
    url(r'^matrix/cartografica/consolidado/$', 
            'matriz_cartografica.views.Consolidado', 
            name='matrix_cartografica_consolidado'),
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
            'matriz_infoidentifi.views.list', 
            name = 'matrix_infoident_list'),
    url(r'^matrix/caracterizacion/(?P<shared_id>\d+)/add/$',
            'matriz_infoidentifi.views.addi', 
            name = 'matrix_infoident_add'),
    url(r'^matrix/caracterizacion/(?P<shared_id>\d+)/add/(?P<subcompo>\w+)/$',
            'matriz_infoidentifi.views.add', 
            name = 'matrix_infoident_add'),
    #Administración Usuarios
    url(r'^login/', 'usuarios.views.loginuser', name='start_sesion'),
    url(r'^logout/', 'usuarios.views.logoutuser', name='close_sesion'),
    url(r'^adduser/', 'usuarios.views.newuser', name = 'create_user'),
    #url(r'^$', 'matriz_institucional.views.upload_matrix', name='matrix_institucional_home'),
    #url(r'^b/', 'regist_carga.views.modelo', name='cargando'),
    #url(r'^proyecto85/b/', 'regist_carga.views.modelo', name='cargandos'),
    #url(r'^info/', 'matriz_recolinfo.views.recolinfo_form', name='recolinfo'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #(r'^%s/' % settings.SUB_SITE, include('asocarssgi.urls_subsite')),
)
