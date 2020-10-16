from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Credentials(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

# class User(AbstractUser):
