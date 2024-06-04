from django.urls import path
from . import views

urlpatterns = [
    path('historial/', views.historial_transacciones, name='historial_transacciones'),
]
# Compare this snippet from SistemaHotel/hotel_manager/urls.py: