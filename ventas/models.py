from django.db import models

# Create your models here.
from producto.models import Producto
from users.models import User


class Factura(models.Model):
    id = models.BigAutoField(primary_key=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    descuento = models.CharField(max_length=10, blank=True)
    total = models.IntegerField()
    usuario = models.ForeignKey(
        User, related_name='usuario_factura', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Venta(models.Model):
    id = models.BigAutoField(primary_key=True)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    descuento = models.CharField(max_length=10, blank=True)
    producto = models.ForeignKey(Producto,
                                 help_text="Producto de la venta",
                                 related_name='producto_venta',
                                 on_delete=models.CASCADE)
    cantidad = models.IntegerField(
        help_text="cantidad de productos en la venta")
    precio_unidad = models.IntegerField()
    precio_final = models.IntegerField()

    def __str__(self):
        return str(self.id)
