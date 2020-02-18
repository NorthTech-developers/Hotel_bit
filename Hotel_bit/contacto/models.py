from django.db import models

# Create your models here.

class contacto(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return f'Nombre: {self.first_name} {self.last_name} ---------- Mensaje -------------> {self.message}'