<<<<<<< HEAD
from django.shortcuts import render
from .models import Historial

def historial_transacciones(request):
    historiales = Historial.objects.all()
    return render(request, 'dashBoard.html', {'historial': historiales})
=======
from django.shortcuts import render
from .models import Historial

def historial_transacciones(request):
    historiales = Historial.objects.all()
    return render(request, 'dashBoard.html', {'historial': historiales})
<<<<<<< HEAD
>>>>>>> 4c3a679 (sitemaHotel)
=======
>>>>>>> 4c3a679 (sitemaHotel)
