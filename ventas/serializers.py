from .models import *
from rest_framework import serializers


class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        # fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'factura': instance.factura.id,
            'producto': instance.producto.nombre,
            'cantidad': instance.cantidad,

            'precio_unidad': instance.precio_unidad,
            'precio_final': instance.precio_final,
        }


class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        # fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'fecha': instance.fecha_creacion,
            'user': instance.usuario.username,
            'total': instance.total,
        }
