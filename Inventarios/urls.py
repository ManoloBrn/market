from django.conf.urls import url
from .views import ProductosViewC, ProductosViewL, ProductosViewD

urlpatterns = [
	url(r'^create/',ProductosViewC.as_view(), name="create-producto"),
	url(r'^list/',ProductosViewL.as_view(), name="list-producto"),
	url(r'^detail/(?P<pk>[0-9]+)/',ProductosViewD.as_view(), name="detail-producto"),
]