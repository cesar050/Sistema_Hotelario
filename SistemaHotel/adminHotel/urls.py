from django.urls import path
<<<<<<< HEAD
<<<<<<< HEAD
from . import views

urlpatterns = [
    path('example/', views.example_view, name='example_view'),
]
=======
=======
>>>>>>> 4c3a679 (sitemaHotel)
from .views import *

urlpatterns = [
   # Agregar esto para la ruta raíz
    path('', admin_dashboard, name='admin_dashboard'),
    path('agregar_trabajador/', crear_trabajador, name='add_worker'),
    path('info_trabajador/<int:id>/', info_trabajadore, name='info_workers'),
    path('trabajadores/', listar_trabajadores, name='list_workers'),
<<<<<<< HEAD
]
>>>>>>> 4c3a679 (sitemaHotel)
=======
]
>>>>>>> 4c3a679 (sitemaHotel)
