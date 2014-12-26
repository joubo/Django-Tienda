#encoding:utf-8
from django.db import models

# Create your models here.

class Categoria(models.Model):
	nombre = models.TextField(max_length=15, unique = True)
	descripcion = models.TextField()

	def __unicode__(self):
		return self.nombre

class Articulo(models.Model):
      
	nombre = models.TextField(max_length=15)
	precio = models.IntegerField()
	descripcion = models.TextField()
	#imagen = models.ImageField(upload_to='articulos', verbose_name='Imagen')
	stock = models.IntegerField()
	categoria = models.ForeignKey(Categoria, related_name='art_cat')

	def __unicode__(self):
		return self.nombre


