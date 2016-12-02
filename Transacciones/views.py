from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Transaction, Checkout
from .forms import CompraForm
# Create your views here.
class TransactionsViewL(ListView):
    model = Transaction
    context_object_name = "transactions"

class TransactionsViewD(ListView):
    model = Transaction

class RegisterCompra(CreateView):
	model = Checkout
	#fields = ["name"]
	fields = ["description","amount","currency"]
	success_redircet = "/"
