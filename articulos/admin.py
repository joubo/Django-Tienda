from django.contrib import admin
from articulos.models import Articulo, Categoria, Fabricante

# Register your models here.

admin.site.register(Articulo)
admin.site.register(Categoria)
admin.site.register(Fabricante)