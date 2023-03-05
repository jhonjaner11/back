from django.db import models

from model_utils.models import TimeStampedModel, SoftDeletableModel

from provedor.models import Provedor
from django.contrib.auth.models import User


class Categoria(models.Model):

    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    ALTA = '1'
    NORMAL = '2'
    BAJA = '3'

    PRIORIDAD_TAREA = (
        (ALTA, 'Alta'),
        (NORMAL, 'Normal'),
        (BAJA, 'Baja'),
    )

    nombre = models.CharField(max_length=100, help_text="Nombre del producto")

    precio_venta = models.IntegerField()
    precio_compra = models.IntegerField()
    activo = models.BooleanField()

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    provedor = models.ForeignKey(
        Provedor, help_text="Provedor del producto", related_name='provedor', on_delete=models.CASCADE)

    categoria = models.ManyToManyField(
        Categoria,  related_name='producto_categoria')

    def __str__(self):
        return self.nombre


class HistoricoProducto(models. Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio_venta = models.IntegerField()
    precio_compra = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    usuario = models.ForeignKey(
        User, related_name='usuario_historico', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.created_at)


class Punto(models.Model):

    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Stock(models.Model):

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField()
    producto = models.ManyToManyField(
        Producto,  related_name='producto_stock')
    punto = models.ForeignKey(Punto,  on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
