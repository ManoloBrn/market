from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Cliente(AbstractUser): 	


	phone = models.CharField(max_length=30, blank=False, null=False) #opcional
	cards = models.CharField(max_length=30, blank=False, null=False) #hacer un array. Opcional
	street = models.CharField(max_length=30, blank=False, null=False) #opcional. Hash
	colonia = models.CharField(max_length=30, blank=False, null=False)
	city = models.CharField(max_length=20, blank=False, null=False)
	state = models.CharField(max_length=20, blank=False, null=False)
	szip =  models.IntegerField(blank=False, null=False)
	country = models.CharField(max_length=20, blank=False, null=False)

class Vendedor(models.Model):

    user = models.OneToOneField(Cliente, on_delete=models.CASCADE)	
    
