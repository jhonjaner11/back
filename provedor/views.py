from django.shortcuts import render

# todo/todo_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import *
from .serializers import *

from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


class ProvedorListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''

        objetos = Provedor.objects.all()
        serializer = ProvedorSerializer(objetos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'tipo_id': request.data.get('tipo_id'),
            'provedor_id': request.data.get('provedor_id'),
            'nombre': request.data.get('nombre'),
            'telefono': request.data.get('telefono'),
            'direccion': request.data.get('direccion'),
            'correo':  request.data.get('correo'),
            'pagina_web': request.data.get('pagina_web')
        }

        serializer = ProvedorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EntregaListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''

        objetos = Entrega.objects.all()
        serializer = EntregaSerializer(objetos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'fecha': request.data.get('fecha'),
            'provedor_id': request.data.get('provedor_id'),
            'productos': request.data.get('productos'),
            'comentarios': request.data.get('comentarios'),
            'periodicidad': request.data.get('periodicidad'),
        }

        serializer = EntregaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, **kwargs):
        

        

        objeto = JSONParser().parse(request)
        print(objeto)
      
        if objeto['id']:
            print("hay")
            try:
                delivery = Entrega.objects.get(pk=objeto['id'])
                print("objeto:")
                print(delivery)
                delivery.finalizado = objeto['finalizado']
                objeto['provedor_id'] = delivery.provedor_id.id
                objeto['fecha'] = delivery.fecha
                
            except Entrega.DoesNotExist:
                print("except")
                return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)


        serializer = EntregaSerializer(delivery,
            data=objeto)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        print("errores:")
        print(serializer.errors)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
