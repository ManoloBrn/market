from django.conf.urls import url
from .views import RegisterView,ProductosView

urlpatterns = [
	url(r'^create/',RegisterView.as_view(), name="create-producto"),
	url(r'^productos/',ProductosView.as_view(), name="productos"),
]
