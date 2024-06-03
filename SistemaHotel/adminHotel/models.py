import enum

from django.db import models

from core.models import Persona


# Create your models here.
class TurnoAsignado(enum.Enum):
    MATUTINO = "MATUTINO"
    VESPERTINO = "VESPERTINO"
    NOCTURNO = "NOCTURNO"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Dias(enum.Enum):
    LUNES = "LUNES"
    MARTES = "MARTES"
    MIERCOLES = "MIERCOLES"
    JUEVES = "JUEVES"
    VIERNES = "VIERNES"
    SABADO = "SABADO"
    DOMINGO = "DOMINGO"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Turno(models.Model):
    dia = models.CharField(max_length=20, choices=Dias.choices())
    turno = models.CharField(max_length=20, choices=TurnoAsignado.choices())
    horaInicio = models.TimeField()
    horaFin = models.TimeField()

    def __str__(self):
        return f"{self.dia} {self.turno} {self.horaInicio} {self.horaFin}"


class PersonalHotel(Persona):
    salarioHora = models.FloatField()
    horasTrabajadas = models.FloatField()
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.salarioHora} {self.horasTrabajadas}"


class Administrador(PersonalHotel):

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.salarioHora} {self.horasTrabajadas}"


class Recepcionista(PersonalHotel):

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.salarioHora} {self.horasTrabajadas}"


class CamareroRestaurante(PersonalHotel):

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.salarioHora} {self.horasTrabajadas}"


class CamareroPiso(PersonalHotel):

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.salarioHora} {self.horasTrabajadas}"