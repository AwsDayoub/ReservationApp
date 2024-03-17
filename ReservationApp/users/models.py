from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    age = models.IntegerField(null=True)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    balance = models.IntegerField(null=True, blank=True, default=0)
    email_verified = models.BooleanField(default=False)
    image = models.ImageField(upload_to="user_profile_image" , null=True , blank=True)





