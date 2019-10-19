from django.contrib.auth.models import AbstractUser

from django.db import models


class User(AbstractUser):
    pass


class Ferme(models.Model):
    nom = models.CharField(max_length=100)
