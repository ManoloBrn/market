from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Negocio
# Create your views here.
class NegocioViewD(DetailView):
	model = Negocio

class NegocioViewL(ListView):
	model = Negocio
	context_object_name = "negocios"

class NegocioViewC(CreateView):
	model = Negocio
	success_url='/negocio/list/'	

