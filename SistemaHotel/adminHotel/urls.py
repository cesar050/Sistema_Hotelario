from django.urls import path
from .views import *

urlpatterns = [
   # Agregar esto para la ruta raíz
    path('', admin_dashboard, name='admin_dashboard'),
    path('agregar_trabajador/', crear_trabajador, name='add_worker'),
    path('info_trabajador/<int:id>/', info_trabajadore, name='info_workers'),
    path('trabajadores/', listar_trabajadores, name='list_workers'),
]