from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from .forms import RegistroUsuario, EditarUsuario
from .models import UsuarioPerfil
from django.contrib.auth.models import User



#Prueba
def prueba(request):
	return render_to_response('albumRegistrar.html',context_instance=RequestContext(request))

#Login Principal
def login_principal(request):
	return render_to_response('login_principal.html',context_instance=RequestContext(request))


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


#Registrar Usuario
def registro_usuario(request):
	if request.method == 'POST':
	    formulario = RegistroUsuario(request.POST, request.FILES)
	    if formulario.is_valid():
	        formulario.procesar_registro()
	contexto = {'formulario': RegistroUsuario()}
	return render_to_response('usuarioRegistrar.html',context_instance=RequestContext(request, contexto))
	

#Pagina de inicio despues de login
def principal_inicio(request,id_usuario):
	return render_to_response('principalinicio.html',context_instance=RequestContext(request))


#Crear Album
def registro_album(request):
	return render_to_response('albumRegistrar.html',context_instance=RequestContext(request))


#Modificar Album
def modificar_album(request):
	return render_to_response('albumModificar.html',context_instance=RequestContext(request))


#Ver Amigos
def ver_amigos(request):
	return render_to_response('verAmigos.html',context_instance=RequestContext(request))


#Ver Amigos
def ver_albumes(request):
	return render_to_response('verAlbumes.html',context_instance=RequestContext(request))

