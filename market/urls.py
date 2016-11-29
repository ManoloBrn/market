"""market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.conf.urls import url, include
from django.contrib import admin
from login import views
from login.views import *
from . import urls_api

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^createcliente/$', ClienteCreateView.as_view(), name="create-clientes"),
   # url(r'^createvendedor/$', VendedorCreateView.as_view(), name="create-vendedor"),
    #url(r'^login/signedup/$', success ),


    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    url(
    regex=r'^login/$', 
    view=login, 
    kwargs={'template_name': 'login.html'}, 
    name='login'
),
    url(
    regex=r'^logout/$', 
    view=logout, 
    kwargs={'next_page': '/'}, 
    name='logout'
),

    url('^', include('django.contrib.auth.urls')),

    url(r'^api/hello', ApiEndpoint.as_view()),
    url(r'^secret$', secret_page, name='secret'),


    url(r'^inventario/', include("Inventarios.urls"), name="inventarios-root"),
    url(r'^negocios/', include("Negocios.urls"), name="negocios-root"),
    url(r'^transacciones/', include("Transacciones.urls"), name="transacciones-root"),
    url(r'^api/v1/', include(urls_api))

]
