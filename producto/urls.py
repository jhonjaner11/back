
from django.contrib import admin
from django.urls import path, include

from producto import urls as producto_urls


# todo/todo_api/urls.py : API urls.py


from .views import *


urlpatterns = [
    path('list', ProductoListApiView.as_view()),
    path('stock', StockListApiView.as_view()),
    path('punto', PuntoListApiView.as_view()),
    path('historico', HistoricoProductoListApiView.as_view()),
    path('categoria', CategoriaListApiView.as_view())

]
