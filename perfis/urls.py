from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
  url(r'^$', include('perfis.views.index'), name='exibir'),
  url(r'^perfis/(?P<perfil_id>\d+)$', 'perfis.views.exibir', name='exibir')
]
