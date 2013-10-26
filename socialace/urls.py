#coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'socialace.views.home', name='home'),
    # url(r'^socialace/', include('socialace.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^loginPrincipal/$', 'polls.views.login_principal', name='login'),
    url(r'^prueba/$', 'polls.views.prueba', name='prueba'),
    url(r'^registroUsuario/$', 'polls.views.registroUsuario', name='registroUsuario'),
    url(r'', include('social_auth.urls')),
    url(r'^principal/$', 'polls.views.principalInicio', name='principalInicio'),
    url(r'^modificarUsuario/$', 'polls.views.modificarUsuario',name ='modificarUsuario'),
    url(r'^modificarAlbum/$', 'polls.views.modificarAlbum',name ='modificarAlbum'),
    url(r'^registroAlbum/$', 'polls.views.registroAlbum',name ='registroAlbum'),
    
)
