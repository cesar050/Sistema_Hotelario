from django.shortcuts import render, redirect, get_object_or_404
from .forms import TrabajadorForm, TurnoForm
from .models import PersonalHotel

<<<<<<< HEAD
<<<<<<< HEAD
def example_view(request):
    return render(request, 'adminHotel/example_template.html')
=======
=======
>>>>>>> 4c3a679 (sitemaHotel)

def admin_dashboard(request):
    return render(request, 'index.html', {})


def crear_trabajador(request):
    if request.method == 'POST':
        form = TrabajadorForm(request.POST)
        if form.is_valid():
            form.save()
            # Redireccionar a alguna página o mostrar un mensaje de éxito
    else:
        form = TrabajadorForm()

    return render(request, 'agrerar_trabajador.html', {'form': form})


def info_trabajadore(request, id):
    trabajador = get_object_or_404(PersonalHotel, id=id)
    if request.method == 'POST':
        form = TrabajadorForm(request.POST, instance=trabajador)
        turno_form = TurnoForm(request.POST)
        if form.is_valid() and turno_form.is_valid():
            form.save()
            turno = turno_form.cleaned_data['turno']
            turno.trabajador = trabajador
            turno.save()
            # Redireccionar a alguna página o mostrar un mensaje de éxito
    else:
        form = TrabajadorForm(instance=trabajador)
        turno_form = TurnoForm()

    return render(request, 'info_trabajador.html', {'form': form, 'turno_form': turno_form, 'trabajador': trabajador})


def modificarTrabajador(request):
    return render(request, 'modificarTrabajador.html')

def listar_trabajadores(request):
    trabajadores = PersonalHotel.objects.all()
    return render(request, 'lista_personal.html', {'trabajadores': trabajadores})


def eliminarTrabajador(request):
<<<<<<< HEAD
    return render(request, 'eliminarTrabajador.html')
>>>>>>> 4c3a679 (sitemaHotel)
=======
    return render(request, 'eliminarTrabajador.html')
>>>>>>> 4c3a679 (sitemaHotel)
