from django.conf.urls import url
from .views_api import CheckoutCreate

urlpatterns = [
	url(r'^checkout/', CheckoutCreate.as_view()),
]