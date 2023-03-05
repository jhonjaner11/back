from django.contrib import admin

# Register your models here.
from ventas.models import Venta, Factura


admin.site.register(Venta)
admin.site.register(Factura)
