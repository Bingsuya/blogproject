from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from userapp.models import User
# Create your models here.
#모델 등록하여 확인할 수 있게 하기( 게시글, 유저 등)


class Post(models.Model):
    picture = models.ImageField(null = True, upload_to="%Y/%m/%d")
    posttitle =  models.TextField(null=True)
    postcontents = models.TextField(null=True)
    date = models.DateField(null = True, auto_now=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)