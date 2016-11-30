from django.conf.urls import url
from .views import ClienteCreateView, ClienteListView, ClienteDetailView

urlpatterns = [
	url(r'^create/',ClienteCreateView.as_view(), name="create-cliente"),
	url(r'^list/',ClienteListView.as_view(), name="list-cliente"),
	url(r'^detail/(?P<pk>[0-9]+)/',ClienteDetailView.as_view(), name="detail-cliente"),
]

