from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib import auth

# Create your models here.

class UserInfo(AbstractUser):
    class Meta:
        db_table = 'userinfo'
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'