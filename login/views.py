from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
from django.views.generic import View, ListView, DetailView, DeleteView, UpdateView, CreateView




class ClienteCreateView(CreateView):
	model= Cliente
	fields=["name","phone","cards","plan","billing_address","shipping_address"]
	success_url="/login/signedup"

#class VendedorCreateView(CreateView):
#	model=Vendedor
#	fields=["username","password","email"]	
#	success_url="/login/signedup"

def success(request):
	return render(request, 'signedup.html')


#API

#class ClienteCreateView(CreateView):
#	model = Cliente
#	context_object_name = "cliente"

class ClienteListView(ListView):
	model = Cliente
	context_object_name = "cliente"

class ClienteDetailView(DetailView):
	model = Cliente
	context_object_name = "cliente"

