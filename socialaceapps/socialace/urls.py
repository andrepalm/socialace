#coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
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
    url(r'^loginPrincipal/$', login,{'template_name':'login_principal.html'}, name='login'),
    url(r'^prueba/$', 'polls.views.prueba', name='prueba'),
    url(r'^registroUsuario/$', 'polls.views.registro_usuario', name='registroUsuario'),
    url(r'^principalInicio/$', 'polls.views.principal_inicio', name='principalInicio'),
    url(r'^modificarUsuario/(?P<id_usuario>\d+)/$', 'polls.views.modificar_usuario',name ='modificarUsuario'),
    
    url(r'^modificarAlbum/(?P<id_album>\d+)/$', 'polls.views.modificar_album',name ='modificarAlbum'),
    
    url(r'^registroAlbum/$', 'polls.views.registro_album',name ='registroAlbum'),
    url(r'^verAmigos/$', 'polls.views.ver_amigos',name ='verAmigos'),
    url(r'^verAlbumes/$', 'polls.views.ver_albumes',name ='verAlbumes'),
    url(r'^logout/$', logout, {'next_page': '/loginPrincipal/'} ,name='logout'),
	url(r'', include('social_auth.urls')),    
    
)
