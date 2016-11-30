from django.contrib import admin
from .models import Transaction, Checkout
# Register your models here.
admin.site.register(Transaction)
admin.site.register(Checkout)