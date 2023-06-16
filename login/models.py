from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class Person(AbstractUser):
    #username=models.CharField(max_length=100)
    #fname=models.CharField(max_length=100)
    #lname=models.CharField(max_length=100)
    nickname=models.CharField(max_length=100, null=True)
    tel=models.IntegerField(null=True)
    team=models.CharField(max_length=100, null=True)
    position=models.CharField(max_length=100, null=True)
    #email=models.EmailField(max_length=100, null=True)
    #password=models.CharField(max_length=100, null=True)
    leader=models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.username






