
from django.contrib import admin
from django.urls import path, include

from producto import urls as ventas_urls


# todo/todo_api/urls.py : API urls.py


from .views import *


urlpatterns = [
    path('ventas', VentaApiView.as_view()),
    path('facturas', FacturaApiView.as_view()),
]
