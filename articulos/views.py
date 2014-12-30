from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, View, DetailView, CreateView, DeleteView
from articulos.models import Articulo, Categoria, Fabricante
from django.core.urlresolvers import reverse_lazy

# Create your views here.

# FABRICANTES

class FabricantesListView(ListView):
	model = Fabricante
	context_object_name = 'listaFabricantes'
	template_name = 'articulos/listaFabricantes.html'

class FabricanteDetailView(DetailView):
	
	queryset = Fabricante.objects.all()
	template_name = 'articulos/detalleFabricante.html'

	def get_object(self):

		# Call the superclass
		context = super(FabricanteDetailView, self).get_object()
		
		# Return the object
		return context

class NuevoFabricanteView(CreateView):
	model = Fabricante
	fields = '__all__'
	template_name = 'articulos/nuevoFabricante.html'


class EliminarFabricanteView(DeleteView):
	model = Fabricante
	template_name = 'articulos/borrarConfirmar.html'
	success_url = reverse_lazy('listaFabricantes')




# CATEGORIAS



class CategoriasListView(ListView):
	model = Categoria
	context_object_name = 'listaCategorias'
	template_name = 'articulos/listaCategorias.html'

class CategoriaDetailView(DetailView):
	
	queryset = Categoria.objects.all()
	template_name = 'articulos/detalleCategoria.html'

	def get_object(self):

		# Call the superclass
		context = super(CategoriaDetailView, self).get_object()
		
		# Return the object
		return context

class NuevoCategoriaView(CreateView):
	model = Categoria
	fields = '__all__'
	template_name = 'articulos/nuevoCategoria.html'


class EliminarCategoriaView(DeleteView):
	model = Categoria
	template_name = 'articulos/borrarConfirmar.html'
	success_url = reverse_lazy('listaCategorias')




# ARTICULOS



class ArticulosListView(ListView):
	model = Articulo
	context_object_name = 'listaArticulos'
	template_name = 'articulos/listaArticulos.html'

class ArticuloDetailView(DetailView):
	
	queryset = Articulo.objects.all()
	template_name = 'articulos/detalleArticulo.html'

	def get_object(self):

		# Call the superclass
		context = super(ArticuloDetailView, self).get_object()
		
		# Return the object
		return context

class NuevoArticuloView(CreateView):
	model = Articulo
	fields = '__all__'
	template_name = 'articulos/nuevoArticulo.html'


class EliminarArticuloView(DeleteView):
	model = Articulo
	template_name = 'articulos/borrarConfirmar.html'
	success_url = reverse_lazy('listaArticulos')
