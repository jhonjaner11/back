from django.contrib import admin

# Register your models here.
from producto.models import Producto, Categoria, HistoricoProducto, Punto, Stock


admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(HistoricoProducto)
admin.site.register(Punto)
admin.site.register(Stock)
