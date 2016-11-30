from django.conf.urls import url, include

urlpatterns = [
	url(r'^producto/', include('Inventarios.urls_api')),
	url(r'^negocio/', include('Negocios.urls_api')),
	url(r'^transacciones/',include('Transacciones.urls_api')),
	url(r'^login/',include('login.urls_api')),
]