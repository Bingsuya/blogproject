from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    address = models.CharField(max_length = 100,null = True)
    phone = models.TextField(null = True)
    age = models.TextField(null = True)
    gender = models.BooleanField(null=True) #남자True 여자 False
