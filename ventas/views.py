from django.shortcuts import render

# todo/todo_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import *
from .serializers import *


class VentaApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''

        objetos = Venta.objects.all()
        serializer = VentaSerializer(objetos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''

        numero = 0

        items = request.data

        # Loop through the items and save each one
        for item in items:
            data = {
                'factura': item['factura'],
                'descuento': item['descuento'],
                'producto': item['producto'],
                'cantidad': item['cantidad'],
                'precio_unidad': item['precio_unidad'],
                'precio_final':  item['precio_final']
            }

            # new_item = Item(name=item['name'], description=item['description'])
            # new_item.save()

            serializer = VentaSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                numero += 1
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(numero, status=status.HTTP_201_CREATED)


class FacturaApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''

        facturas = Factura.objects.all()
        serializer = FacturaSerializer(facturas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'descuento': request.data.get('descuento'),
            'total': request.data.get('total'),
            'usuario': request.user.id,
        }

        serializer = FacturaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
