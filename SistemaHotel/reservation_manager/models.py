from django.db import models


# Create your models here.

class Reserva(models.Model):
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    cantidad_personas = models.IntegerField()
    habitacion = models.ForeignKey('hotel_manager.Habitacion', on_delete=models.CASCADE)
    cliente = models.ForeignKey('client_manager.Cliente', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.fecha_entrada} {self.fecha_salida} {self.cantidad_personas} {self.habitacion} {self.cliente}"


class ServicioExtra(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.precio} {self.descripcion}"


class AsignacionReservaHabitacion(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    habitacion = models.ForeignKey('hotel_manager.Habitacion', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.reserva} {self.habitacion}"
