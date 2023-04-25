from django.shortcuts import render

# todo/todo_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import filters
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


class ProductoListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''

        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'nombre': request.data.get('nombre'),
            'precio_venta': request.data.get('precio_venta'),
            'precio_compra': request.data.get('precio_compra'),
            'activo': request.data.get('activo'),
            'provedor': request.data.get('provedor'),
            'categoria': request.data.get('categoria'),
        }

        serializer = ProductoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            st = Stock()
            print("cantidad:")
            print(request.data.get('cantidad'))
            st.cantidad = request.data.get(
                'cantidad') if request.data.get('cantidad') else 0
            # st.cantidad = request.data.get('cantidad')
            st.producto = Producto.objects.get(pk=serializer.data['id'])
            st.punto = Punto.objects.get(pk=1)
            st.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StockListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''

        if 'producto' in kwargs:
            stock = Stock.objects.filter(producto=kwargs['producto'])
            serializer = StockSerializer(stock, many=True)

        elif 'last' in kwargs:
            if kwargs['last'] == 'last':
                stock = Stock.objects.all().order_by('cantidad')[:5]
                serializer = StockSerializer(stock, many=True)

        else:
            stock = Stock.objects.all().order_by('cantidad')
            serializer = StockSerializer(stock, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'cantidad': request.data.get('cantidad'),
            'producto': request.data.get('id_producto'),
            'punto': request.data.get('punto'),
        }

        serializer = StockSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @api_view(['GET', 'PUT', 'DELETE'])

    def put(self, request, **kwargs):

        tutorial_data = JSONParser().parse(request)

        try:
            if tutorial_data['id']:
                print("hay")
                try:
                    tutorial = Stock.objects.get(pk=tutorial_data['id'])
                    print("tutorial")
                    print(tutorial)
                    print("camino id")
                    # prod = Producto.objects.get(
                    #     pk=tutorial_data['id_producto'])

                    # tutorial_data['producto'] = prod.id

                    tutorial_data['producto'] = tutorial.producto_id
                    tutorial_data['punto'] = 1
                except Stock.DoesNotExist:
                    print("except")
                    return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

        except KeyError:
            print("No hay")
            print(tutorial_data)
            try:
                tutorial = Stock.objects.get(
                    producto_id=tutorial_data['id_producto'])

                tutorial_data['producto'] = tutorial.producto_id
                tutorial_data['punto'] = 1
            except Stock.DoesNotExist:
                return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

        tutorial_serializer = StockSerializer(
            tutorial, data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data)
        print("errores")
        print(tutorial_serializer.errors)

        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        print("requests")
        print(request.method)
        print(kwargs)
        try:
            st = Stock.objects.get(pk=kwargs['producto'])
            print("tutorial")
            print(st)
        except Stock.DoesNotExist:
            return JsonResponse({'message': 'The st does not exist'}, status=status.HTTP_404_NOT_FOUND)

        st.delete()
        return JsonResponse({'message': 'st was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


class PuntoListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''

        puntos = Punto.objects.all()
        serializer = PuntoSerializer(puntos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'nombre': request.data.get('nombre'),
            'descripcion': request.data.get('descripcion'),
            'direccion': request.data.get('direccion'),
        }

        serializer = PuntoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HistoricoProductoListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''

        historico_producto = HistoricoProducto.objects.all()
        serializer = HistoricoProductoSerializer(historico_producto, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'producto': request.data.get('producto'),
            'precio_venta': request.data.get('precio_venta'),
            'precio_compra':  request.data.get('precio_compra'),
            'usuario': request.user.id,

        }

        serializer = HistoricoProductoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoriaListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''

        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'nombre': request.data.get('nombre'),
            'descripcion': request.data.get('descripcion'),
        }

        serializer = CategoriaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, **kwargs):

        object_data = JSONParser().parse(request)

        try:
            if object_data['id']:
                print("hay")
                try:
                    object = Categoria.objects.get(pk=object_data['id'])

                    # object_data['nombre'] = object.nombre
                    # object_data['descripcion'] = object.descripcion
                except Categoria.DoesNotExist:
                    print("except")
                    return JsonResponse({'message': 'The object does not exist'}, status=status.HTTP_404_NOT_FOUND)

        except KeyError:
            print("No hay")
            print(object_data)
            try:
                object = Categoria.objects.get(
                    producto_id=object_data['id_producto'])

                object_data['producto'] = object.producto_id
                object_data['punto'] = 1
            except Categoria.DoesNotExist:
                return JsonResponse({'message': 'The object does not exist'}, status=status.HTTP_404_NOT_FOUND)

        object_serializer = CategoriaSerializer(
            object, data=object_data)
        if object_serializer.is_valid():
            object_serializer.save()
            return JsonResponse(object_serializer.data)
        print("errores")
        print(object_serializer.errors)

        return JsonResponse(object_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        print("requests")
        print(request.method)
        print(kwargs)
        try:
            ct = Categoria.objects.get(pk=kwargs['id'])

            print("Objeto")
            print(ct)
            ct.delete()
        except Stock.DoesNotExist:
            return JsonResponse({'message': 'The st does not exist'}, status=status.HTTP_404_NOT_FOUND)

        return JsonResponse({'message': 'Categoria Eliminada'}, status=status.HTTP_204_NO_CONTENT)
