# Generated by Django 4.1.7 on 2023-03-03 20:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ventas', '0005_venta_factura_alter_factura_descuento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_factura', to=settings.AUTH_USER_MODEL),
        ),
    ]
