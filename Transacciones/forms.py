from .models import *
from django.forms import ModelForm

class CompraForm(ModelForm):
	class Meta:
		model = Checkout
		fields = "__all__"
