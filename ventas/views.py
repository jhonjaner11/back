from django.shortcuts import render

# todo/todo_api/views.py
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import filters
from .models import *
from producto.models import Stock
from .serializers import *


from django.db.models import Sum
from django.utils import timezone
from datetime import date, timedelta, datetime
from calendar import monthrange


class VentaApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''

        if 'factura' in kwargs:
            ventas = Venta.objects.filter(factura=kwargs['factura'])
            print(ventas)
            serializer = VentaSerializer(ventas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:

            ventas = Venta.objects.all()
            serializer = VentaSerializer(ventas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # return Response(serializer.data, status=status.HTTP_200_OK)

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
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''

        # try:

        if 'id' in kwargs:
            facturas = Factura.objects.get(pk=kwargs['id'])
            serializer = FacturaSerializer(facturas)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:

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
            # 'usuario': request.user.id,
            'usuario': request.data.get('usuario')
        }

        serializer = FacturaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            print("factura:")
            print(serializer.data['id'])

            for producto in request.data.get('ventas'):
                print(producto)
                venta = Venta(
                    factura=Factura.objects.get(pk=serializer.data['id']),
                    descuento=0,
                    producto=Producto.objects.get(pk=producto['producto_id']),
                    cantidad=producto['cantidad'],
                    precio_unidad=producto['producto_precio'],
                    precio_final=producto['total']
                )

                stock = Stock.objects.get(producto_id=producto['producto_id'])
                print("primer stock")
                print(stock)

                newCantidad = stock.cantidad - producto['cantidad']
                print("Cantidades: "+str(newCantidad))
                print(stock.cantidad - newCantidad)
                stock.cantidad = newCantidad
                stock.save()

                print("seungdo:")
                print(stock.cantidad)
                venta.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def informe(self, request, *args, **kwargs):
        # Define tu propio método personalizado
        data = {'message': 'Hola, esta es una respuesta personalizada'}
        return Response(data)


class InformeApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        obtiene las cantidades de ventas diaria, semanal y mensual. 
        '''

        # try:

        today = timezone.now().date()

        suma_diaria = Factura.objects.filter(
            fecha_creacion__date=today).aggregate(Sum('total'))['total__sum']

        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        facturas_de_la_semana = Factura.objects.filter(
            fecha_creacion__date__range=[start_of_week, end_of_week])
        suma_semanal = facturas_de_la_semana.aggregate(total=Sum('total'))[
            'total'] or 0

        start_of_month = date(today.year, today.month, 1)
        end_of_month = date(
            today.year, today.month, monthrange(today.year, today.month)[1])
        facturas_del_mes = Factura.objects.filter(
            fecha_creacion__date__range=[start_of_month, end_of_month])
        suma_mensual = facturas_del_mes.aggregate(
            total=Sum('total'))['total'] or 0

        data = {}
        data['diario'] = suma_diaria,
        data['semanal'] = suma_semanal,
        data['mensual'] = suma_mensual,

        return Response(data, status=status.HTTP_200_OK)
