
from django.contrib import admin
from django.urls import path, include

from provedor import urls as provedor_urls


# todo/todo_api/urls.py : API urls.py


from .views import *


urlpatterns = [
    path('provedor', ProvedorListApiView.as_view()),
]
