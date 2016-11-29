from rest_framework import generics
from .serializers import ProductoSerializer
from .models import Producto
from rest_framework import viewsets



class ProductoViewSet(generics.ListAPIView):
	queryset = Producto.objects.all()
	serializer_class = ProductoSerializer

class	ProductoViewCreate(generics.CreateAPIView):
	queryset = Producto.objects.all()
	serializer_class = ProductoSerializer