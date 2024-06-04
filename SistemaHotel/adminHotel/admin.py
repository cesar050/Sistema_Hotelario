from django.contrib import admin
# Register your models here.
<<<<<<< HEAD
<<<<<<< HEAD

from adminHotel.models import *

admin.site.register(Administrador)
admin.site.register(Recepcionista)
admin.site.register(CamareroPiso)
admin.site.register(CamareroRestaurante)

=======
=======
>>>>>>> 4c3a679 (sitemaHotel)
from .models import Recepcionista, Administrador, Turno, PersonalHotel


@admin.register(Recepcionista)
class RecepcionistaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'salarioHora', 'horasTrabajadas']


@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'salarioHora', 'horasTrabajadas']


@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = ['dia', 'turno', 'horaInicio', 'horaFin']



@admin.register(PersonalHotel)
class PersonalHotelAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ['nombre', 'apellido', 'salarioHora', 'horasTrabajadas']
>>>>>>> 4c3a679 (sitemaHotel)
=======
    list_display = ['nombre', 'apellido', 'salarioHora', 'horasTrabajadas']
>>>>>>> 4c3a679 (sitemaHotel)
