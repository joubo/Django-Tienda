from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


# Create your models here.

class Usuario(models.Model):

	username  =  models.CharField(max_length=30, unique = True)
	nombre = models.CharField(max_length=30, blank=True, default='')
	apellidos  = models.CharField(max_length=30, blank=True, default='')
	email = models.EmailField()
	password = models.CharField(max_length=20)
	dni = models.CharField(max_length=9)
	direccion = models.CharField(max_length=50)
	created_time = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.username


class UsuarioForm(ModelForm):
    
	class Meta:
		model = Usuario
		exclude = [] 