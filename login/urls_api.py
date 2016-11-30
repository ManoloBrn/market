from django.conf.urls import url, include
from .views_api import ClienteViewSet, ClienteViewCreate
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'', ProductoViewSet)


urlpatterns = [
	url(r'^listado/', ClienteViewSet.as_view()),
	url(r'^create/', ClienteViewCreate.as_view()),
]