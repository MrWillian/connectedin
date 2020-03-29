from django.conf.urls import url, include
from views import RegistrarUsuarioView
from django.contrib.auth import views as auth_views

urlpatterns = [
  url(r'^registrar/$', RegistrarUsuarioView.as_view(), name="registrar"),
  # url(r'^login/$', auth_views.LoginView.as_view(), { 'template_name' : 'login.html'}, name="login"),
  # url(r'^logout/$', auth_views.LogoutView.as_view(), { 'login_url' : '/login'}, name="logout")
]
