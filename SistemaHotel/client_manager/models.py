import enum

from django.db import models
from core.models import Persona


# Create your models here.

class MetodoPago(enum.Enum):
    EFECTIVO = "EFECTIVO"
    TARJETA = "TARJETA"
    TRANSFERENCIA = "TRANSFERENCIA"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Cliente(Persona):

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Historial(models.Model):
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=20, choices=MetodoPago.choices())
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.fecha} {self.monto} {self.metodo_pago} {self.cliente}"
