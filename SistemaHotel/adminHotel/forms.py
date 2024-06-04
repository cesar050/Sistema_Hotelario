from django import forms
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