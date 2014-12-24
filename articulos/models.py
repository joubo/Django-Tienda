#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Articulo(models.Model):
      
	#idArticulo = models.CharField(max_length=50, unique=True)
	nombre = models.TextField(max_length=15)
	categoria = models.IntegerField(default = 0)
	precio = models.IntegerField()
	descripcion = models.TextField()
	imagen = models.ImageField(upload_to='articulos', verbose_name='Imagen')
	stock = models.IntegerField()

	def __unicode__(self):
		return self.id
