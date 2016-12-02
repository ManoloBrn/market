from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from .models import Checkout, Transaction
from Negocios.models import Negocio
from .serializers import CheckoutSerializer, CheckoutSetSerializer

class CheckoutCreate(generics.CreateAPIView):
	#queryset = Checkout.objects.all()
	serializer_class = CheckoutSetSerializer

	def post(self, request, format=None):
		print(request.data)
		
		return Response("asd")