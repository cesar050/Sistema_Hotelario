from django.contrib import admin

from reservation_manager.models import*

# Register your models here.
admin.site.register(Reserva)
admin.site.register(ServicioExtra)
admin.site.register(AsignacionReservaHabitacion)

