from django.conf.urls import url
from .views import TransactionsViewL, TransactionsViewD, RegisterCompra

urlpatterns = [
	url(r'^list/',TransactionsViewL.as_view(), name="list-transactions"),
	url(r'^detail/(?P<pk>[0-9]+)/',TransactionsViewD.as_view(), name="detail-transactions"),
	url(r'^buy/',RegisterCompra.as_view(), name="buy-transactions"),
]