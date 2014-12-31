from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import login, logout
from django.views.generic import TemplateView
from articulos.views import *
from articulos import views


urlpatterns = patterns('',
	url(r'^$', TemplateView.as_view(template_name='articulos/index.html'),name='index'),
	
	url(r'^listaFabricantes/$', FabricantesListView.as_view(), name ='listaFabricantes'),
	url(r'^detalleFabricante/(?P<pk>\d+)/$', FabricanteDetailView.as_view(), name='detalleFabricante'),
	url(r'^nuevoFabricante/$', NuevoFabricanteView.as_view(success_url='/articulos/listaFabricantes'), name = "nuevoFabricante"),
	url(r'^eliminarFabricante/(?P<pk>\d+)/$',EliminarFabricanteView.as_view(success_url='/articulos/listaFabricantes'), name = "eliminarFabricante"),
	url(r'^editarFabricante/(?P<pk>\d+)/$',EditarFabricanteView.as_view(), name = "editarFabricante"),

	url(r'^listaCategorias/$', CategoriasListView.as_view(), name ='listaCategorias'),
	url(r'^detalleCategoria/(?P<pk>\d+)/$', CategoriaDetailView.as_view(), name='detalleCategoria'),
	url(r'^nuevoCategoria/$', NuevoCategoriaView.as_view(success_url='/articulos/listaCategorias'), name = "nuevoCategoria"),
	url(r'^eliminarCategoria/(?P<pk>\d+)/$',EliminarCategoriaView.as_view(success_url='/articulos/listaCategorias'), name = "eliminarCategoria"),
	url(r'^editarCategoria/(?P<pk>\d+)/$',EditarCategoriaView.as_view(), name = "editarCategoria"),

	url(r'^listaArticulos/$', ArticulosListView.as_view(), name ='listaArticulos'),
	url(r'^detalleArticulo/(?P<pk>\d+)/$', ArticuloDetailView.as_view(), name='detalleArticulo'),
	url(r'^nuevoArticulo/$', NuevoArticuloView.as_view(success_url='/articulos/listaArticulos'), name = "nuevoArticulo"),
	url(r'^eliminarArticulo/(?P<pk>\d+)/$',EliminarArticuloView.as_view(success_url='/articulos/listaArticulos'), name = "eliminarArticulo"),
	url(r'^editarArticulo/(?P<pk>\d+)/$',EditarArticuloView.as_view(), name = "editarArticulo"),

	url(r'^articuloCategoria/(?P<categoria_id>\d+)/$', views.articuloCategoria, name='articuloCategoria'),
	url(r'^articuloFabricante/(?P<fabricante_id>\d+)/$', views.articuloFabricante, name='articuloFabricante'),

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)