from django.conf.urls import patterns, include, url
from pedidos import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView



urlpatterns = patterns('',
	url(r'^$', TemplateView.as_view(template_name='pedidos/index.html'),name='index'),
	url(r'agregarPedido/(?P<articulo_id>\d+)/$', views.agregarPedido, name='agregarPedido'),
	url(r'facturarPedido/$', views.facturarPedido, name='facturarPedido'),
	url(r'verPedido/$', views.verPedido, name='verPedido'),
	url(r'eliminarPedido/(?P<articulo_id>\d+)/$', views.eliminarPedido, name='eliminarPedido'),
	url(r'listaFacturas/$', views.listaFacturas, name='listaFacturas'),
	url(r'detalleFactura/(?P<factura_id>\d+)/$', views.detalleFactura, name='detalleFactura'),

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)