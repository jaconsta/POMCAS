from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'asocarssgi.views.home', name='home'),
    # url(r'^asocarssgi/', include('asocarssgi.foo.urls')),
    url(r'^matrix/institucional/', 'matriz_institucional.views.upload_matrix', name='matrix_institucional_home'),
    url(r'^matrix/institucional/upload', 'matriz_institucional.views.upload_matrix', name='matrix_institucional_upload'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
