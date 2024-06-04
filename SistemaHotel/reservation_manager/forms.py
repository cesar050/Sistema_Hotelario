from django import forms
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> f6d1e94 (ViewsTemplates)

class ReservationManagerForm(forms.Form):
    guest_name = forms.CharField(label='Guest Name', max_length=100)
    room_type = forms.ChoiceField(label='Room Type', choices=[('Single', 'Single'), ('Double', 'Double'), ('Suite', 'Suite')])
    check_in_date = forms.DateField(label='Check-In Date')
    check_out_date = forms.DateField(label='Check-Out Date')
    special_requests = forms.CharField(label='Special Requests', widget=forms.Textarea, required=False)
=======
<<<<<<< HEAD
=======
>>>>>>> b2277ad (ViewsTemplates)
=======
>>>>>>> f6d1e94 (ViewsTemplates)
=======
>>>>>>> b2277ad (ViewsTemplates)
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b2277ad (ViewsTemplates)
=======
=======
>>>>>>> f6d1e94 (ViewsTemplates)
>>>>>>> b2277ad (ViewsTemplates)
=======
>>>>>>> b2277ad (ViewsTemplates)
