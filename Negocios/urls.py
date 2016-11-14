from django.conf.urls import url
from .views import NegocioView

urlpatterns = [
	url(r'^detail/(?P<pk>[0-9]+)/',NegocioView.as_view(), name="detail-negocio"),


]