
from django.contrib import admin
from django.urls import path, include

from producto import urls as ventas_urls


# todo/todo_api/urls.py : API urls.py


from .views import *


urlpatterns = [
    path('list', VentaApiView.as_view()),
    path('list/<int:factura>', VentaApiView.as_view()),
    path('facturas', FacturaApiView.as_view()),
    path('facturas/<int:id>', FacturaApiView.as_view()),
    path('informe/', InformeApiView.as_view()),

    # todo
    path('informe/stock/', StockApiView.as_view()),
]
