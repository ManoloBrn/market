from django.shortcuts import render
from django.views.generic import View,DetailView, DeleteView, UpdateView, CreateView
from .models import Negocio
# Create your views here.
class NegocioView(DetailView):
	model = Negocio