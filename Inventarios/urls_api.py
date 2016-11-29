from django.conf.urls import url, include
from .views_api import ProductoViewSet, ProductoViewCreate
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'', ProductoViewSet)


urlpatterns = [
	url(r'^listado/', ProductoViewSet.as_view()),
	url(r'^create/', ProductoViewCreate.as_view()),
]