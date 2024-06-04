from django import forms
<<<<<<< HEAD
<<<<<<< HEAD

class ReservationManagerForm(forms.Form):
    guest_name = forms.CharField(label='Guest Name', max_length=100)
    room_type = forms.ChoiceField(label='Room Type', choices=[('Single', 'Single'), ('Double', 'Double'), ('Suite', 'Suite')])
    check_in_date = forms.DateField(label='Check-In Date')
    check_out_date = forms.DateField(label='Check-Out Date')
    special_requests = forms.CharField(label='Special Requests', widget=forms.Textarea, required=False)
=======
=======
>>>>>>> b2277ada42f3b63703deac7e599c1eeae3e34251
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
>>>>>>> b2277ad (ViewsTemplates)
=======
>>>>>>> b2277ada42f3b63703deac7e599c1eeae3e34251
