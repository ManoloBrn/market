from rest_framework import serializers
from .models import Negocio 
class NegocioSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Negocio
		fields = ["id","owner", "name", "streetAddress", "phoneNumber"]