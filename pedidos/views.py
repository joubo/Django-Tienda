from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, View, DetailView, CreateView, DeleteView, UpdateView
from pedidos.models import Pedido, DetallePedido, Factura
from articulos.models import Articulo
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy

# Create your views here.

def agregarPedido(request, articulo_id):
	try:
		pedido = Pedido.objects.get(usuario = request.user, estado = 'PE')

	except Pedido.DoesNotExist:
		pedido = Pedido()
		pedido.usuario = request.user
		

	articulo = Articulo.objects.get(id = articulo_id)
	pedido.total = pedido.total + articulo.precio
	pedido.save()

	try:
		detallePedido = DetallePedido.objects.get(pedido = pedido.id, articulo = articulo_id)
		detallePedido.cantidad = detallePedido.cantidad + 1

	except DetallePedido.DoesNotExist:

		detallePedido = DetallePedido()
		detallePedido.pedido = pedido
		detallePedido.articulo = articulo
	
	detallePedido.save()

	detallePedidos = DetallePedido.objects.filter(pedido = pedido.id)
	context = { 'pedido' : pedido, 'detallePedidos':detallePedidos}
	return render(request, 'pedidos/verPedido.html', context)


def eliminarPedido(request, articulo_id):

	pedido = Pedido.objects.get(usuario = request.user, estado = 'PE')
	detallePedido = DetallePedido.objects.get(pedido = pedido.id, articulo = articulo_id)
	pedido.total = pedido.total - detallePedido.articulo.precio

	#Comprobar cantidad de pedidos
	if detallePedido.cantidad > 1:
		detallePedido.cantidad = detallePedido.cantidad - 1
		detallePedido.save()
	else:
		detallePedido.delete()

	#Comprobar si el pedido esta vacio
	if pedido.total == 0:
		pedido.delete()
		pedido = None
		detallePedidos = None
	else:
		pedido.save()
		detallePedidos = DetallePedido.objects.filter(pedido = pedido.id)
	
	context = { 'pedido' : pedido, 'detallePedidos':detallePedidos}
	return render(request, 'pedidos/verPedido.html', context)



def facturarPedido(request):

	try:
		pedido = Pedido.objects.get(usuario = request.user, estado = 'PE')
	except Pedido.DoesNotExist:
		pedido = None

	if pedido is not None:

		factura = Factura()
		factura.pedido = pedido
		factura.save()

		pedido.estado = 'PA'
		pedido.save()

	return redirect	('pedidos/listaFacturas')

def verPedido(request):
	try:
		pedido = Pedido.objects.get(usuario = request.user, estado = 'PE')
	except Pedido.DoesNotExist:
		pedido = None

	if pedido is not None:

		detallePedidos = DetallePedido.objects.filter(pedido = pedido.id)
		context = { 'pedido' : pedido, 'detallePedidos':detallePedidos}
	else:	
		context = { 'pedido' : pedido}

	return render(request, 'pedidos/verPedido.html', context)


def listaFacturas(request):

	listaFacturas = Factura.objects.filter(pedido= Pedido.objects.filter(usuario = request.user))
	context = { 'listaFacturas' : listaFacturas}

	return render(request, 'pedidos/listaFacturas.html', context)

def detalleFactura(request, factura_id):
	
	factura = Factura.objects.get(id = factura_id)
	pedido = Pedido.objects.get(id = factura.pedido.id)
	detallePedidos = DetallePedido.objects.filter(pedido = pedido.id)
	usuario = User.objects.get(id = request.user.id)
		
	context = { 'pedido' : pedido, 'detallePedidos':detallePedidos, 'factura':factura, 'usuario':usuario}
	
	return render(request, 'pedidos/detalleFactura.html', context)



