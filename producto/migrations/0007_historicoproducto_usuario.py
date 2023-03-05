# Generated by Django 4.1.7 on 2023-03-03 20:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('producto', '0006_remove_producto_provedor_producto_provedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicoproducto',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usuario_historico', to=settings.AUTH_USER_MODEL),
        ),
    ]
