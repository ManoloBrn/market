from django.conf.urls import url
from .views import TransactionsView

urlpatterns = [
	url(r'^listado/',TransactionsView.as_view(), name="listado_transactions"),

]
