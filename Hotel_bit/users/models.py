from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class ManagerCuentas(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Debes registrar un email')
		if not username:
			raise ValueError('Debes tener un nombre de usuario')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class RegistroUsuario(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    adress = models.CharField(max_length=80)
    phone = models.CharField(max_length=30)
    ci = models.CharField(max_length=20)
    email = models.EmailField()
    username = models.CharField(max_length=30)

    terminos_condiciones = models.BooleanField(default=False)
    email_newsletter = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'

    def __str__(self):
        return f'{self.username}'

