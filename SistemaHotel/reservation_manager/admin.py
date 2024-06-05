from django.contrib import admin
from reservation_manager.models import Reserva, AsignacionReservaHabitacion, Servicio

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['fecha_inicio', 'fecha_fin', 'numDias', 'numPersonas', 'get_habitacion', 'cuenta', 'fecha_creacion',
                    'fecha_modificacion', 'estado', 'total_costo']
    list_filter = ['fecha_inicio', 'fecha_fin', 'estado']
    search_fields = ['fecha_inicio', 'fecha_fin', 'estado']
    readonly_fields = ['numDias', 'total_costo']

    def get_habitacion(self, obj):

        return obj.nombre_de_habitacion

    get_habitacion.short_description = 'Habitacion'

@admin.register(AsignacionReservaHabitacion)
class AsignacionReservaHabitacionAdmin(admin.ModelAdmin):
    list_display = ['reserva', 'habitacion']
    list_filter = ['reserva', 'habitacion']
    search_fields = ['reserva', 'habitacion']

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'precio', 'estado']
    list_filter = ['nombre', 'precio', 'estado']
    search_fields = ['nombre', 'precio', 'estado']
