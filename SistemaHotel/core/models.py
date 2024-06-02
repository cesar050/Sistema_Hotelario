import enum

from django.db import models
from django.contrib.auth.models import User


class Sexo(enum.Enum):
    MASCULINO = "M"
    FEMENINO = "F"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class TipoDocumento(enum.Enum):
    DNI = "DNI"
    PASAPORTE = "PASAPORTE"
    CARNET_EXTRANJERIA = "CARNET_EXTRANJERIA"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    documento = models.CharField(max_length=8, unique=True)
    telefono = models.CharField(max_length=9)
    email = models.EmailField(unique=True)
    direccion = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices=Sexo.choices())

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
