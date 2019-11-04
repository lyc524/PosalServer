from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(AbstractUser): 
    mobile=models.CharField(verbose_name='电话')


