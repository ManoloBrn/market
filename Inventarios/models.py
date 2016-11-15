from django.db import models
from Negocios.models import Negocio
# Create your models here.
class Producto(models.Model):
	# class Meta:
 #        verbose_name = "Producto"
 #        verbose_name_plural = "Productos"
	CATEGORY_PRODUCTS = (
			("ropa","ropa"),
			("alimento","alimentos"),
			("electronicos","electronicos")
		)

	#ID
	#ID del negocio
	business = models.ForeignKey(Negocio, related_name='producto_negocio')
	name = models.CharField(max_length=60, blank=False)
	category = models.CharField(max_length=15,choices=CATEGORY_PRODUCTS,default="ropa")
	quantity = models.IntegerField(default=0)
	price = models.FloatField(default=0, blank=False)

	def __str__(self):
		return self.name