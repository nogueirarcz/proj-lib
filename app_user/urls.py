from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('cadastro/', views.cadastro, name = 'cadastro'),
    path('validar_cadastro/', views.validar_cadastro, name='validar_cadastro'),
]
