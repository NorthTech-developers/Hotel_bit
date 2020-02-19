from django.db import models

# Create your models here.

class RegistroUsuario(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    adress = models.CharField(max_length=80)
    phone = models.CharField(max_length=30)
    ci = models.CharField(max_length=20)
    email = models.EmailField()
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)
    terminos_condiciones = models.BooleanField(default=False)
    email_newsletter = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.username}'

