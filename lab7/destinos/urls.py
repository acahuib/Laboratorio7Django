from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_destinos, name='listar_destinos'),
    path('anadir/', views.añadir_destino, name='anadir_destino'),
    path('modificar/<int:id>/', views.modificar_destino, name='modificar_destino'),
    path('eliminar/<int:id>/', views.eliminar_destino, name='eliminar_destino'),
]

