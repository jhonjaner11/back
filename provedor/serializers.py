from .models import *
from rest_framework import serializers


class ProvedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provedor
        # fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
        fields = '__all__'

    def to_representation(self, instance):

        JOB_CHOICES = ['cedula', 'Rut']
        return {
            'id': instance.id,
            'tipo_id': JOB_CHOICES[int(instance.tipo_id)],
            'provedor_id': instance.provedor_id,
            'nombre': instance.nombre,
            'telefono': instance.telefono,
            'direccion': instance.direccion,
            'correo': instance.correo,
            'pagina_web': instance.pagina_web,
        }
