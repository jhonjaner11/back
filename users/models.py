from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class Rol(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class User(AbstractUser):

    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True, null=True)
    rol = models.ForeignKey(
        Rol, on_delete=models.DO_NOTHING, null=True, blank=True)
    estado = models.BooleanField(default=True)
    telefono = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name
