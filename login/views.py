from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import CreateView
from .models import *




class ClienteCreateView(CreateView):
	model= Cliente
	fields=["username","password","email","phone","cards","plan","billing_address","shipping_address"]
	success_url="/login/signedup"

class VendedorCreateView(CreateView):
	model=Vendedor
	fields=["username","password","email"]
	success_url="/login/signedup"

def success(request):
	return render(request, 'signedup.html')

