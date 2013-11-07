from django.conf.urls import patterns, include, url
import settings

# Enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', 'matriz_institucional.views.upload_matrix', name='matrix_institucional_home'),
    url(r'^$', 'regist_carga.views.RecolCartografic', name='cargando'),
    url(r'^matrix/institucional/capture', 'regist_carga.views.RecolInstitucional', name='matrix_institucional_upload'),
    url(r'^matrix/cartografica/capture', 'regist_carga.views.RecolCartografic', name='matrix_institucional_upload'),
    url(r'^matrix/recoleccion_informacion/$', 
            'matriz_recolinfo.views.CuencasDeCorpo', name ='matrix_recolinfo_cuencas'),
    url(r'^matrix/recoleccion_informacion/(?P<shared_id>\d+)/upload/$', 
            'matriz_recolinfo.views.recolinfo_form', name = 'matriz_recolinfo_upload'),
    url(r'^login/', 'usuarios.views.loginuser', name='start_sesion'),
    url(r'^logout/', 'usuarios.views.logoutuser', name='close_sesion'),
    url(r'^adduser/', 'usuarios.views.newuser', name = 'create_user'),
    #url(r'^b/', 'regist_carga.views.modelo', name='cargando'),
    #url(r'^proyecto85/b/', 'regist_carga.views.modelo', name='cargandos'),
    #url(r'^info/', 'matriz_recolinfo.views.recolinfo_form', name='recolinfo'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #(r'^%s/' % settings.SUB_SITE, include('asocarssgi.urls_subsite')),
)
