from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('perfis.urls')),
    url(r'^', include('usuarios.urls')),
]
