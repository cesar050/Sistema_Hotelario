<<<<<<< HEAD
<<<<<<< HEAD
from django import forms
from .models import Persona, Usuario

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'  # Para incluir todos los campos de Persona en el formulario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['user']  # Puedes personalizar qué campos del modelo Usuario quieres incluir en el formulario
=======
=======
>>>>>>> 4c3a679 (sitemaHotel)
from django import forms
from .models import Persona, Usuario

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'  # Para incluir todos los campos de Persona en el formulario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['user']  # Puedes personalizar qué campos del modelo Usuario quieres incluir en el formulario
<<<<<<< HEAD
>>>>>>> 4c3a679 (sitemaHotel)
=======
>>>>>>> 4c3a679 (sitemaHotel)
