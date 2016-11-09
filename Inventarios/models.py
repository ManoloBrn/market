from django.db import models

# Create your models here.
class Producto(models.Model):

	CATEGORY_PRODUCTS = (
			("ropa","ropa"),
			("alimento","alimentos"),
			("electronicos","electronicos")
		)
	class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
	#ID
	#ID del negocio

	name = models.CharField(max_length=60, blank=False)
	category = models.CharField(choices=CATEGORY_PRODUCTS,default="ropa")
	quantity = models.IntegerField(default=0)
	price = models.FloatField(default=0, blank=False)
