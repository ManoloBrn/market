from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cliente
		fields= ["name", "phone", "cards", "plan", "billing_address", "shipping_address"]

