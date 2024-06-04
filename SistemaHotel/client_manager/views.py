from django.shortcuts import render
from .models import Historial

def historial_transacciones(request):
    historiales = Historial.objects.all()
    return render(request, 'dashBoard.html', {'historial': historiales})
