from .models import *
from rest_framework import serializers


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        # fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
        fields = '__all__'


class ProvedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provedor
        # fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
        fields = '__all__'


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


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        # fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
        fields = '__all__'
