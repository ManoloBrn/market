from django.conf.urls import url, include

urlpatterns = [
	url(r'^producto/', include('Inventarios.urls_api'))
]