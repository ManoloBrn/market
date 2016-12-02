from django import forms
from .models import *
from django.forms import ModelForm

class CompraForm(ModelForm):
	class Meta:
		model = Checkout
		exclude=[]
		#fields = "__all__"