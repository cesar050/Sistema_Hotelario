from django.db import models


# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=[('ACTIVO', 'ACTIVO'), ('INACTIVO', 'INACTIVO')])

    def __str__(self):
        return f"{self.nombre}, {self.precio}"


class Reserva(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    numDias = models.IntegerField(default=0)
    numPersonas = models.IntegerField()
    habitacion = models.ForeignKey('hotel_manager.Habitacion', on_delete=models.CASCADE)
    cuenta = models.ForeignKey('user_manager.Cuenta', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=20, choices=[('PENDIENTE', 'PENDIENTE'), ('CONFIRMADA', 'CONFIRMADA'),
                                                      ('CANCELADA', 'CANCELADA')])
    total_costo = models.DecimalField(max_digits=10, decimal_places=2, default=0)


    def agregar_habitacion(self, habitacion):
        self.habitacion = habitacion
        self.save()

    def agregar_servicio(self, servicio):
        self.servicios.add(servicio)
        self.save()

    def calcular_dias(self):
        self.numDias = (self.fecha_fin - self.fecha_inicio).days
        self.save()
    def calcular_costo(self):
        self.total_costo = self.habitacion.precio * self.numDias
        self.save()

class AsignacionReservaHabitacion(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    habitacion = models.ForeignKey('hotel_manager.Habitacion', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.reserva}, {self.habitacion}"
