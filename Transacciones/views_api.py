from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from .models import Checkout, Transaction
from Negocios.models import Negocio
from .serializers import CheckoutSerializer, CheckoutSetSerializer

class CheckoutCreate(generics.CreateAPIView):
	#queryset = Checkout.objects.all()
	serializer_class = CheckoutSerializer

	def post(self, request, format=None):
		print(request.data)
		billing = CheckoutSetSerializer(data=request.data)
		if(billing.is_valid()):
			billing.save()
			return Response({"status":"OK","fileCode":billing.data},status=status.HTTP_201_CREATED)
		return Response("Error")