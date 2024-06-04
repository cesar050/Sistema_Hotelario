from django import forms
from reservation_manager.models import Reserva, AsignacionReservaHabitacion, Servicio

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['fecha_inicio', 'fecha_fin', 'numPersonas', 'habitacion', 'cuenta', 'estado']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
            'estado': forms.Select(choices=[('PENDIENTE', 'PENDIENTE'), ('CONFIRMADA', 'CONFIRMADA'), ('CANCELADA', 'CANCELADA')])
        }
