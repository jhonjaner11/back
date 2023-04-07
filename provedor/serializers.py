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


class EntregaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrega
        # fields = ['id', 'titulo', 'imagen', 'estreno', 'resumen']
        fields = '__all__'

    def to_representation(self, instance):
        
        return {
            'id': instance.id,
            'periodo': instance.periodo_CHOICES[int(instance.periodicidad)][1],
            'fecha': instance.fecha.strftime("%d/%m/%Y %H:%M"),
            'provedor': instance.provedor_id.nombre,
            'comentario': instance.comentarios,
            'telefono': instance.provedor_id.telefono,
            'correo': instance.provedor_id.correo,
            'pagina_web': instance.provedor_id.pagina_web,
            'productos': instance.productos,
            'finalizado': instance.finalizado
        }