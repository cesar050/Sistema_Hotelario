
<<<<<<< HEAD
def another_example_view(request):
    return render(request, 'hotel_manager/another_template.html')
=======
from django.shortcuts import render
from .models import Piso, Habitacion


def listar_habitaciones(request):
    pisos = Piso.objects.all().order_by('numero')
    for piso in pisos:
        piso.habitaciones = Habitacion.objects.filter(piso=piso)
    return render(request, 'habitaciones.html', {'pisos': pisos})
>>>>>>> b2277ad (ViewsTemplates)
