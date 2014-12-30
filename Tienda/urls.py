from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Tienda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', TemplateView.as_view(template_name='base.html'), name = 'base'),

    url(r'^admin/', include(admin.site.urls)),

    # Aplicacion articulos 
    url(r'^articulos/', include('articulos.urls', namespace='articulos')),
    url(r'^categorias/', include('articulos.urls', namespace='articulos')),
    url(r'^marcas/', include('articulos.urls', namespace='articulos')),
    
    # Aplicacion pedidos
    #url(r'^pedidos/', include('pedidos.urls', namespace='pedidos')),
    
    # Aplicacion usuarios
    url(r'^usuarios/', include('usuarios.urls', namespace='usuarios')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
