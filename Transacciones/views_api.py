from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from .models import Checkout, Transaction
from Negocios.models import Negocio
from .serializers import CheckoutSerializer

class CheckoutCreate(generics.ListCreateAPIView):
	queryset = Checkout.objects.all()
	serializer_class = CheckoutSerializer

	# def post(self, request,  *args, **kwargs):
	# 	checkout = CheckoutSerializer(data = request.data)
		
	# 	if checkout.is_valid():
			
			

	# 		return Response(checkout.data, status = status.HTTP_201_CREATED)
	# 	return self.create(request, *args, **kwargs)