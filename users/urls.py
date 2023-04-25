
from django.contrib import admin
from django.urls import path, include


# todo/todo_api/urls.py : API urls.py


from .views import *


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('users', UsersView.as_view()),
    path('users/<int:id>', UsersView.as_view()),
    path('rol', RolView.as_view())


]
