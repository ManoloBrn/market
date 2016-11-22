from rest_framework import serializers
from .models import Checkout

class CheckoutSerializer(serializers.ModelSerializer):
	client = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='transaction_cliente'
     )

	class Meta:
		model = Checkout 
		fields = ["business","client"]