#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class usuarioPerfil(models.Model):
	fkusuario = models.OneToOneField(User)
	fechanacimiento	= models.CharField(max_length=50)
	direccion = models.CharField(max_length=100)
	twitter = models.CharField(max_length=50)
	facebook = models.CharField(max_length=50)
	privacidad = models.CharField(max_length=50)
	foto = models.ImageField(upload_to='imagenusuario', null=True,blank=True)

	def __str__(self):
		return self.usu_nombre


class calendario(models.Model):
	fecha = models.DateTimeField('date published')

	def __str__(self):
		return self.cal_fecha


class instagram(models.Model):
	url = models.CharField(max_length=200)

	def __str__(self):
		return self.ins_url


class soundcloud(models.Model):
	url = models.CharField(max_length=200)

	def __str__(self):
		return self.sou_url


class youtube(models.Model):
	url = models.CharField(max_length=200)

	def __str__(self):
		return self.you_url


class album(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=200)
	privacidad = models.BooleanField(default= True)
	foto = models.ImageField(upload_to='imagenalbum')
	fkusuario = models.ForeignKey(usuarioPerfil)
	fkcalendario = models.ForeignKey(calendario)

	def __str__(self):
		return self.alb_nombre


class comentario(models.Model):
	descripcion	= models.CharField(max_length=200)
	fkemisor = models.ForeignKey(usuarioPerfil)
	fkalbum	= models.ForeignKey(album)
	fkinstagram	= models.ForeignKey(instagram)
	fkyoutube = models.ForeignKey(youtube)
	fksoundcloud = models.ForeignKey(soundcloud)
	fkcalendario = models.ForeignKey(calendario)
	
	def __str__(self):
		return self.com_descripcion


class meGusta(models.Model):
	like = models.CharField(max_length=200)
	fkemisor = models.ForeignKey(usuarioPerfil)
	fkalbum	= models.ForeignKey(album)
	fkinstagram	= models.ForeignKey(instagram)
	fkyoutube = models.ForeignKey(youtube)
	fksoundcloud = models.ForeignKey(soundcloud)
	fkcalendario = models.ForeignKey(calendario)

	def __str__(self):
		return self.mgu_like

class notificacion(models.Model):
	fkemisor = models.ForeignKey(usuarioPerfil)
	fkalbum	= models.ForeignKey(album)
	fkinstagram	= models.ForeignKey(instagram)
	fkyoutube = models.ForeignKey(youtube)
	fksoundcloud = models.ForeignKey(soundcloud)
	fkcalendario = models.ForeignKey(calendario)
	def __str__(self):
		return self.not_id

class relacionNotificacion(models.Model):
	fknotificacion = models.ManyToManyField(notificacion)

	def __str__(self):
		return self.mgu_like

class relacionComentario(models.Model):
	fkcomentario = models.ManyToManyField(comentario)

	def __str__(self):
		return self.mgu_like
