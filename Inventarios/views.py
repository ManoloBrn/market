from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, DeleteView, UpdateView, CreateView

from .models import Producto
# Create your views here.

class ProductosViewC(CreateView):
	model = Producto
	fields = ["name","category","quantity","price"]
	success_url = "/inventario/productos/"

class ProductosViewL(ListView):
	model = Producto
	context_object_name = "productos"

class ProductosViewD(DetailView):
	model = Producto
	context_object_name = "producto"
	