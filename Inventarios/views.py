from django.shortcuts import render
from django.views.generic import View,DetailView, DeleteView, UpdateView, CreateView

from .models import Producto
# Create your views here.

class RegisterView(CreateView):
	model = Producto
	fields = ["name","category","quantity","price"]
	success_url = "/inventario/productos/"

class ProductosView(View):
	template = 'productos.html'

	def get(self, request, *args, **kargs):
		return render(request, self.template)
