from django.contrib import admin
from pedidos.models import Pedido, DetallePedido, Factura

# Register your models here.

admin.site.register(Pedido)
admin.site.register(DetallePedido)
admin.site.register(Factura)