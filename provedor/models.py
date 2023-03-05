from django.db import models

# Create your models here.


class Provedor(models.Model):

    JOB_CHOICES = (
        ('0', 'Cedula'),
        ('1', 'Rut'),
    )

    tipo_id = models.CharField(
        max_length=10, help_text="Tipo de id", choices=JOB_CHOICES)
    provedor_id = models.CharField(
        max_length=10, help_text="cedula o ruth del provedor", unique=True)
    nombre = models.CharField(max_length=100, help_text="Nombre del producto")
    telefono = models.JSONField()
    direccion = models.CharField(max_length=100, blank=True)
    correo = models.CharField(max_length=100, blank=True)
    pagina_web = models.CharField(max_length=100, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
