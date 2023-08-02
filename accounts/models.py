from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

# Create your models here.

class CustomUser(AbstractUser):
    roles = [
        ('user','User'),
        ('delivery_personel','Delivery Personel'),
        ('manager','Manager')
    ]

    user_id = models.UUIDField(primary_key=True,default=uuid4)
    phone_number = models.CharField(max_length=10,unique=True)
    role = models.CharField(max_length=200,choices=roles,default='user')

    def __str__(self) -> str:
        return self.username




