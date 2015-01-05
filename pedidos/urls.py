from django.conf.urls import patterns, include, url
from pedidos import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView



urlpatterns = patterns('',
	url(r'^$', TemplateView.as_view(template_name='pedidos/index.html'),name='index'),
	url(r'agregarPedido/(?P<articulo_id>\d+)/$', views.agregarPedido, name='agregarPedido'),
	url(r'facturarPedido/$', views.facturarPedido, name='facturarPedido'),

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)