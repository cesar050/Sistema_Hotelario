from django import forms
<<<<<<< HEAD

class AdminHotelForm(forms.Form):
    name = forms.CharField(label='Hotel Name', max_length=100)
    address = forms.CharField(label='Address', max_length=255)
    phone_number = forms.CharField(label='Phone Number', max_length=15)
    email = forms.EmailField(label='Email')
=======
from .models import PersonalHotel, Turno


class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = PersonalHotel
        fields = ['nombre', 'apellido', 'salarioHora', 'fecha_nacimiento', 'turno', 'horasTrabajadas','documento']

    def save(self, commit=True):
        trabajador = super().save(commit=False)
        # Si hay lógica adicional antes de guardar, aquí se puede agregar
        if commit:
            trabajador.save()
        return trabajador


class TurnoForm(forms.Form):
    turno = forms.ModelChoiceField(queryset=Turno.objects.all())
>>>>>>> b2277ada42f3b63703deac7e599c1eeae3e34251
