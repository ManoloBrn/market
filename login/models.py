from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Cliente(AbstractUser): 	

    phone = models.IntegerField(blank=True, null=True) #opcional
    cards = models.CharField(max_length=30, blank=True, null=True) #hacer un array. Opcional
    plan = models.CharField(max_length=30, blank=True, null=True) #opcional
    billing_address = models.CharField(max_length=30, blank=True, null=True) #opcional. Hash
    shipping_address= models.CharField(max_length=30, blank=True, null=True) # opcional. Hash
    

