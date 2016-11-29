from django.conf.urls import url, include
from .views_api import NegocioViewCreate
from rest_framework.routers import DefaultRouter


urlpatterns = [
	url(r'create/', NegocioViewCreate.as_view())
]