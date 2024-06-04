from django.urls import path
from . import views

urlpatterns = [
    path('habitaciones/', views.listar_habitaciones, name='habitaciones'),
]
