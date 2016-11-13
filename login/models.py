from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Cliente(AbstractUser): 	
    phone = models.IntegerField(blank=True, null=True) #opcional
    cards = models.CharField(max_length=30, blank=True, null=True) #hacer un array. Opcional
    plan = models.CharField(max_length=30, blank=True, null=True) #opcional
    billing_address = models.CharField(max_length=30, blank=True, null=True) #opcional. Hash
    shipping_address= models.CharField(max_length=30, blank=True, null=True) # opcional. Hash


"""
class Usuario(models.Model):
    name = models.CharField(max_length=30)
    password=models.CharField(max_length=30) #No aparece listado
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=False) #opcional
    cards = models.CharField(max_length=30, blank=False) #hacer un array. Opcional
    plan = models.CharField(max_length=30, blank=False) #opcional
    billing_address = models.CharField(max_length=30, blank=False) #opcional. Hash
    shipping_address= models.CharField(max_length=30, blank=False) # opcional. Hash

    def __str__(self):
    	return u'%s %s' % (self.name,self.email)
"""



