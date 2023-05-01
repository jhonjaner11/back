from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

from .serializers import UserSerializer, RolSerializer
from .models import User, Rol
from rest_framework.exceptions import AuthenticationFailed
import jwt
import datetime
from django.contrib.auth import authenticate
from django.http.response import JsonResponse

# Create your views here.


class UsersView(APIView):
    def get(self, request):

        objects = User.objects.all()
        serializer = UserSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, **kwargs):
        try:
            st = User.objects.get(pk=kwargs['id'])

            print(st)
        except User.DoesNotExist:
            return JsonResponse({'message': 'The User does not exist'}, status=status.HTTP_404_NOT_FOUND)

        st.delete()
        return JsonResponse({'message': 'Usuario fue eliminado exitosamente!'}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, **kwargs):
        print(request.data)
        print(kwargs)
        # object = JSONParser().parse(request)

        # try:
        if kwargs['id']:
            print("hay")
            print(kwargs['id'])
            try:
                u = User.objects.get(pk=kwargs['id'])
                print(u)

                if 'first_name' in request.data:
                    u.first_name = request.data['first_name']
                if 'last_name' in request.data:
                    u.last_name = request.data['last_name']
                if 'username' in request.data:
                    u.username = request.data['username']
                if 'email' in request.data:
                    u.email = request.data['email']
                if 'telefono' in request.data:
                    u.telefono = request.data['telefono']

                if 'password' in request.data:
                    u.password = request.data['password']

                if 'rol' in request.data:
                    u.rol = Rol.objects.get(name=request.data['rol'])
                if 'estado' in request.data:
                    u.estado = request.data['estado']
                u.save()

            except User.DoesNotExist:
                print("except")
                return JsonResponse({'message': 'The User does not exist'}, status=status.HTTP_404_NOT_FOUND)

        # except KeyError:
        #     print("No hay")
        #     print(KeyError)

        #     return JsonResponse({'message': 'The User ID is not provided!'}, status=status.HTTP_404_NOT_FOUND)

        tutorial_serializer = UserSerializer(u)

        return JsonResponse(tutorial_serializer.data)


class RolView(APIView):
    def get(self, request):

        objects = Rol.objects.all()
        serializer = RolSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RegisterView(APIView):
    def post(self, request):
        print(request.data)
        u = User()
        u.first_name = request.data['first_name']
        u.last_name = request.data['last_name']
        u.telefono = request.data['telefono']
        u.username = request.data['username']
        u.email = request.data['email']
        u.password = request.data['password']
        u.rol = Rol.objects.get(name=request.data['rol'])
        u.save()
        serializer = UserSerializer(u)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()
        # print(user.id)
        if user is None:
            raise AuthenticationFailed('user not found!')

        # user = authenticate(request, username=username, password=password)
        # print(user)

        if not user.check_password(password):

            # TODO
            if (user.password != password):
                raise AuthenticationFailed(user.check)

        payload = {
            'id': user.id,
            'username': user.username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow(),
            'name': user.first_name,
            'rol': user.rol.name
        }

        token = jwt.encode(payload, 'secret',
                           algorithm='HS256')

        res = Response()
        res.set_cookie(key='jwt', value=token, httponly=True)

        # tokenR = jwt.decode(token, 'secret', algorithms=['HS256'])
        # res.data = {
        #     'jwt': token

        # }

        res.data = payload
        return res


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            "message": "success"
        }

        return response
