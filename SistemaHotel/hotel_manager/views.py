
from django.shortcuts import render
from .models import Piso, Habitacion


def listar_habitaciones(request):
    pisos = Piso.objects.all().order_by('numero')
    for piso in pisos:
        piso.habitaciones = Habitacion.objects.filter(piso=piso)
    return render(request, 'habitaciones.html', {'pisos': pisos})
