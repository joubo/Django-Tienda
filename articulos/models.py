#encoding:utf-8
from django.db import models

# Create your models here.

class Categoria(models.Model):
	nombre = models.CharField(max_length=30, unique = True, default = '')
	imagen = models.ImageField(upload_to='categorias', verbose_name='Imagen', default = '')

	descripcion = models.TextField(blank = True, null = True)

	def __unicode__(self):
		return self.nombre


class Fabricante(models.Model):
	nombre = models.CharField(max_length=30, unique = True, default = '')
	imagen = models.ImageField(upload_to='fabricantes', verbose_name='Imagen', default = '')


	def __unicode__(self):
		return self.nombre

class Articulo(models.Model):
	nombre = models.CharField(max_length=30, unique = True, null = False, default='')
	descripcion = models.TextField(blank = True, null = True)
	imagen = models.ImageField(upload_to='articulos', verbose_name='Imagen', default = '')
	precio = models.DecimalField(default=0, max_digits=6, decimal_places=2)
	descuento = models.IntegerField(default=0)
	stock = models.IntegerField(default=0)
	categoria = models.ForeignKey(Categoria, related_name='art_cat', default = '')
	fabricante = models.ForeignKey(Fabricante, related_name='art_fab', default = '')

	def __unicode__(self):
		return self.nombre

