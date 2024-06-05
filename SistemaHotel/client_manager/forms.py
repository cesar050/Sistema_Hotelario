from django import forms
from django.core.exceptions import ValidationError
from .models import Cliente, CuentaCliente

class RegistroForm(forms.Form):
    # Campos de Cliente
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    telefono = forms.CharField(max_length=10)
    email = forms.EmailField()
    domicilio = forms.CharField(widget=forms.Textarea)
    fecha_nacimiento = forms.DateField()
    sexo = forms.ChoiceField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')])
    documento = forms.CharField(max_length=10)

    # Campos de CuentaCliente
    usuario = forms.CharField(max_length=50)
    contrasena = forms.CharField(max_length=50, widget=forms.PasswordInput)
    repetir_contrasena = forms.CharField(max_length=50, widget=forms.PasswordInput)

    def clean_usuario(self):
        usuario = self.cleaned_data['usuario']
        if CuentaCliente.objects.filter(usuario=usuario).exists():
            raise ValidationError("El nombre de usuario ya está en uso.")
        return usuario

    def clean(self):
        cleaned_data = super().clean()
        contrasena = cleaned_data.get('contrasena')
        repetir_contrasena = cleaned_data.get('repetir_contrasena')

        if contrasena and repetir_contrasena and contrasena != repetir_contrasena:
            raise ValidationError("Las contraseñas no coinciden. Por favor, inténtalo de nuevo.")

        email = cleaned_data.get('email')
        usuario = cleaned_data.get('usuario')

        # Verificar si el correo electrónico ya está en uso
        if Cliente.objects.filter(email=email).exists():
            self.add_error('email', 'Este correo electrónico ya está registrado.')

        # Verificar si el nombre de usuario ya está en uso
        if CuentaCliente.objects.filter(usuario=usuario).exists():
            self.add_error('usuario', 'Este nombre de usuario ya está en uso.')

    def save(self):
        cliente = Cliente(
            nombre=self.cleaned_data['nombre'],
            apellido=self.cleaned_data['apellido'],
            telefono=self.cleaned_data['telefono'],
            email=self.cleaned_data['email'],
            domicilio=self.cleaned_data['domicilio'],
            fecha_nacimiento=self.cleaned_data['fecha_nacimiento'],
            sexo=self.cleaned_data['sexo'],
            documento=self.cleaned_data['documento']
        )
        cliente.save()

        cuenta_cliente = CuentaCliente(
            usuario=self.cleaned_data['usuario'],
            cliente=cliente
        )
        cuenta_cliente.set_password(self.cleaned_data['contrasena'])  # Establece la contraseña cifrada
        cuenta_cliente.save()
