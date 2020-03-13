from django.db import models
from django.utils import timezone

# Create your models here.

class Comentario(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    def publicacion(self):
        self.fecha_publicacion = timezone.now()
        self.save()
    
    def __str__(self):
        return self.texto
    