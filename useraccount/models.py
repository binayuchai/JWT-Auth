from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15,unique=True)
    photo = models.ImageField(upload_to='user_photos/',blank=True,null=True)
    
    objects = UserManager()

    def __str__(self):
        return self.name


