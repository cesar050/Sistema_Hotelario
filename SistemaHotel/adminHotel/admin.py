from django.contrib import admin
# Register your models here.
<<<<<<< HEAD

from adminHotel.models import *

admin.site.register(Administrador)
admin.site.register(Recepcionista)
admin.site.register(CamareroPiso)
admin.site.register(CamareroRestaurante)

=======
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
    list_display = ['nombre', 'apellido', 'salarioHora', 'horasTrabajadas']
>>>>>>> b2277ada42f3b63703deac7e599c1eeae3e34251
