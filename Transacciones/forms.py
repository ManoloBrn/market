from django import forms
from django.forms import ModelForm



#    class Meta:
#        model = MODELNAME
#        fields = ('',)


class CompraForm(forms.Form):
	name = forms.CharField(max_length=60)
	creditCard = forms.CharField(max_length=24)
	cvc = forms.DecimalField()
	expDate = forms.DateField()
	street = forms.CharField(max_length=100)
	colonia = forms.CharField(max_length=100)
	city = forms.CharField(max_length=100)
	estate = forms.CharField(max_length=100)
	zipcode = forms.IntegerField()
	country = forms.CharField(max_length=30)

	class Meta:
		exclude = []