from django.conf.urls import url
from .views import NegocioViewD, NegocioViewL, NegocioViewC

urlpatterns = [
	url(r'^detail/(?P<pk>[0-9]+)/',NegocioViewD.as_view(), name="detail-negocio"),
	url(r'^list/',NegocioViewL.as_view(), name="list-negocio"),
	url(r'^create/',NegocioViewC.as_view(), name="create-negocio"),

]