from rest_framework import serializers
from .models import Checkout
from Inventarios.models import Producto 
from Negocios.models import Negocio
from Inventarios.serializers import ProductoSerializer
from Negocios.serializers import NegocioSerializer

class CheckoutSerializer(serializers.ModelSerializer):

	checkout_negocio  = NegocioSerializer(source="business",many = False, read_only=True)
	#checkout_cliente
	checkout_producto = ProductoSerializer(source="product",many=False, read_only=False)
	class Meta:
		model = Checkout 
		fields = ["business", "client", "product", 
		"description", "amount", "currency","quantity", "checkout_negocio","checkout_producto"]

class CheckoutSetSerializer(serializers.ModelSerializer):

	
	class Meta:
		model = Checkout 
		fields = ["business", "client", "product", 
		"description", "amount", "currency","quantity"]