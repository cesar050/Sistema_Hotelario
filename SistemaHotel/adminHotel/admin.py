from django.contrib import admin

# Register your models here.

from adminHotel.models import *

admin.site.register(Administrador)
admin.site.register(Recepcionista)
admin.site.register(CamareroPiso)
admin.site.register(CamareroRestaurante)

