from rest_framework import serializers
from .models import User, Rol


class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'email', 'username']

    def to_representation(self, instance):

        if instance.rol == None:
            rol_name = ''
        else:
            rol_name = instance.rol.name

        return {
            'id': instance.id,
            'first_name': instance.first_name,
            'last_name': instance.last_name,
            'username': instance.username,
            'email': instance.email,
            'rol': rol_name,
            'telefono': instance.telefono,
            'estado': instance.estado
        }


class RolSerializer (serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'
