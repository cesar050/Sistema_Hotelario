
<<<<<<< HEAD
<<<<<<< HEAD
def another_example_view(request):
    return render(request, 'hotel_manager/another_template.html')
=======
=======
>>>>>>> b2277ada42f3b63703deac7e599c1eeae3e34251
from django.shortcuts import render
from .models import Piso, Habitacion


def listar_habitaciones(request):
    pisos = Piso.objects.all().order_by('numero')
    for piso in pisos:
        piso.habitaciones = Habitacion.objects.filter(piso=piso)
    return render(request, 'habitaciones.html', {'pisos': pisos})
<<<<<<< HEAD
>>>>>>> b2277ad (ViewsTemplates)
=======
>>>>>>> b2277ada42f3b63703deac7e599c1eeae3e34251
