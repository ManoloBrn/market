from rest_framework import generics
from .serializers import ClienteSerializer
from .models import Cliente
from rest_framework import viewsets



class ClienteViewSet(generics.ListAPIView):
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer

class ClienteViewCreate(generics.CreateAPIView):
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer