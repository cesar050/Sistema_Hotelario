from django.contrib import admin


from hotel_manager.models import *


# Register your models here.
admin.site.register(Hotel)
admin.site.register(Piso, PisoAdmin)
admin.site.register(Habitacion)
