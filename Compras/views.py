from django.shortcuts import render
from django.views.generic import ListView
from .models import Transaction
# Create your views here.
class TransactionsView(ListView):
    model = Transaction
    context_object_name = "transactions"