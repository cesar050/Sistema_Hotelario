
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
def another_example_view(request):
    return render(request, 'hotel_manager/another_template.html')
=======
=======
>>>>>>> b2277ad (ViewsTemplates)
=======
def another_example_view(request):
    return render(request, 'hotel_manager/another_template.html')
=======
>>>>>>> f6d1e94 (ViewsTemplates)
=======
>>>>>>> b2277ad (ViewsTemplates)
from django.shortcuts import render
from .models import Piso, Habitacion


def listar_habitaciones(request):
    pisos = Piso.objects.all().order_by('numero')
    for piso in pisos:
        piso.habitaciones = Habitacion.objects.filter(piso=piso)
    return render(request, 'habitaciones.html', {'pisos': pisos})
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> b2277ad (ViewsTemplates)
=======
=======
>>>>>>> f6d1e94 (ViewsTemplates)
>>>>>>> b2277ad (ViewsTemplates)
=======
>>>>>>> b2277ad (ViewsTemplates)
