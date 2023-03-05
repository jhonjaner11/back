
from django.contrib import admin
from django.urls import path, include

from producto import urls as producto_urls


# todo/todo_api/urls.py : API urls.py


from .views import (
    ProductoListApiView,
)

urlpatterns = [
    path('productos', ProductoListApiView.as_view()),
]
