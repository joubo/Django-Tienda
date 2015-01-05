from django.db import models
from articulos.models import Articulo
from django.contrib.auth.models import User

# Create your models here.

class Pedido(models.Model):
	usuario = models.ForeignKey(User, related_name = 'Ped_User')
	#fecha = models.DateField(auto_now_add = True)
	total = models.DecimalField(default=0, max_digits=6, decimal_places=2)
	ESTADO_PEDIDO = (
			('PA','Pagado'),
			('PE', 'Pendiente'),
		)
	estado = models.CharField(max_length = 2, choices = ESTADO_PEDIDO, default = 'PE')

	def __unicode__(self):	
		return unicode(self.id)

class DetallePedido(models.Model):
	pedido = models.ForeignKey(Pedido, related_name = 'DeP_Ped')
	articulo = models.ForeignKey(Articulo, related_name = 'DeP_Art')
	cantidad = models.IntegerField(default=1)

	def __unicode__(self):	
		return unicode(self.id)


class Factura(models.Model):
	pedido = models.ForeignKey(Pedido, related_name = 'Fac_Ped')
	fecha = models.DateField(auto_now_add = True)

	# def Pagado(request, pedido):
	# 	p = Pedido.objects.get(pk=pedido)
	# 	p.estado = 'PA'
	# 	p.save()

	def __unicode__(self):	
		return unicode(self.id)

