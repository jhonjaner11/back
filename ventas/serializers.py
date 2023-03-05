from .models import *
from rest_framework import serializers


class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        # fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
        fields = '__all__'


class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        # fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
        fields = '__all__'
