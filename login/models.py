from django.db import models
from django.contrib.auth.models import User, AbstractUser
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse


class Cliente(models.Model): 	

    user = models.OneToOneField(User, on_delete=models.CASCADE)	
    phone = models.IntegerField(blank=True, null=True) #opcional
    cards = models.CharField(max_length=30, blank=True, null=True) #hacer un array. Opcional
    plan = models.CharField(max_length=30, blank=True, null=True) #opcional
    billing_address = models.CharField(max_length=30, blank=True, null=True) #opcional. Hash
    shipping_address= models.CharField(max_length=30, blank=True, null=True) # opcional. Hash

    def __str__(self):
        return str(self.user)

#class Vendedor(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)

class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')