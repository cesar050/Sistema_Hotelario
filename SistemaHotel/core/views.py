from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Persona, Usuario
from .forms import PersonaForm, UsuarioForm

def agregar_persona_usuario(request):
    if request.method == 'POST':
        persona_form = PersonaForm(request.POST)
        usuario_form = UsuarioForm(request.POST)
        if persona_form.is_valid() and usuario_form.is_valid():
            # Guarda la persona
            persona = persona_form.save()
            # Crea el usuario asociado a la persona
            usuario = usuario_form.save(commit=False)
            usuario.persona = persona
            usuario.save()
            return redirect('index')  # Redirige a la página principal
    else:
        persona_form = PersonaForm()
        usuario_form = UsuarioForm()
    return render(request, 'agregar_persona_usuario.html', {'persona_form': persona_form, 'usuario_form': usuario_form})
def index(request):
    # Aquí puedes agregar cualquier lógica adicional que necesites antes de renderizar el template
    context = {
        'variable': 'valor',  # Puedes pasar variables al template si es necesario
    }
    return render(request, 'index.html', context)
def reservas(request):
    # Aquí puedes agregar cualquier lógica adicional que necesites antes de renderizar el template
    context = {
        'variable': 'valor',  # Puedes pasar variables al template si es necesario
    }
    return render(request, 'reservas.html', context)

def home(request):
    return render(request, 'home.html')