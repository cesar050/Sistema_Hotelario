from django.shortcuts import render, redirect
from .forms import RegistroForm


def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir a alguna página de éxito o a donde desees
            return redirect('confirmacion.html')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

