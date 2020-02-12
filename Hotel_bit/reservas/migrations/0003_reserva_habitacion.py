# Generated by Django 3.0.2 on 2020-02-11 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0002_auto_20200211_0006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva_habitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_usuario', models.CharField(max_length=200, verbose_name='Nombre usuario')),
                ('Numero_menores', models.IntegerField(verbose_name='Cantidad de Niños')),
                ('Numero_adultos', models.IntegerField(verbose_name='Cantidad de Adultos')),
                ('Fecha_ingreso', models.DateTimeField(verbose_name='fecha_ingreso')),
                ('Fecha_egreso', models.DateTimeField(verbose_name='fecha_egreso')),
            ],
        ),
    ]
