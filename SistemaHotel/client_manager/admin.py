from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import CuentaCliente, Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'telefono', 'email', 'domicilio', 'fecha_nacimiento', 'sexo', 'edad']  # Agrega el método 'mostrar_edad' para mostrar la edad calculada en el listado

    def mostrar_edad(self, obj):
        return obj.calcular_edad()  # Llama al método calcular_edad para obtener la edad calculada


class CuentaClienteAdmin(CuentaCliente):
    model = CuentaCliente
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
