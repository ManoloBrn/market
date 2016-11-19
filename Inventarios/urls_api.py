from django.conf.urls import url, include
from .views_api import ProductoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ProductoViewSet)


urlpatterns = [
	url(r'^listado/', include(router.urls) )
]