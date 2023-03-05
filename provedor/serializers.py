from .models import *
from rest_framework import serializers


class ProvedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provedor
        # fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
        fields = '__all__'
