from django.urls import path
from . import views

urlpatterns = [
    path('hacer_reserva/', views.hacer_reserva, name='hacer_reserva'),
    path('detalle_reserva/', views.hacer_reserva, name='detalle_reserva'),

    ]