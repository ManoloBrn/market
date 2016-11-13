from django.db import models
from Inventarios.models import Producto
# Create your models here.

class Transaction(models.Model):
    #ID Transaction
    #ID vendedor
    #ID del cliente
    idproducto = models.ForeignKey(Producto, related_name="producto_transaction")
    name = models.CharField(max_length=20)
    quantity = models.IntegerField(default=0)
    total = models.FloatField(default=0)
    eventtime = models.DateTimeField(auto_now=True)