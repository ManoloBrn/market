from rest_framework import generics
from .serializers import NegocioSerializer
from .models import Negocio
from rest_framework import viewsets

class NegocioViewCreate(generics.CreateAPIView):
	queryset = Negocio.objects.all()
	serializer_class = NegocioSerializer