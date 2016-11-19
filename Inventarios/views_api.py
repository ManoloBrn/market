from rest_framework import generics
from .serializers import ProductoSerializer
from .models import Producto
from rest_framework import viewsets



class ProductoViewSet(viewsets.ModelViewSet):
	queryset = Producto.objects.all()
	serializer_class = ProductoSerializer