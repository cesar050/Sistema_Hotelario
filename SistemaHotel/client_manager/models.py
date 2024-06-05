from django.db import models
from core.models import Persona, CuentaUsuario



# Create your models here.

class Cliente(Persona):

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class CuentaCliente(CuentaUsuario):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, related_name='usuario_cliente')

    def save(self, *args, **kwargs):
        if not self.pk:  # Si es un nuevo usuario
            if self.cliente:
                self.email = self.cliente.email
                self.first_name = self.cliente.nombre
                self.last_name = self.cliente.apellido
                # Aquí puedes copiar más atributos según sea necesario
        super().save(*args, **kwargs)
