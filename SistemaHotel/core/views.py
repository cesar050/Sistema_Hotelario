<<<<<<< HEAD
<<<<<<< HEAD
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
=======
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Persona, Usuario
from .forms import PersonaForm, UsuarioForm

<<<<<<< HEAD
=======
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Persona, Usuario
from .forms import PersonaForm, UsuarioForm

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 67d9ed0 (inicio del modelado)
=======
>>>>>>> 1e8ee1d (inicio del modelado)
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')
def some_view(request):
    return render(request, 'core/some_view.html')
def masthead(request):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    background = 'img/home-bg.jpg'
>>>>>>> 67d9ed0 (inicio del modelado)
=======
    background = 'img/home-bg.jpg'
>>>>>>> 1e8ee1d (inicio del modelado)
=======
=======
>>>>>>> 4c3a679 (sitemaHotel)
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
<<<<<<< HEAD
    return render(request, 'index.html', context)
>>>>>>> 4c3a679 (sitemaHotel)
=======
    background = 'img/home-bg.jpg'
>>>>>>> 67d9ed0 (inicio del modelado)
=======
    background = 'img/home-bg.jpg'
>>>>>>> 1e8ee1d (inicio del modelado)
=======
    return render(request, 'index.html', context)
>>>>>>> 4c3a679 (sitemaHotel)
