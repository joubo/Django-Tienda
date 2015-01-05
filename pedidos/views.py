from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, View, DetailView, CreateView, DeleteView, UpdateView
from pedidos.models import Pedido, DetallePedido, Factura
from articulos.models import Articulo
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

	dp = DetallePedido()
	dp.pedido = pedido
	dp.articulo = articulo
	dp.save()

	return redirect	('/')

def facturarPedido(request):

	p = Pedido.objects.get(usuario = request.user, estado = 'PE')

	f = Factura()
	f.pedido = p
	f.save()

	p.estado = 'PA'
	p.save()

	return redirect	('/')
