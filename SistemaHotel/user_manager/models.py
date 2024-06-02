import enum
from django.db import models
from django.contrib.auth.models import User
from core.models import *


class TipoUsuario(enum.Enum):
    ADMINISTRADOR = "ADMINISTRADOR"
    RECEPCIONISTA = "RECEPCIONISTA"
    CAMARERO = "CAMARERO"
    LIMPIEZA = "LIMPIEZA"
    CLIENTE = "CLIENTE"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Cuenta(Usuario):
    tipo = models.CharField(max_length=20, choices=TipoUsuario.choices())

    def __str__(self):
        return f"{self.user.username}, {self.persona.nombre} {self.persona.apellido} {self.tipo}"
