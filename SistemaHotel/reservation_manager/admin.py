from django.contrib import admin
from reservation_manager.models import Reserva, AsignacionReservaHabitacion, Servicio


@admin.register(Reserva)
class Reserva(admin.ModelAdmin):
    list_display = ['fecha_inicio', 'fecha_fin', 'numDias', 'numPersonas', 'habitacion', 'cuenta', 'fecha_creacion',
                    'fecha_modificacion', 'estado', 'total_costo']
    list_filter = ['fecha_inicio', 'fecha_fin', 'estado']
    search_fields = ['fecha_inicio', 'fecha_fin', 'estado']
    readonly_fields = ['numDias', 'total_costo']
@admin.register(AsignacionReservaHabitacion)
class AsignacionReservaHabitacion(admin.ModelAdmin):
    list_display = ['reserva', 'habitacion']
    list_filter = ['reserva', 'habitacion']
    search_fields = ['reserva', 'habitacion']
@admin.register(Servicio)
class Servicio(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'precio', 'estado']
    list_filter = ['nombre', 'precio', 'estado']
    search_fields = ['nombre', 'precio', 'estado']

