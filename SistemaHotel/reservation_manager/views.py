from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from .forms import ReservaForm

# Create your views here.

def hacer_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'detalle_reserva.html')
    else:
        form = ReservaForm()
    return render(request, 'reserva.html', {'form': form})