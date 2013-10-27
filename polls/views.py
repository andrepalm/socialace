from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from .forms import RegistroUsuario, EditarUsuario, RegistroAlbum
from .models import UsuarioPerfil , Album , Calendario
from django.contrib.auth.models import User



#Prueba
def prueba(request):
	return render_to_response('albumRegistrar.html',context_instance=RequestContext(request))

#Pagina de inicio despues de login
@login_required
def principal_inicio(request):
    usuario = request.user
    contexto = {'usuario': usuario}
    return render_to_response('principalinicio.html',context_instance=RequestContext(request, contexto))

#Modificar usuario
def modificar_usuario(request,id_usuario):    
    usuario = get_object_or_404(User, id=id_usuario)
    if request.method == 'POST':
        formulario = EditarUsuario(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.modificar_registro(usuario)           
    form_data = {
        'usuario': usuario.username,
        'nombre': usuario.first_name,
        'apellido' : usuario.last_name,
        'nacimiento' : usuario.usuarioperfil.fechanacimiento,
        'direccion' : usuario.usuarioperfil.direccion,
        'twitter' : usuario.usuarioperfil.twitter,
        'facebook' : usuario.usuarioperfil.facebook,
        'correo' : usuario.email,
        'privacidad' : usuario.usuarioperfil.privacidad,
        'foto' : usuario.usuarioperfil.foto,
    }
    contexto = {'formulario': EditarUsuario(initial=form_data), 'usuario': usuario}
    return render_to_response('usuarioModificar.html',context_instance=RequestContext(request, contexto))

#Modificar Album
@login_required
def modificar_album(request,id_album):
    usuario = request.user
    album = get_object_or_404(Album,id=id_album)
    if request.method == 'POST':
        formulario = RegistroAlbum(request.POST, request.FILES)       
        if formulario.is_valid():
            formulario.modificar_album(album)
            
    form_data = {
        'nombre': album.nombre,
        'descripcion': album.descripcion,
        'privacidad' : album.privacidad,
        'foto' : album.foto,
    }
    contexto = {'formulario': RegistroAlbum(initial=form_data), 'usuario': usuario, 'album': album}
    return render_to_response('albumModificar.html',context_instance=RequestContext(request, contexto))


#Registrar Usuario
def registro_usuario(request):
	if request.method == 'POST':
	    formulario = RegistroUsuario(request.POST, request.FILES)
	    if formulario.is_valid():
	        formulario.procesar_registro()
	contexto = {'formulario': RegistroUsuario()}
	return render_to_response('usuarioRegistrar.html',context_instance=RequestContext(request, contexto))
	

#Crear Album
@login_required
def registro_album(request): 
    usuario = request.user
    if request.method == 'POST':
        formulario = RegistroAlbum(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.procesar_album(usuario)
            return HttpResponseRedirect(reverse('principalInicio'))   
    contexto = {'formulario': RegistroAlbum(),'usuario': usuario}
    return render_to_response('albumRegistrar.html',context_instance=RequestContext(request, contexto))
	
	
#Ver Amigos
def ver_amigos(request):
    contexto = {'usuario': usuario}
    return render_to_response('verAmigos.html',context_instance=RequestContext(request, contexto))

#Ver Albumes
@login_required
def ver_albumes(request):
    usuario = request.user
    albumes = Album.objects.filter(fkusuario=usuario)
    contexto = {'albumes': albumes,'usuario': usuario}
    return render_to_response('verAlbumes.html',context_instance=RequestContext(request,contexto))
