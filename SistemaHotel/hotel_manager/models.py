import enum

from django.db import models
from django.contrib import admin



# Create your models here.

class Hotel(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    email = models.EmailField()
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.direccion} {self.telefono} {self.email} {self.descripcion}"


class Piso(models.Model):
    numero = models.IntegerField()
    cantidad_habitaciones = models.IntegerField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.numero} {self.cantidad_habitaciones} {self.hotel}"


class Categoria(enum.Enum):
    ECONOMICA = "ECONOMICA"
    SUIETE_JR = "SUIETE_JR"
    SUITEPRESIDENCIAL = "SUITEPRESIDENCIAL"

    @classmethod
    def choices(cls):
          return [(key.value, key.name) for key in cls]


class Estado(enum.Enum):
    DISPONIBLE = "DISPONIBLE"
    OCUPADA = "OCUPADA"
    MANTENIMIENTO = "MANTENIMIENTO"
    RESERVADA = "RESERVADA"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Habitacion(models.Model):
    numero = models.IntegerField()
    capacidad = models.IntegerField()
    piso = models.ForeignKey(Piso, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=20, choices=Categoria.choices())
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=Estado.choices())

    def save(self, *args, **kwargs):
        # Si la habitación es nueva, incrementa la cantidad de habitaciones en el piso
        if not self.pk:
            self.piso.cantidad_habitaciones += 1
            self.piso.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.numero} {self.capacidad} {self.piso}"

class PisoAdmin(admin.ModelAdmin):
    exclude = ('cantidad_habitaciones',)
