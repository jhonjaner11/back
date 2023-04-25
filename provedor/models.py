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
    correo = models.CharField(max_length=100, blank=True, null=True)
    pagina_web = models.CharField(max_length=100, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Entrega(models.Model):

    periodo_CHOICES = (
        ('0', 'diario'),
        ('1', 'semanal'),
        ('2', 'quincenal'),
        ('3', 'mensual'),
        ('4', 'bimensual'),
        ('5', 'trimensual'),
        ('6', 'personalizado')
    )

    fecha = models.DateTimeField()
    provedor_id = models.ForeignKey(Provedor, on_delete=models.DO_NOTHING)
    productos = models.JSONField(blank=True)
    comentarios = models.CharField(max_length=500, blank=True)
    periodicidad = models.CharField(
        max_length=100, choices=periodo_CHOICES, blank=True)
    finalizado = models.BooleanField(default=False)

    def __str__(self):
        return str(self.provedor_id) + ' ' + str(self.fecha)
