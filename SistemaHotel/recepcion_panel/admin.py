from django.contrib import admin


# Register your models here
from recepcion_panel.models import PanelGestion, Factura

admin.site.register(PanelGestion)

admin.site.register(Factura)