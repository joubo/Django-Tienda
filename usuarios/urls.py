from django.conf.urls import patterns, include, url
from usuarios import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import login, logout
from django.views.generic import TemplateView


urlpatterns = patterns('',
	url(r'^$', TemplateView.as_view(template_name='usuarios/index.html'),name='index'),
	url(r'^login/$', views.userLogin, name='login'),
	url(r'^logout/$', views.userLogout, name='logout'),
	url(r'^register/$', views.userRegister, name='register'),
)