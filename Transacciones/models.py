from django.db import models
from login.models import Cliente
from Inventarios.models import Producto
from Negocios.models import Negocio
from django.conf import settings

# Create your models here.

class Transaction(models.Model):
    #ID Transaction
    #ID vendedor
    #ID del client0e
    business = models.ForeignKey(Negocio, related_name='transaction_negocio')
    client = models.ForeignKey(Cliente, related_name="transaction_cliente")
    product = models.ForeignKey(Producto, related_name="producto_transaction")
    name = models.CharField(max_length=20)
    quantity = models.IntegerField(default=0)
    total = models.FloatField(default=0)
    eventtime = models.DateTimeField(auto_now=True)