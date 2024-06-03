from datetime import date

from django.db import models
from adminHotel.models import *


# Create your models here.


class GestionReserva:

    def hacer_reserva(self):
        pass

    def cancelar_reserva(self):
        pass

    def modificar_reserva(self):
        pass


class PanelGestion(GestionReserva, models.Model):
    nombreRecepcionista = models.ForeignKey(Recepcionista, on_delete=models.CASCADE)
    fecha = models.DateField(default=date.today)

    def hacer_reserva(self):
        pass

    def cancelar_reserva(self):
        pass

    def modificar_reserva(self):
        pass


class Factura(models.Model):
    fecha = models.DateField(default=date.today)
    dias_hospedaje = models.IntegerField()
    servicios_adicinales = models.CharField(max_length=100)
    total = models.FloatField()
    panelGestion = models.ForeignKey(PanelGestion, on_delete=models.CASCADE)

    def generar_factura(self):

        pass

    def enviar_factura(self):
        pass

    def anular_factura(self):
        pass

    def modificar_factura(self):
        pass
