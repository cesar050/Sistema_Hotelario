from datetime import date
from django.contrib.auth.models import User
from django.db import models
import enum
# Create your models here.

class Sexo(enum.Enum):
    MASCULINO = 'M'
    FEMENINO = 'F'
    OTRO = 'O'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
class Persona(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField(editable= False)
    telefono = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    domicilio = models.TextField()
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices=Sexo.choices(), default=Sexo.MASCULINO)
    documento = models.CharField(max_length=10, unique=True)

    class Meta:
        abstract = True

    def calcular_edad(self):
        today = date.today()
        return today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))

    def save(self, *args, **kwargs):
        self.edad = self.calcular_edad()  # Llama al método calcular_edad con paréntesis para obtener el valor de la edad
        super().save(*args, **kwargs)
    def __str__(self):
        return self.nombre

class CuentaUsuario(User):
    usuario = models.CharField(max_length=50, unique=True)
    contrasena = models.CharField(max_length=50)

    class Meta:
        abstract = True

    def __str__(self):
        return self.usuario
