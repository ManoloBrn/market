from django.db import models
from login.models import Cliente
# Create your models here.
class Negocio(models.Model):
	class Meta():
		verbose_name='Negocio'
		verbose_name_plural='Negocios'

	#id 
	owner = models.ForeignKey(Cliente, related_name='neogocio_cliente')
	name = models.CharField(max_length=30, blank=False)
	streetAddress = models.CharField(max_length=100, blank=False)
	phoneNumber = models.PositiveIntegerField(default=0)
