from .models import *

from rest_framework import serializers
from provedor.serializers import ProvedorSerializer


class ProductoSerializer(serializers.ModelSerializer):
    # provedor = ProvedorSerializer

    class Meta:
        model = Producto
        exclude = ['fecha_creacion']

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'nombre': instance.nombre,
            'provedor': instance.provedor.nombre,
            'precio_venta': instance.precio_venta,
            'precio_compra': instance.precio_compra,
        }


class PuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Punto
        # fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
        fields = '__all__'


class HistoricoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoProducto
        # fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
        fields = '__all__'


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        # fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
        fields = '__all__'

    def to_representation(self, instance):
        print(instance)

        return {
            'id': instance.id,
            'fecha_creacion': instance.fecha_creacion.strftime("%d/%m/%Y"),
            'cantidad': instance.cantidad,
            'punto': instance.punto.nombre,
            'producto': instance.producto.nombre,
            'id_producto': instance.producto.id,
            'precio_producto': instance.producto.precio_venta

        }


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        # fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
        fields = '__all__'
