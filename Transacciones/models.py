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

    def __str__(self):
        return self.name

class Checkout(models.Model):

    CURRENCY_CHOICES = (
        ("MXN","Mexican Peso"),
        ("USD", "American Dollar")
    )

    CATEGORY_CHOICES = (
        ("FOOD", "Comida"),
        ("CLO", "Ropa")
    )

    business = models.ForeignKey(Negocio, related_name='checkout_negocio')
    client = models.ForeignKey(Cliente, related_name="checkout_cliente")
    product = models.ForeignKey(Producto, related_name='checkout_producto')

    description = models.CharField(max_length=100, blank=False)
    amount  = models.DecimalField(max_digits=7, decimal_places=2)
    currency = models.CharField(max_length=25, choices=CURRENCY_CHOICES, default=False)


    quantity = models.IntegerField()


    # #details
    # name = models.CharField(max_length=50)
    # phone = models.CharField(max_length=20, blank=False)
    # demail = models.EmailField()

    # #items []
    # product = models.ForeignKey(Producto, related_name="checkout_producto")

    # itemName = models.CharField(max_length=30)
    # itemdescription = models.CharField(max_length=50)
    # unitprice =  models.DecimalField(max_digits=7, decimal_places=2)
    # quantity = models.IntegerField()
    # category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    # #billing Adress
    # street1 = models.CharField(max_length=50)
    # street2 = models.CharField(max_length=30)
    # colonia = models.CharField(max_length=30)

    # city =  models.CharField(max_length=30)
    # state = models.CharField(max_length=30)
    # szip = models.IntegerField(default=0)
    # country = models.CharField(max_length=30)
    # phone = models.CharField(max_length=20, blank=False)
    # bemail = models.EmailField()