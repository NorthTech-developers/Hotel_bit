from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    adress = models.CharField(max_length=80, blank=True)
    phone = models.CharField(max_length=12, blank=True)
    ci = models.CharField(max_length=6, blank=True)


