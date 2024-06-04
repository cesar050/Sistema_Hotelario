from django.urls import path
<<<<<<< HEAD
from . import views

urlpatterns = [
    path('example/', views.example_view, name='example_view'),
]
=======
from .views import *

urlpatterns = [
   # Agregar esto para la ruta raíz
    path('', admin_dashboard, name='admin_dashboard'),
    path('agregar_trabajador/', crear_trabajador, name='add_worker'),
    path('info_trabajador/<int:id>/', info_trabajadore, name='info_workers'),
    path('trabajadores/', listar_trabajadores, name='list_workers'),
]
>>>>>>> b2277ada42f3b63703deac7e599c1eeae3e34251
