from django.contrib import admin


from hotel_manager.models import *


# Register your models here.
@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'direccion', 'telefono', 'email', 'descripcion', 'numHabitaciones']
@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = ['numero', 'capacidad', 'piso', 'categoria', 'precio', 'estado', 'disponible']
@admin.register(Piso)
class PisoAdmin(admin.ModelAdmin):
    list_display = ['numero', 'cantidad_habitaciones']
