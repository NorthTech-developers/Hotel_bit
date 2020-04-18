from django.db import models
from django.utils import timezone

# Create your models here.

class Comentario(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    comentario_aprobado = models.BooleanField(default=False)

    def publicacion(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def aprobado(self):
        self.comentario_aprobado = True
        self.save()
    
    def __str__(self):
        return self.texto



    