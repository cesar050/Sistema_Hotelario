from django.db import models
from hotel_manager.models import Habitacion
from client_manager.models import Cliente
from user_manager.models import Cuenta
from django.db import models

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=[('ACTIVO', 'ACTIVO'), ('INACTIVO', 'INACTIVO')])

    def __str__(self):
        return f"Servicio: {self.nombre}, Precio: {self.precio}"

class Reserva(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    numDias = models.IntegerField(default=0)
    numPersonas = models.IntegerField()
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=20, choices=[('PENDIENTE', 'PENDIENTE'), ('CONFIRMADA', 'CONFIRMADA'),
                                                      ('CANCELADA', 'CANCELADA')])
    total_costo = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calcular_dias(self):
        self.numDias = (self.fecha_fin - self.fecha_inicio).days
        self.save()

    def calcular_costo(self):
        if self.habitacion:
            self.total_costo = self.habitacion.precio * self.numDias
            self.save()

    def __str__(self):
        return f"Reserva: {self.fecha_inicio} - {self.fecha_fin}, Cliente: {self.cuenta}"


class AsignacionReservaHabitacion(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)

    def __str__(self):
        return f"Asignación: {self.reserva}, Habitación: {self.habitacion}"
