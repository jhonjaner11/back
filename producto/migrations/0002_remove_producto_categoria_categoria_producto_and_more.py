# Generated by Django 4.1.7 on 2023-03-03 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provedor', '0002_alter_provedor_correo_alter_provedor_direccion_and_more'),
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
        migrations.AddField(
            model_name='categoria',
            name='producto',
            field=models.ManyToManyField(related_name='producto_categoria', to='producto.producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='provedor',
            field=models.ManyToManyField(help_text='Provedor del producto', related_name='provedor', to='provedor.provedor'),
        ),
        migrations.CreateModel(
            name='Punto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('cantidad', models.IntegerField()),
                ('producto', models.ManyToManyField(related_name='producto_punto', to='producto.producto')),
            ],
        ),
    ]
