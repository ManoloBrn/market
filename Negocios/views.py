from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Negocio
# Create your views here.
# class NegocioViewD(DetailView):
# 	model = Negocio
# 	context_object_name = "negocio"

# class NegocioViewL(ListView):
# 	model = Negocio
# 	context_object_name = "negocios"

# class NegocioViewCreate(CreateView):
# 	model = Negocio
# 	fields = ["owner", "name", "streetAddress","phoneNumber"]
# 	success_url='/negocio/list/'	

