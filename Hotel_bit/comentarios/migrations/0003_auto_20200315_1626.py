# Generated by Django 3.0.2 on 2020-03-15 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0002_comentario_usuarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='comentario_aprobado',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='Comentario_Usuarios',
        ),
    ]