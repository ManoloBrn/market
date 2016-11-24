from rest_framework import serializers
from .models import Checkout
from Inventarios.models import Producto 
from Negocios.models import Negocio
from Inventarios.serializers import ProductoSerializer

class CheckoutSerializer(serializers.ModelSerializer):
	checkout_producto  = ProductoSerializer(many = True, read_only=True) 
	class Meta:
		model = Checkout 
		fields = [
				"product",
				"checkout_producto"]