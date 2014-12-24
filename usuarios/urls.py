from django.conf.urls import patterns, include, url
from usuarios import views

urlpatterns = patterns('',
	url(r'^login$', views.userLogin, name='login'),
	url(r'^logout$', views.userLogout, name='logout'),
	url(r'^registro$', views.registro, name='registro'),
	#url(r'^detalles$', views.Configuracion, name='configuracion'),
)